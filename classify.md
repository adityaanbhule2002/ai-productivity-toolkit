# Template: Classify

## Template

```
Classify this text as {labels}. Reply with one word only: "{text}"
```

## Fill in

- `{labels}`: the allowed answers, for example `Positive or Negative`
- `{text}`: the text to classify

## Example

```
Classify this text as Positive or Negative. Reply with one word only: "The battery dies in two hours."
```

## Tested?

Yes. This is the zero-shot prompt from Test 1: the model answered `Negative`, which is correct.

Few-shot versions were also tested (Tests 2, 3 and 4 in `testing_report.md`):

| Version | Result |
|---|---|
| Examples only, no instruction | Failed |
| Instruction + 2 examples | Wrong answer with extra text |
| Role + "one word only" + 4 examples | Correct and clean |

## Tips

- Always say what the allowed answers are.
- Say "one word only" to stop extra text.
- If a simple prompt is not enough, add a role, a strict rule and more examples.
