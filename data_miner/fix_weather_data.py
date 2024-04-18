import pandas as pd
import os

def is_alphanumeric_with_numeric(s):
    if s.isalnum() and any(char.isdigit() for char in s) and any(char.isalpha() for char in s):
        return True
    else:
        return False

def fix_columns(row):
    if is_alphanumeric_with_numeric(str(row['weather.description'])): #desc is icon
        if str(row['weather.icon']).isdigit(): #icon is code then code is desc
            row['weather.icon'], row['weather.description'], row['weather.code'] = row['weather.description'], row['weather.code'], row['weather.icon']
        else:
            row['weather.icon'], row['weather.description'] = row['weather.description'], row['weather.icon']
    elif str(row['weather.description']).isdigit():# desc is code
        if is_alphanumeric_with_numeric(str(row['weather.code'])):# code is icon then icon is desc
            row['weather.icon'], row['weather.description'], row['weather.code'] = row['weather.code'], row['weather.icon'], row['weather.description']
        else:
            row['weather.description'], row['weather.code'] = row['weather.code'], row['weather.description']
    return row

# Directory containing the CSV files
directory = './data/'

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)
        
        # Load the CSV file
        df = pd.read_csv(file_path)

        # Apply the fix_columns function
        df = df.apply(fix_columns, axis=1)

        # Save the DataFrame back to the CSV file
        df.to_csv(file_path, index=False)

print("All CSV files have been successfully fixed.")
