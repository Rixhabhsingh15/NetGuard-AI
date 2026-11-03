import random
import pandas as pd

data = []

for i in range(1000):

    fault = random.choice([
        "Normal",
        "Congestion",
        "Link_Failure",
        "Device_Overload",
        "Routing_Issue"
    ])

    if fault == "Normal":
        latency = random.randint(5, 30)
        packet_loss = random.uniform(0, 2)
        jitter = random.randint(1, 5)
        bandwidth = random.randint(20, 60)
        cpu = random.randint(20, 60)
        memory = random.randint(30, 65)
        error_rate = random.uniform(0, 2)

    elif fault == "Congestion":
        latency = random.randint(80, 180)
        packet_loss = random.randint(8, 25)
        jitter = random.randint(20, 50)
        bandwidth = random.randint(80, 100)
        cpu = random.randint(40, 80)
        memory = random.randint(40, 80)
        error_rate = random.randint(2, 10)

    elif fault == "Link_Failure":
        latency = random.randint(100, 250)
        packet_loss = random.randint(20, 50)
        jitter = random.randint(30, 70)
        bandwidth = random.randint(60, 100)
        cpu = random.randint(30, 75)
        memory = random.randint(30, 75)
        error_rate = random.randint(8, 20)

    elif fault == "Device_Overload":
        latency = random.randint(50, 150)
        packet_loss = random.randint(2, 10)
        jitter = random.randint(10, 30)
        bandwidth = random.randint(30, 70)
        cpu = random.randint(85, 100)
        memory = random.randint(85, 100)
        error_rate = random.randint(1, 8)

    else:
        latency = random.randint(70, 180)
        packet_loss = random.randint(5, 15)
        jitter = random.randint(15, 40)
        bandwidth = random.randint(40, 80)
        cpu = random.randint(30, 70)
        memory = random.randint(30, 70)
        error_rate = random.randint(5, 12)

    data.append([
        latency,
        round(packet_loss, 2),
        jitter,
        bandwidth,
        cpu,
        memory,
        round(error_rate, 2),
        fault
    ])

columns = [
    "latency",
    "packet_loss",
    "jitter",
    "bandwidth",
    "cpu",
    "memory",
    "error_rate",
    "fault"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("dataset.csv", index=False)

print("Dataset created successfully!")
print(df.head())
print("\nFault distribution:")
print(df["fault"].value_counts())