"""
Collects data from the Open Exoplanet Catalogue git repository.

This code uses the libraries xml, urllib, gzip, and io to collect data from
the Open Exoplanet Catalogue git repository and store it as an Element Tree
datatype. Then, the program finds the distance of each exoplanet (system) from
Earth, the year of the planet's discovery, discovery method, orbit period,
and name, and stores these values (except for name) in dictionaries and
pandas dataframes. This data is used in the exoplanet_visualization.py file.
"""

import xml.etree.ElementTree as ET
import urllib.request
import gzip
import io
import pandas as pd

URL = "https://github.com/OpenExoplanetCatalogue/oec_gzip/raw/master/systems.xml.gz"
oec = ET.parse(gzip.GzipFile(fileobj=io.BytesIO(urllib.request.urlopen(URL).read())))

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
            discovery_method not in planet_distance_dict
            and discovery_method is not None
        ):
            planet_distance_dict[discovery_method] = []
            planet_year_dict[discovery_method] = []
        if (
            name is not None
            and distance is not None
            and discovery_method is not None
            and discovery_year is not None
        ):
            planet_distance_dict[discovery_method].append(float(distance))
            planet_year_dict[discovery_method].append(float(discovery_year))

        period = planet.findtext("period")
        discovery_year = planet.findtext("discoveryyear")
        name = planet.findtext("name")

        if (
            name is not None
            and period is not None
            and discovery_year is not None
            and period != ""
        ):
            planet_period_dict["name"].append(name)
            planet_period_dict["period"].append(float(period))
            planet_period_dict["discovery_year"].append(int(discovery_year))

planet_panda = pd.DataFrame.from_dict(planet_period_dict)
