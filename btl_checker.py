# BTL Mortgage Deal Tester for Limited Company Interest-Only
# Run this script to test deals for your £410k property scenario

import sys

# Pre-loaded deals: [name, rate (%), fixed_term (years), fee (% of loan)]
DEALS = [
    ["CHL Mortgages", 2.30, 2, 7.0],
    ["The Mortgage Works (TMW)", 2.74, 2, 1.9],
    ["Molo Finance", 2.68, 2, 1.0],
    ["Vida Homeloans", 2.92, 2.5, 3.7],
    ["Aldermore (New Edition)", 5.79, 2, 0.0]
]

def parse_input(prompt, default):
    """Parse float input, stripping commas and handling defaults."""
    s = input(prompt).strip().replace(',', '')
    if not s:
        return float(default)
    return float(s)

def calculate_metrics(property_price, monthly_rent, deposit_pct, rate, fee_pct):
    deposit = property_price * (deposit_pct / 100)
    loan = property_price - deposit
    monthly_payment = (loan * (rate / 100)) / 12  # Interest-only
    annual_rent = monthly_rent * 12
    agent_fee = annual_rent * 0.10  # 10% agent fee
    maintenance = property_price * 0.01  # 1% of value
    insurance = 600  # Estimate
    annual_expenses = agent_fee + maintenance + insurance
    annual_cash_flow = (annual_rent - annual_expenses) - (monthly_payment * 12)
    gross_yield = (annual_rent / property_price) * 100
    net_yield = (annual_cash_flow / property_price) * 100
    icr_pay = (monthly_rent / monthly_payment) * 100  # Fixed: *100 for %
    stressed_rate = 5.5  # Typical stress test
    stressed_payment = (loan * (stressed_rate / 100)) / 12
    icr_stress = (monthly_rent / stressed_payment) * 100  # Fixed: *100 for %
    upfront_fee = loan * (fee_pct / 100)
    
    return {
        'deposit': deposit,
        'loan': loan,
        'monthly_payment': monthly_payment,
        'annual_cash_flow': annual_cash_flow,
        'gross_yield': gross_yield,
        'net_yield': net_yield,
        'icr_pay': icr_pay,
        'icr_stress': icr_stress,
        'upfront_fee': upfront_fee
    }

def print_summary(deal_name, metrics, property_price, monthly_rent, deposit_pct, fixed_term):
    print(f"\n--- {deal_name} Deal Summary ---")
    print(f"Property Price: £{property_price:,.0f}")
    print(f"Monthly Rent: £{monthly_rent:,.0f}")
    print(f"Fixed Term: {fixed_term} years")
    print(f"Deposit: {deposit_pct}% (£{metrics['deposit']:,.0f})")
    print(f"Loan Amount: £{metrics['loan']:,.0f}")
    print(f"Upfront Fee: £{metrics['upfront_fee']:,.0f}")
    print(f"Monthly Interest Payment: £{metrics['monthly_payment']:.0f}")
    print(f"Annual Cash Flow (after basic expenses): £{metrics['annual_cash_flow']:,.0f}")
    print(f"Gross Rental Yield: {metrics['gross_yield']:.2f}%")
    print(f"Net Yield: {metrics['net_yield']:.2f}%")
    print(f"ICR (at pay rate): {metrics['icr_pay']:.0f}%")
    print(f"ICR (stressed at 5.5%): {metrics['icr_stress']:.0f}% (needs >125% for most lenders)")
    print("---")

def main():
    print("=== Limited Company BTL Interest-Only Deal Tester (Oct 2025) ===")
    
    try:
        property_price = parse_input("Enter property price (£, default 410,000): ", 410000)
        monthly_rent = parse_input("Enter monthly rent (£, default 1,700): ", 1700)
        deposit_pct = parse_input("Enter deposit % (default 25): ", 25)
        
        print("\nAvailable Deals:")
        for i, deal in enumerate
