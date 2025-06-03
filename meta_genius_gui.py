import os
import openai
from dotenv import load_dotenv
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, font
from tkinter import ttk

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

def handle_generate():
    content = input_text.get("1.0", tk.END).strip()
    if not content:
        messagebox.showwarning("Input Required", "Please enter or load some content.")
        return

    output_box.delete("1.0", tk.END)
    result = generate_meta_tags(content)
    output_box.insert(tk.END, result)

def load_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filepath:
        with open(filepath, "r", encoding="utf-8") as f:
            input_text.delete("1.0", tk.END)
            input_text.insert(tk.END, f.read())

# ---------- UI Setup ----------
BG_COLOR = "#1e1e1e"
TEXT_COLOR = "#ffffff"
INPUT_BG = "#2c2c2c"

window = tk.Tk()
window.title("Meta Genius")
window.geometry("800x600")
window.configure(bg=BG_COLOR)

default_font = font.nametofont("TkDefaultFont")
default_font.configure(size=11)

# Apply TTK dark button style
style = ttk.Style()
style.theme_use("default")
style.configure("Dark.TButton",
    foreground=TEXT_COLOR,
    background="#444444",
    font=("Helvetica", 11),
    padding=6)
style.map("Dark.TButton",
    background=[("active", "#666666")],
    foreground=[("active", TEXT_COLOR)])

# Labels
tk.Label(window, text="Input Content", font=("Helvetica", 13, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=(15, 5))

# Input box
input_text = scrolledtext.ScrolledText(
    window, wrap=tk.WORD, height=13,
    font=("Helvetica", 11),
    bg=INPUT_BG, fg=TEXT_COLOR,
    insertbackground=TEXT_COLOR
)
input_text.pack(padx=20, fill=tk.BOTH, expand=True)

# Buttons
button_frame = tk.Frame(window, bg=BG_COLOR)
button_frame.pack(pady=15)

ttk.Button(button_frame, text="Load File", command=load_file, style="Dark.TButton", width=18).pack(side=tk.LEFT, padx=10)
ttk.Button(button_frame, text="Generate Meta Tags", command=handle_generate, style="Dark.TButton", width=22).pack(side=tk.LEFT, padx=10)

# Output label
tk.Label(window, text="Generated Meta Tags", font=("Helvetica", 13, "bold"), bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=(10, 5))

# Output box
output_box = scrolledtext.ScrolledText(
    window, wrap=tk.WORD, height=10,
    font=("Helvetica", 11),
    bg=INPUT_BG, fg=TEXT_COLOR,
    insertbackground=TEXT_COLOR
)
output_box.pack(padx=20, fill=tk.BOTH, expand=True)

window.mainloop()
