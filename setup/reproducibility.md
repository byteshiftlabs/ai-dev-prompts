# Reproducibility

Make results reproducible by other people on other machines.

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
- `[content-integrity constraint]`: See [content-integrity.md](../development/content-integrity.md)

## Variations

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
- Document the tested environment in the README
- For ML, set seeds at the start, ideally before imports that create random state
- Consider containerization (Docker) when full environment reproducibility matters
