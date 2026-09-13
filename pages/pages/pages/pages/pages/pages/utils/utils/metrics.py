def rolling_average(series, window=5):
    return series.tail(window).mean()
