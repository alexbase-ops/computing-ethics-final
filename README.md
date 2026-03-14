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
cd C:\Users\YourName\Downloads\computing-ethics-final-Wage-Gap-Calculator--main
```
 
**macOS / Linux:**
```bash
cd ~/Downloads/computing-ethics-final-Wage-Gap-Calculator--main
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
streamlit run code.py
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
streamlit run code.py
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
streamlit run code.py
```
 
---
 
**The web app** opens automatically at `http://localhost:8501` in your browser. No additional configuration is needed. Follow the sidebar prompts to enter your profile.

---

**The web app** opens automatically at `http://localhost:8501` in your browser. No additional configuration is needed. Follow the sidebar prompts to enter your profile.

---

## Notes
- All salary figures are estimates based on BLS median earnings data and published wage ratios. They are not a guarantee of individual salary.
- The tool uses an unadjusted wage gap. This reflects real-world outcomes and not a controlled comparison.
- Lifetime earnings projections assume 3% annual salary growth and retirement at age 65.
