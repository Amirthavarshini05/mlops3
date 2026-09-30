import matplotlib.pyplot as plt

days = list(range(1, 11))
data = {
    "Deployment Frequency": ([2,3,2,4,3,2,5,3,4,3], "Deployments/day"),
    "Lead Time": ([4,3,5,2,4,3,6,2,3,4], "Hours"),
    "CFR": ([10,20,10,15,20,10,25,15,10,20], "%"),
    "MTTR": ([3,2,4,3,5,2,4,3,2,4], "Hours"),
}

for name, (values, ylabel) in data.items():
    plt.figure(figsize=(8, 4))
    plt.bar(days, values)
    plt.title(name)
    plt.xlabel("Day")
    plt.ylabel(ylabel)
    plt.tight_layout()
    plt.savefig(name.replace(" ", "_").lower() + ".png")
    plt.show()
