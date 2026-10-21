import pandas as pd

MOVING_AVERAGE_DAYS = 7
SPIKE_THRESHOLD = 0.2

def find_sales_spikes(sales, window_days = MOVING_AVERAGE_DAYS):
    daily_sales = sales.groupby("date")["amount"].sum()
    moving_average = daily_sales.rolling(window_days).mean()
    deviation = daily_sales / moving_average - 1
    return deviation[deviation > SPIKE_THRESHOLD]
