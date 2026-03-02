# Wage Gap Calculator

A Python tool that calculates annual salary, compares earnings to a White male baseline, and projects lifetime earnings gaps based on demographic and job information.

## Overview
This project visualizes wage disparities across gender and racial lines using real labor market data.  A user inputs their gender, race/ethnicity, industry, education level, years of experience, and current age.
The tool outputs their expected salary, the dollar and percentage gap compared to a White man with the same job profile, and a projection of how that gap compounds over a 40-year career.
The project connects to DSJ by making making wage inequality visible and measurable.

## Background and Key Terms


## Dependencies
**Python version:** 3.8 or higher

**Third-party libraries:**

- `matplotlib` — generates all charts and graphs
- `numpy` — supports numerical calculations

**Data sources:**


## Installation and Execution

**1. Clone or download the repository.**

**2. Install dependencies:**

```bash
pip install matplotlib numpy
```

If you are using a system-managed Python environment (e.g., Ubuntu 24+):

```bash
pip install matplotlib numpy --break-system-packages
```

**3. Run the calculator:**

```bash
python wage_gap_calculator.py
```

**4. Follow the prompts.** The tool walks you through each input one at a time. No configuration file is needed.

## Notes
- All salary figures are estimates based on BLS median earnings data and published wage ratios. They are not a guarantee of individual salary.
- The tool uses an unadjusted wage gap. This reflects real-world outcomes and not a controlled comparison.
- Lifetime earnings projections assume 3% annual salary growth and retirement at age 65.
