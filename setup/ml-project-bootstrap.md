---
pack: task-workflows
summary: Bootstrap guidance for ML-oriented project setup.
tags: [setup, ml, bootstrap]
---

# Project Bootstrap

Initialize a new ML or research project with minimal, verified code.

## Prompt

```
Create a new local repo and its remote [public/private] counterpart for [PROJECT_NAME].

Create only the code and scripts needed for the software to run correctly and for the results to be presented correctly.

Base your work on the original paper [PAPER_TITLE, DOI/URL] and create the logic for:
- Downloading the dataset(s)
- Feature extraction
- Training
- Validation
- Results presentation

Tech stack: [Python X.X, PyTorch/TensorFlow, etc.]

Create a to-do list and execute it in order.
```

## Placeholders

- `[PROJECT_NAME]`: Repository and project name
- `[public/private]`: Repository visibility
- `[PAPER_TITLE, DOI/URL]`: Reference paper for methodology
- `[Python X.X, PyTorch/TensorFlow, etc.]`: Preferred tech stack

## Tips

- Specify the source paper so the implementation stays grounded in a real reference
- Check the licenses of the original dataset, code, and paper before reuse
- Define test expectations when needed, such as unit tests or validation splits
- Add output format requirements if the results must be presented in a specific way
