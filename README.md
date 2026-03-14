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
- `streamlit` — powers the web app interface
 
**Data sources:**
 
- U.S. Bureau of Labor Statistics, *Highlights of Women's Earnings in 2023*
- AAUW, *The Simple Truth About the Gender Pay Gap*
- Pew Research Center, *Gender pay gap in U.S. has narrowed slightly over 2 decades*

---

## Installation and Execution

### Finding Your Project Directory
 
After downloading or cloning the repo, open your terminal and navigate to the project directory before running any commands.
 
**Windows (Command Prompt):**
```cmd
cd C:\Users\YourName\Downloads\computing-ethics-final-Wage-Gap-Calculator--main\computing-ethics-final-Wage-Gap-Calculator--main
```
 
**macOS / Linux:**
```bash
cd ~/Downloads/computing-ethics-final-Wage-Gap-Calculator--main\computing-ethics-final-Wage-Gap-Calculator--main
```
 
Replace `YourName` with your actual username. If you cloned the repo with Git, the folder will be wherever you ran `git clone`.
 
If you can't find the folder, use these commands to locate it by filename:
 
**Windows:**
```cmd
dir /s /b "gui.py"
```
 
**macOS / Linux:**
```bash
find ~ -name "gui.py"
```
 
Once you are inside the project directory, all run commands will work as written.
 
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
 
1. macOS includes Python 3, but we recommend installing the latest version via [python.org](https://www.python.org/downloads/) or Homebrew:
 
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
 
1. Python 3 is typically pre-installed. Verify with `python3 --version`.
2. Install Tkinter if it is not already present:
 
```bash
sudo apt install python3-tk
```
 
3. Install dependencies. Ubuntu 24+ uses a system-managed Python environment, so use the `--break-system-packages` flag:
 
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
 
**The web app** opens automatically at `http://localhost:8501` in your browser. No additional configuration is needed. Follow the sidebar prompts to enter your profile.

---

## Sample Use Cases
 
### Desktop GUI (gui.py)
 
The screenshot below shows the Tkinter desktop interface. The user selects their gender via radio buttons, then picks their race/ethnicity and education level from listboxes. Bachelor's Degree is selected by default. Clicking "See My Statistics" displays the salary comparison and wage ratio results below the button.
 
![Screenshot of the Wage Gap Calculator desktop GUI. A dark navy background with white text shows three input sections: a Gender row with radio buttons for Male, Female, Non-binary, and Prefer not to say; a Race/Ethnicity listbox with options including White, Black, Hispanic/Latino, Asian, Native American, and Multiracial; and an Education Level listbox with eight options from Less than High School to Professional Degree, with Bachelor's Degree highlighted in pink. A pink See My Statistics button sits below the inputs.](screenshot.png)
 
---
 
### Web App (code.py)
 
The Streamlit web app provides the same inputs via a sidebar, with additional fields for industry, years of experience, and current age. It displays four summary metrics at the top of the page and renders three charts: an annual salary comparison bar chart, a demographic comparison across all groups in the selected industry, and a lifetime earnings trajectory showing how the gap compounds from the user's current age to retirement.
 
> Additional screenshots of the web app output will be added once the Streamlit deployment is complete.
 
---
 
## File Table
 
| File | Description | Contributor |
|------|-------------|-------------|
| `code.py` | Main Streamlit web app. Handles salary calculation, lifetime earnings projection, chart generation, and UI. | Alexander Gardner |
| `gui.py` | Tkinter desktop GUI. Takes user inputs via dropdowns and radio buttons and displays salary gap results. | Nathaniel Cisler |
| `README.md` | Project documentation, background research, and instructions. | Alexander Gardner, Jaeden Poole |
| `screenshot.png` | Screenshot of the desktop GUI showing all input fields and the See My Statistics button. | Alexander Gardner |
 
---
 
## Citations
 
Bureau of Labor Statistics. (2024). *Highlights of women's earnings in 2023* (Report 1100). U.S. Department of Labor. https://www.bls.gov/opub/reports/womens-earnings/2023/

AAUW. “The Simple Truth about the Pay Gap.” AAUW : Empowering Women since 1881, AAUW, 2022, www.aauw.org/resources/research/simple-truth/.

Aragao, C. (2023). *Gender pay gap in U.S. has narrowed slightly over 2 decades, but remains large*. Pew Research Center. https://www.pewresearch.org/short-reads/2023/03/01/gender-pay-gap-facts/

---

## Notes
- All salary figures are estimates based on BLS median earnings data and published wage ratios. They are not a guarantee of individual salary.
- The tool uses an unadjusted wage gap. This reflects real-world outcomes and not a controlled comparison.
- Lifetime earnings projections assume 3% annual salary growth and retirement at age 65.
