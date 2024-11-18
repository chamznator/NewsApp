import os
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")  # Replace with your API key if not using environment variables
)

def summarize_text(text):
    try:
        # Create a chat completion request
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Please summarize the following text:\n\n{text}"
                }
            ],
            model="gpt-3.5-turbo"  # Use a model you have access to, like 'gpt-3.5-turbo' or 'gpt-4'
        )
        
        # Extract the response content using dot notation
        summary = chat_completion.choices[0].message.content.strip()
        return summary
    except Exception as e:
        print(f"Error during summarization: {e}")
        return "An error occurred during summarization."
