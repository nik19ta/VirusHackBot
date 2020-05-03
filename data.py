import COVID19Py
import json
import pandas as pd

covid19 = COVID19Py.COVID19()

# location = covid19.getLatestChanges()
# location = covid19.getAll()
# location = covid19.getLocations()
# location = covid19.getLatest()
# location = covid19.getLocationByCountryCode("US")

def latest():
    latest = covid19.getLatest()
    return f'Данные о распространении 🦠Coronavirus: \n\n😷 Заражено: {latest["confirmed"]}, \n😔 Погибло: {latest["deaths"]}, \n🙃 Вылечилось: {latest["recovered"]}'

def getLocations():
    cov = covid19.getLocations()

    data = []
    max = []


    for i in cov:
        max.append(i['latest']['confirmed'])

    df = pd.DataFrame({'count':max})
    print(df.sort_values(by=['count']).tail(15))



getLocations()
# print(getLocations()[1])
# print(getLocations()[2])
# print(getLocations()[3])
# print(getLocations()[4])


# if i['latest']['confirmed'] > max:
#     max = i['latest']['confirmed']



#
# for i in cov:
#     data.append(f"\nСтрана: {i['country']}, \nПогибло: {i['latest']['deaths']}, \nЗаражено: {i['latest']['confirmed']} \nВылечилось:   {i['latest']['recovered']} \n= = = = = = = = = =")
#     return data
