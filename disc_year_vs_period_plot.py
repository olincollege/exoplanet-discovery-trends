import matplotlib.pyplot as plt
from disc_year_vs_period_data import planet_panda


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
