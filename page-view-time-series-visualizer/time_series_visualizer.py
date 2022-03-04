import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import numpy as np
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)

# Clean data
df = df[(df['value']>df['value'].quantile(0.025)) &
       ((df['value']<df['value'].quantile(0.975)))]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(18,6))
    plt.plot(df,color='firebrick')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy(deep=True)
    df_bar['year'] = df_bar.index.year
    months = ["January", "February", "March", "April", "May", "June", "July", "August",
              "September", "October", "November", "December"]
    df_bar['month'] = df_bar.index.month_name()
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=months)
    df_bar_pivot = pd.pivot_table(
        df_bar,
        values="value",
        index="year",
        columns="month",
        aggfunc=np.mean
    )

    # Draw bar plot
    fig = df_bar_pivot.plot(kind='bar').get_figure()
    fig.set_figheight(6)
    fig.set_figwidth(8)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
              "Sep", "Oct", "Nov", "Dec"]
    df_box['month'] = pd.Categorical(df_box['month'], categories=months)

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2,figsize=(18,6))
    plt.subplot(1, 2, 1)
    sns.boxplot(x=df_box['year'], y=df_box['value']).get_figure()
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df_box['month'], y=df_box['value']).get_figure()
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig