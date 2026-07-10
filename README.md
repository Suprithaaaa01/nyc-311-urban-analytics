# 🗽 NYC 311 Urban Service Analytics

A data science analysis of 500,000 real NYC 311 service requests, investigating patterns in complaint volume, borough-level service disparities, temporal trends, and the predictability of government response times.

Built using a professional data science stack — SQL queries via SQLite, exploratory analysis with pandas, statistical hypothesis testing with scipy, interactive visualizations with Plotly, and a predictive model with scikit-learn.

## 🔍 Key Findings

| Finding | Detail |
|---|---|
| Most common complaint | Illegal Parking (79,388 reports in ~6 weeks) |
| Fastest borough | Queens (34.8h avg response) |
| Slowest borough | Manhattan (49.3h avg response) |
| Hardest to resolve | UNSANITARY CONDITION (173h avg) |
| Evening noise spike | 9-10pm is peak complaint hour, driven by noise |
| Model R² | 0.53 — complaint type + borough + time explain 53% of response time variance |

## 📊 Statistical Insight

Borough response time differences are **statistically significant** (Kruskal-Wallis H=2058.12, p≈0), but the **practical difference at the median is only 11 minutes** (Queens: 3.37h vs Manhattan: 3.55h). The large average differences are driven by a small number of extremely slow resolutions in complex complaint categories — a distinction between statistical and practical significance that matters enormously in real-world data analysis.

## 🏗️ Project Structure

| File | Purpose |
|---|---|
| `download_data.py` | Pulls 500K records from NYC Open Data Socrata API |
| `analysis.ipynb` | Full analysis notebook — EDA, SQL, stats, modeling, visualizations |
| `borough_response.png` | Borough response time and unresolved rate charts |
| `complaint_scatter.html` | Interactive Plotly: complaint volume vs response time |
| `hourly_pattern.html` | Interactive Plotly: complaint volume by hour |
| `feature_importance.png` | Random Forest feature importance chart |
| `dashboard.png` | 4-panel summary dashboard |

## 🛠️ Tech Stack

- **Data wrangling:** Python, pandas, NumPy
- **Database & SQL:** SQLite (500K records loaded and queried via SQL)
- **Statistical testing:** scipy (Kruskal-Wallis, Mann-Whitney U)
- **Machine learning:** scikit-learn (Random Forest Regressor, LabelEncoder, train/test split)
- **Visualization:** matplotlib, seaborn, Plotly (interactive HTML charts)
- **Data source:** [NYC Open Data — 311 Service Requests](https://data.cityofnewyork.us/resource/erm2-nwe9.csv) via Socrata API

## 🚀 Running it yourself

```bash
git clone https://github.com/Suprithaaaa01/nyc-311-urban-analytics.git
cd nyc-311-urban-analytics
python3.11 -m venv venv
source venv/bin/activate
pip install pandas numpy matplotlib seaborn plotly scikit-learn scipy jupyterlab requests
python3.11 download_data.py
jupyter lab
```

Then open `analysis.ipynb` and run all cells.

## 📚 Methods

- **SQL:** All borough and complaint-level aggregations performed via SQLite queries, not just pandas — reflecting real-world data workflows where data lives in databases
- **Non-parametric testing:** Kruskal-Wallis and Mann-Whitney U used instead of ANOVA/t-tests because response times are heavily right-skewed (median 3.1h, mean 22.6h), violating normality assumptions
- **Random Forest:** Chosen over linear regression because response time relationships are non-linear; 100 estimators, 80/20 train-test split, evaluated on MAE and R²
