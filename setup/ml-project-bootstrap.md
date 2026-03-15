# Project Bootstrap

Initialize a new ML/research project with minimal, verified code.

## Prompt

```
Create a new local repo and its remote [public/private] counterpart for [PROJECT_NAME].

We want only the minimum amount of code and scripts for the correct functioning of the software and the correct presentation of the results.

[content-integrity constraint]

Base your work on the original paper [PAPER_TITLE, DOI/URL] and create the logic for:
- Downloading the dataset(s)
- Feature extraction
- Training
- Validation
- Results presentation

Tech stack: [Python X.X, PyTorch/TensorFlow, etc.]

Create a to-do list and get on with it.
```

## Placeholders

- `[PROJECT_NAME]`: Repository and project name
- `[public/private]`: Repository visibility
- `[PAPER_TITLE, DOI/URL]`: Reference paper for methodology
- `[Python X.X, PyTorch/TensorFlow, etc.]`: Preferred tech stack
- `[content-integrity constraint]`: See [content-integrity.md](../development/content-integrity.md)

## Tips

- Always specify the source paper to ground the implementation, and keep in mind the original dataset/repo's type of license
- Define test expectations if needed (unit tests, validation splits)
- Add output format requirements if results need specific presentation
