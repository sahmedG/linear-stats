import sys
import numpy as np
from scipy.stats import pearsonr, linregress

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = [int(line.strip()) for line in file]
        return data
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        sys.exit(1)
    except ValueError:
        print("Invalid data in the file. Ensure it contains only integers separated by newlines.")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    data = read_file(input_file)

    x = list(range(0, len(data)))
    y = data

    # Calculate Linear Regression Line
    slope, intercept, _, _, _ = linregress(x, y)
    print(f"Linear Regression Line: y = {slope:.6f}x + {intercept:.6f}")
    # Calculate Pearson Correlation Coefficient
    pearson_corr, _ = pearsonr(x, y)
    print(f"Pearson Correlation Coefficient: {pearson_corr:.10f}")


if __name__ == "__main__":
    main()
