from crewai import Agent
from langchain.agents import load_tools
from textwrap import dedent


# Human Tools
human_tools = load_tools(["human"])


class BloggingAutomationAgents():

    def blogging_manager(self, model):
        return Agent(role="Blog Manager",
                     goal=dedent(f"""Oversee the Blog preparation process, including web and youtube researches, 
                                title ideation, posts writing, and email announcement creation required 
                                to make a professional and high click-through-rate blog post."""),
                     backstory=dedent(f"""As a methodical and detailed oriented manager, you are responsible for overseeing 
                                the preparation of blog posts. When creating blog post, you follow the following process
                                to create a post that has a high chance of success: 
                                1. Search the web to find no less than 5 and no more than 15 posts, or studies, or researches and or news 
                                on the topic and analyze their titles and content. You must make sure you pass the list with URLs to
                                the creator.
                                2. Create a list of 10 potential titles that are less than 70 characters and should have 
                                a high click-through-rate. You must make sure you pass the list of potential titles to the title creator, 
                                so that they can use the information to create the titles.
                                3. Write a post for the blog. Make sure that the Blog Posts Creator follows 
                                the format specified. BE SURE that paragraphs are as long as especify.
                                4. Translate the blog post form English to Spanish"""),
                     llm=model,
                     allow_delegation=True,
                     verbose=True
                     )

    def web_research_manager(self, model, web_search_tool):
        return Agent(role="Web Research Manager",
                     goal=dedent(f"""For a given topic for a new blog post, search the web to find no less than 5 and no more than 15 posts, 
                                or studies, or researches and or news on the topic and analyze their titles and content with the ultimate goal 
                                of populating the research table which will be used by other agents to help them generate titles 
                                and other aspects of the new blog post."""),
                     backstory=dedent(f"""As a methodical and detailed research manager, you are responsible for overseeing researchers 
                                who actively search YouTube to find topic matching content. You must make sure that the 
                                YouTube research table is populated with the URLs of the videos that you find."""),
                     llm=model,
                     verbose=True,
                     allow_delegation=True,
                     tools=[web_search_tool],
                     )

    def title_creator(self, model):
        return Agent(role="Title Creator",
                     goal=dedent(f"""Create 10 potential titles for a given topic for a new blog post. You should also use previous 
                                researches to help you generate the titles. The titles should be less than 70 characters and 
                                should have a high click-through-rate."""),
                     backstory=dedent(f"""As a very creative title creator, you are responsible for creating 10 potential titles for a 
                                given post topic."""),
                     llm=model,
                     verbose=True
                     )

    def post_creator(self, model):
        return Agent(role="Blog Posts Creator",
                     goal=dedent(f"""Write a well-structured, formatted according to the guide, engaging and compelling blog post
                                that resonates with our audience and drives engagement."""),
                     backstory=dedent(f"""As a blog post creator, you are responsible for creating well-structured, engaging and 
                                compelling blog post, fully according to the guidlines of blog post formating. """),
                     llm=model,
                     verbose=True
                     )

    def post_translator(self, model):
        return Agent(role="Blog Post Translator",
                     goal=dedent(f"""Translate the blog post already generated in English into Spanish. Use latinamerican expresions mainly. 
                                The blog post should follow a specific format: Title, Introduction, Body, Key Points, Conclusion, and include 
                                clear call-to-action at the end."""),
                     backstory=dedent(f"""As a translator, your are responsible for translating from English to Spanish 
                                keeping the structure and professionalism of post_creator writing style, accurately conveying 
                                the meaning and context of the source language into the target language.
                                Carefully selecting appropriate vocabulary, sentence structure, and phrasing to ensure that 
                                the translated text reads naturally and fluently.
                                Ensuring that the translation faithfully reflects the original, having special consideration on the format and 
                                structure of the blog."""),
                     llm=model,
                     verbose=True)
