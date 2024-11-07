from flask import Flask, jsonify, request, render_template
import requests
from datetime import datetime, timedelta, timezone
from dateutil import parser

app = Flask(__name__)

@app.route('/')
def index():
    # Renderizamos la plantilla inicial con el selector de fecha y el contenedor para programas
    return render_template('index.html')

@app.route('/get_shows', methods=['POST'])
def get_shows():
    data = request.get_json()
    selection_type = data.get('selection_type')
    selected_date = data.get('selected_date')

    base_url = "https://api.kexp.org/v2/shows/"
    limit = 50
    
    start_time_after = datetime.strptime(selected_date, '%Y-%m-%d').replace(tzinfo=timezone.utc)
    end_time = start_time_after

    if selection_type == 'day':
        limit = 50
        end_time = start_time_after + timedelta(days=1)
        app.logger.info(f"Parámetros {start_time_after} end time: {end_time}    fecha")
    elif selection_type == 'week':
        limit = 150
        end_time = start_time_after + timedelta(days=7)
    elif selection_type == 'month':
        limit = 550
        year = start_time_after.year
        month = start_time_after.month
        if month == 12:
            end_time = datetime(year + 1, 1, 1, tzinfo=timezone.utc)
        else:
            end_time = datetime(year, month + 1, 1, tzinfo=timezone.utc)

    params = {
        "start_time_after": start_time_after.strftime('%Y-%m-%dT%H:%M:%S'),
        "limit": limit
    }
    
    request_url = f"{base_url}?start_time_after={params['start_time_after']}&limit={params['limit']}"
    app.logger.info(f"Llamada a la API de KEXP: {request_url}")

    response = requests.get(base_url, params=params)
    shows_data = response.json().get('results', [])
    
    filtered_shows = [
        {
            "id": show["id"],
            "program_name": show["program_name"],
            "host_names": show["host_names"],
            "program_tags": show.get("program_tags", ""),
            "start_time": parser.parse(show['start_time']).isoformat(),
            "download_url": f"https://api.kexp.org/get_streaming_url/?bitrate=256&timestamp={show['start_time']}"
        }

        for show in shows_data        
        if start_time_after <= parser.parse(show['start_time']).astimezone(timezone.utc) < end_time
    ]
    app.logger.info(f"Shows filtrados {filtered_shows}")
    return jsonify(filtered_shows)

if __name__ == '__main__':
    app.run(debug=True)
