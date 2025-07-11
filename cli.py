import argparse
import csv
from pubmed_fetcher.fetcher import fetch_pubmed_ids, fetch_pubmed_details
from pubmed_fetcher.utils import setup_logger

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with pharma affiliations.")
    parser.add_argument("query", type=str, help="PubMed query")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename")

    args = parser.parse_args()

    setup_logger(args.debug)

    ids = fetch_pubmed_ids(args.query)
    details = fetch_pubmed_details(ids)

    if not details:
        print("No results with non-academic authors found.")
        return

    if args.file:
        with open(args.file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=details[0].keys())
            writer.writeheader()
            writer.writerows(details)
        print(f"Results written to {args.file}")
    else:
        for row in details:
            print(row)

if __name__ == "__main__":
    main()
