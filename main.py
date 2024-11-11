# main.py
from interview_simulation import InterviewSimulation

def main():
    job_titles = [
        "Marketing Associate",
        "Business Development Representative",
        "Product Manager",
        "Customer Success Representative",
        "Data Analyst",
        "Content Creator",
        "AI Engineer" #add more if you want
    ]
    
    job_title = job_titles[5]  # Change index to try different positions
    simulation = InterviewSimulation(job_title)
    simulation.conduct_interviews()

if __name__ == "__main__":
    main()
