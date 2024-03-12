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
i = 0
for system in oec.findall(".//system"):
    distance = system.findtext("distance")
    for planet in system.findall(".//planet"):
        discovery_method = planet.findtext("discoverymethod")
        name = planet.findtext("name")
        if discovery_method not in planet_dict.keys() and discovery_method != None:
            planet_dict[discovery_method] = []
        if name != None and distance != None and discovery_method != None:
            planet_dict[discovery_method].append(float(distance))
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

for key, value in planet_dict.items():
    planet_dict[key] = statistics.mean(planet_dict[key])
print(planet_dict)
plt.figure(figsize=(15, 8))
plt.bar(planet_dict.keys(), planet_dict.values())
plt.xlabel("Discovery method")
plt.ylabel("Average distance from Sun")
plt.yscale("log")
plt.show()
