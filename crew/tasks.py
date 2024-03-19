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
            a high number of clicks. The post should have three main sections: introduction, body and conclusions.
            
            The subject of the post is: {post_topic}.
            
            It is crucial to guarantee that the English version of the post is accurately translated, 
            resulting in a Spanish version that closely mirrors the original content.
            
            Important notes:
            - The body section of the post should be at least 7 paragraphs and 2,500 words long.
            - The ideas for the title MUST BE CREATED BASED on the findings from the web search..
            - The blog post MUST BE CREATED BASED on the ideas for the title and the web search.
            """),
            agent=agent,
            expected_output="There is no output expected."
            # output_file=f"outputs/{datetime.now().strftime('%m-%d-%Y_%H:%M')}_post_creation.md"
        )

    def manage_websearch(self, agent, post_topic):
        return Task(
            description=dedent(f"""
            For a given post topic, search for posts, or studies, or researches or news or youtube videos 
            to find 15 sources of information or web sites that include the topic.
            
            The goal is to create a Research Report in a CSV format.
            
            Research Report CSV Outline:
            - Title of the content source
            - URL of the website
            - Snippet
            
            Once you have found the 15 sources, make sure you include the title, url and snippet in the 
            Research Report before delegating tasks to other agents.
                        
            This Research Report CSV file will be used by other agents to help them generate titles and other aspects 
            of the new blog post that we are planning to create.
                
            The post topic is: {post_topic}

            Important Notes: 
            - Make sure the CSV file uses ';' as the delimiter.
            - Make sure the final Research Report CSV Outline doesn't contain duplicate sources.
            - It is SUPER IMPORTANT that you only populate the research report CSV with URLs that 
            actually link to the website.
            """),
            agent=agent,
            expected_output=dedent(f"""
            "Lifestyle Behaviors That Harm Your Lungs the Most"; https://www.lompocvmc.com/blogs/2022/november/lifestyle-behaviors-that-harm-your-lungs-the-mos/ ; Smoking, exposure to pollutants, and lack of exercise are all common risk factors for poor lung health. 
            "Exercise and Lung Health, American Lung Association"; https://www.lung.org/lung-health-diseases/wellness/exercise-and-lung-health ; Physical activity can reduce your risk of serious illness, including heart disease, stroke, diabetes and some forms of cancer, including lung ...        
                ...
            """),
            output_file=f"outputs/{datetime.now().strftime('%m-%d_%H:%M')}_post_websearch.csv"
        )

    def manage_title_creation(self, agent, post_topic):
        return Task(
            description=dedent(f"""Generate 10 possible titles for a specified post topic using 
                the Research Report CSV provided by the Web Research Manager.
                
                The titles should be less than 70 characters and should have a high click-through-rate.
                               
                The post Topic: {post_topic}
                
                Be sure to create a CSV file that uses ';' as delimiter.
                """),
            agent=agent,
            expected_output=dedent(f"""A CSV file such as this:
                1; Revolutionizing Education: The Impact of AI
                2; AI in Education: A Game-Changer for Learning
                3; The Future of Learning: AI's Role in Education
                4; Enhancing Education with Artificial Intelligence
                5; Navigating the AI Frontier in Education
                6; Empowering Students: The AI Education Revolution
                7; AI: Transforming the Classroom Experience
                8; The Rise of AI: Reshaping Education for Tomorrow
                9; Unlocking Potential: AI's Influence on Education
                10; Adapting to Change: AI's Influence on the Education Sector
                ...
            """),
            output_file=f"outputs/{datetime.now().strftime('%m-%d_%H:%M')}_post_titles.csv"
        )

    def manage_post_writing(self, agent, post_topic):
        return Task(
            description=dedent(f"""Compose a post at most 1000 words, about the topic between backticks.
            The post must be captivating, well-structured, and engaging, tailored to resonate with non-savvy audiences, driving significant engagement. 
            
            The topic is ```{post_topic}```.
            
            To compose the post follow the next instructions:
            
            1. Create the first attempt of the post trying to reach the 1000 words.
            2. Count the words of the post, and andjust the post until the count would be more than 1000 words.
            3. Adhere to the following structure or outline:
            
                -Title: Start with a catchy and descriptive title that grabs the reader's attention and gives them an idea
                of what the post is about.
                
                -Introduction: Begin with an engaging introduction that sets the tone for the rest of the post. Clearly state
                what the post will cover and why it is relevant to the reader.
                
                -Body: The body of the blog post should be divided into sections or paragraphs that flow logically and provide
                valuable information or insights. Use subheadings to break up the text and make it easier to read.
                
                -Key Points: Highlight key points or takeaways throughout the post to help readers easily grasp the main ideas.
                
                -Conclusion: Summarize the main points of the post in the conclusion and reiterate its significance. You can also
                pose a question or encourage discussion to engage readers further.
                
                -Call-to-action: Include a clear call-to-action at the end of the post, prompting readers to engage further with 
                the content, such as subscribing to the blog, leaving a comment, sharing the post on social media, or exploring 
                related resources."""),
            agent=agent,
            expected_output=dedent(f"""A well formatted post at most 1000 words long.
                                   
            ### **The Power of Mindfulness in Daily Life: Transforming Your Experience**
            
            Given the constraints, I'll expand on the existing topics and introduce more depth to ensure we reach the desired 
            word count. Let's delve deeper into the transformative journey of mindfulness, exploring its historical roots, 
            the scientific underpinning affirming its benefits, and a more comprehensive guide on weaving this practice into 
            the fabric of our daily lives.
            
            ### Understanding Mindfulness: A Journey Through Time
            
            Mindfulness, while popularized in the West over the last few decades, has its origins in ancient spiritual traditions, 
            most notably Buddhism. However, mindfulness is not exclusive to any one religion or philosophy. It is a universal 
            practice of focusing one's mind on the present moment with acceptance and without judgment. The practice was introduced 
            to Western medicine and psychology by pioneers like Jon Kabat-Zinn, who founded the Mindfulness-Based Stress 
            Reduction (MBSR) program in the late 1970s. Kabat-Zinn's work has been instrumental in demonstrating mindfulness's 
            effectiveness in stress reduction and overall well-being, bridging the gap between ancient wisdom and modern science.
            
            ### The Scientific Foundation of Mindfulness
            
            Extensive research over the years has provided a robust scientific foundation for mindfulness, illustrating its 
            positive impacts across various dimensions of human health and psychology. Neuroscientific research utilizing MRI 
            scans has shown that mindfulness meditation can lead to structural changes in the brain, including increased gray 
            matter density in regions associated with memory, empathy, and stress regulation. Moreover, mindfulness practices 
            have been linked to reduced activity in the amygdala, the brain's center for emotional reactions, stress, and fear, 
            offering a neurological basis for how mindfulness helps manage anxiety and emotional reactivity.
            
            ### Diving Deeper Into Mindfulness Benefits
            
            ### Enhanced Emotional Regulation
            
            Mindfulness equips individuals with the tools to approach their feelings and emotions with greater clarity and 
            understanding. By observing our emotions without immediate reaction, we can make more thoughtful decisions about how 
            to respond to challenging situations, leading to healthier emotional responses and interactions with others.
            
            ### Boosting Immune Health
            
            Emerging research suggests that mindfulness meditation can enhance the body's immune response, helping to fend off 
            illness and disease. This is thought to be due to the stress-reducing effects of mindfulness, as chronic stress can 
            weaken the immune system.
            
            ### Improving Relationship Satisfaction
            
            Mindfulness can profoundly impact relationships, fostering a greater capacity for empathy, active listening, 
            and open communication. By being fully present with our partners, friends, and family, we cultivate deeper, more 
            meaningful connections.
            
            ### Integrating Mindfulness Into Everyday Life: Beyond the Basics
            
            ### Mindfulness in Nature
            
            Spending time in nature can be a powerful mindfulness practice. Whether walking through a forest, sitting by a 
            lake, or simply observing the trees and sky from a city park, nature offers a unique setting for mindfulness. 
            It encourages a sense of connection with the larger world and can provide profound moments of insight and peace.
            
            ### Mindful Creativity
            
            Engaging in creative activities such as drawing, writing, or playing music with a mindful approach can enhance 
            the creative process, making it more enjoyable and fulfilling. By focusing fully on the activity without concern 
            for the outcome, we can free ourselves from the constraints of critical judgment and allow our creative energies 
            to flow more freely.
            
            ### Mindfulness and Technology
            
            In an age where digital distractions are omnipresent, practicing mindfulness with our use of technology can be 
            incredibly beneficial. This could involve setting boundaries around tech use, engaging in digital detoxes, or simply
            bringing a more attentive and intentional approach to how we use digital devices.
            
            ### Overcoming Common Mindfulness Challenges
            
            ### Consistency
            
            One of the biggest challenges in mindfulness practice is maintaining consistency. Life's demands can easily 
            sideline our intentions to practice regularly. Setting a specific time for mindfulness practice can help, as 
            can integrating mindfulness into routine activities such as brushing teeth or doing dishes.
            
            ### Judgment and Frustration
            
            Many beginners in mindfulness face the challenge of self-judgment or frustration with the practice. It's common 
            to have expectations about what mindfulness "should" feel like or to become frustrated when the mind wanders. 
            Recognizing these feelings and gently bringing the attention back to the present moment without self-criticism 
            is a core aspect of mindfulness practice.
            
            ### Finding the Right Practice
            
            There are numerous ways to practice mindfulness, from seated meditation to mindful walking, and not every 
            practice suits everyone. Experimenting with different forms of mindfulness can help you find the one that 
            resonates most with you and fits best into your lifestyle.
            
            ### Deepening Your Mindfulness Journey
            
            ### Retreats and Workshops
            
            For those looking to deepen their mindfulness practice, attending retreats or workshops can be transformative. 
            These settings offer immersive experiences, expert guidance, and the support of a community, all of which can enrich 
            your understanding and commitment to mindfulness.
            
            ### Advanced Practices
            
            As your mindfulness practice matures, you may wish to explore more advanced techniques or delve deeper into the 
            philosophical and spiritual roots of mindfulness. This could involve studying Buddhist teachings on mindfulness, 
            exploring the intersection of mindfulness with other spiritual traditions, or engaging in longer, more intensive 
            meditation practices.
            
            ### **Conclusion**: The Lifelong Journey of Mindfulness
            
            Mindfulness is not a destination but a journey—a continuous process of coming back to the present moment with 
            kindness and curiosity. Its benefits unfold over time, with each mindful moment offering an opportunity for growth, 
            understanding, and connection. Whether you're just beginning this journey or seeking to deepen your practice, 
            remember that every breath offers a new chance to practice mindfulness. In cultivating mindfulness, we open ourselves
            to the richness of the present moment, finding peace, joy, and fulfillment in the simplicity of being.
           
            ### **Call-to-action**:
            As we conclude this exploration of mindfulness, I invite you to reflect on your own experiences and aspirations 
            with mindfulness. What challenges have you faced, and what benefits have you noticed? How do you see your practice 
            evolving? Share your thoughts and insights in the comments below, and let's continue to support each other on this 
            shared journey of mindful living.
            
            Thank you for taking the time to explore the profound impact mindfulness can have on our lives. May your path be 
            filled with awareness, compassion, and presence, guiding you to a richer, more connected experience of life..
                        """),
            output_file=f"outputs/{datetime.now().strftime('%m-%d_%H:%M')}_post_writing.md"
        )

    def manage_editing(self, agent, post_topic):
        return Task(
            description=f"""Count the words in the blog post.
            Adjust the blog post if there are less than 1000 words.
            Respect the ouline, enhance the content adding examples or extend some ideas.
            The topic is {post_topic}""",
            agent=agent,
            expected_output="""A post with no less than 1000 words and the same outline and topic. """,
            output_file=f"outputs/{datetime.now().strftime('%m-%d_%H:%M')}_post_english.md"

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
            output_file=f"outputs/{datetime.now().strftime('%m-%d_%H:%M')}_post_spanish.md"
        )
