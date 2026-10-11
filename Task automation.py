import time

tasks = [
    "Complete assignment",
    "Study for exam",
    "Submit project"
]

print("Daily Task Automation")

for task in tasks:
    print("Reminder:", task)
    time.sleep(2)

print("All tasks displayed successfully!")
