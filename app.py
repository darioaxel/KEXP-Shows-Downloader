from flask import Flask, render_template, request, jsonify, send_file
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

KEXP_MAIN_URL = "https://www.kexp.org/"
KEXP_DOWNLOAD_BASE_URL = "https://kexp-archive.streamguys1.com/content/kexp/"
LIMIT_SHOWS = 550

# Este es el endpoint para listar los shows por día
@app.route('/')
def index():
    today = datetime.today()
    start_date = today - timedelta(days=1)  # Start fetching shows from yesterday
    shows_by_date = get_shows_by_date(start_date)

    return render_template('index.html', shows_by_date=shows_by_date)

# Función para obtener los shows desde el API
def get_shows_by_date(start_date):
    date_str = start_date.strftime('%Y-%m-%dT00:00:00.000Z')
    api_url = f"https://api.kexp.org/v2/shows/?expand=hosts&start_time_after={date_str}&limit={LIMIT_SHOWS}"
    
    # Mostrar la llamada al API en consola
    print(f"API call: {api_url}")

    response = requests.get(api_url)
    shows_data = response.json()

    shows_by_date = {}

    # Agrupar shows por fecha
    for show in shows_data['results']:
        start_time = show['start_time']
        show_date = datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S%z').date()
        if show_date not in shows_by_date:
            shows_by_date[show_date] = []
        
        # Añadir el show al día correspondiente
        shows_by_date[show_date].append(show)

    return shows_by_date

# Endpoint para descargar un MP3 de un show
@app.route('/download_mp3/<show_id>', methods=['GET'])
def download_mp3(show_id):
    session = requests.Session()

    # Hacer la solicitud para obtener la cookie de sesión
    response = session.get(KEXP_MAIN_URL)
    
    # Obtener todas las cookies recibidas en la respuesta
    cookies = session.cookies.get_dict()
    print(f"Cookies recibidas: {cookies}")  # Esto mostrará todas las cookies en la consola

    # Verificar si se ha recibido la cookie 'AISSessionId'
    if 'AISSessionId' not in cookies:
        return jsonify({"error": "No se pudo obtener la cookie de sesión"}), 400
    
    session_id = cookies.get('AISSessionId')

    # Generar la URL de descarga del archivo MP3
    mp3_filename = f"{show_id}.mp3"  # Se debe construir el nombre del archivo MP3 con el show_id
    mp3_download_url = f"{KEXP_DOWNLOAD_BASE_URL}{mp3_filename}?listeningSessionID={session_id}"

    # Agregar las cabeceras necesarias para la descarga
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'es-ES,es;q=0.9,de;q=0.8,en;q=0.7',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)',
        'Referer': KEXP_MAIN_URL,
        'Range': 'bytes=0-'
    }

    # Hacer la solicitud para descargar el archivo
    download_response = session.get(mp3_download_url, headers=headers, stream=True)
    
    if download_response.status_code == 200:
        # Guardar el archivo temporalmente y luego enviarlo al usuario
        mp3_path = f"downloads/{mp3_filename}"
        with open(mp3_path, 'wb') as file:
            for chunk in download_response.iter_content(chunk_size=1024):
                file.write(chunk)
        return send_file(mp3_path, as_attachment=True)
    else:
        return jsonify({"error": f"Error en la descarga: {download_response.status_code}"}), 400

if __name__ == '__main__':
    app.run(debug=True)
