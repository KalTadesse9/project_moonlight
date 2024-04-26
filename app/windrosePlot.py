import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from windrose import WindroseAxes 

def plotWindrose(df):
    wd = df['WD']
    ws = df['WS']
    ax = WindroseAxes.from_ax()
    ax.set_title("Windrose from 2021 - 2022")
    ax.bar(wd,ws,normed=True)
    ax.set_legend()

    fmt = '%.0f%%' 
    yticks = mtick.FormatStrFormatter(fmt)
    ax.yaxis.set_major_formatter(yticks)
    return ax
