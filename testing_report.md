# Testing Report

**Project:** AI Productivity Toolkit (Module 02: Prompt Engineering & AI Productivity)
**Author:** Aditya Nitin Anbhule
**Notebook with all outputs:** https://colab.research.google.com/drive/164M7u5noKep_Xy_RpiRufyRjHUb4Dfd8?usp=sharing

## 1. Setup

| Item | Value |
|---|---|
| Model | `Qwen/Qwen2.5-0.5B-Instruct` (about 0.5 billion parameters) |
| Library | Hugging Face `transformers` |
| Environment | Google Colab (free tier) |
| Settings | `do_sample=False` (the same prompt gives the same answer), `max_new_tokens` between 5 and 150 |

## 2. How I tested

1. Write a prompt.
2. Run it and read the real output.
3. Where possible, **check the output with code** (word count, JSON validity, running the AI's code on test cases) instead of judging by eye.
4. If it failed, change the prompt and test again.

Word counts include the subject line and greeting when the output was an email.

## 3. Results

| # | What was tested | Output / measurement | Verdict |
|---|---|---|---|
| 1 | Zero-shot sentiment (with instruction, "one word only") | `Negative` | Pass |
| 2 | Few-shot sentiment, examples only, no instruction | `I'm sorry, but` | Fail |
| 3 | Few-shot sentiment, instruction + 2 examples | `Positive` followed by "Explanation:" | Fail (wrong answer, extra text) |
| 4 | Few-shot sentiment, role + "one word only" + 4 examples | `Negative` | Pass |
| 5 | JSON extraction (name, role, skills) | Correct data, but wrapped in ```json marks | Pass after cleanup |
| 6 | Summary in one sentence, under 20 words | 20 or more words (exact count not recorded) | Fail |
| 7 | Email, under 60 words | 99 words; left `[Manager's Name]` placeholder | Fail |
| 8 | Email, with manager's name and "no placeholders" | 70 words; placeholder fixed; wrote "with your team" | Partial |
| 9 | Email, "exactly 3 short sentences" | 85 words; more than 3 sentences | Fail |
| 10 | Mini test tool, 3 automatic checks | Summary: fail, sentiment: pass, email: fail (1 of 3) | Partial |
| 11 | AI writes `is_even(n)`, tested with 4 and 7 | Correct; added a docstring and ``` marks despite "only the code" | Pass |
| 12 | AI fixes buggy `average`, whole reply run as code | Error: the reply had sentences around the code; the AI also wrongly said the function had no bug | Fail |
| 13 | Same reply, only the code block extracted | Correct fix: `sum(nums) / len(nums)`; passed test cases | Pass |
| 14 | Resume-bullet template | Usable, but started with "Successfully" (an adverb, not an action verb) | Partial |
| 15 | Research template, 3 bullet points | 3 numbered points, plus an unwanted intro | Partial |

**Totals:** 4 pass, 1 pass after cleanup, 4 partial, 6 fail (15 tests).

## 4. Findings

### What worked
- **Short classification** worked once the prompt had a role, a strict rule ("one word only") and enough examples (Tests 1 and 4).
- **JSON output** had the right data and keys (Test 5).
- **Code writing and fixing** gave correct code that passed my test cases (Tests 11 and 13).
- **Fixed settings** (`do_sample=False`) made every test repeatable.

### What did not work
- **Length limits were ignored.** "Under 20 words", "under 60 words" and "exactly 3 sentences" all failed. Rewording the limit did not fix it, and the third attempt was worse (85 words) than the second (70).
- **Extra text appeared everywhere.** Examples: ``` marks around JSON and code, "Explanation:", "Certainly!", and long docstrings.
- **Examples alone were not enough.** A few-shot prompt with no instruction (Test 2) failed, and with only 2 examples plus an instruction (Test 3) it was still wrong.
- **Wrong statements.** In Test 12 the model said the function had no bug, then fixed it anyway.

### Lessons for prompt design
1. Start with a clear instruction. Add a role, constraints and examples when needed.
2. Give real facts (names, details). Missing details become placeholders.
3. Ask for the format you need, and still clean and validate the output.
4. Measure limits with code. Do not trust "it looks short".
5. Run AI-written code on test cases, and read it first.
6. Check the test tool too. Test 12 failed because my test ran the whole reply as code, not because the fix was wrong.

## 5. Limits of this report

- Only one small model was tested. A larger model would probably follow the limits better.
- Each prompt ran once, with fixed settings.
- The summarize, email, classify and fix-code templates were not each run through the template function. Only the resume-bullet and research templates were (Tests 14 and 15). The others are based on prompts tested earlier in the notebook.
- The "pass" and "fail" rules are simple checks (word count, exact answer, test cases) and do not judge writing quality.

## 6. Next steps

- Repeat the tests on a larger model and compare.
- Run each prompt several times with sampling turned on.
- Add automatic checks for every template.
