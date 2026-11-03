# AI Productivity Toolkit

**Module 02: Prompt Engineering & AI Productivity**
Codomax Digital Solutions Internship | Aditya Nitin Anbhule

A small, honest toolkit of reusable prompt templates, plus a testing report that shows what worked and what did not when I tried them on a small AI model.

## Google Colab notebook

All experiments were run in this notebook (open it to see the real outputs):
https://colab.research.google.com/drive/164M7u5noKep_Xy_RpiRufyRjHUb4Dfd8?usp=sharing

## What is inside

| Path | What it is |
|---|---|
| `prompts/` | Six reusable prompt templates (summarize, email, classify, fix code, resume bullet, research) |
| `toolkit.py` | The same templates as Python code, plus helper functions to fill them, clean JSON and extract code from model replies |
| `examples/json_extraction.md` | A structured-output (JSON) example with a validity check |
| `testing_report.md` | 15 real tests with results, findings and limits |

## How the experiments were run

- **Model:** `Qwen/Qwen2.5-0.5B-Instruct` (a very small, free model) through the Hugging Face `transformers` library
- **Where:** Google Colab, free tier
- **Settings:** `do_sample=False`, so the model gives the same answer every time and the tests can be repeated

## Quick start

```python
from toolkit import use

print(use("resume_bullet", task="Tested prompts on a small AI model in Google Colab"))
print(use("research", topic="what an API is", n=3))
```

Only the model-calling functions need `transformers`. The template, JSON and code-extraction helpers are plain Python.

## What I learned (short version)

1. **A clear instruction beats examples alone.** A few-shot prompt with no instruction failed. Adding an instruction, a role, a strict constraint and four examples fixed the sentiment task.
2. **Small models ignore length limits.** Asking for "under 60 words" or "exactly 3 sentences" gave 70 to 99 words.
3. **Models add extra text.** Even when told "only code" or "only JSON", replies had ``` marks, explanations or an intro. Clean and validate the output before using it.
4. **Test, don't trust.** Word counts, JSON checks and running AI-written code showed problems that were not obvious by reading.
5. **Test tools can fail too.** One "failed" debugging test was caused by my own code, which tried to run the whole reply instead of only the code block.

## Limits of this project

- Only one small model was tested, so results may differ on larger models.
- Each prompt was run once with fixed settings, not many times.
- The `summarize`, `email`, `classify` and `fix_code` templates are built from prompts tested in the notebook, but only the `resume_bullet` and `research` templates were run through the template function itself.

See `testing_report.md` for the full details.
