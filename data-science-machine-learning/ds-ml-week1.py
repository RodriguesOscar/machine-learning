import pandas as pd
from scipy.stats import ttest_ind

# Load dataset offline
# df = pd.read_csv("wetter-data/wetter.csv")

### Load dataset online, so you can run the code without downloading the file and fetch realtime data from github
url = "https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-und-ml/main/wetter.csv"
df = pd.read_csv(url)

# Convert date column to datetime
df["Datum"] = pd.to_datetime(df["Datum"])

# Overall average temperature
overall_avg_temp = df["Temperatur"].mean()
print("Overall average temperature:", overall_avg_temp)

# July average temperature
july_data = df[df["Datum"].dt.month == 7]
july_avg_temp = july_data["Temperatur"].mean()
print("July average temperature:", july_avg_temp)

# May average temperature
may_data = df[df["Datum"].dt.month == 5]
may_avg_temp = may_data["Temperatur"].mean()
print("May average temperature:", may_avg_temp)

# T-test to compare July and May temperatures
temperature_difference_t_statistic, significance_probability_p_value = ttest_ind(
    july_data["Temperatur"], may_data["Temperatur"], equal_var=False
)
print(
    "T-test statistic (larger values mean the temperature averages of July and May are more likely truly different):",
    temperature_difference_t_statistic,
)
print(
    "P-value (probability that the difference is just random chance):",
    significance_probability_p_value,
)

# Possible interpretation of the result
if significance_probability_p_value < 0.05:
    print(
        "Conclusion: Yes, the average temperatures in July and May differ significantly."
    )
else:
    print(
        "Conclusion: No, there is no significant difference between the average temperatures in July and May."
    )
