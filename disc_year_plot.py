from disc_year_data import discovery_year_dict
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
