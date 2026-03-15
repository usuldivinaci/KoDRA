# Contributing to KoDRA

Thank you for your interest in KoDRA (Kiss Of the Dragon).

## How to contribute

- **Bug reports and feature requests** : open an [Issue](https://github.com/usuldivinaci/KoDRA/issues).
- **Code or new cases** : fork the repo, create a branch, make your changes, then open a Pull Request.

## Development setup

```bash
git clone https://github.com/usuldivinaci/KoDRA.git
cd KoDRA
pip install -r requirements.txt
python KoDRA.py list
```

## Adding a new case

- Add a folder under `Cases/` with a `handler.py` and optional `README.md`, and register the case in `Cases/manifest.json` (or as discovered by the engine).
- See existing cases (e.g. `KODRA_SINGULARITY_TEST`) for structure.

## Code style

- Python: UTF-8, cross-platform. Follow existing style in the codebase.
