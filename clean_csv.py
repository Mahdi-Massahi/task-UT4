import pandas as pd

# Read the CSV file
data = pd.read_csv("data.csv")

# Remove duplicates
data = data.drop_duplicates()

# Fill missing values
data = data.fillna(0)

# Convert dates
data["date"] = pd.to_datetime(data["date"])

# Save the cleaned data to a new CSV file
data.to_csv("cleaned_data.csv", index=False)
