import pandas as pd

# Sample data
data = [
    {"Name": "Alice Smith", "Email": "alice@example.com", "Address": "123 Maple St"},
    {"Name": "Bob Johnson", "Email": "bob@example.com", "Address": "456 Oak Ave"},
    {"Name": "Carol Lee", "Email": "carol@example.com", "Address": "789 Pine Rd"},
    {"Name": "David Kim", "Email": "david@example.com", "Address": "321 Cedar Blvd"},
    {"Name": "Eva Brown", "Email": "eva@example.com", "Address": "654 Birch Ln"},
]

# Create DataFrame
df = pd.DataFrame(data)

# Display the table
print(df)