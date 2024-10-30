# interview_simulation.py
import os
from typing import List
import json
from datetime import datetime
from crewai import Crew, Process

from agents import create_interviewer, create_candidate
from tasks import (
    create_question_task, 
    create_answer_task, 
    create_evaluation_task,
    create_comparative_analysis_task
)

class InterviewSimulation:
    def __init__(self, job_title: str):
        self.job_title = job_title
        self.models = {
            "candidate1": "groq/llama-3.1-8b-instant",
            "candidate2": "groq/llama3-8b-8192",
            "candidate3": "groq/mixtral-8x7b-32768",
            "candidate4": "groq/llama2-70b-4096",
        }
        self.interview_results = {}
        self.interviewer = create_interviewer(job_title)

    def conduct_single_interview(self, candidate_id: str, num_questions: int = 5) -> dict:
        print(f"\n=== Starting Interview for Candidate using {self.models[candidate_id]} ===\n")
        
        candidate = create_candidate(self.job_title, self.models[candidate_id])
        interview_history = []
        
        for i in range(num_questions):
            # Generate question
            question_crew = Crew(
                agents=[self.interviewer],
                tasks=[create_question_task(self.job_title, self.interviewer, i + 1, interview_history)],
                process=Process.sequential
            )
            question = str(question_crew.kickoff())
            print(f"\nCo-founder: {question}")
            
            # Generate answer
            answer_crew = Crew(
                agents=[candidate],
                tasks=[create_answer_task(question, candidate)],
                process=Process.sequential
            )
            answer = str(answer_crew.kickoff())
            print(f"Candidate: {answer}\n")
            
            interview_history.append({
                "question": question,
                "answer": answer
            })

        # Generate evaluation
        evaluation_crew = Crew(
            agents=[self.interviewer],
            tasks=[create_evaluation_task(self.job_title, self.interviewer, interview_history)],
            process=Process.sequential
        )
        evaluation = str(evaluation_crew.kickoff())
        
        return {
            "model": self.models[candidate_id],
            "interview_history": interview_history,
            "evaluation": evaluation
        }

    def conduct_interviews(self, num_questions: int = 5):
        for candidate_id in self.models.keys():
            self.interview_results[candidate_id] = self.conduct_single_interview(candidate_id, num_questions)

        analysis_crew = Crew(
            agents=[self.interviewer],
            tasks=[create_comparative_analysis_task(
                self.job_title, 
                self.interviewer, 
                self.interview_results,
                self.models
            )],
            process=Process.sequential
        )
        comparative_analysis = str(analysis_crew.kickoff())
        
        filename = self.save_results(comparative_analysis)
        
        print("\n=== Comparative Analysis ===\n")
        print(comparative_analysis)
        print(f"\nResults saved to: {filename}")
        
        return comparative_analysis

    def save_results(self, comparative_analysis: str):
        results = {
            "job_title": self.job_title,
            "interview_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "candidates": self.interview_results,
            "comparative_analysis": comparative_analysis
        }
        
        filename = f"interview_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2)
        return filename
