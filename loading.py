import requests
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": "-23.5475",
    "longitude": "-46.6361",
    "hourly": "temperature_2m",
    "timezone": "America/Sao_Paulo"
}

response = requests.get(url, params=params)

data = response.json()
temps = data['hourly']['temperature_2m']

grid = np.array(temps).reshape(7, 24)
highs = grid.max(axis=1)

times = pd.DataFrame(data['hourly'])
times['time'] = pd.to_datetime(times['time'])

fig, ax = plt.subplots(figsize=(18, 6))


def main() -> None:
    ax.plot(times['time'], temps, color="red")
    ax.set_title("7-Day Hourly Temperature in São Paulo")
    ax.set_xlabel("Time")
    ax.set_ylabel("Temperature (°C)")
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.show()


if __name__ == "__main__":
    main()
