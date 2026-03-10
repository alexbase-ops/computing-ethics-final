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

Windows

Download and install Python 3.8+ from python.org. Check "Add Python to PATH" during installation.
Open Command Prompt and clone or download the repository.
Install dependencies:

cmdpip install matplotlib numpy streamlit

Run the command-line version:

cmdpython wage_gap_calculator.py
Or run the web app:
cmdstreamlit run app.py

macOS

macOS includes Python 3, but we recommend installing the latest version via python.org or Homebrew:

bashbrew install python

Open Terminal and clone or download the repository.
Install dependencies:

bashpip3 install matplotlib numpy streamlit

Run the command-line version:

bashpython3 wage_gap_calculator.py
Or run the web app:
bashstreamlit run app.py

Linux (Ubuntu/Debian)

Python 3 is typically pre-installed. Verify with python3 --version.
Install dependencies. Ubuntu 24+ uses a system-managed Python environment, so use the --break-system-packages flag:

bashpip install matplotlib numpy streamlit --break-system-packages

Run the command-line version:

bashpython3 wage_gap_calculator.py
Or run the web app:
bashstreamlit run app.py

The web app opens automatically at http://localhost:8501 in your browser. No additional configuration is needed. Follow the sidebar prompts to enter your profile.
```

**4. Follow the prompts.** The tool walks you through each input one at a time. No configuration file is needed.

## Notes
- All salary figures are estimates based on BLS median earnings data and published wage ratios. They are not a guarantee of individual salary.
- The tool uses an unadjusted wage gap. This reflects real-world outcomes and not a controlled comparison.
- Lifetime earnings projections assume 3% annual salary growth and retirement at age 65.
