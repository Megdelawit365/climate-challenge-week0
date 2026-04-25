
# Climate Challenge Week 0

## Overview
This project is part of the 10 Academy: Artificial Intelligence Mastery Week 0 challenge.  The goal is to analyze historical climate data from Ethiopia, Kenya, Sudan, Tanzania and Nigeria to understand climate trends and vulnerabilities.

The project includes:
- Git and environment setup
- Data cleaning and exploratory data analysis (EDA)
- Cross-country climate comparison and ranking

---

## Project Structure
climate-challenge-week0/
├── .github/
│   └── workflows/
│       └── ci.yml
├── data/
├── notebooks/
│   ├── ethiopia_eda.ipynb
│   ├── kenya_eda.ipynb
│   ├── nigeria_eda.ipynb
│   ├── sudan_eda.ipynb
│   ├── tanzania_eda.ipynb
│   └── compare_countries.ipynb
├── scripts/
├── src/
├── tests/
├── .gitignore
├── requirements.txt
└── README.md

---

## Setup Instructions

### 1. Clone repository
```bash
git clone https://github.com/Megdelawit365/climate-challenge-week0
cd climate-challenge-week0
```
### 2. Create virtual environment
```bash
python -m venv venv
```
### 3. Activate environment
Windows:
```bash
python -m venv venv
```
Mac/Linux:
```bash
source venv/bin/activate
```
### 4. Install dependencies
```bash
pip install -r requirements.txt
```
  
## CI

This project uses GitHub Actions to run basic CI checks on every push to main.