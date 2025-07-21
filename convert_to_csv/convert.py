import pandas as pd

# Load the Excel file
df = pd.read_excel("quest_list.xlsx")

# Replace empty quest_owner values with "none"
if "quest_owner" in df.columns:
    df["quest_owner"] = df["quest_owner"].fillna("none")

# Save as CSV with ; as delimiter
df.to_csv("quest_list.csv", sep=";", index=False)

print("✅ quest_list.csv created with ; delimiter.")
