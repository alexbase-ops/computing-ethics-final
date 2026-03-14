"""
Wage Gap Calculator - Streamlit Web App
Run with: streamlit run app.py
Dependencies: pip install streamlit matplotlib numpy
"""

import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


# Wage ratios relative to a White man (1.00 = baseline).
# Source: BLS Highlights of Women's Earnings 2023, AAUW, Pew Research Center.
WAGE_RATIOS = {
    ("Man",   "White"):           1.00,
    ("Man",   "Asian"):           1.15,
    ("Man",   "Black"):           0.76,
    ("Man",   "Hispanic/Latino"): 0.68,
    ("Man",   "Native American"): 0.70,
    ("Man",   "Multiracial"):     0.83,
    ("Woman", "White"):           0.79,
    ("Woman", "Asian"):           0.87,
    ("Woman", "Black"):           0.64,
    ("Woman", "Hispanic/Latino"): 0.54,
    ("Woman", "Native American"): 0.51,
    ("Woman", "Multiracial"):     0.68,
}

# How much each industry pays relative to the national median.
# 1.85 = 85% above median, 0.60 = 40% below median.
INDUSTRY_MULTIPLIERS = {
    "Arts/Entertainment":  0.80,
    "Construction":        1.10,
    "Education":           0.90,
    "Finance":             1.70,
    "Food Service":        0.60,
    "Government":          1.15,
    "Healthcare":          1.30,
    "Manufacturing":       1.05,
    "Nonprofit":           0.85,
    "Other":               1.00,
    "Retail":              0.70,
    "Technology":          1.85,
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

# BLS 2023 national median annual earnings — the base for all calculations.
NATIONAL_MEDIAN = 59000

# Research callouts shown in the UI for specific demographic groups.
CONTEXT = {
    ("Woman", "Hispanic/Latino"): "Hispanic women earn 54 cents per White man's dollar, the largest gap of any group tracked by BLS.",
    ("Woman", "Black"):           "Black women earn 64 cents per White man's dollar. Progress has slowed significantly since 2000 (Pew, 2023).",
    ("Woman", "White"):           "White women earn 79 cents per White man's dollar. The gender pay gap has narrowed only slightly over two decades.",
    ("Woman", "Native American"): "Native American women earn 51 cents per White man's dollar, one of the most severe gaps in BLS data.",
    ("Man",   "Black"):           "Black men earn 76 cents per White man's dollar, reflecting both hiring and promotion discrimination.",
    ("Man",   "Hispanic/Latino"): "Hispanic men earn 68 cents per White man's dollar across all industries.",
    ("Man",   "Asian"):           "Asian men earn 15% more than White men on average, though this masks variation across Asian subgroups.",
}


# ── Calculations ──────────────────────────────────────────────────────────────

def calculate_salary(gender, race, industry, education, experience):
    """
    Estimates annual salary by multiplying the national median by four factors:
    the demographic wage ratio, industry pay level, education premium, and
    an experience bump of roughly 2% per year.
    """
    ratio    = WAGE_RATIOS.get((gender, race), 1.0)
    ind_mult = INDUSTRY_MULTIPLIERS.get(industry, 1.0)
    edu_mult = EDUCATION_MULTIPLIERS.get(education, 1.0)
    exp_mult = 1 + (experience * 0.02)
    return round(NATIONAL_MEDIAN * ratio * ind_mult * edu_mult * exp_mult, 2)


def calculate_baseline(industry, education, experience):
    """
    Same calculation as calculate_salary but with a wage ratio of 1.0,
    so the comparison is apples-to-apples within the same job context.
    """
    ind_mult = INDUSTRY_MULTIPLIERS.get(industry, 1.0)
    edu_mult = EDUCATION_MULTIPLIERS.get(education, 1.0)
    exp_mult = 1 + (experience * 0.02)
    return round(NATIONAL_MEDIAN * 1.0 * ind_mult * edu_mult * exp_mult, 2)


def lifetime_earnings(annual_salary, current_age, retirement_age=65, growth=0.03):
    """
    Projects cumulative earnings from current_age to retirement, applying
    3% annual growth each year. The gap between two people's lifetime totals
    shows how a small annual difference compounds into a much larger one.
    """
    total  = 0
    salary = annual_salary
    for _ in range(retirement_age - current_age):
        total  += salary
        salary *= (1 + growth)
    return round(total, 2)


# ── Charts ────────────────────────────────────────────────────────────────────

def make_charts(user_salary, baseline_salary, gender, race, industry, current_age):
    """
    Builds a 3-panel figure:
      1. Bar chart: user salary vs. baseline
      2. Horizontal bars: all demographic groups in the selected industry
         (standardized to Bachelor's degree, 10 years experience)
      3. Line chart: cumulative lifetime earnings from current age to 65,
         with the gap shaded between the two lines
    """
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    fig.patch.set_facecolor("#0f0f1a")
    for ax in axes:
        ax.set_facecolor("#1a1a2e")

    # ── Panel 1: Annual salary bar chart ──────────────────────────────────────
    ax1 = axes[0]
    bars = ax1.bar(
        ["You", "White Man\n(Baseline)"],
        [user_salary, baseline_salary],
        color=["#e94560", "#4ecca3"],
        width=0.5,
        edgecolor="none"
    )
    for bar, val in zip(bars, [user_salary, baseline_salary]):
        ax1.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 500,
            f"${val:,.0f}",
            ha="center", va="bottom",
            color="white", fontsize=11, fontweight="bold"
        )
    gap_pct = ((baseline_salary - user_salary) / baseline_salary) * 100
    ax1.set_title("Annual Salary Comparison", color="white", fontsize=12, pad=12)
    ax1.set_ylabel("Annual Salary ($)", color="#aaaaaa")
    ax1.tick_params(colors="white")
    for spine in ax1.spines.values():
        spine.set_visible(False)
    ax1.set_ylim(0, max(user_salary, baseline_salary) * 1.2)
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x:,.0f}"))
    ax1.text(
        0.5, 0.02, f"Gap: {gap_pct:.1f}% less than baseline",
        transform=ax1.transAxes, ha="center",
        color="#f5a623", fontsize=9, style="italic"
    )

    # ── Panel 2: All demographic groups ───────────────────────────────────────
    # Fixed profile (Bachelor's, 10 yrs exp) so every group is on equal footing.
    ax2 = axes[1]
    ind_mult       = INDUSTRY_MULTIPLIERS.get(industry, 1.0)
    edu_mult       = 1.20
    exp_mult       = 1.20
    base_for_chart = NATIONAL_MEDIAN * 1.0 * ind_mult * edu_mult * exp_mult

    groups, group_salaries = [], []
    for (g, r), ratio in sorted(WAGE_RATIOS.items(), key=lambda x: -x[1]):
        groups.append(f"{g}\n{r}")
        group_salaries.append(
            round(NATIONAL_MEDIAN * ratio * ind_mult * edu_mult * exp_mult, 2)
        )

    colors = ["#4ecca3" if s >= base_for_chart else "#e94560" for s in group_salaries]
    ax2.barh(groups, group_salaries, color=colors, edgecolor="none")
    ax2.set_title(
        f"All Groups: {industry}\n(Bachelor's, 10 yrs exp)",
        color="white", fontsize=10, pad=12
    )
    ax2.set_xlabel("Annual Salary ($)", color="#aaaaaa")
    ax2.tick_params(colors="white", labelsize=7)
    for spine in ax2.spines.values():
        spine.set_visible(False)
    ax2.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x/1000:.0f}k"))
    legend_items = [
        mpatches.Patch(color="#4ecca3", label="At or above baseline"),
        mpatches.Patch(color="#e94560", label="Below baseline"),
    ]
    ax2.legend(handles=legend_items, loc="lower right",
               facecolor="#1a1a2e", labelcolor="white", fontsize=8)

    # ── Panel 3: Lifetime earnings trajectory ─────────────────────────────────
    ax3 = axes[2]
    ages             = list(range(current_age, 66))
    u_cumul, b_cumul = [], []
    u_total, b_total = 0, 0
    u_sal, b_sal     = user_salary, baseline_salary

    for _ in ages:
        u_total += u_sal
        b_total += b_sal
        u_cumul.append(u_total)
        b_cumul.append(b_total)
        u_sal *= 1.03
        b_sal *= 1.03

    final_gap = b_total - u_total
    ax3.fill_between(ages, u_cumul, b_cumul, alpha=0.25, color="#e94560")
    ax3.plot(ages, u_cumul, color="#e94560", linewidth=2.5, label="Your earnings")
    ax3.plot(ages, b_cumul, color="#4ecca3", linewidth=2.5, label="White man earnings")
    ax3.set_title(
        "Lifetime Earnings Trajectory\n(3% annual growth)",
        color="white", fontsize=10, pad=12
    )
    ax3.set_xlabel("Age", color="#aaaaaa")
    ax3.set_ylabel("Cumulative Earnings ($)", color="#aaaaaa")
    ax3.tick_params(colors="white")
    for spine in ax3.spines.values():
        spine.set_visible(False)
    ax3.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"${x/1e6:.1f}M"))
    ax3.legend(facecolor="#1a1a2e", labelcolor="white", fontsize=9)
    ax3.text(
        0.5, 0.05, f"Lifetime gap: ${final_gap:,.0f}",
        transform=ax3.transAxes, ha="center",
        color="#f5a623", fontsize=10, fontweight="bold"
    )

    plt.tight_layout()
    return fig


