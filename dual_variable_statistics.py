import numpy as np

def calculate_statistics(data_x, data_f):
    sum_fx = np.sum(data_x * data_f)
    sum_fx_squared = np.sum((data_x ** 2) * data_f)
    sum_f = np.sum(data_f)
    sum_x_squared = np.sum(data_x ** 2)
    count_x = len(data_f)
    mean = sum_fx / sum_f
    variance = (sum_fx_squared / sum_f) - (mean ** 2)
    std_dev = np.sqrt(variance)
    return mean, variance, std_dev, sum_fx, sum_fx_squared, sum_f, sum_x_squared, count_x

data_x_str = input("Enter the data points (x) separated by spaces: ")
data_f_str = input("Enter the corresponding frequencies (f) separated by spaces: ")
data_x = np.array([float(x) for x in data_x_str.split()])
data_f = np.array([float(f) for f in data_f_str.split()])

print("x\t  f\t  x²\t  fx\t  fx²")

for x, f in zip(data_x, data_f):
    x_squared = x ** 2
    fx = x * f
    fx_squared = (x ** 2) * f
    print(f"{x:.3f}\t  {f:.3f}\t  {x_squared:.3f}\t  {fx:.3f}\t  {fx_squared:.3f}")

mean, variance, std_dev, sum_fx, sum_fx_squared, sum_f, sum_x_squared, count_x = calculate_statistics(data_x, data_f)
print("\nSummary:")
print(f"Sum of x²: {sum_x_squared:.10f}")
print(f"Sum of f: {sum_f:.10f}")
print(f"Sum of fx: {sum_fx:.10f}")
print(f"Sum of fx²: {sum_fx_squared:.10f}")
print(f"Total number of data points (n): {count_x}")

print("\nMean: {:.10f}".format(mean))
print("Variance: {:.10f}".format(variance))
print("Standard Deviation: {:.10f}".format(std_dev))
