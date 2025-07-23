from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from dotenv import load_dotenv
from crewai_tools import SerperDevTool,ScrapeWebsiteTool, FileWriterTool

load_dotenv()

@CrewBase
class AiNews():
    """AiNews crew"""
    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def retrieve_news(self) -> Agent:
        return Agent(
            config=self.agents_config['retrieve_news'],
            tools=[SerperDevTool()], 
            verbose=True
        )

    @agent
    def web_scrapper(self) -> Agent:
        return Agent(
            config=self.agents_config['web_scrapper'],
            tools=[ScrapeWebsiteTool()],
            verbose=True
        )

    @agent 
    def summarizer(self) -> Agent:
        return Agent(
            config=self.agents_config['summarizer'], 
            verbose=True
        )
    
    @agent 
    def file_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['file_writer'], 
            tools=[FileWriterTool()],
            verbose=True
        )
    @task
    def retrieve_news_task(self) -> Task:
        return Task(
            config=self.tasks_config['retrieve_news_task'], # type: ignore[index]
        )

    @task
    def website_scrape_task(self) -> Task:
        return Task(
            config=self.tasks_config['website_scrape_task'], # type: ignore[index]
        )
    
    @task 
    def ai_news_write_task(self) -> Task:
        return Task(
            config=self.tasks_config['ai_news_write_task'], # type: ignore[index]
        )
    
    @task
    def file_write_task(self) -> Task:
        return Task(
            config=self.tasks_config['file_write_task'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AiNews crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
