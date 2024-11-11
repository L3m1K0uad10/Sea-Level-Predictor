import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Reading data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Creating scatter plot
    plt.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"],
        marker = "o",
        color = "blue",
        s = 10
    )

    # Creating first line of best fit
    slope, intercept, r, p, se = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_1 = np.arange(1880, 2051)
    y_1 = intercept + slope * x_1

    plt.plot(x_1, y_1, "r")

    # Creating second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    slope, intercept, r, p, se = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_2 = np.arange(2000, 2051)
    y_2 = intercept + slope * x_2

    plt.plot(x_2, y_2, 'y')

    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Saving plot and returning data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()