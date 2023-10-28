import statistics

# Create and load a dataset
dataset = [10, 20, 30, 40, 50, 60, 70, 80, 90, 15,
           25, 35, 45, 55, 65, 75, 85,95]

# Calculate statistics
mean = statistics.mean(dataset)
median = statistics.median(dataset)
mode_value = statistics.mode(dataset)
variance = statistics.variance(dataset)
std_dev = statistics.stdev(dataset)

# Finding the result 
print("Dataset Statistics:")
print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode_value}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_dev}")
