import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load data
data = {
    'customer_id': [12345, 67890, 54321, 24680, 13579, 98765, 11223, 99887, 66778, 43210, 45678, 54329, 23456, 87654, 13580, 98764, 11224, 99888, 66779, 43211],
    'customer_name': ['John Doe', 'Jane Smith', 'Mike Johnson', 'Emily Brown', 'David Lee', 'Sarah Wilson', 'Lisa Davis', 'Chris Clark', 'Olivia Martinez', 'Alex Thompson', 'Jessica White', 'Michael Green', 'Sophia Hall', 'William Turner', 'Amanda Young', 'Daniel King', 'Elizabeth Scott', 'Matthew Baker', 'Ashley Garcia', 'Kevin Lewis'],
    'age': [35, 28, 45, 40, 30, 32, 38, 50, 27, 33, 42, 37, 29, 48, 31, 36, 39, 47, 26, 34],
    'gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'total_spent': [2500.00, 1500.00, 4500.00, 3000.00, 1800.00, 2200.00, 3500.00, 4000.00, 1200.00, 2800.00, 3200.00, 3800.00, 2000.00, 4200.00, 2600.00, 3400.00, 3700.00, 4300.00, 1100.00, 3000.00]
}

df = pd.DataFrame(data)

# Encode 'gender'
label_encoder = LabelEncoder()
df['gender'] = label_encoder.fit_transform(df['gender'])
df['age'] = pd.to_numeric(df['age'], errors='coerce')  # Converts 'age' to numeric, setting non-convertible values to NaN

# Convert 'age' and 'gender' columns to float
df['age'] = df['age'].astype(float)
df['gender'] = df['gender'].astype(float)

# Drop non-numeric columns
df = df.drop(columns=['customer_id', 'customer_name'])

print(df.head())
print(df.dtypes)
# Save prepared data to CSV
df.to_csv('prepared_data.csv', index=False)

