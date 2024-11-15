import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Loan eligibility calculation function
def calculate_eligibility():
    try:
        # Collect inputs
        name = name_entry.get()
        age = int(age_entry.get())
        employment_status = employment_var.get()
        employment_duration = int(employment_duration_entry.get())
        monthly_income = float(monthly_income_entry.get())
        collateral_available = collateral_var.get()
        collateral_worth = float(collateral_worth_entry.get())
        loan_amount = float(loan_amount_entry.get())
        intended_repayment = float(intended_repayment_entry.get())
        collateral_confirmed = collateral_confirmed_var.get()
        credit_score = int(credit_score_entry.get())
        admin_name = admin_name_entry.get()
        date = datetime.now().strftime("%Y-%m-%d")

        # Validate inputs
        if age < 18:
            messagebox.showerror("Error", "Applicant is underage.")
            return
        if not employment_status:
            messagebox.showerror("Error", "Applicant is unemployed.")
            return
        if not collateral_available or collateral_worth <= 0 or not collateral_confirmed:
            messagebox.showerror("Error", "Collateral is missing or unverified.")
            return
        if credit_score < 0 or credit_score > 850:
            messagebox.showerror("Error", "Credit score must be between 0 and 850.")
            return

        # Calculate Debt-to-Income Ratio (DTI)
        dti_ratio = (intended_repayment / monthly_income) * 100

        # Points-based system
        score = 0

        # Employment Duration
        if employment_duration >= 10:
            score += 20
        elif 5 <= employment_duration < 10:
            score += 15
        elif 1 <= employment_duration < 5:
            score += 10
        else:
            score += 0

        # Income Level (monthly income as a percentage of loan amount)
        income_level = (monthly_income / loan_amount) * 100
        if income_level >= 100:
            score += 25
        elif 50 <= income_level < 100:
            score += 20
        elif 25 <= income_level < 50:
            score += 10
        else:
            score += 0

        # Debt-to-Income Ratio
        if dti_ratio < 20:
            score += 20
        elif 20 <= dti_ratio < 35:
            score += 15
        elif 35 <= dti_ratio < 50:
            score += 10
        else:
            score += 0

        # Credit Score
        if credit_score >= 750:
            score += 30
        elif 600 <= credit_score < 750:
            score += 20
        elif 500 <= credit_score < 600:
            score += 10
        else:
            score += 0

        # Eligibility Threshold
        is_eligible = score >= 70
        result = f"""
        Applicant Name: {name}
        Applicant Age: {age}
        Application Date: {date}
        Employment Status: {'Employed' if employment_status else 'Unemployed'}
        Employment Duration: {employment_duration} years
        Monthly Income: ${monthly_income}
        Collateral Worth: ${collateral_worth}
        Loan Amount: ${loan_amount}
        Intended Monthly Repayment: ${intended_repayment}
        Credit Score: {credit_score}
        DTI Ratio: {round(dti_ratio, 2)}%
        Applicant Score: {score}
        Eligibility: {"Eligible" if is_eligible else "Not Eligible"}
        """
        messagebox.showinfo("Loan Eligibility Result", result)

    except ValueError as ve:
        messagebox.showerror("Error", "Please enter valid numerical values.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")


# Create GUI window
window = tk.Tk()
window.title("Loan Eligibility System")
window.geometry("700x850")
window.configure(bg="#f2f2f2")

# Style configurations
label_font = ("Arial", 14, "bold")
entry_font = ("Arial", 14)
button_font = ("Arial", 16, "bold")

# Name
tk.Label(window, text="Name:", font=label_font, bg="#f2f2f2").grid(row=0, column=0, sticky="w", padx=20, pady=10)
name_entry = tk.Entry(window, font=entry_font, width=30)
name_entry.grid(row=0, column=1, padx=20)

