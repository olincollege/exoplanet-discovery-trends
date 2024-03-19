import xml.etree.ElementTree as ET
import urllib.request
import gzip
import io
import pandas as pd
import matplotlib.pyplot as plt

plt.close("all")

url = "https://github.com/OpenExoplanetCatalogue/oec_gzip/raw/master/systems.xml.gz"
oec = ET.parse(gzip.GzipFile(fileobj=io.BytesIO(urllib.request.urlopen(url).read())))


planet_dict = {"name": [], "period": [], "discovery_year": []}
i = 0
for system in oec.findall(".//system"):
    #   period = system.findtext("period")
    for planet in system.findall(".//planet"):
        period = planet.findtext("period")
        discovery_year = planet.findtext("discoveryyear")
        name = planet.findtext("name")
        if name != None and period != None and discovery_year != None and period != "":
            planet_dict["name"].append(name)
            planet_dict["period"].append(float(period))
            planet_dict["discovery_year"].append(int(discovery_year))
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


planet_panda = pd.DataFrame.from_dict(planet_dict)
# planet_panda.plot.scatter(x="Radius", y="Mass", c="DarkBlue")
print(planet_panda)
plt.figure()
plt.scatter(planet_panda["discovery_year"], planet_panda["period"])
plt.xlabel("Discovery Year")
plt.ylabel("Orbital Period (days)")
plt.title("Exoplanet Orbital Period v. Discovery Year")
plt.xlim(1992, 2024)
plt.ylim(0, 8000)
plt.show()
