"""
Wage Gap Calculator
Based on BLS 2023 data, AAUW research, and Pew Research Center findings.
Compares expected salary to a White male baseline and projects lifetime earnings gaps.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


# ── Wage ratio data relative to White men (baseline = 1.0) ──────────────────
# Sources: BLS Highlights of Women's Earnings 2023, AAUW, Pew Research Center

WAGE_RATIOS = {
    # (gender, race): ratio vs white man
    ("man",   "white"):           1.00,
    ("man",   "asian"):           1.15,
    ("man",   "black"):           0.76,
    ("man",   "hispanic/latino"): 0.68,
    ("man",   "native american"): 0.70,
    ("man",   "multiracial"):     0.83,

    ("woman", "white"):           0.79,
    ("woman", "asian"):           0.87,
    ("woman", "black"):           0.64,
    ("woman", "hispanic/latino"): 0.54,
    ("woman", "native american"): 0.51,
    ("woman", "multiracial"):     0.68,
}

# Industry salary multipliers relative to national median (~$59,000 in 2023)
INDUSTRY_MULTIPLIERS = {
    "technology":          1.85,
    "finance":             1.70,
    "healthcare":          1.30,
    "education":           0.90,
    "retail":              0.70,
    "food service":        0.60,
    "construction":        1.10,
    "manufacturing":       1.05,
    "government":          1.15,
    "nonprofit":           0.85,
    "arts/entertainment":  0.80,
    "other":               1.00,
}

# Education multipliers
EDUCATION_MULTIPLIERS = {
    "less than high school": 0.65,
    "high school diploma":   0.80,
    "some college":          0.90,
    "associate degree":      0.95,
    "bachelor degree":       1.20,
    "master degree":         1.40,
    "doctoral degree":       1.65,
    "professional degree":   1.80,
}

NATIONAL_MEDIAN = 59000  # BLS 2023 median weekly earnings annualized
BASELINE_SALARY  = 75000  # White man baseline used for gap comparison
CAREER_YEARS     = 40     # Standard working career length


def get_choice(prompt, options):
    print(f"\n{prompt}")
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt.title()}")
    while True:
        try:
            choice = int(input("Enter number: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
        except ValueError:
            pass
        print(f"Enter a number between 1 and {len(options)}.")


def get_int(prompt, min_val, max_val):
    while True:
        try:
            val = int(input(prompt))
            if min_val <= val <= max_val:
                return val
        except ValueError:
            pass
        print(f"Enter a number between {min_val} and {max_val}.")


def calculate_salary(gender, race, industry, education, experience_years):
    ratio       = WAGE_RATIOS.get((gender, race), 1.0)
    ind_mult    = INDUSTRY_MULTIPLIERS.get(industry, 1.0)
    edu_mult    = EDUCATION_MULTIPLIERS.get(education, 1.0)
    exp_mult    = 1 + (experience_years * 0.02)   # ~2% growth per year experience

    salary = NATIONAL_MEDIAN * ratio * ind_mult * edu_mult * exp_mult
    return round(salary, 2)


def calculate_baseline_salary(industry, education, experience_years):
    ind_mult = INDUSTRY_MULTIPLIERS.get(industry, 1.0)
    edu_mult = EDUCATION_MULTIPLIERS.get(education, 1.0)
    exp_mult = 1 + (experience_years * 0.02)
    return round(NATIONAL_MEDIAN * 1.0 * ind_mult * edu_mult * exp_mult, 2)


def lifetime_earnings(annual_salary, current_age, retirement_age=65, growth_rate=0.03):
    years = retirement_age - current_age
    total = 0
    salary = annual_salary
    for _ in range(years):
        total += salary
        salary *= (1 + growth_rate)
    return round(total, 2)


def plot_salary_comparison(user_salary, baseline_salary, gender, race, industry):
    fig, axes = plt.subplots(1, 3, figsize=(16, 6))
    fig.patch.set_facecolor("#0f0f1a")
    for ax in axes:
        ax.set_facecolor("#1a1a2e")

    # ── Chart 1: Salary comparison bar chart ────────────────────────────────
    ax1 = axes[0]
    categories = ["You", "White Man\n(Baseline)"]
    salaries   = [user_salary, baseline_salary]
    colors     = ["#e94560", "#4ecca3"]
    bars = ax1.bar(categories, salaries, color=colors, width=0.5, edgecolor="none")

    for bar, val in zip(bars, salaries):
        ax1.text(bar.get_x() + bar.get_width() / 2,
                 bar.get_height() + 500,
                 f"${val:,.0f}",
                 ha="center", va="bottom", color="white", fontsize=11, fontweight="bold")

    ax1.set_title("Annual Salary Comparison", color="white", fontsize=13, pad=15)
    ax1.set_ylabel("Annual Salary ($)", color="#aaaaaa")
    ax1.tick_params(colors="white")
    ax1.yaxis.label.set_color("#aaaaaa")
    for spine in ax1.spines.values():
        spine.set_visible(False)
    ax1.set_ylim(0, max(salaries) * 1.2)
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))

    gap_pct = ((baseline_salary - user_salary) / baseline_salary) * 100
    ax1.text(0.5, 0.02,
             f"Gap: {gap_pct:.1f}% less than White man baseline",
             transform=ax1.transAxes, ha="center", color="#f5a623",
             fontsize=9, style="italic")

    # ── Chart 2: All demographic groups in this industry ────────────────────
    ax2 = axes[1]
    groups = []
    group_salaries = []
    ind_mult = INDUSTRY_MULTIPLIERS.get(industry, 1.0)
    edu_mult = 1.20  # bachelor degree for fair comparison
    exp_mult = 1.20  # 10 years experience

    for (g, r), ratio in sorted(WAGE_RATIOS.items(), key=lambda x: -x[1]):
        label = f"{g.title()}\n{r.title()}"
        sal   = round(NATIONAL_MEDIAN * ratio * ind_mult * edu_mult * exp_mult, 2)
        groups.append(label)
        group_salaries.append(sal)

    bar_colors = ["#e94560" if s < baseline_salary * ind_mult * edu_mult * exp_mult else "#4ecca3"
                  for s in group_salaries]
    bar_colors[0] = "#4ecca3"  # White man always green (baseline)

    bars2 = ax2.barh(groups, group_salaries, color=bar_colors, edgecolor="none")
    ax2.set_title(f"All Groups: {industry.title()} Industry\n(Bachelor's, 10 yrs exp)",
                  color="white", fontsize=11, pad=15)
    ax2.set_xlabel("Annual Salary ($)", color="#aaaaaa")
    ax2.tick_params(colors="white", labelsize=7)
    ax2.xaxis.label.set_color("#aaaaaa")
    for spine in ax2.spines.values():
        spine.set_visible(False)
    ax2.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x/1000:.0f}k"))

    legend_items = [
        mpatches.Patch(color="#4ecca3", label="At or above baseline"),
        mpatches.Patch(color="#e94560", label="Below baseline"),
    ]
    ax2.legend(handles=legend_items, loc="lower right",
               facecolor="#1a1a2e", labelcolor="white", fontsize=8)

    # ── Chart 3: Lifetime earnings gap over career ───────────────────────────
    ax3 = axes[2]
    ages         = list(range(22, 66))
    user_cumul   = []
    base_cumul   = []
    user_annual  = user_salary
    base_annual  = baseline_salary
    u_total = 0
    b_total = 0

    for _ in ages:
        u_total += user_annual
        b_total += base_annual
        user_cumul.append(u_total)
        base_cumul.append(b_total)
        user_annual *= 1.03
        base_annual *= 1.03

    ax3.fill_between(ages, user_cumul, base_cumul, alpha=0.25, color="#e94560")
    ax3.plot(ages, user_cumul, color="#e94560", linewidth=2.5, label="Your earnings")
    ax3.plot(ages, base_cumul, color="#4ecca3", linewidth=2.5, label="White man earnings")

    final_gap = b_total - u_total
    ax3.set_title("Lifetime Earnings Trajectory\n(3% annual growth assumed)",
                  color="white", fontsize=11, pad=15)
    ax3.set_xlabel("Age", color="#aaaaaa")
    ax3.set_ylabel("Cumulative Earnings ($)", color="#aaaaaa")
    ax3.tick_params(colors="white")
    for spine in ax3.spines.values():
        spine.set_visible(False)
    ax3.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x/1e6:.1f}M"))
    ax3.legend(facecolor="#1a1a2e", labelcolor="white", fontsize=9)
    ax3.text(0.5, 0.05,
             f"Lifetime gap: ${final_gap:,.0f}",
             transform=ax3.transAxes, ha="center", color="#f5a623",
             fontsize=10, fontweight="bold")

    plt.suptitle("Wage Gap Analysis", color="white", fontsize=16, fontweight="bold", y=1.01)
    plt.tight_layout()
    output_path = "/mnt/user-data/outputs/wage_gap_analysis.png"
    plt.savefig(output_path, dpi=150, bbox_inches="tight", facecolor="#0f0f1a")
    plt.close()
    print(f"\nChart saved to: {output_path}")


def print_report(gender, race, industry, education, experience, current_age,
                 user_salary, baseline_salary):
    gap_dollars = baseline_salary - user_salary
    gap_pct     = (gap_dollars / baseline_salary) * 100
    user_life   = lifetime_earnings(user_salary, current_age)
    base_life   = lifetime_earnings(baseline_salary, current_age)
    life_gap    = base_life - user_life

    print("\n" + "=" * 55)
    print("           WAGE GAP ANALYSIS REPORT")
    print("=" * 55)
    print(f"  Profile  : {gender.title()}, {race.title()}")
    print(f"  Industry : {industry.title()}")
    print(f"  Education: {education.title()}")
    print(f"  Experience: {experience} years  |  Current age: {current_age}")
    print("-" * 55)
    print(f"  Your expected salary    : ${user_salary:>12,.2f}")
    print(f"  White man baseline      : ${baseline_salary:>12,.2f}")
    print(f"  Annual gap              : ${gap_dollars:>12,.2f}  ({gap_pct:.1f}% less)")
    print("-" * 55)
    print(f"  Your lifetime earnings  : ${user_life:>12,.2f}")
    print(f"  Baseline lifetime earn. : ${base_life:>12,.2f}")
    print(f"  Lifetime gap            : ${life_gap:>12,.2f}")
    print("=" * 55)

    print("\n  CONTEXT (from AAUW, Pew Research, BLS 2023)")
    print("  -----------------------------------------------")
    ratio = WAGE_RATIOS.get((gender, race), 1.0)
    if gender == "woman" and race == "hispanic/latino":
        print("  Hispanic women earn 54 cents per White man's dollar,")
        print("  the largest gap of any group tracked by BLS.")
    elif gender == "woman" and race == "black":
        print("  Black women earn 64 cents per White man's dollar.")
        print("  Progress has slowed significantly since 2000 (Pew, 2023).")
    elif gender == "woman" and race == "white":
        print("  White women earn 79 cents per White man's dollar.")
        print("  The gender pay gap has narrowed only slightly over 2 decades.")
    elif gender == "man" and race == "black":
        print("  Black men earn 76 cents per White man's dollar,")
        print("  reflecting both hiring and promotion discrimination.")
    elif gender == "man" and race == "asian":
        print("  Asian men earn 15% more than White men on average,")
        print("  though this masks large variation across Asian subgroups.")

    print(f"\n  Your wage ratio: {ratio:.2f} cents per White man's dollar.")
    print(f"  Over a 40-year career, this compounds to ${life_gap:,.0f} lost.")
    print("=" * 55)


def main():
    print("=" * 55)
    print("         WAGE GAP CALCULATOR")
    print("  Based on BLS 2023, AAUW, and Pew Research data")
    print("=" * 55)

    genders    = ["woman", "man"]
    races      = ["white", "black", "hispanic/latino", "asian",
                  "native american", "multiracial"]
    industries = sorted(INDUSTRY_MULTIPLIERS.keys())
    educations = list(EDUCATION_MULTIPLIERS.keys())

    gender    = get_choice("Select your gender:", genders)
    race      = get_choice("Select your race/ethnicity:", races)
    industry  = get_choice("Select your industry:", industries)
    education = get_choice("Select your highest education level:", educations)
    experience = get_int("\nYears of work experience (0-45): ", 0, 45)
    current_age = get_int("Current age (18-60): ", 18, 60)

    user_salary     = calculate_salary(gender, race, industry, education, experience)
    baseline_salary = calculate_baseline_salary(industry, education, experience)

    print_report(gender, race, industry, education, experience, current_age,
                 user_salary, baseline_salary)

    print("\nGenerating charts...")
    plot_salary_comparison(user_salary, baseline_salary, gender, race, industry)
    print("Done.")


if __name__ == "__main__":
    main()
