# Figure  5.  Cumulative negative content viewed over the 10-day period across the #ForYou pages on both accounts. Note: Posts identified with the themes fitness, diet, vanity, depression, and restrictive were considered relevant criteria.

import matplotlib.pyplot as plt
import numpy as np

# Data: Total posts viewed per day and count of negative-related posts per day for each account

# Days (2 to 10)
days = np.arange(2, 11)

# Negative content posts per day for each account
negative_posts_control = [2, 2, 0, 0, 0, 0, 1, 0, 0]
negative_posts_test = [1, 3, 4, 6, 5, 6, 5, 7, 6]

total_negative_control = np.cumsum(negative_posts_control)
total_negative_test = np.cumsum(negative_posts_test)

plt.figure(figsize=(10, 5))
plt.plot(days, total_negative_control, marker='o', linestyle='-', label="Control Account", color="blue")
plt.plot(days, total_negative_test, marker='s', linestyle='-', label="Test Account", color="red")

for i, txt in enumerate(total_negative_control):
    plt.text(days[i], total_negative_control[i] + 1, str(txt), ha='center', fontsize=10, color='blue')
for i, txt in enumerate(total_negative_test):
    if i == 0:
      plt.text(days[i], total_negative_test[i] + 4, str(txt), ha='center', fontsize=10, color='red')
    else:
      plt.text(days[i], total_negative_test[i] + 1, str(txt), ha='center', fontsize=10, color='red')

plt.xlabel("Day")
plt.ylabel("Cumulative Count of Negative Content Viewed")
plt.legend()
plt.grid(True)

plt.yticks(np.arange(0, 50 + 2, 5))

plt.show()
