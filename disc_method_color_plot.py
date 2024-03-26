import matplotlib.pyplot as plt
from disc_method_color_data import planet_dict, time_planet_dict


def plot_disc_method_color(start_year, end_year):
    """
    Creates a scatter plot of the distance of discovered exoplanets over time
    given a start and end year.

    The x-axis represents the discovery year and the y-axis represents the
    distance (in parsecs) between the exoplanet and our Sun. Each dot is color
    coded based on the method used to discover the exoplanet.

    Args:
        start_year: an integer representing the year the graph starts at
        end_year: an integer representing the year the graph ends at
    """

    plt.figure(figsize=(15, 8))
    colors = ["r", "b", "g", "darkorchid", "c", "lime", "fuchsia"]

    limit_time_planet_dict = {}
    limit_planet_dict = {}

    for discovery_type, years in time_planet_dict.items():
        limit_years_list = []
        limit_distance_list = []

        for i, year in enumerate(years):
            if (year >= start_year) & (year <= end_year):
                limit_years_list.append(year)
                limit_distance_list.append(planet_dict[discovery_type][i])

        limit_time_planet_dict[discovery_type] = limit_years_list
        limit_planet_dict[discovery_type] = limit_distance_list

    for i, discovery_type in enumerate(planet_dict):
        plt.scatter(
            limit_time_planet_dict[discovery_type],
            limit_planet_dict[discovery_type],
            s=10,
            color=colors[i],
        )

    plt.legend(planet_dict.keys())
    plt.title("Exoplanet Distance v. Discovery Year and Discovery Method")
    plt.xlabel("Discovery Year")
    plt.ylabel("Distance from Earth (parsecs)")
    plt.show()
