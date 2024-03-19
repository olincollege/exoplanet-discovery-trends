from disc_year_data import discovery_year_list
import matplotlib.pyplot as plt

plt.hist(discovery_year_list, bins=250, edgecolor="black")
plt.title("Number of Exoplanet Discoveries Over the Years")
plt.xlim(1992, 2024)
plt.xlabel("Year")
plt.ylabel("Number of Exoplanets Discovered")
plt.show()