# ── Streamlit UI ──────────────────────────────────────────────────────────────
# Streamlit reruns the whole script every time an input changes, so all
# calculations below always reflect whatever is currently in the sidebar.

st.set_page_config(page_title="Wage Gap Calculator", layout="wide")
st.title("Wage Gap Calculator")
st.caption("Based on BLS 2023 data, AAUW research, and Pew Research Center findings.")

st.sidebar.header("Your Profile")

gender = st.sidebar.selectbox("Gender", ["Woman", "Man"])
race = st.sidebar.selectbox(
    "Race / Ethnicity",
    ["White", "Black", "Hispanic/Latino", "Asian", "Native American", "Multiracial"]
)
industry  = st.sidebar.selectbox("Industry", sorted(INDUSTRY_MULTIPLIERS.keys()))
education = st.sidebar.selectbox("Education Level", list(EDUCATION_MULTIPLIERS.keys()))
experience  = st.sidebar.slider("Years of Experience", 0, 45, 5)
current_age = st.sidebar.slider("Current Age", 18, 60, 25)

user_salary     = calculate_salary(gender, race, industry, education, experience)
baseline_salary = calculate_baseline(industry, education, experience)
gap_dollars     = baseline_salary - user_salary
gap_pct         = (gap_dollars / baseline_salary) * 100
user_life       = lifetime_earnings(user_salary, current_age)
base_life       = lifetime_earnings(baseline_salary, current_age)
life_gap        = base_life - user_life
ratio           = WAGE_RATIOS.get((gender, race), 1.0)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Your Expected Salary", f"${user_salary:,.0f}")
col2.metric("White Man Baseline",   f"${baseline_salary:,.0f}")
col3.metric("Annual Gap", f"${gap_dollars:,.0f}", delta=f"-{gap_pct:.1f}%", delta_color="inverse")
col4.metric("Lifetime Gap", f"${life_gap:,.0f}")

st.divider()

st.subheader("Your Wage Ratio")
st.markdown(f"For every **$1.00** a White man earns, you earn **${ratio:.2f}**.")

context_note = CONTEXT.get((gender, race))
if context_note:
    st.info(context_note)

st.divider()

st.subheader("Visual Analysis")
fig = make_charts(user_salary, baseline_salary, gender, race, industry, current_age)
st.pyplot(fig)

st.divider()

with st.expander("Data Sources"):
    st.markdown("""
- **BLS** — *Highlights of Women's Earnings in 2023* (Report 1100)
- **AAUW** — *Today's Gender Pay Gap Data Shows Decline in Progress Towards Equity*
- **Pew Research Center** — *Gender pay gap in U.S. has narrowed slightly over 2 decades*

All salary figures are estimates based on published wage ratios. This tool uses an **unadjusted** wage gap, which reflects real-world outcomes including occupational segregation and discrimination. Lifetime earnings assume 3% annual growth and retirement at age 65.
    """)
