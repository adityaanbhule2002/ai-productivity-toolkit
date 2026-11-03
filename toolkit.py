"""AI Productivity Toolkit: reusable prompt templates and small helpers.

The template, JSON and code-extraction helpers are plain Python.
Only ask() / use() need the `transformers` library (and download a model).
"""

import json
import re

TEMPLATES = {
    "summarize": "Summarize the text below in {n} sentence(s).\n\nText: {text}",
    "email": (
        "You are a polite {role}. Write a short email to {recipient} about {topic}. "
        "Use a subject line. Do not use placeholders. Sign off as {sender}."
    ),
    "classify": 'Classify this text as {labels}. Reply with one word only: "{text}"',
    "fix_code": (
        "Fix the bug in this Python function. "
        "Put the corrected code in a ```python block.\n\n{code}"
    ),
    "resume_bullet": (
        "Rewrite this task as one strong resume bullet that starts with an action verb: {task}"
    ),
    "research": "Explain {topic} in simple words in {n} bullet points for a beginner.",
}


def fill(name, **kw):
    """Fill the blanks of a template. Uses simple replace (not str.format),
    so code containing curly braces cannot break a template."""
    text = TEMPLATES[name]
    for key, value in kw.items():
        text = text.replace("{" + key + "}", str(value))
    return text


def extract_code(text):
    """Return only the code inside a ``` block. If there is no block, return the text."""
    match = re.search(r"```(?:python)?\n(.*?)```", text, re.DOTALL)
    return match.group(1).strip() if match else text.strip()


def clean_json(text):
    """Remove ```json fences that models often add, then parse the JSON.
    Raises ValueError if the result is not valid JSON."""
    cleaned = text.replace("```json", "").replace("```", "").strip()
    return json.loads(cleaned)


_generator = None


def load_model(name="Qwen/Qwen2.5-0.5B-Instruct"):
    """Load the text-generation model once (needs `pip install transformers`)."""
    global _generator
    if _generator is None:
        from transformers import pipeline

        _generator = pipeline("text-generation", model=name)
    return _generator


def ask(prompt, max_tokens=100):
    """Send one prompt to the model. do_sample=False gives repeatable answers."""
    gen = load_model()
    messages = [{"role": "user", "content": prompt}]
    out = gen(messages, max_new_tokens=max_tokens, do_sample=False)
    return out[0]["generated_text"][-1]["content"]


def use(name, max_tokens=150, **kw):
    """Fill a template and ask the model in one step."""
    return ask(fill(name, **kw), max_tokens)
