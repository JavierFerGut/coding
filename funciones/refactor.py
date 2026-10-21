"""Versión refactorizada de report().

Ofrece estas dos funciones, que sustituyen al argumento by_region:

    write_monthly_report(sales_path)   -> mismo informe que report(path, by_region=False)
    write_regional_report(sales_path)  -> mismo informe que report(path, by_region=True)

Cuando creas que está, ejecuta: python comprobar.py
"""
import pandas as pd

REPORT_PATH = "report.txt"


def write_monthly_report(sales_path):
    sales = load_sales(sales_path)
    monthly_totals = calc_monthly_totals(sales, ["month"])
    # Crecimiento respecto al mes anterior sobre toda la serie
    monthly_totals["growth"] = monthly_totals["amount"].pct_change()
    lines = format_lines(monthly_totals, ["month"])
    return write_report(lines)


def write_regional_report(sales_path):
    sales = load_sales(sales_path)
    monthly_totals = calc_monthly_totals(sales, ["region", "month"])
    # Crecimiento respecto al mes anterior dentro de cada región
    monthly_totals["growth"] = monthly_totals.groupby("region")["amount"].pct_change()
    lines = format_lines(monthly_totals, ["region", "month"])
    return write_report(lines)


def load_sales(sales_path):
    sales = pd.read_csv(sales_path, parse_dates=["date"])
    positive_sales = sales[sales["amount"] > 0].dropna()
    return positive_sales.assign(month=positive_sales["date"].dt.to_period("M"))


def calc_monthly_totals(sales, group_columns):
    return sales.groupby(group_columns)["amount"].sum().reset_index()


def format_lines(totals, label_columns):
    return [format_line(row, label_columns) for _, row in totals.iterrows()]


def format_line(row, label_columns):
    label = " ".join(str(row[col]) for col in label_columns)
    line = f"{label}: {row['amount']:.2f}"
    if pd.notna(row["growth"]):
        line += f" ({row['growth']:+.1%})"
    return line


def write_report(lines):
    with open(REPORT_PATH, "w") as f:
        f.write("\n".join(lines))
    return len(lines)
