#ejecicios 1
import scipy.stats as stats
diet_1 = [2.0, 2.5, 3.0, 2.8, 2.3, 2.7, 2.5]
diet_2 = [3.0, 3.2, 3.1, 2.9, 2.8, 3.0, 3.2]

# Student's t-test
t_value, p_value = stats.ttest_ind(diet_1, diet_2)

print(f"t-value: {t_value}")
print(f"p-value: {p_value}")

#ejercio 2
import scipy.stats as stats

fertilizer_1 = [20, 21, 20, 19, 20]
fertilizer_2 = [22, 21, 23, 22, 21]
fertilizer_3 = [24, 23, 22, 23, 24]

# ANOVA test
f_value, p_value = stats.f_oneway(fertilizer_1, fertilizer_2, fertilizer_3)

print(f"f-value: {f_value}")
print(f"p-value: {p_value}")

#ejercio 3

import numpy as np
from statsmodels.stats.multicomp import pairwise_tukeyhsd

data = np.concatenate([fertilizer_1, fertilizer_2, fertilizer_3])
labels = ["F1"] * 5 + ["F2"] * 5 + ["F3"] * 5

# Tukey test
result = pairwise_tukeyhsd(data, labels, alpha = 0.05)
print(result)

