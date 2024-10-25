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

@app.route('/get_shows', methods=['POST'])
def get_shows():
    """Devuelve los programas en función de la fecha seleccionada y el límite configurado."""
    selection_type = request.json.get('selection_type')
    selected_date = request.json.get('selected_date')
    
    if not selection_type or not selected_date:
        return jsonify({"error": "Falta el tipo de selección o la fecha."}), 400

    date_obj = datetime.strptime(selected_date, '%Y-%m-%d')
    
    # Establecer el rango de fechas y límite en función del tipo de selección
    if selection_type == 'day':
        start_date = date_obj
        end_date = start_date
        limit = 50
    elif selection_type == 'week':
        start_date = date_obj - timedelta(days=date_obj.weekday())
        end_date = start_date + timedelta(days=6)
        limit = 150
    elif selection_type == 'month':
        start_date = date_obj.replace(day=1)
        end_date = (start_date + timedelta(days=31)).replace(day=1) - timedelta(days=1)
        limit = 550
    else:
        return jsonify({"error": "Tipo de selección inválido."}), 400
    
    params = {
        "expand": "hosts",
        "limit": limit,
        "start_time_after": start_date.isoformat() + "T00:00:00Z",
        "start_time_before": end_date.isoformat() + "T23:59:59Z"
    }
    response = requests.get(KEXP_SHOWS_API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data['results'])
    else:
        return jsonify({"error": "Error al obtener los programas de KEXP"}), 500

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
