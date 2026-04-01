# philiprehberger-list-chunk

[![Tests](https://github.com/philiprehberger/py-list-chunk/actions/workflows/publish.yml/badge.svg)](https://github.com/philiprehberger/py-list-chunk/actions/workflows/publish.yml)
[![PyPI version](https://img.shields.io/pypi/v/philiprehberger-list-chunk.svg)](https://pypi.org/project/philiprehberger-list-chunk/)
[![Last updated](https://img.shields.io/github/last-commit/philiprehberger/py-list-chunk)](https://github.com/philiprehberger/py-list-chunk/commits/main)

Split iterables into evenly sized chunks.

## Installation

```bash
pip install philiprehberger-list-chunk
```

## Usage

```python
from philiprehberger_list_chunk import chunk, chunk_by, sliding_window, interleave, flatten

chunk([1, 2, 3, 4, 5], size=2)
# [[1, 2], [3, 4], [5]]

chunk([1, 2, 3], size=2, pad=0)
# [[1, 2], [3, 0]]

chunk_by([1, 1, 2, 2, 3], key=lambda x: x)
# [[1, 1], [2, 2], [3]]

sliding_window([1, 2, 3, 4, 5], size=3)
# [[1, 2, 3], [2, 3, 4], [3, 4, 5]]

interleave([1, 2, 3], ["a", "b", "c"])
# [1, "a", 2, "b", 3, "c"]

flatten([[1, 2], [3, 4]])
# [1, 2, 3, 4]
```

## API

| Function / Class | Description |
|------------------|-------------|
| `chunk(items, size, pad=None)` | Fixed-size chunks |
| `chunk_by(items, key)` | Group consecutive elements by key |
| `sliding_window(items, size, step=1)` | Sliding window views |
| `interleave(*iterables)` | Round-robin interleave |
| `flatten(nested)` | Flatten one level of nesting |

## Development

```bash
pip install -e .
python -m pytest tests/ -v
```

## Support

If you find this project useful:

⭐ [Star the repo](https://github.com/philiprehberger/py-list-chunk)

🐛 [Report issues](https://github.com/philiprehberger/py-list-chunk/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

💡 [Suggest features](https://github.com/philiprehberger/py-list-chunk/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement)

❤️ [Sponsor development](https://github.com/sponsors/philiprehberger)

🌐 [All Open Source Projects](https://philiprehberger.com/open-source-packages)

💻 [GitHub Profile](https://github.com/philiprehberger)

🔗 [LinkedIn Profile](https://www.linkedin.com/in/philiprehberger)

## License

[MIT](LICENSE)
