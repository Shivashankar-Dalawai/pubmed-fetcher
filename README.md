# PubMed Fetcher

A command-line tool to fetch PubMed papers based on a user-defined query and extract papers authored by pharmaceutical or biotech-affiliated authors.

## Features
- Supports full PubMed query syntax
- Filters non-academic authors using keyword heuristics
- Outputs CSV with:
  - PubmedID
  - Title
  - Publication Date
  - Non-academic Authors
  - Company Affiliations
  - Corresponding Author Emails

## Setup

```powershell
git clone https://github.com/Shivashankar-Dalawai/pubmed-fetcher
cd pubmed-fetcher
poetry install
```

## Usage

```powershell
poetry run get-papers-list "cancer treatment" -d -f results.csv
```

## Tools Used
- [NCBI E-utilities](https://www.ncbi.nlm.nih.gov/books/NBK25499/)
- [Poetry](https://python-poetry.org/)
- Optionally: ChatGPT/OpenAI

## Test

```powershell
poetry run pytest
```

## Publish to TestPyPI

```powershell
poetry config repositories.test-pypi https://test.pypi.org/legacy/
poetry publish --build -r test-pypi
```
## 📽 Demo Video

[▶️ Watch on My_Drive]()
