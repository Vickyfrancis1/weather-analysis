import pandas as pd
import matplotlib.pyplot as plt

log = pd.read_json(r"C:\Users\user\weather_log.json")
log = log.drop_duplicates()

averages = log.groupby("city")["temp"].mean()
averages.plot(kind="bar")
plt.title("Average temperature by city")
plt.ylabel("Temperature(°C)")
plt.savefig("average_temps.png")
plt.show()

log["time"] = pd.to_datetime(log["time"])

table = log.pivot_table(index="time", columns="city", values="temp")
table.plot(marker="o")
plt.title("Temperature over time")
plt.ylabel("Temperature (degrees C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("temps_over_time.png")
plt.show()