from crewai import Crew, Process

from crew.agents import BloggingAutomationAgents
from crew.tasks import BlogPostAutomationTasks
from tools.serper_dev_tool import SerperDevTool
from tools.count_words_tool import WordsCountTool
from models.models import LargeLanguageModel


from dotenv import load_dotenv
load_dotenv()

llm = LargeLanguageModel()

# Initialize the Language Models
openai35 = llm.chat_Openai(temp=0.6)
gemini = llm.gemini()
mixtral = llm.mixtral_groq(temp=0.3)
claude_opus = llm.claude3_opus(temp=0.3)  # Most expensive
claude_sonnet = llm.claude3_sonnet(temp=0.3)  #
claude_haiku = llm.claude3_haiku(temp=0.3)  #

# Instantiate agents and tools
agents = BloggingAutomationAgents()
tasks = BlogPostAutomationTasks()

web_search_tool = SerperDevTool()
count_words_tool = WordsCountTool()

# Create agents
web_searcher = agents.web_research_manager(openai35, web_search_tool)
title_creator = agents.title_creator(openai35)
post_creator = agents.post_creator(openai35)
post_editor = agents.post_editor(openai35)
spanish_translator = agents.post_translator(gemini)


# Determine blog post topic
# post_topic = "The risk of biased LLMs explained to non-savvy audiences."


def write_post(post_topic):
    """Write a post based on a topic"""
    # Create Tasks
    web_search_report = tasks.manage_websearch(
        web_searcher, post_topic)
    title_creation = tasks.manage_title_creation(
        title_creator, post_topic)
    write_post = tasks.manage_post_writing(
        post_creator, post_topic)
    edit_post = tasks.manage_editing(
        post_editor, post_topic)
    translate_post = tasks.spanish_translation(
        spanish_translator, post_topic)

    # Assemble the Crew
    crew = Crew(
        agents=[web_searcher,
                title_creator,
                post_creator,
                post_editor,
                spanish_translator
                ],
        tasks=[web_search_report,
               title_creation,
               write_post,
               edit_post,
               translate_post
               ],
        process=Process.sequential
    )

    # Kick of the crew
    crew.kickoff()

    return crew.usage_metrics
