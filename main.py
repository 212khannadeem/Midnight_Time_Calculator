import tkinter as tk
from datetime import datetime, timedelta

window=tk.Tk()
# title
window.title("Midnight Time Calculator")

# creating level and entry field for sunset
sunset_label = tk.Label(window, text="Sunset Time (HH:MM): ")
sunset_label.pack()
sunset_entry = tk.Entry(window)
sunset_entry.pack()

# creating level and entry field for sunset
sunrise_lebel=tk.Label(window, text="Enter Sunrise Time(HH:MM)")
sunrise_lebel.pack()
sunrise_entry = tk.Entry(window)
sunrise_entry.pack()

result_label = tk.Label(window, text="")
result_label.pack()


def calculate_midnight_time():
    sunrise_time = datetime.strptime(sunrise_entry.get(), "%H:%M")
    sunset_time = datetime.strptime(sunset_entry.get(), "%H:%M")

    # Calculate the difference between sunset and sunrise times
    time_diff = sunset_time - sunrise_time

    # Add half of the time difference to the sunrise time
    midnight_time = sunrise_time + (time_diff / 2)

    # Display the midnight time
    result_label.config(text=f"Midnight Time: {midnight_time.strftime('%H:%M')}")

calculate_button = tk.Button(window, text="Calculate", command=calculate_midnight_time)
calculate_button.pack()


window.mainloop()


