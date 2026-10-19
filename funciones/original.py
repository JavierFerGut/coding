import pandas as pd


def report(path, by_region):
    df = pd.read_csv(path, parse_dates=["date"])
    df = df[df["amount"] > 0].dropna()
    df["month"] = df["date"].dt.to_period("M")
    lines = []
    if by_region:
        out = df.groupby(["region", "month"])["amount"].sum().reset_index()
        out["growth"] = out.groupby("region")["amount"].pct_change()
        for _, r in out.iterrows():
            txt = f"{r['region']} {r['month']}: {r['amount']:.2f}"
            if not pd.isna(r["growth"]):
                txt += f" ({r['growth']:+.1%})"
            lines.append(txt)
    else:
        out = df.groupby("month")["amount"].sum().reset_index()
        out["growth"] = out["amount"].pct_change()
        for _, r in out.iterrows():
            txt = f"{r['month']}: {r['amount']:.2f}"
            if not pd.isna(r["growth"]):
                txt += f" ({r['growth']:+.1%})"
            lines.append(txt)
    with open("report.txt", "w") as f:
        f.write("\n".join(lines))
    return len(lines)
