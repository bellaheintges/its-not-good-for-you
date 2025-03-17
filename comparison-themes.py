# Figure  4.  Visualized comparison of themes in content propagated on each #ForYou page

from collections import Counter
import matplotlib.pyplot as plt
import pandas as pd

control_themes = [
    "Advice", "Edit", "Food", "Edit", "Jewelry", "Advice", "Miscellaneous", "Edit", "Beauty", "Vanity",
    "Music", "Education", "Education", "Education", "Nature", "Dance", "News", "Beauty", "Beauty", "Beauty",
    "News", "Edit", "Filter", "Beauty", "Nature", "Filter", "Food", "News", "Beauty", "Filter",
    "Food", "Filter", "Sports", "Ad", "Depression", "Dance", "Beauty", "Meme", "Filter", "Music",
    "Ad", "Dance", "Sports", "Miscellaneous", "Nature", "Nature", "Nature", "Depression", "Depression", "Beauty",
    "Dance", "Vanity", "Edit", "Beauty", "News", "Beauty", "Edit", "Music", "Meme", "Beauty",
    "Advice", "Edit", "Food", "Food", "Filter", "Edit", "Filter", "Filter", "Advice", "Dance",
    "Dance", "Meme", "Dance", "Meme", "Nature", "Dance", "Meme", "Music", "News", "News",
    "Meme", "Dance", "Beauty", "Filter", "Advice", "Filter", "Beauty", "Filter", "Filter", "Beauty"
]

test_themes = [
    "Edit", "Filter", "Edit", "Filter", "Edit", "Dance", "Dance", "Vanity", "Meme", "Meme",
    "Filter", "Edit", "Vanity", "Edit", "Music", "Music", "Vanity", "Diet", "Filter", "Dance",
    "Dance", "Filter", "Diet", "Dance", "Diet", "Diet", "Animals", "Fitness", "Fitness", "Food",
    "Edit", "Filter", "Diet", "Advice", "Fitness", "Diet", "Restrictive", "Filter", "Fitness", "Restrictive",
    "Vanity", "Diet", "Filter", "Miscellaneous", "Diet", "Edit", "Edit", "Dance", "Dance", "Fitness",
    "Music", "Fitness", "News", "Edit", "Diet", "News", "Diet", "Music", "Vanity", "Depression",
    "Diet", "Food", "Fitness", "Vanity", "Diet", "Edit", "Fitness", "Filter", "Vanity", "Fitness",
    "Diet", "Edit", "Diet", "News", "Fitness", "Beauty", "Diet", "Vanity", "Diet", "Ad",
    "Diet", "Filter", "Fitness", "Filter", "Diet", "Restrictive", "Restrictive", "Vanity", "Beauty", "News"
]

control_counts = Counter(control_themes)
test_counts = Counter(test_themes)

all_themes = sorted(set(control_counts.keys()).union(set(test_counts.keys())))

control_values = [control_counts.get(theme, 0) for theme in all_themes]
test_values = [test_counts.get(theme, 0) for theme in all_themes]

theme_counts_df = pd.DataFrame({
    "Theme": all_themes,
    "Control Account": control_values,
    "Test Account": test_values
})

total_control = sum(control_values)
total_test = sum(test_values)
total_all = total_control + total_test

theme_counts_df.loc[len(theme_counts_df)] = ["Total", total_control, total_test]

theme_counts_df["Total Count"] = theme_counts_df["Control Account"] + theme_counts_df["Test Account"]

fig, ax = plt.subplots(figsize=(12,6))
ax.bar(all_themes, control_values, label="Control Account", color="blue", alpha=0.7)
ax.bar(all_themes, test_values, bottom=control_values, label="Test Account", color="red", alpha=0.7)

plt.xticks(rotation=90)
plt.xlabel("Themes")
plt.ylabel("Frequency")
plt.title("Comparison of Themes Across Control and Test Accounts")
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.7)

plt.show()
