
processes = {
    "P1": 0,
    "P2": 0,
    "P3": 0,
    "P4": 0,
    "P5": 0
}

messages = [
    ("P1", "P2"),
    ("P1", "P3"),
    ("P2", "P4"),
    ("P3", "P5"),
    ("P4", "P1"),
    ("P5", "P2"),
    ("P2", "P3"),
    ("P3", "P4"),
    ("P4", "P5"),
    ("P5", "P1")
]

timestamps = []

for i, (sender, receiver) in enumerate(messages, start=1):
    # Send event
    processes[sender] += 1
    send_time = processes[sender]

    # Receive event
    processes[receiver] = max(processes[receiver], send_time) + 1
    receive_time = processes[receiver]

    timestamps.append(
        f"M{i}: {sender} sends at {send_time}, {receiver} receives at {receive_time}"
    )

# Display results
for entry in timestamps:
    print(entry)
