def generate_table(n, m):
    # Define column width for alignment
    col_width = 7  # Adjust this value to control column width

    # Create the header row with aligned columns
    header = "| " + " | ".join([f"Col{i+1}".ljust(col_width) for i in range(n)]) + " |\n"
    
    # Create the separator row with aligned dashes
    separator = "| " + " | ".join(["-" * col_width for _ in range(n)]) + " |\n"
    
    # Create the data rows with aligned columns
    rows = ""
    for j in range(m):
        rows += "| " + " | ".join([f"Row{j+1}".ljust(col_width) for _ in range(n)]) + " |\n"
    
    # Combine all parts into a markdown table
    table = header + separator + rows
    return table

# Example usage:
n = 3  # Number of columns
m = 1  # Number of rows
t2 = generate_table(n, m)

def helper_method(n,m):
    return {
        f"table{m}x{n}": {
            "prefix": f"/table{m}x{n}",
            "body": generate_table(n, m).split("\n")[:-1],
            "description": f"Generate table with {m} rows {n} columns"
        }
    }

import json
res = {}
for i in range(1, 11):
    for j in range(1, 11):
        res.update(helper_method(i, j))
print(json.dumps(res))