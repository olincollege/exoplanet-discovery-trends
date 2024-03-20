from disc_year_data import discovery_year_list
import matplotlib.pyplot as plt
import numpy as np


def plot_disc_year_histogram(start_year, end_year):

    plt.hist(
        [
            year
            for year in discovery_year_list
            if (year >= start_year) & (year <= end_year)
        ],
        bins=30,
        edgecolor="black",
    )
    plt.autoscale(axis="y")
    plt.title("Number of Exoplanet Discoveries Over the Years")
    plt.xlabel("Year")
    plt.ylabel("Number of Exoplanets Discovered")
    plt.show()
