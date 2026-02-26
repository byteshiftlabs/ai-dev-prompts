# Reproducibility

Ensure results can be reproduced by anyone, anywhere, anytime.

## Prompt

```
Make [PROJECT_NAME] reproducible.

[content-integrity constraint]

Ensure:
- All dependencies are pinned to exact versions (requirements.txt, package-lock.json, etc.)
- Random seeds are set and documented for all stochastic operations
- Environment setup is documented (OS, hardware requirements if relevant)
- Data sources are versioned or checksummed
- All configuration is explicit, not implicit
```

## Placeholders

- `[PROJECT_NAME]`: Project to make reproducible
- `[content-integrity constraint]`: See [content-integrity.md](content-integrity.md)

## Variations

### ML experiment reproducibility
```
Ensure [EXPERIMENT] is reproducible:
- Pin random seeds: numpy, torch/tensorflow, python random
- Log all hyperparameters
- Record dataset version/hash
- Save model checkpoints with metadata
- Document hardware (GPU model, CUDA version)
- Use deterministic algorithms where available
```

### Environment setup
```
Create reproducible environment setup for [PROJECT]:
- requirements.txt with pinned versions (==, not >=)
- Document Python/Node/compiler version
- Include setup script or Makefile
- Add .env.example for environment variables
- Document any system dependencies (apt, brew packages)
```

## Tips

- `pip freeze > requirements.txt` captures exact versions
- Use lockfiles (poetry.lock, package-lock.json, Cargo.lock)
- Document "it works on" environment in README
- For ML: set seeds at the very start, before any imports if possible
- Consider containerization (Docker) for complete reproducibility
