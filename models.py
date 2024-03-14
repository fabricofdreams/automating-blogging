from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()


class LargeLanguageModel():
    """API LLMs services"""

    def chat_Openai(self, temp: int):
        return ChatOpenAI(
            model_name="gpt-3.5-turbo", temperature=temp)

    def gemini(self):
        return ChatGoogleGenerativeAI(
            model="gemini-pro")

    def mixtral_groq(self, temp: int):
        return ChatGroq(temperature=temp, model_name="mixtral-8x7b-32768")
