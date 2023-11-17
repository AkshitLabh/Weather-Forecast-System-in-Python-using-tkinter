import requests
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

def gen_report():
    city = city_entry.get()
    url = 'https://wttr.in/{}'.format(city)
    try:
        response = requests.get(url)
        weather_report = response.text
        result_text.delete(1.0, tk.END)  # Clear the previous content
        result_text.insert(tk.END, weather_report)
        result_text.tag_configure("darker", foreground="darkblue")  # Define a darker color tag
        result_text.tag_add("darker", "1.0", "end")  # Apply the darker color tag to the entire text
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error Occurred")

# Create the main window
window = tk.Tk()
window.title('Colorful Weather Forecaster')
window.configure(bg='lightgray')  # Set a common background color

# Welcome message
welcome_label = tk.Label(window, text="Welcome to the Colorful Weather Forecaster!", bg='lightgray', fg='blue')
welcome_label.pack()

instructions_label = tk.Label(window, text="Just enter the City you want the weather report for and click on the button. It's that simple!", bg='lightgray')
instructions_label.pack()

# Entry for city name
city_entry = tk.Entry(window)
city_entry.pack()

# Button to generate report
generate_button = tk.Button(window, text="Get Weather Report", command=gen_report, bg='green', fg='white')
generate_button.pack()

# ScrolledText widget to display the weather report without text wrapping
result_text = ScrolledText(window, wrap="none", height=60, width=90, bg='lightgray')
result_text.pack()

# Start the tkinter main loop
window.mainloop()
