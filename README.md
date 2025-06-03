# Meta Genius
An AI-powered meta tag and snippet generator built with GPT-4.
Give it raw text and get SEO-optimized meta titles and descriptions in seconds.

## Features
- Desktop GUI (no browser required)
- Generates meta titles (≤ 60 characters)
- Generates meta descriptions (≤ 155 characters)
- Ensures semantic relevance using LLMs (GPT-3.5)

### 1. Clone the Repository
```bash
git clone https://github.com/taimuradam/meta-genius.git
cd meta-genius
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Add Your API Key
Create a .env file in the root folder:
```bash
OPENAI_API_KEY=your-openai-key-here
```

### 4. Run The App
```bash
python meta_genius_gui.py
```

## Input Format
You can either:
- Paste text directly into the app, or
- Click "Load File" to select a .txt file

## Output
The app will return:
- A meta title under 60 characters
- A meta description under 155 characters

## License
MIT License

## Author
Made by Taimur Adam