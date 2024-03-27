# Exoplanet Discovery Trends
This project looks at the data and characteristics of discovered exoplanets to find trends in exoplanet discovery over 
time. We looked at exoplanet discovery methods, orbital period, and distance, and how each changed over time as 
more exoplanets were discovered.

## Data Source
We used data from the Open Exoplanet Catalog (OEC)
(GitHub repo link: https://github.com/OpenExoplanetCatalogue/open_exoplanet_catalogue/tree/d778792da9e83a8c8fefd97697ea4eade8463047).
The OEC GitHub repository has some example code that shows how to obtain their data.

## Implementation
To run the code used in our project and on the OEC repository, import the libraries and modules found in the `requirements.txt` file 
in this repository. 

We followed the instructions in the OEC repository to obtain our data, and then we stored the data in dictionaries and pandas 
data frames (see `exoplanet_data_generation.py`). This allowed us to visualize and plot the data (see functions in 
`exoplanet_visualization.py`). Using the code in these files should result in the same plots as those found in `computational_essay.py`.

To make similar plots with different characteristics, look at the OEC repository README's "Data Structure" section.
This shows how all the characteristics are categorized, which can change how you go about obtaining the data. For example, `planet` 
is a child of `system` (planetary system) and `period` (orbital period) is a child of `planet`. However, `distance` is a child of
`system`, rather than `planet`, so it would be obtained from the planetary systems rather than the planets themselves 
(unlike the orbital period which is obtained from the planets). Code for obtaining these can be found in `exoplanet_data_generation.py`.
