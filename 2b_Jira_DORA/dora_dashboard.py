import matplotlib.pyplot as plt

days = list(range(1, 11))
deployment_frequency = [2, 3, 2, 4, 3, 2, 5, 3, 4, 3]
lead_time = [4, 3, 5, 2, 4, 3, 6, 2, 3, 4]
change_failure_rate = [10, 20, 10, 15, 20, 10, 25, 15, 10, 20]
mttr = [3, 2, 4, 3, 5, 2, 4, 3, 2, 4]

metrics = [
    ("Deployment Frequency", deployment_frequency, "Deployments/day"),
    ("Lead Time for Changes", lead_time, "Hours"),
    ("Change Failure Rate", change_failure_rate, "Percent"),
    ("Mean Time to Recovery", mttr, "Hours"),
]

for title, values, ylabel in metrics:
    plt.figure(figsize=(8, 4))
    plt.plot(days, values, marker="o")
    plt.title(title)
    plt.xlabel("Day")
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(title.lower().replace(" ", "_") + ".png")
    plt.show()

print("Average Deployment Frequency:", sum(deployment_frequency)/len(deployment_frequency))
print("Average Lead Time:", sum(lead_time)/len(lead_time))
print("Average CFR:", sum(change_failure_rate)/len(change_failure_rate), "%")
print("Average MTTR:", sum(mttr)/len(mttr), "hours")
