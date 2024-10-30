from flask import Flask, jsonify, render_template, request
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

KEXP_SHOWS_API_URL = "https://api.kexp.org/v2/shows/"
KEXP_STREAM_URL_API = "https://api.kexp.org/get_streaming_url/"

@app.route('/')
def index():
    """Renderiza la página principal con la interfaz de selección de rango de fechas."""
    return render_template("index.html")

# Ruta para obtener los shows
@app.route('/get_shows', methods=['POST'])
def get_shows():
    data = request.get_json()
    selection_type = data.get('selection_type')
    selected_date = data.get('selected_date')

    # Parámetros para la API de KEXP
    base_url = "https://api.kexp.org/v2/shows/"
    limit = 50  # Default limit
    
    # Filtrar por límite según el tipo de selección
    if selection_type == 'day':
        limit = 50
        start_time_after = datetime.strptime(selected_date, '%Y-%m-%d')
        end_time = start_time_after + timedelta(days=1)
    elif selection_type == 'week':
        limit = 150
        start_time_after = datetime.strptime(selected_date, '%Y-%m-%d')
        end_time = start_time_after + timedelta(days=7)
    elif selection_type == 'month':
        limit = 550
        start_time_after = datetime.strptime(selected_date, '%Y-%m-%d')
        year = start_time_after.year
        month = start_time_after.month
        # Calcular el final del mes
        if month == 12:
            end_time = datetime(year + 1, 1, 1)
        else:
            end_time = datetime(year, month + 1, 1)

    # Parámetros de la consulta a la API de KEXP
    params = {
        "start_time_after": start_time_after.isoformat(),
        "limit": limit
    }

    # Log de la URL completa antes de realizar la llamada
    request_url = f"{base_url}?start_time_after={params['start_time_after']}&limit={params['limit']}"
    app.logger.info(f"Llamada a la API de KEXP: {request_url}")

    # Realizar la solicitud a la API
    response = requests.get(base_url, params=params)
    shows_data = response.json().get('results', [])

    # Filtrar los shows que estén dentro del rango solicitado
    filtered_shows = [
        show for show in shows_data
        if start_time_after <= datetime.fromisoformat(show['start_time'][:-1]) < end_time
    ]

    return jsonify(filtered_shows)

@app.route('/download_link/<show_id>', methods=['GET'])
def get_download_link(show_id):
    """Genera la URL de descarga basada en el `start_time` del programa."""
    response = requests.get(f"{KEXP_SHOWS_API_URL}{show_id}")
    if response.status_code != 200:
        return jsonify({"error": "No se pudo obtener la información del show"}), 400
    
    show_data = response.json()
    start_time = show_data.get("start_time")
    
    if not start_time:
        return jsonify({"error": "No se encontró el campo start_time"}), 400
    
    download_response = requests.get(f"{KEXP_STREAM_URL_API}?bitrate=256&timestamp={start_time}")
    if download_response.status_code == 200:
        data = download_response.json()
        return jsonify({"download_url": data.get("sg-url")})
    else:
        return jsonify({"error": "No se pudo obtener la URL de descarga"}), 500

if __name__ == '__main__':
    app.run(debug=True)
