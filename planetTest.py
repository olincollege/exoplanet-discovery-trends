import xml.etree.ElementTree as ET, urllib.request, gzip, io
import pandas as pd
import matplotlib.pyplot as plt

plt.close("all")

url = "https://github.com/OpenExoplanetCatalogue/oec_gzip/raw/master/systems.xml.gz"
oec = ET.parse(gzip.GzipFile(fileobj=io.BytesIO(urllib.request.urlopen(url).read())))


planet_dict = {"Name": [], "Radius": [], "Mass": []}
for planet in oec.findall(".//planet"):
    planet_name = planet.findtext("name")
    planet_radius = planet.findtext("radius")
    planet_mass = planet.findtext("mass")
    if (
        planet_radius != None
        and planet_mass != None
        and planet_mass != ""
        and planet_radius != ""
    ):
        planet_dict["Name"].append(planet_name)
        planet_dict["Radius"].append(planet_radius)
        planet_dict["Mass"].append(planet_mass)

planet_panda = pd.DataFrame.from_dict(planet_dict)
print(planet_panda)

plt.figure()
plt.scatter(planet_panda["Radius"], planet_panda["Mass"])
plt.xlabel("Radius")
plt.ylabel("Mass")
plt.show()
