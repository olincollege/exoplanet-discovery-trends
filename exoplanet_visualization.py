from exoplanet_data_generation import (
    discovery_year_dict,
    planet_distance_dict,
    planet_year_dict,
    planet_panda,
)
import matplotlib.pyplot as plt


def plot_disc_year_bars(start_year, end_year):
    """
    Creates a bar graph of the year vs the number of discovered exoplanets

    The x-axis represent the discovery year and the y-axis represents the
    number of planets discovered in each year.

    Args:
        start_year: an integer representing the year the graph starts at
        end_year: an integer representing the year the graph ends at
    """

    limit_discovery_year_dict = {
        year: value
        for year, value in discovery_year_dict.items()
        if (year >= start_year) & (year <= end_year)
    }

    years = list(limit_discovery_year_dict.keys())
    values = list(limit_discovery_year_dict.values())

    plt.bar(
        years,
        values,
    )
    plt.locator_params(axis="both", integer=True, tight=True)
    plt.title("Number of Exoplanet Discoveries Over the Years")
    plt.xlabel("Year")
    plt.ylabel("Number of Exoplanets Discovered")


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

    limit_planet_year_dict = {}
    limit_planet_distance_dict = {}

    for discovery_type, years in planet_year_dict.items():
        limit_years_list = []
        limit_distance_list = []

        for i, year in enumerate(years):
            if (year >= start_year) & (year <= end_year):
                limit_years_list.append(year)
                limit_distance_list.append(planet_distance_dict[discovery_type][i])

        limit_planet_year_dict[discovery_type] = limit_years_list
        limit_planet_distance_dict[discovery_type] = limit_distance_list

    for i, discovery_type in enumerate(planet_distance_dict):
        plt.scatter(
            limit_planet_year_dict[discovery_type],
            limit_planet_distance_dict[discovery_type],
            s=10,
            color=colors[i],
        )

    plt.legend(planet_distance_dict.keys())
    plt.title("Exoplanet Distance v. Discovery Year and Discovery Method")
    plt.xlabel("Discovery Year")
    plt.ylabel("Distance from Earth (parsecs)")
    plt.show()


def plot_disc_year_vs_period(
    start_year=1992, end_year=2024, min_orb_period=0, max_orb_period=8000
):
    """
    Creates a scatter plot of exoplanet orbital period vs their discovery
    years

    The x-axis represents the discovery year and they y-axis represents
    the orbital period in days

    Args:
        start_year: integer representing the start year on the x-axis
        end_year: integer representing the end year on the x-axis
        min_orb_period: integer representing the start period on the y-axis
        max_orb_period: integer representing the end period on the y-axis
    """
    plt.figure()
    plt.scatter(planet_panda["discovery_year"], planet_panda["period"])
    plt.title("Exoplanet Orbital Period vs. Discovery Year")
    plt.xlabel("Discovery Year")
    plt.ylabel("Orbital Period")
    plt.xlim(start_year, end_year)
    plt.ylim(min_orb_period, max_orb_period)
    plt.show()
