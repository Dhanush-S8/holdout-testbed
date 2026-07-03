# mathkit

A tiny, dependency-free toolkit of everyday helpers:

- `mathkit.stats` — `mean`, `median`, `variance`, `zscore`
- `mathkit.pricing` — `apply_discount`, `tiered_price`, `tax`
- `mathkit.strings` — `slugify`, `truncate`, `word_count`

## Install

```bash
pip install -e ".[test]"
```

## Test

```bash
pytest -q
```

Pure standard library. No runtime dependencies.
