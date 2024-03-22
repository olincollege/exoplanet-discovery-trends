import pandas as pd
import matplotlib.pyplot as plt
from disc_method_color_data import planet_dict, time_planet_dict


def plot_disc_method_color():
    """
    Creates a scatter plot of the distance of discovered exoplanets over time.

    The x-axis represents the discovery year and the y-axis represents the distance
    (in parsecs) between the exoplanet and our Sun. Each dot is color coded
    based on the method used to discover the exoplanet.
    """

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
    plt.title("Exoplanet Distance v. Discovery Year and Discovery Method")
    plt.xlabel("Discovery Year")
    plt.ylabel("Distance from Earth (parsecs)")
    plt.show()
