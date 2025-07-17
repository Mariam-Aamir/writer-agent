from agents import Agent , AsyncOpenAI , Runner ,  OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv
import os

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
print(gemini_api_key)
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


writer = Agent(
    name = 'writer agent',
    instructions = """ You are a writer and translator agent. Generate poem,
       stories, essay, email etc.  """

)

response = Runner.run_sync(
    writer,
    input= 'اردو ادب، شاعری، نثر اور اردو کتابوں کا سب سے بڑا ذخیرہ۔  translate it in english',
    run_config= config
)
print(response)