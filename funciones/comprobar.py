"""Comprueba que la versión refactorizada produce los mismos informes que la original."""
from pathlib import Path

from original import report
from refactor import write_monthly_report, write_regional_report

SALES_PATH = "sales.csv"
REPORT_PATH = Path("report.txt")


def check(original_call, refactored_call, description):
    original_call()
    expected = REPORT_PATH.read_text()
    refactored_call()
    actual = REPORT_PATH.read_text()
    if actual == expected:
        print(f"OK  {description}")
        return True
    print(f"MAL {description}: el informe ha cambiado")
    return False


results = [
    check(lambda: report(SALES_PATH, by_region=False),
          lambda: write_monthly_report(SALES_PATH),
          "informe mensual"),
    check(lambda: report(SALES_PATH, by_region=True),
          lambda: write_regional_report(SALES_PATH),
          "informe por regiones"),
]
print("Todo correcto." if all(results) else "Revisa los informes que han cambiado.")
