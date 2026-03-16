import tkinter as tk
from tkinter import Listbox, StringVar, Radiobutton, Button, Label, END

# Wage ratios relative to a White man (1.00). Source: BLS 2023, AAUW, Pew Research.
WAGE_RATIOS = {
    ("Male",              "White"):           1.00,
    ("Male",              "Asian"):           1.15,
    ("Male",              "Black"):           0.76,
    ("Male",              "Hispanic/Latino"): 0.68,
    ("Male",              "Native American"): 0.70,
    ("Male",              "Multiracial"):     0.83,
    ("Female",            "White"):           0.79,
    ("Female",            "Asian"):           0.87,
    ("Female",            "Black"):           0.64,
    ("Female",            "Hispanic/Latino"): 0.54,
    ("Female",            "Native American"): 0.51,
    ("Female",            "Multiracial"):     0.68,
    ("Non-binary",        "White"):           0.82,
    ("Non-binary",        "Asian"):           0.90,
    ("Non-binary",        "Black"):           0.67,
    ("Non-binary",        "Hispanic/Latino"): 0.58,
    ("Non-binary",        "Native American"): 0.60,
    ("Non-binary",        "Multiracial"):     0.72,
    ("Prefer not to say", "White"):           0.90,
    ("Prefer not to say", "Asian"):           1.00,
    ("Prefer not to say", "Black"):           0.70,
    ("Prefer not to say", "Hispanic/Latino"): 0.61,
    ("Prefer not to say", "Native American"): 0.65,
    ("Prefer not to say", "Multiracial"):     0.77,
}

EDUCATION_MULTIPLIERS = {
    "Less than High School": 0.65,
    "High School Diploma":   0.80,
    "Some College":          0.90,
    "Associate Degree":      0.95,
    "Bachelor's Degree":     1.20,
    "Master's Degree":       1.40,
    "Doctoral Degree":       1.65,
    "Professional Degree":   1.80,
}

NATIONAL_MEDIAN = 59000


def calculate(gender, race, education):
    """Returns (user_salary, baseline_salary, gap_dollars, gap_pct, ratio)."""
    ratio           = WAGE_RATIOS.get((gender, race), 1.0)
    edu_mult        = EDUCATION_MULTIPLIERS.get(education, 1.0)
    user_salary     = round(NATIONAL_MEDIAN * ratio * edu_mult, 2)
    baseline_salary = round(NATIONAL_MEDIAN * 1.0 * edu_mult, 2)
    gap_dollars     = round(baseline_salary - user_salary, 2)
    gap_pct         = round((gap_dollars / baseline_salary) * 100, 1) if baseline_salary else 0
    return user_salary, baseline_salary, gap_dollars, gap_pct, ratio


# ── Window setup ──────────────────────────────────────────────────────────────

window = tk.Tk()
window.title("Wage Gap Calculator")
window.geometry("1000x680")
window.configure(bg="#1a1a2e")

HEADING_FONT = ("Arial", 13, "bold")
LABEL_FONT   = ("Arial", 11)
RESULT_FONT  = ("Arial", 12)

# ── Gender ────────────────────────────────────────────────────────────────────

tk.Label(window, text="Gender", font=HEADING_FONT,
         bg="#1a1a2e", fg="white").pack(pady=(20, 5))

gender_var   = StringVar(value="Male")
gender_frame = tk.Frame(window, bg="#1a1a2e")
gender_frame.pack()

for option in ["Male", "Female", "Non-binary", "Prefer not to say"]:
    Radiobutton(
        gender_frame, text=option, variable=gender_var, value=option,
        font=LABEL_FONT, bg="#1a1a2e", fg="white",
        selectcolor="#e94560", activebackground="#1a1a2e", activeforeground="white"
    ).pack(side="left", padx=10)

# ── Race / Ethnicity ──────────────────────────────────────────────────────────

tk.Label(window, text="Race / Ethnicity", font=HEADING_FONT,
         bg="#1a1a2e", fg="white").pack(pady=(15, 5))

race_listbox = Listbox(
    window, height=6, font=LABEL_FONT,
    bg="#0f0f1a", fg="white", selectbackground="#e94560",
    selectforeground="white", bd=0, highlightthickness=1,
    highlightcolor="#e94560"
)
for item in ["White", "Black", "Hispanic/Latino", "Asian", "Native American", "Multiracial"]:
    race_listbox.insert(END, item)
race_listbox.select_set(0)
race_listbox.pack()

# ── Education Level ───────────────────────────────────────────────────────────

tk.Label(window, text="Education Level", font=HEADING_FONT,
         bg="#1a1a2e", fg="white").pack(pady=(15, 5))

education_listbox = Listbox(
    window, height=8, font=LABEL_FONT,
    bg="#0f0f1a", fg="white", selectbackground="#e94560",
    selectforeground="white", bd=0, highlightthickness=1,
    highlightcolor="#e94560", exportselection=False
)
for item in EDUCATION_MULTIPLIERS.keys():
    education_listbox.insert(END, item)
education_listbox.select_set(4)  # Default to Bachelor's Degree
education_listbox.pack()
# Put exportselection=False to make sure the person can track which selection they currently have
# ── Button and results ────────────────────────────────────────────────────────

def show_statistics():
    gender  = gender_var.get()
    race_sel = race_listbox.curselection()
    edu_sel  = education_listbox.curselection()

    # Fall back to defaults if the user somehow clicks before selecting
    race      = race_listbox.get(race_sel[0]) if race_sel else "White"
    education = education_listbox.get(edu_sel[0]) if edu_sel else "Bachelor's Degree"

    user_salary, baseline_salary, gap_dollars, gap_pct, ratio = calculate(
        gender, race, education
    )
    

    result_label.config(
        if gap_dollars <= 0:
            text=(
                    f"Profile: {gender}  |  {race}  |  {education}\n\n"
                    f"Your estimated salary:    ${user_salary:,.2f}\n"
                    f"White man baseline:       ${baseline_salary:,.2f}\n"
                   f"Annual gap:               ${gap_dollars*-1:,.2f}  ({gap_pct*-1}% more)\n"
                    f"Wage ratio:               ${ratio:.2f} per White man's $1.00"
        )
        else :
            text=(
                    f"Profile: {gender}  |  {race}  |  {education}\n\n"
                    f"Your estimated salary:    ${user_salary:,.2f}\n"
                    f"White man baseline:       ${baseline_salary:,.2f}\n"
                    f"Annual gap:               ${gap_dollars:,.2f}  ({gap_pct}% less)\n"
                    f"Wage ratio:               ${ratio:.2f} per White man's $1.00"
        ),
        fg="#4ecca3"
    )
Button(
    window, text="See My Statistics", command=show_statistics,
    font=("Arial", 12, "bold"), bg="#e94560", fg="white",
    activebackground="#c73652", activeforeground="white",
    relief="flat", padx=20, pady=8
).pack(pady=(15, 5))

# Result label sits below the button
result_label = tk.Label(
    window, text="", font=RESULT_FONT,
    bg="#1a1a2e", fg="#4ecca3", justify="left"
)
result_label.pack(pady=(10, 20))

window.mainloop()
