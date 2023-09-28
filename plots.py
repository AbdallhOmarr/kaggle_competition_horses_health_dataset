import seaborn as sns
import matplotlib.pyplot as plt

def histplot(data, bins=None, xlim=None, xticks=None, xtick_rotation=None):

    # Create a histplot with the specified number of bins
    if bins:
        sns.histplot(data, bins=bins, kde=False, color='blue')
    else:
        sns.histplot(data,  kde=False, color='blue')
    # Get the axes
    ax = plt.gca()

    # Annotate each bin with its count
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height())}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom')

    # Set xlim if provided
    if xlim:
        ax.set_xlim(xlim)

    # Set xticks if provided
    if xticks:
        ax.set_xticks(xticks)

    # Rotate x-axis labels if rotation is specified
    if xtick_rotation:
        ax.tick_params(axis='x', labelrotation=xtick_rotation)

    # Show the plot
    plt.show()
