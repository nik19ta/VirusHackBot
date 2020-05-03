import COVID19Py
import json
import pandas as pd

covid19 = COVID19Py.COVID19()

def latest():
    latest = covid19.getLatest()
    return f'Данные о распространении 🦠Coronavirus: \n\n😷 Заражено: {latest["confirmed"]}, \n😔 Погибло: {latest["deaths"]}, \n🙃 Вылечилось: {latest["recovered"]}'

def getLocations():
    cov = covid19.getLocations()

    DataF = ''
    max = []
    for i in cov:
        max.append(i['latest']['confirmed'])

    df = pd.DataFrame({'count':max})

    data = df.sort_values(by=['count']).tail(15).to_json()
    jsonD = json.loads(data)

    for value in jsonD['count']:

        DataF += f" \nСтрана: {covid19.getLocationById(value)['country']}, / Заражено: {covid19.getLocationById(value)['latest']['confirmed']} / Погибло: {covid19.getLocationById(value)['latest']['deaths']}, / Вылечилось: {covid19.getLocationById(value)['latest']['recovered']}"
    return DataF
