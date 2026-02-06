"""
 Download CIMIS data from https://cimis.water.ca.gov/WSNReportCriteria.aspx
"""

import pandas as pd
import statsmodels.api as sm
import sys

fn_csv = 'cimis-daily-5-139.csv'
df = pd.read_csv(fn_csv)
df = df[['Avg Air Temp (F)', 'Avg Rel Hum (%)', 'Precip (in)']].dropna()

print(df.head())
temp = df['Avg Air Temp (F)']
humid = df['Avg Rel Hum (%)']
rain = df['Precip (in)']

temp_fit = sm.OLS(rain, sm.add_constant(temp)).fit()
humid_fit = sm.OLS(rain, sm.add_constant(humid)).fit()

print("\n___ Temperature and Rain fit ___", temp_fit.summary())
print("\n___ Humidity and Rain fit ___", humid_fit.summary())

print(f"\nR-value for fit rain:\t tempurature={temp_fit.rsquared:.5f}"
      f" \t humidity={humid_fit.rsquared:.5f}")
