# from covid import Covid
import pprint

import COVID19Py
covid19 = COVID19Py.COVID19()

location = covid19.getLatestChanges()
# location = covid19.getAll()
# location = covid19.getLocations()
# location = covid19.getLatest()
# location = covid19.getLocationByCountryCode("US")

print(location)
