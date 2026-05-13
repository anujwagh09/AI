def job_scheduling(jobs):
    # Sort jobs based on profit (descending order)
    jobs.sort(key=lambda x: x[2], reverse=True)

    n = len(jobs)
    slot = [0] * n
    profit = 0

    for job in jobs:
        # Find a free slot for this job (starting from last possible slot)
        for j in range(min(n, job[1]) - 1, -1, -1):
            if slot[j] == 0:
                slot[j] = job[0]
                profit += job[2]
                break

    print("Jobs done:", slot)
    print("Total Profit:", profit)


# Jobs format: (JobID, Deadline, Profit)
jobs = [
    ('J1', 2, 100),
    ('J2', 1, 50),
    ('J3', 2, 10),
    ('J4', 1, 20),
    ('J5', 3, 30)
]

# Function call
job_scheduling(jobs)