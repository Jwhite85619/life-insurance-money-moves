"""Simple IUL growth estimator (illustrative only - not financial advice)

Run: python3 iul_growth_calculator.py
"""
def estimate_cash_value(initial_premium, annual_premium, years, assumed_rate=0.05, cap=0.10, floor=0.0, fee_rate=0.01):
    cash = initial_premium
    for y in range(years):
        # apply growth
        growth = cash * assumed_rate + annual_premium
        # apply fees
        fees = cash * fee_rate
        cash = max(floor * cash, min(cash + growth - fees, cash + cap * cash + annual_premium))
    return round(cash,2)

if __name__ == '__main__':
    print("Simple IUL Growth Estimator (illustrative)")
    init = float(input("Initial premium (one-time): "))
    ann = float(input("Annual premium: "))
    yrs = int(input("Years: "))
    val = estimate_cash_value(init, ann, yrs)
    print(f"Estimated cash value after {yrs} years: ${val}")
