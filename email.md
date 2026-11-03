# Template: Email

## Template

```
You are a polite {role}. Write a short email to {recipient} about {topic}. Use a subject line. Do not use placeholders. Sign off as {sender}.
```

## Fill in

- `{role}`: who is writing, for example `intern`
- `{recipient}`: who gets it, for example `my manager, Mr. Sharma`
- `{topic}`: what it is about
- `{sender}`: the name to sign off with

## Example

```
You are a polite intern. Write a short email to my manager, Mr. Sharma, about a 15 minute meeting on my Module 02 progress. Use a subject line. Do not use placeholders. Sign off as Aditya.
```

## Tested?

Tested in the notebook in three versions (Tests 7, 8 and 9 in `testing_report.md`):

- Version 1 left a placeholder: `Dear [Manager's Name],`
- Giving the name and adding "Do not use placeholders" fixed the placeholder.
- The model still **ignored the length limit** and once wrote "with your team" instead of "with you".

## Tips

- Give real names and facts, otherwise the model fills the gap with placeholders.
- Always read the email before sending it.
