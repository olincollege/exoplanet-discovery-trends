from disc_year_vs_period_data import planet_dict
import pandas as pd
import matplotlib.pyplot as plt

planet_panda = pd.DataFrame.from_dict(planet_dict)
# planet_panda.plot.scatter(x="Radius", y="Mass", c="DarkBlue")
print(planet_panda)
plt.figure()
plt.scatter(planet_panda["period"], planet_panda["discovery_year"])
plt.xlabel("period")
plt.ylabel("discovery_year")
plt.xlim(0, 8000)
plt.ylim(1992, 2024)
plt.show()
