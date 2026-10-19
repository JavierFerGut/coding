"""Escribe aquí tu versión refactorizada de report().

Tiene que ofrecer estas dos funciones, que sustituyen al argumento by_region:

    write_monthly_report(sales_path)   -> mismo informe que report(path, by_region=False)
    write_regional_report(sales_path)  -> mismo informe que report(path, by_region=True)

Cuando creas que está, ejecuta: python comprobar.py
"""
import pandas as pd


def write_monthly_report(sales_path):
    raise NotImplementedError


def write_regional_report(sales_path):
    raise NotImplementedError


