# Template: Fix code

## Template

````
Fix the bug in this Python function. Put the corrected code in a ```python block.

{code}
````

## Fill in

- `{code}`: the broken code

## Example

```python
def average(nums):
    return sum(nums) / (len(nums) + 1)
```

The bug: it divides by `len + 1`, so `average([2, 4, 6])` gives `3.0` instead of `4.0`.

## Tested?

Yes, with a slightly different wording ("Return only the corrected code"). See Tests 12 and 13 in `testing_report.md`.

- The model's fixed code was **correct** (`sum(nums) / len(nums)`, with an empty-list check) and passed my checks.
- But the model **also wrote sentences around the code**, and wrongly said the original function had no bug.
- My first test ran the whole reply as code and failed. Extracting only the code block (`extract_code()` in `toolkit.py`) fixed the test.

This template asks for a ```python block on purpose, so the code is easy to extract.

## Tips

- Run the fixed code against test cases. Do not trust it by reading alone.
- Read AI-written code before running it. Do not run unknown code blindly.
