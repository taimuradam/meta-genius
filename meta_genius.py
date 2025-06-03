import os
import sys
import openai
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_meta_tags(content):
    prompt = (
        "You are an SEO expert. Generate:\n"
        "1. A meta title under 60 characters.\n"
        "2. A meta description under 155 characters.\n\n"
        f"Content:\n{content.strip()}"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"OpenAI API error: {e}"

def read_input(arg):
    if os.path.isfile(arg):
        with open(arg, "r", encoding="utf-8") as f:
            return f.read()
    else:
        return arg

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python meta_genius.py <input-text-or-file>")
        sys.exit(1)

    input_text = read_input(sys.argv[1])
    result = generate_meta_tags(input_text)

    print("\nGenerated Meta Tags:\n")
    print(result)
