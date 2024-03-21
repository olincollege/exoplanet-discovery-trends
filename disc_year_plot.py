from bartest import discovery_year_dict
import matplotlib.pyplot as plt


def plot_disc_year_bars(start_year, end_year):

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
