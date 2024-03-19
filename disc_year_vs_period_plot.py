from disc_year_vs_period_data import planet_dict
import pandas as pd
import matplotlib.pyplot as plt

planet_panda = pd.DataFrame.from_dict(planet_dict)
# planet_panda.plot.scatter(x="Radius", y="Mass", c="DarkBlue")
print(planet_panda)
plt.figure()
plt.scatter(planet_panda["discovery_year"], planet_panda["period"])
plt.title("Exoplanet Orbital Period vs. Discovery Year")
plt.xlabel("Discovery Year")
plt.ylabel("Orbital Period")
plt.xlim(1992, 2024)
plt.ylim(0, 8000)
plt.show()
