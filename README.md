# Retail Banking Customer Segmentation & Cross-Sell Analysis
![Dashboard](docs/dashboard.png)

An end-to-end analytics project on a public bank telemarketing dataset: data cleaning (Python/Pandas), a SQL
analysis layer (SQLite, 10 queries), rule-based customer segmentation, a term-deposit propensity model for
cross-sell targeting, and an interactive Excel dashboard. A Power BI build guide is included.

> **Honest scope.** The data comes from a *Portuguese* bank (2008-2010), not ICICI Bank. The only observed product
> outcome is a **term deposit**; loan holdings are observed, but credit cards, insurance and investments are not in the
> data and are not analysed. Segments and thresholds are my assumptions and are labelled as such.

## Dataset
- **UCI Bank Marketing** (`bank-full.csv`), Moro, Rita & Cortez (2014). https://archive.ics.uci.edu/dataset/222/bank+marketing
- Licence: CC BY 4.0 (attribution required - see Citation). DOI: 10.24432/C5K306
- Why this one: real, anonymised retail-banking data with customer demographics, balances, loan holdings and a campaign
  outcome - exactly what segmentation and cross-sell need - and it is small enough for a laptop.
- Fields: see [`docs/data_dictionary.md`](docs/data_dictionary.md).
- A **synthetic generator** (`src/generate_synthetic_data.py`) exists *only* to smoke-test the pipeline offline. Its output is
  labelled SYNTHETIC everywhere and must never be quoted.

## Quick start
```bash
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python run_all.py                                       # downloads real data, runs everything
```
If the download is blocked, get the zip from the UCI page, extract `bank-full.csv` into `data/raw/`, then run
`python run_all.py` again. Offline smoke test: `python run_all.py --synthetic`.

Run time: under a minute. Python 3.9+.

## Pipeline
| Step | Script | Output |
|---|---|---|
| 0 | `src/download_data.py` | `data/raw/bank-full.csv` |
| 1 | `src/clean_data.py` | `data/processed/bank_clean.csv`, `reports/cleaning_log.md` |
| 2 | `src/segment_customers.py` | `bank_segmented.csv`, `segment_definitions.csv` |
| 3 | `src/build_database.py` + `sql/*.sql` | `bank.db`, `reports/sql_results/q01..q10.csv` |
| 4 | `src/crosssell_analysis.py` | opportunity, lending-gap, lift table, target list, metrics |
| 5 | `src/generate_insights.py` | `reports/insights.md` (numbers read from results) |
| 6 | `src/build_excel_dashboard.py` | `dashboard/Retail_Banking_Dashboard.xlsx` |
| 7 | `src/validate.py` | 23 pass/fail checks (reconciles SQL vs pandas) |

## SQL queries (`sql/`)
Q01 headline KPIs - Q02 segment performance - Q03 age x balance matrix - Q04 occupation ranking - Q05 monthly trend -
Q06 contact intensity - Q07 product-holding mix - Q08 previous-campaign effect - Q09 lending-gap pool -
Q10 segment x channel. They use JOINs (including a dimension table), GROUP BY, HAVING, CASE WHEN, window functions and aggregates.

## Dashboard
`dashboard/Retail_Banking_Dashboard.xlsx`: 8 KPI cards, 4 drop-down filters (segment, job, age band, channel), 6 charts,
plus Segment_Summary / CrossSell / Data sheets. Formulas (COUNTIFS/AVERAGEIFS) calculate when Excel opens the file.
`dashboard/SAMPLE_synthetic_preview.xlsx` is a layout preview built from SYNTHETIC data only. For Power BI see
[`docs/powerbi_guide.md`](docs/powerbi_guide.md) (I could not generate a `.pbix` here, so it is a guide, not a claimed deliverable).

## Documentation
[Methodology](docs/methodology.md) - [Data dictionary](docs/data_dictionary.md) - [Power BI guide](docs/powerbi_guide.md) -
[CV & interview prep](docs/cv_and_interview.md)

## Limitations
Observational, one bank, 2008-2010, euro balances; correlation not causation; `y` is "took a term deposit in this
campaign", not lifetime value; no revenue, income, geography or time-series of balances; the propensity model is a
simple logistic regression evaluated by cross-validation, not a production model.

## Citation / attribution
Moro, S., Rita, P., & Cortez, P. (2014). *Bank Marketing* [Dataset]. UCI Machine Learning Repository.
https://doi.org/10.24432/C5K306 (CC BY 4.0). All code in this repo is original; MIT licence (see LICENSE) - put your own name there.
