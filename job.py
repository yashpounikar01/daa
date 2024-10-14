class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def job_sequencing(jobs, n):
    # Sort jobs according to descending order of profit
    jobs.sort(key=lambda job: job.profit, reverse=True)

    # Find the maximum deadline
    max_deadline = max(job.deadline for job in jobs)
    
    # Initialize a slot array to keep track of free time slots
    slots = [-1] * max_deadline
    
    # Initialize the result array
    result = [None] * n
    
    # Iterate through all jobs
    for job in jobs:
        # Find a free slot for this job (from the last possible slot)
        for j in range(min(max_deadline, job.deadline) - 1, -1, -1):
            if slots[j] == -1:
                slots[j] = job.id
                result[j] = job
                break
    
    # Print the jobs in the sequence of their deadlines
    print("Job ID | Deadline | Profit")
    for job in result:
        if job is not None:
            print(f"   {job.id}    |    {job.deadline}     |   {job.profit}")

if __name__ == "__main__":
    # Input number of jobs
    n = int(input("Enter the number of jobs: "))
    
    # List to store jobs
    jobs = []
    
    # Input job details
    for i in range(n):
        job_id = int(input(f"Enter Job ID for job {i + 1}: "))
        deadline = int(input(f"Enter Deadline for job {i + 1}: "))
        profit = int(input(f"Enter Profit for job {i + 1}: "))
        jobs.append(Job(job_id, deadline, profit))
    
    # Perform job sequencing
    job_sequencing(jobs, n)
