import matplotlib
import matplotlib.colors as mcolors
from cycler import cycler

matplotlib.rcParams['font.sans-serif'] = 'Akkurat Pro'
matplotlib.rcParams['font.serif'] = 'Vesterbro'
matplotlib.rcParams['font.family'] = 'sans-serif'
matplotlib.rcParams['font.size'] = '50'

matplotlib.rcParams['figure.figsize'] = (50, 15)
matplotlib.rcParams['figure.titlesize'] = '50'

matplotlib.rcParams['axes.titlesize'] = '50'
matplotlib.rcParams['axes.labelsize'] = '50'
matplotlib.rcParams['axes.labelpad'] = '50'
matplotlib.rcParams['xtick.labelsize'] = '40'
matplotlib.rcParams['ytick.labelsize'] = '40'

matplotlib.rcParams['legend.fontsize'] = '40'
matplotlib.rcParams['legend.title_fontsize'] = '40'

matplotlib.rcParams['xtick.major.pad'] = '30'
matplotlib.rcParams['ytick.major.pad'] = '30'

matplotlib.rcParams['legend.frameon'] = False
matplotlib.rcParams['axes.facecolor'] = '#00000000'

flux_colors = {
    'green': '#007565',
    'pink': '#F8E3DE',
    'mint': '#9FD4CD',

    'snow': '#F5F5F5',
    'black': '#121212',

    'merman': '#248E7A',
    'sage': '#51B79C',
    'tmnt': '#034D42',

    'fairy': '#FCE8E2',
    'percy': '#F3D9D5',
    'chansey': '#EECFCE'
}

matplotlib.rcParams['axes.prop_cycle'] = cycler(color=flux_colors.values())
mcolors.get_named_colors_mapping().update(flux_colors)


def finalise(ax):
    for tick in ax.get_xticklabels():
        tick.set_fontfamily('serif')

    for tick in ax.get_yticklabels():
        tick.set_fontfamily('serif')