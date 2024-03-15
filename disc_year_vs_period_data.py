import xml.etree.ElementTree as ET
import urllib.request
import gzip
import io

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
