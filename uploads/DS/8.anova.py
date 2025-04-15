import numpy as np
from scipy.stats import f_oneway
from statsmodels.stats.multicomp  import pairwise_tukeyhsd # type: ignore
import pandas as pd
import matplotlib.pyplot as plt

method_a = [80, 82, 85, 78, 88]
method_b = [75, 79, 82, 80, 81]
method_c = [70, 75, 78, 72, 80]

data = pd.DataFrame({'Method A': method_a, 'Method B': method_b, 'Method C': method_c})

f_statistic, p_value = f_oneway(method_a, method_b, method_c)

print("One-way ANOVA:")
print(f"F=statistic: {f_statistic}")
print(f"P-value: {p_value}")

if p_value < 0.05:
    print("Reject the null hypothesis. At least one group mean is different.")
else:
    print("Fail to reject the null hypothesis. No significant difference in group means.")
flatten_data = np.concatenate([method_a, method_b, method_c])
group_labels = np.repeat(['Method A', 'Method B', 'Method C'], len(method_a))
posthoc = pairwise_tukeyhsd(flatten_data, group_labels)

print("\nPost-hoc test:")
print(posthoc)

posthoc.plot_simultaneous()
plt.show()
