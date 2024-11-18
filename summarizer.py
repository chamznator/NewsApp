import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


# Initialize the OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")  # Replace with your API key if not using environment variables
)

def summarize_text(text):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Summarize the following text into 3 or fewer paragraphs:\n\n{text}"
                }
            ],
            model="gpt-4o"
        )
        summary = chat_completion.choices[0].message.content.strip()
        return summary
    except Exception as e:
        print(f"Error during summarization: {e}")
        return "An error occurred during summarization."

