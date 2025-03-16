
import tkinter as tk
from tkinter import messagebox
import joblib
import numpy as np

# Load the trained Random Forest model
model = joblib.load('random_forest_model.pkl')

# Function to create tooltips
def create_tooltip(widget, text):
    tooltip = tk.Toplevel(widget, bg='white', padx=5, pady=5)
    tooltip.overrideredirect(True)
    tooltip.withdraw()
    label = tk.Label(tooltip, text=text, bg='white')
    label.pack()
    
    def show_tooltip(event):
        tooltip.geometry(f"+{event.x_root + 10}+{event.y_root + 10}")
        tooltip.deiconify()
    
    def hide_tooltip(event):
        tooltip.withdraw()
    
    widget.bind("<Enter>", show_tooltip)
    widget.bind("<Leave>", hide_tooltip)

# Define the GUI window
root = tk.Tk()
root.title('Heart Disease Prediction')
root.geometry('450x550')

# Function to predict heart disease
def predict_heart_disease():
    try:
        # Get user input
        age = int(entry_age.get())
        sex = int(entry_sex.get())
        cp = int(entry_cp.get())
        trestbps = int(entry_trestbps.get())
        chol = int(entry_chol.get())
        fbs = int(entry_fbs.get())
        restecg = int(entry_restecg.get())
        thalach = int(entry_thalach.get())
        exang = int(entry_exang.get())
        oldpeak = float(entry_oldpeak.get())
        slope = int(entry_slope.get())
        ca = int(entry_ca.get())
        thal = int(entry_thal.get())

        # Prepare the data for prediction
        input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        # Predict using the trained model
        prediction = model.predict(input_data)

        # Show the result in a message box
        if prediction[0] == 1:
            result = "The person is likely to have heart disease."
        else:
            result = "The person is not likely to have heart disease."
        messagebox.showinfo("Prediction Result", result)

    except Exception as e:
        messagebox.showerror("Input Error", f"Please check your inputs. {str(e)}")

# Create labels, entries, and info buttons for each feature
def add_input_with_info(label_text, description, row):
    label = tk.Label(root, text=label_text)
    label.grid(row=row, column=0, pady=5)
    
    entry = tk.Entry(root)
    entry.grid(row=row, column=1, pady=5)
    
    info_button = tk.Button(root, text="i", width=2, height=1, relief="solid")
    info_button.grid(row=row, column=2)
    create_tooltip(info_button, description)
    
    return entry

# Adding input fields with descriptions
entry_age = add_input_with_info("Age", "The age of the patient (e.g., 29, 50).", 0)
entry_sex = add_input_with_info("Sex (1: Male, 0: Female)", "1 for male and 0 for female.", 1)
entry_cp = add_input_with_info("Chest Pain Type (0-3)", "Type of chest pain experienced (0-3).", 2)
entry_trestbps = add_input_with_info("Resting Blood Pressure", "Resting blood pressure in mmHg.", 3)
entry_chol = add_input_with_info("Serum Cholesterol (mg/dl)", "Serum cholesterol in mg/dl.", 4)
entry_fbs = add_input_with_info("Fasting Blood Sugar (>120 mg/dl, 1=True, 0=False)", "1 if fasting blood sugar > 120 mg/dl, else 0.", 5)
entry_restecg = add_input_with_info("Resting ECG Results (0-2)", "Results of resting ECG (0-2).", 6)
entry_thalach = add_input_with_info("Max Heart Rate Achieved", "Maximum heart rate achieved.", 7)
entry_exang = add_input_with_info("Exercise Induced Angina (1=Yes, 0=No)", "1 if exercise-induced angina, else 0.", 8)
entry_oldpeak = add_input_with_info("Oldpeak (ST Depression)", "ST depression induced by exercise relative to rest.", 9)
entry_slope = add_input_with_info("Slope (0-2)", "The slope of the peak exercise ST segment (0-2).", 10)
entry_ca = add_input_with_info("Number of Major Vessels (0-3)", "Number of major vessels colored by fluoroscopy (0-3).", 11)
entry_thal = add_input_with_info("Thal (3=Normal, 6=Fixed Defect, 7=Reversible Defect)", "Thalassemia type (3, 6, 7).", 12)

# Button to make the prediction
button_predict = tk.Button(root, text="Predict", command=predict_heart_disease)
button_predict.grid(row=13, column=1, pady=20)

# Start the GUI event loop
root.mainloop()
