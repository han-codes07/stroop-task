import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("stroop_results.csv")

# Add a 'congruent' column: when word and font color are the same
df["congruent"] = df["word_shown"] == df["font_color"]

# Print summary
print("Average Reaction Time:", df["reaction_time"].mean())
print("Accuracy:", df["correct"].mean())

# Plot reaction times
plt.figure(figsize=(10, 5))
plt.plot(df["trial"], df["reaction_time"], marker='o')
plt.title("Reaction Time per Trial")
plt.xlabel("Trial")
plt.ylabel("Reaction Time (s)")
plt.grid(True)
plt.show()

# Bar plot: avg RT for congruent vs. incongruent
plt.figure(figsize=(6, 4))
df.groupby("congruent")["reaction_time"].mean().plot(kind="bar", color=["green", "red"])
plt.xticks([0, 1], ["Incongruent", "Congruent"], rotation=0)
plt.ylabel("Avg Reaction Time (s)")
plt.title("Reaction Time: Congruent vs Incongruent")
plt.tight_layout()
plt.show()

# Accuracy plot
plt.figure(figsize=(6, 4))
df["correct"].value_counts().plot(kind="bar", color=["red", "green"])
plt.xticks([0, 1], ["Incorrect", "Correct"], rotation=0)
plt.ylabel("Number of Trials")
plt.title("Accuracy Count")
plt.tight_layout()
plt.show()
