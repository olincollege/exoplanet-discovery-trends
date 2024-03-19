import pandas as pd
import matplotlib.pyplot as plt
from disc_method_color_data import planet_dict, time_planet_dict

plt.figure(figsize=(15, 8))
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
