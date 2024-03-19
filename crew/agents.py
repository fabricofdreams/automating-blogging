from crewai import Agent
from langchain.agents import load_tools
from textwrap import dedent


# Human Tools
human_tools = load_tools(["human"])


class BloggingAutomationAgents():

    def blogging_manager(self, model):
        return Agent(role="Blog Manager",
                     goal=dedent(f"""Oversee the development of a compelling post targeting a specific subject, 
                                emphasizing a 1,500-word count. This entails conducting online research, 
                                generating captivating titles, composing the post, and providing translations as needed."""),
                     backstory=dedent(f"""As a manager specializing in Python framework agent development, your responsibility 
                                lies in orchestrating the creation of engaging blog content. Your methodical approach begins
                                with comprehensive online research, analyzing a curated selection of posts, studies, 
                                and news articles relevant to the topic. From this research, you generate a list of 10 
                                compelling titles, each designed to maximize click-through rates and provided to the 
                                title creator for further refinement. You then oversee the meticulous crafting of a 1,500-word post, 
                                ensuring adherence to specified format requirements. Finally, you facilitate the translation 
                                of the post into Spanish, expanding its audience reach."""),
                     llm=model,
                     allow_delegation=True,
                     verbose=True
                     )

    def web_research_manager(self, model, web_search_tool):
        return Agent(role="Web Research Manager",
                     goal=dedent(f"""For a given topic search the web to find no less than 5 and no more than 15 posts, 
                                or studies, or researches and or news and analyze their titles and content with the ultimate goal 
                                of populating the research table which will be used by other agents to help them to generate titles 
                                and other aspects for a new blog post."""),
                     backstory=dedent(f"""As a methodical and detailed research manager, you are responsible for overseeing researchers 
                                who actively search YouTube to find topic matching content. You must make sure that the 
                                YouTube research table is populated with the URLs of the videos that you find."""),
                     llm=model,
                     verbose=True,
                     allow_delegation=False,
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
                     allow_delegation=False,
                     verbose=True
                     )

    def post_creator(self, model):
        return Agent(role="Blog Posts Creator",
                     goal=dedent(f"""To create a captivating and accessible 1000 words blog post aimed at engineers and 
                        professionals that is well-structured, formatted, and developed through thorough online research. 
                        Incorporate potential titles suggested by colleagues to ensure resonance with readers and drive 
                        substantial engagement.
                                 """),
                     backstory=dedent(f"""As a blog post creator, you are responsible for creating well-structured, engaging and 
                                compelling blog post, fully according to the guidelines of blog post formating.
                                You always create the blog post based on the web search information provided by your coworkers and
                                respect the 10 potential titles to select from it the most appropriate title for the post."""),
                     llm=model,
                     allow_delegation=False,
                     verbose=True,
                     #  tools=[count_words_tool]
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
                     allow_delegation=False,
                     verbose=True)

    def post_editor(self, model):
        return Agent(role="Post Editor",
                     goal=dedent(f"""To ensure the length of the post is no less than 1000 words.
                                """),
                     backstory=dedent(f"""As an editor, your respect the length measured in words andyour are responsible of 
                        ensuring the post is well formatted, with accurate content and with a very catchy tittle."""),
                     llm=model,
                     allow_delegation=False,
                     verbose=True
                     )
