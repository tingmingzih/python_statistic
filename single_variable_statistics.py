import numpy as np

def calculate_statistics(data):
    mean = np.mean(data)
    variance = np.var(data)
    std_dev = np.std(data)
    return mean, variance, std_dev

data_str = input("Enter the data points separated by spaces: ")
data = np.array([float(x) for x in data_str.split()])

print("x    x²")

for x in data:
    x_squared = x ** 2
    print(f"{x:.10f}\t  {x_squared:.10f}")

sum_x_squared = np.sum(data**2)
sum_x = np.sum(data)
n = len(data)

print(f"\nSum of x: {sum_x}")
print(f"Sum of x²: {sum_x_squared}")
print(f"Number of data points (n): {n}")

mean, variance, std_dev = calculate_statistics(data)
print(f"\nMean: {mean:.10f}")
print(f"Variance: {variance:.10f}")
print(f"Standard Deviation: {std_dev:.10f}")
