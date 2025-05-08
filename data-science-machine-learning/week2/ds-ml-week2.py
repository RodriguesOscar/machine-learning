# save the files 'kiwo.csv', 'umsatzdaten_gekuerzt.csv', and 'wetter.csv' from this GitHub repository:
# https://github.com/opencampus-sh/einfuehrung-in-data-science-und-ml

# create a Jupyter notebook that
# reads the dataset 'umsatzdaten_gekuerzt.csv' and
# uses a bar chart to show the relationship of average sales per weekday.

# in a second step, add confidence intervals for the sales per weekday.

# in a further step, sort the weekdays from Monday to Sunday.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


wetter_file = "https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-und-ml/blob/main/wetter.csv"
kiwo_file = "https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-und-ml/blob/main/kiwo.csv"
umsatzdaten_gekuerzt_file = "https://raw.githubusercontent.com/opencampus-sh/einfuehrung-in-data-science-und-ml/main/umsatzdaten_gekuerzt.csv"


df = pd.read_csv(umsatzdaten_gekuerzt_file)

# Ensure 'Datum' is in datetime format
df["Datum"] = pd.to_datetime(df["Datum"])

# Extract weekday names
df["Wochentag"] = df["Datum"].dt.day_name()

# Group by weekday and calculate mean and standard error
weekday_order = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
sales_stats = (
    df.groupby("Wochentag")["Umsatz"]
    .agg(["mean", "count", "std"])
    .reindex(weekday_order)
)
sales_stats["sem"] = (
    sales_stats["std"] / sales_stats["count"] ** 0.5
)  # standard error of the mean

sales_stats = sales_stats.dropna()

# Plot with confidence intervals (95% CI ≈ mean ± 1.96*sem)
plt.figure(figsize=(10, 6))
ax = sns.barplot(
    x=sales_stats.index,
    y=sales_stats["mean"],
    errorbar=None,
)
plt.errorbar(
    x=range(len(sales_stats)),
    y=sales_stats["mean"],
    yerr=1.96 * sales_stats["sem"],
    fmt='none',
    capsize=5,
    color='black'
)
plt.ylabel("Durchschnittlicher Umsatz")
plt.xlabel("Wochentag")
plt.title("Durchschnittlicher Umsatz pro Wochentag mit Konfidenzintervallen (95%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("umsatz_pro_wochentag.png")
