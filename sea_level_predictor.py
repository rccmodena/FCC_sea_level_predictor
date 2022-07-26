import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.rcParams.update({'font.size': 16})
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.scatter(df["Year"], df["CSIRO Adjusted Sea Level"], s=30, facecolor='C0', edgecolor='black')
    
    # Create first line of best fit
    regression = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    years = [year for year in range(1880, 2051)]
    ax.plot(years,[year * regression.slope + regression.intercept for year in years], c='orange')

    # Create second line of best fit
    df_2000 = df[df["Year"] >= 2000].copy()

    regression = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    years_2000 = [year for year in range(2000, 2051)]
    ax.plot(years_2000, [year * regression.slope + regression.intercept for year in years_2000], c='red')

    # Add labels and title
    ax.set(xlabel="Year", ylabel='Sea Level (inches)', title="Rise in Sea Level")
    fig.tight_layout()

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()