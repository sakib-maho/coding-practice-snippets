# Coding Practice Snippets (Structured Toolkit)

<!-- BrandCloud:readme-standard -->
[![Maintained](https://img.shields.io/badge/Maintained-yes-brightgreen.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Showcase](https://img.shields.io/badge/Portfolio-Showcase-blue.svg)](#)

_Part of the `sakib-maho` project showcase series with consistent documentation and quality standards._

This repository has been upgraded from standalone scripts into a small Python algorithm toolkit.
It groups common interview-style problems into reusable modules and includes automated tests.

## Included Algorithms

- `two_sum(nums, target)`
- `binary_search(arr, value)`
- `is_valid_brackets(text)`
- `jewel_count(jewels, stones)`

## Run Demo

```bash
python3 main.py
```

## Run Tests

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

## Project Structure

```text
coding-practice-snippets/
├── algorithms/
│   ├── search.py
│   ├── strings.py
│   └── twosum.py
├── tests/test_algorithms.py
└── main.py
```

## License

MIT License. See `LICENSE`.
