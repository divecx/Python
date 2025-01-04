# Measures of central tendency and dispersion\

# 1. Central Tendency
#     - Mean: the average values of a dataset
#     - median: the middle value when data is sorted
#     - mode: the most frequently occurring value

# from statistics import mode

# data = [10, 20, 30, 40, 50, 20]
# mean = sum(data) /len(data)

# print("Mean: ", mean)

# sorted_data = sorted(data)
# median = sorted_data[len(data) // 2] if len(data) % 2 != 0 else (sorted_data[len(data) // 2 - 1] + sorted_data[len(data) // 2]) / 2

# print("Median: ", median)

# print("Mode: ", mode(data))

# 2. Dispersion
#     - Variance: the average squared deviation from the mean
#     - Standard Deviation: the square root of variance, indicating the spread of data. python copy code
# variance = sum((x - mean) ** 2 for x in data) / len(data)
# print("Variance: ", variance)

# std_dev = variance ** 0.5
# print("Standard Deviation: ", std_dev)

# 3. Hypothesis Testing
#     - Steps
#         - Formulate hypotheses: null hypothesis, alternative hypothesis
#         - calculate test statistic
#         - determine P-Value
#         - Interpret Results

# 4. Confidence intervals and statistical significance
#     - confidence interval: range of values within which the true population parameter is expected to lie 

import scipy.stats as stats

data = [10, 20, 30, 40, 50]
mean = sum(data) / len(data)

variance = sum((x - mean) ** 2 for x in data) / len(data)
std_dev = variance ** 0.5

sample_mean = mean 
z_score = 1.96

ci = (sample_mean - z_score * (std_dev / len(data) ** 0.5), 
      sample_mean + z_score * (std_dev / len(data) ** 0.5))

print("95% Confidence Interval: ", ci)