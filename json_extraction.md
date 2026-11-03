# Example: structured output (JSON)

Goal: get an AI to return data a program can read, not a sentence.

## Prompt

```
You are an assistant that extracts information. Return ONLY valid JSON with these keys: name, role, skills (a list). No extra text.

Text: "Riya is a cloud engineering student who knows AWS, Linux and Docker."
JSON:
```

## Real output from the model (Qwen2.5-0.5B-Instruct)

````
```json
{
  "name": "Riya",
  "role": "Cloud Engineering Student",
  "skills": ["AWS", "Linux", "Docker"]
}
```
````

## What I noticed

- The data is correct and has exactly the keys I asked for.
- The model **added ` ```json ` marks** even though the prompt said "No extra text". Without cleaning them, `json.loads` fails.

## Validation code

```python
import json

clean = raw.replace("```json", "").replace("```", "").strip()
try:
    data = json.loads(clean)
    print("Valid JSON", data)
except Exception as e:
    print("Not valid JSON", e)
```

Result: **Valid JSON** after cleaning. The same logic is available as `clean_json()` in `toolkit.py`.

## Tips for JSON prompts

1. Say "Return ONLY valid JSON".
2. Name the exact keys.
3. Say "No extra text", and still clean the output, because models often ignore it.
4. Always validate with `json.loads` before using the data.
