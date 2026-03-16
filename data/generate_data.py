import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta
import os

fake = Faker()
random.seed(42)
np.random.seed(42)

NUM_CUSTOMERS = 500
START_DATE = datetime(2024, 1, 1)
END_DATE = datetime(2026, 3, 31)

SEGMENTS = {
    "Enterprise":  {"weight": 0.20, "mrr_min": 5000,  "mrr_max": 15000, "churn_rate": 0.01},
    "Mid-Market":  {"weight": 0.35, "mrr_min": 1000,  "mrr_max": 4999,  "churn_rate": 0.03},
    "SMB":         {"weight": 0.45, "mrr_min": 200,   "mrr_max": 999,   "churn_rate": 0.06},
}

def generate_customers():
    customers = []
    seg_names = list(SEGMENTS.keys())
    seg_weights = [SEGMENTS[s]["weight"] for s in seg_names]
    for i in range(1, NUM_CUSTOMERS + 1):
        segment = random.choices(seg_names, weights=seg_weights)[0]
        signup = START_DATE + timedelta(days=random.randint(0, 600))
        customers.append({
            "customer_id": i,
            "company_name": fake.company(),
            "segment": segment,
            "country": random.choices(["Canada","USA","UK","Australia"], weights=[0.5,0.3,0.1,0.1])[0],
            "signup_date": signup.strftime("%Y-%m-%d"),
        })
    return pd.DataFrame(customers)

def generate_contracts(customers_df):
    contracts = []
    for _, cust in customers_df.iterrows():
        seg = SEGMENTS[cust["segment"]]
        mrr = round(random.uniform(seg["mrr_min"], seg["mrr_max"]), -1)
        start = datetime.strptime(cust["signup_date"], "%Y-%m-%d")
        contracts.append({
            "contract_id": cust["customer_id"],
            "customer_id": cust["customer_id"],
            "mrr": mrr,
            "arr": mrr * 12,
            "start_date": start.strftime("%Y-%m-%d"),
            "end_date": None,
            "status": "Active",
        })
    return pd.DataFrame(contracts)

def generate_revenue(customers_df, contracts_df):
    transactions = []
    txn_id = 1
    current = START_DATE
    while current <= END_DATE:
        for _, cust in customers_df.iterrows():
            signup = datetime.strptime(cust["signup_date"], "%Y-%m-%d")
            if signup > current:
                continue
            contract = contracts_df[contracts_df["customer_id"] == cust["customer_id"]].iloc[0]
            seg = SEGMENTS[cust["segment"]]
            if random.random() < seg["churn_rate"]:
                continue
            noise = random.uniform(0.97, 1.03)
            revenue = round(contract["mrr"] * noise, 2)
            transactions.append({
                "transaction_id": txn_id,
                "customer_id": cust["customer_id"],
                "month": current.strftime("%Y-%m-%d"),
                "revenue": revenue,
                "segment": cust["segment"],
            })
            txn_id += 1
        current = (current.replace(day=1) + timedelta(days=32)).replace(day=1)
    return pd.DataFrame(transactions)

def generate_headcount():
    headcount = []
    dept_sizes = {"Sales & Marketing": 12, "R&D": 10, "G&A": 6, "Engineering": 8, "Operations": 6}
    salary_ranges = {
        "Sales & Marketing": (60000, 120000),
        "R&D": (80000, 150000),
        "G&A": (55000, 110000),
        "Engineering": (85000, 160000),
        "Operations": (50000, 95000),
    }
    emp_id = 1
    for dept, size in dept_sizes.items():
        for _ in range(size):
            sal_min, sal_max = salary_ranges[dept]
            hire = START_DATE + timedelta(days=random.randint(-365, 600))
            headcount.append({
                "employee_id": emp_id,
                "name": fake.name(),
                "department": dept,
                "salary": round(random.uniform(sal_min, sal_max), -3),
                "hire_date": hire.strftime("%Y-%m-%d"),
                "status": "Active",
            })
            emp_id += 1
    return pd.DataFrame(headcount)

def generate_budget():
    budget = []
    monthly_targets = {
        "Sales & Marketing": 85000,
        "R&D": 70000,
        "G&A": 45000,
        "Engineering": 75000,
        "Operations": 38000,
    }
    current = START_DATE
    while current <= END_DATE:
        for dept, base in monthly_targets.items():
            growth = 1 + (0.005 * ((current - START_DATE).days / 30))
            budgeted = round(base * growth, -2)
            actual = round(budgeted * random.uniform(0.88, 1.18), -2)
            budget.append({
                "month": current.strftime("%Y-%m-%d"),
                "department": dept,
                "budgeted_opex": budgeted,
                "actual_opex": actual,
                "variance": round(actual - budgeted, -2),
            })
        current = (current.replace(day=1) + timedelta(days=32)).replace(day=1)
    return pd.DataFrame(budget)

print("Generating customers...")
customers = generate_customers()
customers.to_csv("data/customers.csv", index=False)

print("Generating contracts...")
contracts = generate_contracts(customers)
contracts.to_csv("data/contracts.csv", index=False)

print("Generating revenue transactions...")
revenue = generate_revenue(customers, contracts)
revenue.to_csv("data/revenue_transactions.csv", index=False)

print("Generating headcount...")
headcount = generate_headcount()
headcount.to_csv("data/headcount.csv", index=False)

print("Generating budget...")
budget = generate_budget()
budget.to_csv("data/budget.csv", index=False)

print("\nDone! Files saved to data/")
print(f"  customers:    {len(customers)} rows")
print(f"  contracts:    {len(contracts)} rows")
print(f"  revenue:      {len(revenue)} rows")
print(f"  headcount:    {len(headcount)} rows")
print(f"  budget:       {len(budget)} rows")