from flask import Flask, render_template
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    shows_by_date = get_shows_for_current_month()
    return render_template('index.html', shows_by_date=shows_by_date)

def get_shows_for_current_month():
    # Obtener el mes actual y el año
    now = datetime.now()
    month = now.month
    year = now.year

    # Calcular el primer y último día del mes
    first_day = datetime(year, month, 1)
    if month == 12:  # Si es diciembre, el próximo mes es enero del siguiente año
        last_day = datetime(year + 1, 1, 1) - timedelta(days=1)
    else:
        last_day = datetime(year, month + 1, 1) - timedelta(days=1)

    shows_by_date = {}

    # Iterar por cada día del mes
    current_day = first_day
    while current_day <= last_day:
        shows = get_shows_by_date(current_day)
        if shows:
            shows_by_date[current_day.date()] = shows
        current_day += timedelta(days=1)

    return shows_by_date

def get_shows_by_date(date):
    # Convertir la fecha a un formato adecuado para la API
    date_str = date.strftime('%Y-%m-%dT10:00:00.000Z')  # Formato ISO 8601
    url = f'https://api.kexp.org/v2/shows/?expand=hosts&start_time_after={date_str}&limit=200'
    
    # Imprimir la URL de la API en la consola
    print(f'Llamando a la API: {url}')

    response = requests.get(url)

    if response.status_code == 200:
        json_response = response.json()
        if '_embedded' in json_response:
            return json_response['_embedded']['shows']
    return []

if __name__ == '__main__':
    app.run(debug=True)
