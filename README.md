# Wage Gap Calculator

A Python tool that takes a user's gender, race/ethnicity, industry, education level, years of experience, and current age, then calculates their estimated annual salary, the dollar and percentage gap compared to a White man with the same job profile, and a projection of how that gap grows over a 40-year career.

Two interfaces are included: a Streamlit web app (`app.py`) and a Tkinter desktop GUI (`gui.py`).

This project was built for a Digital Social Justice course. The goal is to make wage inequality concrete and measurable using real labor data.

---

## Background and Research

This project aims to support and highlight the people across out country who experience differentiated pay than other people. Here are some facts we found on the matter:

Average pay gap in United States: 17% 
For age 16+: 19% 
For age 25+: 12% 
Women make on average 83 cents for every dollar a man makes 

Based on 2021 statistics: 
Highest pay gap job is insurance/financing with 36% gap 
Lowest is real estate with only 2%, followed closely by mining/quarrying with 2.2% 
Average still 17% for all jobs 

On average, Asian and White/Caucasian men make the most.
Hispanic and Native American women make the least.

Years of experience and level of degree will have an effect on the wage gap.

---

## Dependencies

**Python version:** 3.8 or higher

**Third-party libraries:**

- `matplotlib` — chart generation
- `numpy` — numerical support
- `streamlit` — web app interface

**Data sources:**

- U.S. Bureau of Labor Statistics, *Highlights of Women's Earnings in 2023*
- AAUW, *The Simple Truth About the Gender Pay Gap*
- Pew Research Center, *Gender pay gap in U.S. has narrowed slightly over 2 decades*

---

## Installation and Execution

### Finding Your Project Directory

After downloading or cloning the repo, open your terminal and navigate to the project folder before running anything.

**Windows (Command Prompt):**
```cmd
cd C:\Users\YourName\Downloads\computing-ethics-final-Wage-Gap-Calculator--main\computing-ethics-final-Wage-Gap-Calculator--main
```

**macOS / Linux:**
```bash
cd ~/Downloads/computing-ethics-final-Wage-Gap-Calculator--main/computing-ethics-final-Wage-Gap-Calculator--main
```

Replace `YourName` with your actual username. If you used `git clone`, the folder is wherever you ran that command.

If you can't find it, search by filename:

**Windows:**
```cmd
dir /s /b "gui.py"
```

**macOS / Linux:**
```bash
find ~ -name "gui.py"
```

---

### Windows

1. Download and install Python 3.8+ from [python.org](https://www.python.org/downloads/). Check **"Add Python to PATH"** during installation.
2. Open Command Prompt and navigate to the project directory.
3. Install dependencies:

```cmd
pip install matplotlib numpy streamlit
```

4. Run the desktop GUI:

```cmd
python gui.py
```

Or run the web app:

```cmd
streamlit run app.py
```

---

### macOS

1. macOS includes Python 3, but the latest version is recommended via [python.org](https://www.python.org/downloads/) or Homebrew:

```bash
brew install python
```

2. Open Terminal and navigate to the project directory.
3. Install dependencies:

```bash
pip3 install matplotlib numpy streamlit
```

4. Run the desktop GUI:

```bash
python3 gui.py
```

Or run the web app:

```bash
streamlit run app.py
```

---

### Linux (Ubuntu/Debian)

1. Python 3 is usually pre-installed. Check with `python3 --version`.
2. Install Tkinter if missing:

```bash
sudo apt install python3-tk
```

3. Install dependencies. Ubuntu 24+ requires the `--break-system-packages` flag:

```bash
pip install matplotlib numpy streamlit --break-system-packages
```

4. Run the desktop GUI:

```bash
python3 gui.py
```

Or run the web app:

```bash
streamlit run app.py
```

---

The web app opens at `http://localhost:8501` in your browser. Use the sidebar to enter your profile.

---

## Usage

### Desktop GUI (gui.py)

Select gender via radio buttons, then pick race/ethnicity and education level from the listboxes. Bachelor's Degree is selected by default. Click **See My Statistics** to display the salary comparison and wage ratio.

![Screenshot of the Wage Gap Calculator desktop GUI showing gender radio buttons for Male, Female, Non-binary, and Prefer not to say; a Race/Ethnicity listbox; an Education Level listbox with Bachelor's Degree highlighted in pink; and a pink See My Statistics button, all on a dark navy background.](screenshot.png)

---

### Web App (app.py)

The sidebar takes gender, race/ethnicity, industry, education level, years of experience, and current age. The main panel shows four summary metrics and three charts: annual salary vs. baseline, all demographic groups in the selected industry, and a lifetime earnings trajectory from current age to retirement.

![Screenshot of the Wage Gap Calculator Streamlit web app. The sidebar shows inputs set to Man, Asian, Technology, Professional Degree, 45 years of experience, and age 43. The main panel shows four metric cards, a wage ratio of 1.15 per $1.00, a data callout for Asian men, and three charts: a salary bar chart, a demographic comparison for Technology, and a lifetime earnings line chart.](screenshot(streamlit).png)

---

## File Table

| File | Description | Contributor |
|------|-------------|-------------|
| `app.py` | Streamlit web app. Salary calculation, lifetime earnings projection, chart generation, and UI. | Alexander Gardner |
| `gui.py` | Tkinter desktop GUI. Radio buttons and listboxes for input, results displayed below. | Nathaniel Cisler |
| `README.md` | Project documentation and instructions. | Alexander Gardner, Jaeden Poole |
| `screenshot.png` | Screenshot of the desktop GUI. | Alexander Gardner |
| `screenshot(streamlit).png` | Screenshot of the Streamlit web app showing sidebar inputs, metric cards, and all three charts. | Alexander Gardner |

---

## Citations

Bureau of Labor Statistics. (2024). *Highlights of women's earnings in 2023* (Report 1100). U.S. Department of Labor. https://www.bls.gov/opub/reports/womens-earnings/2023/

AAUW. "The Simple Truth about the Pay Gap." AAUW : Empowering Women since 1881, AAUW, 2022, www.aauw.org/resources/research/simple-truth/.

Aragao, C. (2023). *Gender pay gap in U.S. has narrowed slightly over 2 decades, but remains large*. Pew Research Center. https://www.pewresearch.org/short-reads/2023/03/01/gender-pay-gap-facts/

---

## Notes

- All salary figures are estimates based on BLS median earnings data and published wage ratios. They are not a guarantee of individual salary.
- The tool uses an unadjusted wage gap, which reflects real-world outcomes rather than a controlled comparison.
- Lifetime earnings projections assume 3% annual salary growth and retirement at age 65.
