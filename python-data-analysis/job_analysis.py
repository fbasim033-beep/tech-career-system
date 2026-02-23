# Tech Career Job Data Analysis System
# Author: Fatima
# Description: Simple analysis for tech job salaries using Python

jobs = [
    {"title": "Python Developer", "salary": 1200},
    {"title": "Java Developer", "salary": 1100},
    {"title": "Data Analyst", "salary": 1000},
    {"title": "Medical Physicist", "salary": 1500},
    {"title": "Backend Developer", "salary": 1300}
]

def average_salary(job_list):
    total = 0
    for job in job_list:
        total += job["salary"]
    return total / len(job_list)

def highest_paying_job(job_list):
    return max(job_list, key=lambda x: x["salary"])

print("=== Tech Career Analysis ===")
print("Average Salary:", average_salary(jobs))
print("Highest Paying Job:", highest_paying_job(jobs)["title"])
