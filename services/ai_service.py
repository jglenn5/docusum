from dotenv import load_dotenv
from anthropic import Anthropic 
import os 

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def summarize_text(text):
    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=200,
        messages=[
            {"role": "user", "content": f"Summarize this document in 2-3 sentences. Respond with only the summary text, no headers or titles: {text}"}
        ]
    )
    return message.content[0].text


if __name__ == "__main__":
    sample_text = "The quick brown fox jumps over the lazy dog. This sentence is often used to text typefaces because it contains every letter of the English alphabet. It has been used since the late 1800s by typists and typesetters."
    result = summarize_text(sample_text)
    print(result)