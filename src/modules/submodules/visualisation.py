from modules.submodules.dataframe import init as dataframe_init
import matplotlib.pyplot as pl
from itertools import cycle


def init(con):
    headings, dfs = dataframe_init(con, True)
    cycol = cycle("bgrcmk")
    for i, df in enumerate(dfs):
        pl.title(headings[i])
        pl.bar(
            list(df.iloc[:, 0]),
            list(df.iloc[:, 2]),
            color=[next(cycol) for _ in range(0, len(df))],
        )
        pl.show()
