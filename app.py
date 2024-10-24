from flask import Flask, render_template
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    # Definimos la fecha para la que queremos obtener los shows (15 de octubre en tu caso)
    target_date = datetime(2024, 10, 15)
    shows = get_shows_by_date(target_date)

    # Convertimos la fecha a una cadena para el uso en el template
    formatted_date = target_date.date().strftime('%Y-%m-%d')

    # Renderizamos el template y pasamos los shows filtrados
    return render_template('index.html', shows=shows, formatted_date=formatted_date)

def get_shows_by_date(date):
    # Usamos el día anterior para el start_time_after
    day_before = date - timedelta(days=1)
    start_time = day_before.strftime('%Y-%m-%dT00:00:00.000Z')
    
    # Llamada a la API para obtener los shows
    url = f'https://api.kexp.org/v2/shows/?expand=hosts&start_time_after={start_time}&limit=1050'
    print(f'Llamando a la API: {url}')
    
    response = requests.get(url)

    if response.status_code == 200:
        json_response = response.json()

        # Imprimimos el JSON completo para depuración
        print("Respuesta completa de la API:")
        print(json_response['results'])
        print('START TIME')
        print(start_time)
        print(date)
        # Filtramos los shows que coinciden con la fecha deseada
        shows_filtered = []
        if 'results' in json_response:
            for show in json_response['results']:
                show_start_time = datetime.strptime(show['start_time'], '%Y-%m-%dT%H:%M:%S%z')
                print(show_start_time)
                # Si el show es del día deseado (15 de octubre en este caso)
                if show_start_time.date() == date.date():
                    print(f"Show encontrado para {date.date()}: {show['program_name']} - {show['host_names'][0] if show['host_names'] else 'Desconocido'}")
                    shows_filtered.append({
                        'program_name': show['program_name'],
                        'host_name': show['host_names'][0] if show['host_names'] else 'Desconocido',
                        'start_time': show_start_time.strftime('%Y-%m-%d %H:%M:%S'),
                        'tags': show['program_tags'] if show['program_tags'] else 'Sin tags',
                        'image_uri': show['image_uri']
                    })

        return shows_filtered
    else:
        print(f"Error al llamar a la API: {response.status_code}")
        return []

if __name__ == '__main__':
    app.run(debug=True)
