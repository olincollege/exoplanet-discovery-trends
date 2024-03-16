import xml.etree.ElementTree as ET
import urllib.request
import gzip
import io
import pandas as pd
import matplotlib.pyplot as plt
import statistics

plt.close("all")

url = "https://github.com/OpenExoplanetCatalogue/oec_gzip/raw/master/systems.xml.gz"
oec = ET.parse(gzip.GzipFile(fileobj=io.BytesIO(urllib.request.urlopen(url).read())))


planet_dict = {}
time_planet_dict = {}
i = 0
for system in oec.findall(".//system"):
    distance = system.findtext("distance")
    for planet in system.findall(".//planet"):
        discovery_method = planet.findtext("discoverymethod")
        discovery_year = planet.findtext("discoveryyear")
        name = planet.findtext("name")
        if discovery_method not in planet_dict.keys() and discovery_method != None:
            planet_dict[discovery_method] = []
            time_planet_dict[discovery_method] = []
        if (
            name != None
            and distance != None
            and discovery_method != None
            and discovery_year != None
        ):
            planet_dict[discovery_method].append(float(distance))
            time_planet_dict[discovery_method].append(float(discovery_year))
#     planet_name = system.findtext("name")
#     planet_age = system.findtext("discoveryyear")
#     planet_radius = system.findtext("distance")
#     if (
#         planet_age != None
#         and planet_radius != None
#         and planet_radius != ""
#         and planet_age != ""
#     ):
#         print("yes")
#         planet_dict["Name"].append(planet_name)
#         planet_dict["Age"].append(float(planet_radius))
#         planet_dict["Radius"].append(float(planet_radius))

print(planet_dict)
plt.figure(figsize=(15, 8))
print(planet_dict.keys())
colors = ["r", "b", "g", "darkorchid", "c", "lime", "fuchsia"]
for i, discovery_type in enumerate(planet_dict):
    plt.scatter(
        time_planet_dict[discovery_type],
        planet_dict[discovery_type],
        s=10,
        color=colors[i],
    )
plt.legend(planet_dict.keys())
plt.xlabel("Discovery Year")
plt.ylabel("Distance from Sun (parsecs)")
plt.show()
