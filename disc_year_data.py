import xml.etree.ElementTree as ET
import urllib.request
import gzip
import io

url = "https://github.com/OpenExoplanetCatalogue/oec_gzip/raw/master/systems.xml.gz"
oec = ET.parse(gzip.GzipFile(fileobj=io.BytesIO(urllib.request.urlopen(url).read())))

discovery_year_list = []
for system in oec.findall(".//system"):
    for planet in system.findall(".//planet"):
        discovery_year = planet.findtext("discoveryyear")

        if discovery_year != None:
            discovery_year_list.append(int(discovery_year))