# Age
tk.Label(window, text="Age:", font=label_font, bg="#f2f2f2").grid(row=1, column=0, sticky="w", padx=20, pady=10)
age_entry = tk.Entry(window, font=entry_font, width=30)
age_entry.grid(row=1, column=1, padx=20)

# Employment Status
tk.Label(window, text="Employment Status:", font=label_font, bg="#f2f2f2").grid(row=2, column=0, sticky="w", padx=20, pady=10)
employment_var = tk.BooleanVar()
tk.Checkbutton(window, text="Employed", variable=employment_var, font=label_font, bg="#f2f2f2").grid(row=2, column=1, sticky="w", padx=20)

# Employment Duration
tk.Label(window, text="Employment Duration (years):", font=label_font, bg="#f2f2f2").grid(row=3, column=0, sticky="w", padx=20, pady=10)
employment_duration_entry = tk.Entry(window, font=entry_font, width=30)
employment_duration_entry.grid(row=3, column=1, padx=20)

# Monthly Income
tk.Label(window, text="Monthly Income:", font=label_font, bg="#f2f2f2").grid(row=4, column=0, sticky="w", padx=20, pady=10)
monthly_income_entry = tk.Entry(window, font=entry_font, width=30)
monthly_income_entry.grid(row=4, column=1, padx=20)

# Collateral Availability
tk.Label(window, text="Collateral Availability:", font=label_font, bg="#f2f2f2").grid(row=5, column=0, sticky="w", padx=20, pady=10)
collateral_var = tk.BooleanVar()
tk.Checkbutton(window, text="Available", variable=collateral_var, font=label_font, bg="#f2f2f2").grid(row=5, column=1, sticky="w", padx=20)

# Collateral Worth
tk.Label(window, text="Collateral Worth:", font=label_font, bg="#f2f2f2").grid(row=6, column=0, sticky="w", padx=20, pady=10)
collateral_worth_entry = tk.Entry(window, font=entry_font, width=30)
collateral_worth_entry.grid(row=6, column=1, padx=20)

# Loan Amount
tk.Label(window, text="Requested Loan Amount:", font=label_font, bg="#f2f2f2").grid(row=7, column=0, sticky="w", padx=20, pady=10)
loan_amount_entry = tk.Entry(window, font=entry_font, width=30)
loan_amount_entry.grid(row=7, column=1, padx=20)

# Intended Monthly Repayment
tk.Label(window, text="Intended Monthly Repayment:", font=label_font, bg="#f2f2f2").grid(row=8, column=0, sticky="w", padx=20, pady=10)
intended_repayment_entry = tk.Entry(window, font=entry_font, width=30)
intended_repayment_entry.grid(row=8, column=1, padx=20)

# Credit Score
tk.Label(window, text="Credit Score:", font=label_font, bg="#f2f2f2").grid(row=9, column=0, sticky="w", padx=20, pady=10)
credit_score_entry = tk.Entry(window, font=entry_font, width=30)
credit_score_entry.grid(row=9, column=1, padx=20)

# Collateral Confirmation
tk.Label(window, text="Collateral Confirmation:", font=label_font, bg="#f2f2f2").grid(row=10, column=0, sticky="w", padx=20, pady=10)
collateral_confirmed_var = tk.BooleanVar()
tk.Checkbutton(window, text="Confirmed", variable=collateral_confirmed_var, font=label_font, bg="#f2f2f2").grid(row=10, column=1, sticky="w", padx=20)

# Admin Name
tk.Label(window, text="Admin Name:", font=label_font, bg="#f2f2f2").grid(row=11, column=0, sticky="w", padx=20, pady=10)
admin_name_entry = tk.Entry(window, font=entry_font, width=30)
admin_name_entry.grid(row=11, column=1, padx=20)

# Submit Button
submit_button = tk.Button(window, text="Check Eligibility", font=button_font, bg="#4CAF50", fg="white", command=calculate_eligibility)
submit_button.grid(row=12, column=0, columnspan=2, pady=20)

# Run the GUI
window.mainloop()
