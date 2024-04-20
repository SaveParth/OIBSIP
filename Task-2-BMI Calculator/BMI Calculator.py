import tkinter as tk

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def calculate_button_clicked():
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)
    result_label.config(text=f"BMI: {bmi:.2f}, Category: {category}", fg="blue", font=("Helvetica", 12, "bold"))


window = tk.Tk()
window.title("BMI Calculator")
window.geometry("300x150")  

tk.Label(window, text="Weight (kg):",fg="Red", font=("Aerial", 10)).grid(row=0, column=0, padx=5, pady=5)
weight_entry = tk.Entry(window)
weight_entry.grid(row=0, column=1, padx=5, pady=5)


tk.Label(window, text="Height (m):",fg="Green", font=("Aerial", 10)).grid(row=1, column=0, padx=5, pady=5)
height_entry = tk.Entry(window)
height_entry.grid(row=1, column=1, padx=5, pady=5)


calculate_button = tk.Button(window, text="Calculate",fg="Purple", command=calculate_button_clicked, font=("Times new Roman", 12, "bold"))
calculate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=10)


result_label = tk.Label(window, text="", font=("Aerial", 20))
result_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()
