# agents.py
from crewai import Agent
from typing import List

def create_interviewer(job_title: str) -> Agent:
    """Creates and returns the interviewer agent (Co-founder)"""
    return Agent(
        role="Co-founder and CEO",
        goal=f"Evaluate candidates for the {job_title} position and make hiring decisions",
        backstory="""You are the co-founder of a fast-growing startup. You believe in 
        hiring people who are not just skilled, but also passionate, adaptable, and 
        align with your company culture. You create dynamic questions based on 
        candidate responses to thoroughly evaluate their potential.""",
        verbose=True,
        allow_delegation=False,
        llm="groq/llama-3.1-8b-instant"
    )

def create_candidate(job_title: str, model_name: str) -> Agent:
    """Creates and returns a candidate agent with specified LLM model"""
    return Agent(
        role="Fresh Graduate Candidate",
        goal=f"Secure the {job_title} position by demonstrating potential and enthusiasm",
        backstory="""You are a recent graduate eager to start your career. While you 
        lack professional experience, you have relevant academic projects and a strong 
        desire to learn and grow. You provide honest, enthusiastic responses while 
        showing your potential.""",
        verbose=True,
        allow_delegation=False,
        llm=model_name
    )
