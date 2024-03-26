import xml.etree.ElementTree as ET
import urllib.request
import gzip
import io
import pandas as pd

url = "https://github.com/OpenExoplanetCatalogue/oec_gzip/raw/master/systems.xml.gz"
oec = ET.parse(gzip.GzipFile(fileobj=io.BytesIO(urllib.request.urlopen(url).read())))

discovery_year_dict = {}
planet_distance_dict = {}
planet_year_dict = {}
planet_period_dict = {"name": [], "period": [], "discovery_year": []}

for system in oec.findall(".//system"):
    distance = system.findtext("distance")
    for planet in system.findall(".//planet"):
        discovery_year = planet.findtext("discoveryyear")

        if discovery_year is not None:
            discovery_year = int(discovery_year)
            if discovery_year not in discovery_year_dict:
                discovery_year_dict[discovery_year] = 1
            else:
                discovery_year_dict[discovery_year] += 1

        discovery_method = planet.findtext("discoverymethod")
        discovery_year = planet.findtext("discoveryyear")
        name = planet.findtext("name")

        if (
            discovery_method not in planet_distance_dict.keys()
            and discovery_method != None
        ):
            planet_distance_dict[discovery_method] = []
            planet_year_dict[discovery_method] = []
        if (
            name != None
            and distance != None
            and discovery_method != None
            and discovery_year != None
        ):
            planet_distance_dict[discovery_method].append(float(distance))
            planet_year_dict[discovery_method].append(float(discovery_year))

        period = planet.findtext("period")
        discovery_year = planet.findtext("discoveryyear")
        name = planet.findtext("name")

        if name != None and period != None and discovery_year != None and period != "":
            planet_period_dict["name"].append(name)
            planet_period_dict["period"].append(float(period))
            planet_period_dict["discovery_year"].append(int(discovery_year))

planet_panda = pd.DataFrame.from_dict(planet_period_dict)
