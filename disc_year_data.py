import xml.etree.ElementTree as ET
import urllib.request
import gzip
import io

url = "https://github.com/OpenExoplanetCatalogue/oec_gzip/raw/master/systems.xml.gz"
oec = ET.parse(gzip.GzipFile(fileobj=io.BytesIO(urllib.request.urlopen(url).read())))

discovery_year_dict = {}
for system in oec.findall(".//system"):
    for planet in system.findall(".//planet"):
        discovery_year = planet.findtext("discoveryyear")

        if discovery_year is not None:
            discovery_year = int(discovery_year)
            if discovery_year not in discovery_year_dict:
                discovery_year_dict[discovery_year] = 1
            else:
                discovery_year_dict[discovery_year] += 1
