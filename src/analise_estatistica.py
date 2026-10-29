import numpy as np
import pandas as pd

print(" Starting Advanced Statistical Analysis...")

# ==============================================================================
# 1. LOADING PROCESSED DATA
# ==============================================================================
try:
    df = pd.read_csv("processed_transactions_EmpresaX.csv")
    print(
        f" Database loaded successfully! Records for analysis: {len(df)}"
    )
except FileNotFoundError:
    print(
        " Error: The file 'processed_transactions_EmpresaX.csv' was not found."
    )
    exit()

# Filtering only 'Approved' transactions to prevent skewing the real consumption analysis
df_approved = df[df["status"] == "Approved"].copy()

# ==============================================================================
# 2. DESCRIPTIVE STATISTICS
# ==============================================================================
# Using Pandas and NumPy to calculate population spending metrics
mean_spending = df_approved["amount_usd"].mean()
median_spending = df_approved["amount_usd"].median()
standard_deviation = df_approved["amount_usd"].std()

print("\n --- STATISTICAL SPENDING SUMMARY (USD) ---")
print(f"• Transaction Mean:         ${mean_spending:,.2f}")
print(f"• Median (Central Value):   ${median_spending:,.2f}")
print(f"• Standard Deviation (Var): ${standard_deviation:,.2f}")
print("----------------------------------------------")

# ==============================================================================
# 3. ANOMALY DETECTION WITH Z-SCORE (Outlier Identification)
# ==============================================================================
print("\n Vector-calculating the Z-Score for each transaction...")

# Mathematical Z-Score formula applied with Pandas/NumPy: (Value - Mean) / Standard Deviation
df_approved["Z_Score"] = (df_approved["amount_usd"] - mean_spending) / standard_deviation

# Financial business rule: Any spending with a Z-Score greater than 3 completely deviates
# from normal behavior (outlier) and must be flagged for a fraud audit.
statistical_limit = 3
anomalies = df_approved[df_approved["Z_Score"] > statistical_limit]

print(
    f" System Alert: Found {len(anomalies)} transactions with anomalous behavior!"
)

# ==============================================================================
# 4. DISPLAY AND EXPORT OF AUDIT RESULTS
# ==============================================================================
print("\n Table of Isolated Suspicious Transactions for the Risk Team:")
display_columns = [
    "transaction_id",
    "company",
    "country",
    "category",
    "amount_usd",
    "Z_Score",
]

# Displaying the final result on screen in an organized format
print(anomalies[display_columns].to_string(index=False))

# Saving the fraud/alert table to feed the audit and the BI dashboard
anomalies[display_columns].to_csv("fraud_alerts_audit.csv", index=False)
print(
    "\n Audit file successfully saved as 'fraud_alerts_audit.csv'!"
)
print(" Pipeline finished with 100% success!")
