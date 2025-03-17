import matplotlib.pyplot as plt
import numpy as np

# Data: Total posts viewed per day and count of negative-related posts per day for each account
total_posts_per_day = 10  # Constant number of posts viewed per day

# Days (2 to 10)
days = np.arange(2, 11)

negative_posts_control = [2, 2, 0, 0, 0, 0, 1, 0, 0]
negative_posts_test = [1, 3, 4, 6, 5, 6, 5, 7, 6]

negative_percent_control = [(count / total_posts_per_day) * 100 for count in negative_posts_control]
negative_percent_test = [(count / total_posts_per_day) * 100 for count in negative_posts_test]

plt.figure(figsize=(10, 5))
plt.plot(days, negative_percent_control, marker='o', linestyle='-', label="Control Account", color="blue")
plt.plot(days, negative_percent_test, marker='s', linestyle='-', label="Test Account", color="red")

plt.xlabel("Day")
plt.ylabel("Percentage of Negative Content Viewed (%)")
plt.legend()
plt.grid(True)

plt.show()
