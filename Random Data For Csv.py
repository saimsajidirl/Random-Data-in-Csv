import csv
import random

# Define the denominations
denominations = [100, 200, 750, 1500, 7500, 15000, 25000, 40000]

# Define the number of entries per denomination
entries_per_denomination = 10

# Define the range for bond numbers
start_bond_num = 1
end_bond_num = 100000

# Generate a list of random bond numbers
bond_numbers = random.sample(range(start_bond_num, end_bond_num + 1), len(denominations) * entries_per_denomination)

# Open a CSV file to write
with open('bonds.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['denomination_num', 'bond_num'])
    
    # Write entries with the correct denomination pattern
    for i, bond_num in enumerate(bond_numbers):
        # Format bond number as 6 digits
        bond_num_str = str(bond_num).zfill(6)
        
        # Select a denomination based on the block
        denomination_num = denominations[(i // entries_per_denomination) % len(denominations)]
        
        # Write to CSV
        writer.writerow([denomination_num, bond_num_str])

print("CSV file 'bonds.csv' created successfully.")
