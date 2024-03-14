from crewai import Crew, Process

from agents import BloggingAutomationAgents
from tasks import BlogPostAutomationTasks
from tools.serper_dev_tool import SerperDevTool
from models import LargeLanguageModel


from dotenv import load_dotenv
load_dotenv()

llm = LargeLanguageModel()

# Initialize the Language Models
openai35 = llm.chat_Openai(temp=0.3)
gemini = llm.gemini()
mixtral = llm.mixtral_groq(temp=0.3)

# Instantiate agents, tasks and tools
agents = BloggingAutomationAgents()
tasks = BlogPostAutomationTasks()

web_search_tool = SerperDevTool()


# Create agents
blogging_manager = agents.blogging_manager(openai35)
web_searcher = agents.web_research_manager(openai35, web_search_tool)
title_creator = agents.title_creator(openai35)
post_creator = agents.post_creator(openai35)
spanish_translator = agents.post_translator(openai35)


# Determine blog post topic
post_topic = "Artists and technologists are collaborating to push the boundaries of creativity."

# Tasks
manage_blog_post_creation = tasks.manage_blog_post_creation(
    blogging_manager, post_topic)
web_search_report = tasks.manage_websearch(
    web_searcher, post_topic)
title_creation = tasks.manage_title_creation(
    title_creator, post_topic)
write_post = tasks.manage_post_writing(
    post_creator, post_topic)
translate_post = tasks.spanish_translation(
    spanish_translator, post_topic)

# Assemble the Crew
crew = Crew(
    agents=[blogging_manager,
            web_searcher,
            title_creator,
            post_creator,
            spanish_translator
            ],
    tasks=[manage_blog_post_creation,
           web_search_report,
           title_creation,
           write_post,
           translate_post
           ],
    process=Process.hierarchical,
    manager_llm=openai35,
)

# Kick of the crew
results = crew.kickoff()

print("Crew usage", crew.usage_metrics)
