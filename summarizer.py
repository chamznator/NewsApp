import openai
import os

# Initialize OpenAI client with your API key
openai.api_key = os.getenv("OPENAI_API_KEY") or "your_openai_api_key"  # Replace as needed

def summarize_text(text):
    try:
        # Make the API call to generate a completion (synchronous version)
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use the appropriate model, e.g., 'gpt-3.5-turbo' or 'gpt-4'
            messages=[
                { "role": "system", "content": "You are a helpful assistant that summarizes text." },
                { "role": "user", "content": f"Please summarize the following text:\n\n{text}" }
            ]
        )

        # Extract the summary from the response
        summary = response.choices[0].message['content'].strip()
        return summary
    except Exception as e:
        print(f"Error during summarization: {e}")
        return "An error occurred during summarization."
