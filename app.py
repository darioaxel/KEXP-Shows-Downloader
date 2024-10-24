from flask import Flask, render_template
import requests
from datetime import datetime, timedelta
from collections import defaultdict

app = Flask(__name__)

@app.route('/')
def index():
    start_date = datetime(2024, 10, 1)
    shows_by_week = get_shows_by_weeks(start_date)
    return render_template('index.html', shows_by_week=shows_by_week)

def get_shows_by_weeks(start_date):
    day_before = start_date - timedelta(days=1)
    start_time = day_before.strftime('%Y-%m-%dT00:00:00.000Z')

    url = f'https://api.kexp.org/v2/shows/?expand=hosts&start_time_after={start_time}&limit=50'
    print(f'Llamando a la API: {url}')
    
    response = requests.get(url)

    if response.status_code == 200:
        json_response = response.json()
        print("Respuesta completa de la API:")
        print(json_response)

        shows_by_week = defaultdict(list)

        if 'results' in json_response:
            for show in json_response['results']:
                show_start_time = datetime.strptime(show['start_time'], '%Y-%m-%dT%H:%M:%S%z')
                week_start = show_start_time - timedelta(days=show_start_time.weekday())
                week_end = week_start + timedelta(days=6)
                week_range = (week_start.date(), week_end.date())

                download_link = generate_mp3_download_link(show)

                shows_by_week[week_range].append({
                    'program_name': show['program_name'],
                    'host_name': show['host_names'][0] if show['host_names'] else 'Desconocido',
                    'start_time': show_start_time.strftime('%Y-%m-%d %H:%M:%S'),
                    'tags': show['program_tags'] if show['program_tags'] else 'Sin tags',
                    'image_uri': show['image_uri'],
                    'download_link': download_link
                })

        return shows_by_week
    else:
        print(f"Error al llamar a la API: {response.status_code}")
        return {}

def generate_mp3_download_link(show):
    start_time = datetime.strptime(show['start_time'], '%Y-%m-%dT%H:%M:%S%z')
    date_str = start_time.strftime('%Y%m%d%H%M%S')
    program_name_slug = show['program_name'].lower().replace(" ", "-")
    download_link = (
        f"https://kexp-archive.streamguys1.com/content/kexp/{date_str}-4-485-{program_name_slug}.mp3?"
        "listeningSessionID=0CD_382_78__ef17e74236afc239e88f1de6cdaade26743a3ea6"
    )
    return download_link

if __name__ == '__main__':
    app.run(debug=True)
