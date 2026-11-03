# Template: Summarize

## Template

```
Summarize the text below in {n} sentence(s).

Text: {text}
```

## Fill in

- `{n}`: how many sentences you want
- `{text}`: the text to summarize

## Example

```
Summarize the text below in 1 sentence(s).

Text: Generative AI creates new content such as text, images and code. It learns patterns from huge amounts of data. It is useful for drafting and coding, but it can make mistakes, so people must check its answers.
```

## Tested?

Tested in the notebook with an added limit ("under 20 words"). The small model **did not keep to the word limit** (Test 6 and Test 10 in `testing_report.md`).

## Tips

- Ask for a number of sentences. Do not rely on word limits with small models.
- Count the words of the reply with code if the limit really matters.
