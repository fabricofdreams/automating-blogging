from crewai import Task
from textwrap import dedent
from datetime import datetime


class BlogPostAutomationTasks():

    def manage_blog_post_creation(self, agent, post_topic):
        return Task(
            description=dedent(f"""
            Manage the process of preparing the blog, which involves the following steps:
            1. Conducting online research,
            2. Generating ideas for the title,
            3. Creating the blog post,
            4. Translating the blog post from English to Spanish.
            
            The primary objective is to produce a professional blog post in Spanish that attracts 
            a high number of clicks.
            
            The subject of the post is: {post_topic}.
            
            It is crucial to guarantee that the English version of the post is accurately translated, 
            resulting in a Spanish version that closely mirrors the original content.
            """),
            agent=agent,
            expected_output="A report with the list of findings from the web search.",
            output_file=f"outputs/{datetime.now().strftime('%m-%d-%Y_%H:%M')}_post_creation.md"
        )

    def manage_websearch(self, agent, post_topic):
        return Task(
            description=dedent(f"""
            For a given post topic, search for posts, or studies, or researches or news to find 15 websites/blogs including the topic. 
            Once you have found the websites/blogs, make sure you include the title, url and snippet before delegating tasks to other agents.
                        
            This research CSV which will be used by other agents to help them generate titles and other aspects of the new blog post 
            that we are planning to create.
                        
            Research CSV Outline:
            - Title of the content source
            - URL of the website
            - Snippet
                
            The post topic is: {post_topic}

            Important Notes: 
            - Make sure the CSV uses ',' as the delimiter.
            - Make sure the final Research CSV Outline doesn't contain duplicate sources.
            - It is SUPER IMPORTANT that you only populate the research CSV with URLs that actually link to the website.
            """),
            agent=agent,
            expected_output=dedent(f"""
            Title, URL,Snippet
            Lifestyle Behaviors That Harm Your Lungs the Most, https://www.lompocvmc.com/blogs/2022/november/lifestyle-behaviors-that-harm-your-lungs-the-mos/, Smoking, exposure to pollutants, and lack of exercise are all common risk factors for poor lung health. 
            Exercise and Lung Health | American Lung Association, https://www.lung.org/lung-health-diseases/wellness/exercise-and-lung-health, Physical activity can reduce your risk of serious illness, including heart disease, stroke, diabetes and some forms of cancer, including lung ...        
                ...
            """),
            output_file=f"outputs/{datetime.now().strftime('%m-%d-%Y_%H:%M')}_post_websearch.csv"
        )

    def manage_youtube_search(self, agent, post_topic):
        return Task(
            description=dedent(f"""For a given video topic, search youtube videos to find 
                15 high-performing YouTube videos on the same topic. Once you have found the videos, 
                research the YouTube video details to finish populate the missing fields in the 
                research CSV. When delegating tasks to other agents, make sure you include the 
                URL of the video that you need them to research.
                            
                This research CSV which will be used by other agents to help them generate titles 
                and other aspects of the new YouTube video that we are planning to create.
                               
                Research CSV Outline:
                - Title of the video
                - View count
                - Days since published
                - Channel subscriber count
                - Video URL
                       
                The video topic is: {post_topic}
                

                Important Notes: 
                - Make sure the CSV uses ; as the delimiter
                - Make sure the final Research CSV Outline doesn't contain duplicate videos
                - It is SUPER IMPORTANT that you only populate the research CSV with real YouTube videos 
                    and YouTube URLs that actually link to the YouTube Video.
                """),
            agent=agent,
            expected_output=dedent(f"""
                Video Title; View Count; Days Since Published; Channel Subscriber Count; Video URL
                How to Make a YouTube Video; 100,000; 30; 1,000; https://www.youtube.com/watch?v=1234;
                How to Get Your First 1000 Subscribers; 100,000; 30; 1,000; https://www.youtube.com/watch?v=1234;
                       ...              
                """),
            output_file=f"outputs/{datetime.now().strftime('%m-%d-%Y_%H-%M')}_post_youtube_search.csv"
        )

    def manage_title_creation(self, agent, post_topic):
        return Task(
            description=dedent(f"""Create 10 potential titles for a given post topic. 
                It is also very important to use researched videos to help you generate the post titles.
                The titles should be less than 70 characters and should have a high click-through-rate.
                               
                The post Topic: {post_topic}
                
                Be sure to create a CSV file taht uses comma as delimiter.
                """),
            agent=agent,
            expected_output=dedent(f"""A CSV file such this
                Number, Title
                1, Revolutionizing Education: The Impact of AI
                2, AI in Education: A Game-Changer for Learning
                3, The Future of Learning: AI's Role in Education
                4, Enhancing Education with Artificial Intelligence
                5, Navigating the AI Frontier in Education
                6, Empowering Students: The AI Education Revolution
                7, AI: Transforming the Classroom Experience
                8, The Rise of AI: Reshaping Education for Tomorrow
                9, Unlocking Potential: AI's Influence on Education
                10, Adapting to Change: AI's Influence on the Education Sector
                ...
            """),
            output_file=f"outputs/{datetime.now().strftime('%m-%d-%Y_%H:%M')}_post_titles.csv"
        )

    def manage_post_writing(self, agent, post_topic):
        return Task(
            description=dedent(f"""
            Write a well-structured, engaging and compelling blog post that resonates with our audience and drives engagement.
            Make sure that the content is formatted according to the guide specified below and the topic is {post_topic}.

            When it comes to writing a blog post, there are several key elements to consider in order to create 
            a well-structured and engaging piece. 
            
            Here is a general format you can follow for a regular blog post:

            -Title: Start with a catchy and descriptive title that grabs the reader's attention and gives them an idea 
            of what the post is about.
            -Introduction: Begin with an engaging introduction that sets the tone for the rest of the post. Clearly state 
            what the post will cover and why it is relevant to the reader.
            -Body: The body of your blog post should be divided into sections or paragraphs that flow logically and provide 
            valuable information or insights. Each paragraph MUST be no less than 2500 words long. Use subheadings to break up 
            the text and make it easier to read. This MUST BE the longest part of the post.
            -Key Points: Highlight key points or takeaways throughout the post to help readers easily grasp the main ideas.
            -Conclusion: Summarize the main points of your post in the conclusion and reiterate its significance. You can also 
            pose a question or encourage discussion to engage readers further.
            -Include a clear call-to-action at the end of your post, prompting readers to engage further with your content, 
            such as subscribing to your blog, leaving a comment, sharing the post on social media, or exploring 
            related resources.
            """),
            agent=agent,
            expected_output=dedent(f"""
            # Unveiling the Latest in Open Source Language Models: A Closer Look at State-of-the-Art Innovations

            ### Introduction
            In today's fast-paced digital world, language models play a crucial role in various applications such 
            as natural language processing, text generation, and machine translation. Open source language models, in particular, 
            have been at the forefront of innovation, constantly pushing the boundaries of what is possible in the field 
            of artificial intelligence. In this blog post, we will dive deep into the state of the art language models, 
            exploring the latest advancements and how they are revolutionizing the way we interact with technology.

            ### The Evolution of Language Models
            The journey of language models from their inception to the sophisticated entities we interact with today is nothing 
            short of remarkable. This evolution begins with **traditional rule-based systems**, which relied on manually crafted 
            rules for understanding and generating language. These systems, while pioneering for their time, were limited by their 
            inability to scale and adapt to the nuances of natural language.

            As we progressed, **statistical models** like n-grams became popular for their ability to predict the likelihood of 
            a sequence of words, leveraging vast amounts of text data. However, the real transformation came with the advent 
            of **deep learning models**, which shifted the paradigm to learning directly from data, without relying heavily on 
            predefined rules. This era introduced us to models like **LSTM (Long Short-Term Memory) networks** 
            and **RNNs (Recurrent Neural Networks)**, which were better at capturing long-range dependencies in text.

            Key milestones in this journey include the introduction of **Word2Vec** by Google in 2013, which showcased 
            the power of word embeddings, and the subsequent development of **contextual embeddings** by models such 
            as **ELMo** and **BERT**. These advancements enabled models to understand the context of words in a sentence, 
            leading to a significant leap in performance across a range of language tasks.

            ### Open Source Language Innovations
            The landscape of language models has been significantly enriched by open source contributions, with models 
            like **GPT-3**, **BERT**, and **T5** leading the charge. GPT-3, developed by OpenAI, showcased an unprecedented capacity 
            for generating human-like text, while BERT, from Google, revolutionized how models understand word context 
            in a sentence. **T5 (Text-to-Text Transfer Transformer)** further pushed the boundaries by treating every language 
            problem as a text-to-text problem, demonstrating impressive versatility.

            The advantages of open source models are manifold. They provide **accessibility**, allowing researchers and developers 
            from around the world to experiment with and build upon cutting-edge technology. **Transparency** in these models fosters 
            trust and facilitates deeper understanding and innovation. Additionally, **community-driven development** ensures 
            continuous improvement and adaptation, as contributors from diverse backgrounds bring in new ideas and solutions.

            ### Mastering Large Language Models
            Large language models have redefined what's possible in text generation and understanding. Their ability to grasp the 
            subtleties of human language, generate coherent and contextually relevant text, and even perform tasks like translation 
            and summarization without specific programming for each task, marks a new era in AI.

            However, training and deploying these behemoths comes with its set of challenges. The **computational cost** of training 
            models with billions, or even trillions, of parameters is astronomical, limiting access to those with significant resources. 
            Furthermore, issues such as **bias**, **ethical concerns**, and **environmental impact** are at the forefront of discussions 
            around large language models.

            Despite these challenges, the opportunities are vast. Improved efficiency in training, advances in understanding and 
            mitigating biases, and the development of more sustainable AI practices are areas ripe for innovation.

            ### The Future of Language Models
            The future of language models holds incredible promise. As we refine these models and make them more accessible, 
            their integration into various sectors could revolutionize how we interact with information and technology.

            In **healthcare**, language models could assist in diagnosing diseases from patient histories or help in creating 
            personalized treatment plans. The **finance sector** could see enhanced fraud detection systems and more nuanced 
            risk assessment tools. **Education** could be transformed through personalized learning experiences and automated 
            content generation, making knowledge more accessible to diverse populations.

            Moreover, as we continue to push the boundaries of what language models can do, we're likely to see more novel 
            applications, perhaps in creativity, entertainment, or in entirely new domains we've yet to imagine. The key to these 
            advancements will be in addressing the current limitations, ensuring that as these models evolve, they do so in 
            a way that is ethical, sustainable, and inclusive.

            The journey of language models is an ongoing one, marked by rapid advancements and immense potential. As we stand 
            on the brink of what's next, it's clear that language models will continue to be at the heart of the AI revolution, 
            transforming our interaction with technology and each other in profound ways.

            ### Conclusion
            As we wrap up our exploration of open source language models, it is clear that we are witnessing a paradigm shift 
            in the way we interact with technology. The state of the art innovations in language models are not only pushing 
            the boundaries of what is possible but also opening up new possibilities for communication and collaboration. 
            By staying ahead with the best language models, we can enhance our ability to engage with the world around us and drive 
            innovation in the digital age.

            Stay tuned for more updates on the latest advancements in language models and how they are shaping the future of AI. 
            Thank you for joining us on this journey through the world of open source language innovations.
                        """),
            output_file=f"outputs/{datetime.now().strftime('%m-%d-%Y_%H:%M')}_post_writing.md"
        )

    def spanish_translation(self, agent, post_topic):
        return Task(
            description=dedent(f"""Translate the text orginally post already writen in English by the Post Creator into Spanish.
                               The topic of the post is {post_topic}.
                               Respect the original structured of the post in English. YOU MUST follow the text in Ensligh and
                               translate into Spanish without changing the context and modify the structure or the original format.
                               If you find technical jargon try to translate into Spanish, but don't
                               force the translation. Consider that there are some words that must be
                               stay in English."""),
            agent=agent,
            expected_output=dedent(
                f"""A markdown file with translation into Spanish of the original Post created."""),
            output_file=f"outputs/{datetime.now().strftime('%m-%d-%Y_%H:%M')}_post_spanish.md"
        )
