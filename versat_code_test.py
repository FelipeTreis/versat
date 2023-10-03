class AccountingRecord:
    def __init__(self, date, concept, value):
        self.date = date
        self.concept = concept
        self.value = value 

def calc_balance(records):
    current_assets = 0
    fixed_assets = 0
    current_liabilities = 0
    long_term_liabilities = 0

    for record in records:
        value = record.value
        if value > 0:
            current_assets += value
        else:
            current_liabilities -= value

    balance_sheet = {
        "Current Assets": current_assets,
        "Fixed Assets": fixed_assets,
        "Current Liabilities": current_liabilities,
        "Long Term Liabilities": long_term_liabilities
    }

    return balance_sheet

def calc_income_statement(records):
    total_revenue = 0
    total_expenses = 0

    for record in records:
        value = record.value
        if value > 0:
            total_revenue += value
        else:
            total_expenses -= value

    net_profit = total_revenue - total_expenses

    income_statement = { 
        "Total Revenue": total_revenue,
        "Total Expenses": total_expenses,
        "Net Profit": net_profit
    }

    return income_statement

def calc_liquidity_ratio(records):
    current_assets = 0
    current_liabilities = 0
    
    for record in records:
        value = record.value
        if value > 0:
            current_assets += value
        else:
            current_liabilities -= value

    liquidity_ratio = current_assets / current_liabilities
    return liquidity_ratio

def calc_profit_margin(records):
    result = calc_income_statement(records)
    total_revenue = result["Total Revenue"]
    net_profit = result["Net Profit"]

    profit_margin = (net_profit / total_revenue) * 100

    return profit_margin
