from typing import List, Dict
import requests
from xml.etree import ElementTree
import logging

logger = logging.getLogger(__name__)

def fetch_pubmed_ids(query: str, retmax: int = 20) -> List[str]:
    logger.debug("Fetching PubMed IDs for query: %s", query)
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {"db": "pubmed", "term": query, "retmode": "json", "retmax": retmax}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()["esearchresult"]["idlist"]

def fetch_pubmed_details(pmid_list: List[str]) -> List[Dict]:
    logger.debug("Fetching details for PubMed IDs: %s", pmid_list)
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {"db": "pubmed", "id": ",".join(pmid_list), "retmode": "xml"}
    response = requests.get(url, params=params)
    response.raise_for_status()
    root = ElementTree.fromstring(response.content)

    results = []
    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        pub_date = article.findtext(".//PubDate/Year") or "Unknown"
        affiliations = [aff.text for aff in article.findall(".//AffiliationInfo/Affiliation")]
        authors = [au.findtext("LastName") for au in article.findall(".//Author") if au.findtext("LastName")]

        from .parser import is_pharma_affiliation, extract_emails
        non_academic_authors = [aff for aff in affiliations if is_pharma_affiliation(aff)]
        emails = extract_emails(" ".join(affiliations))

        if non_academic_authors:
            results.append({
                "PubmedID": pmid,
                "Title": title,
                "Publication Date": pub_date,
                "Non-academic Author(s)": "; ".join(authors),
                "Company Affiliation(s)": "; ".join(non_academic_authors),
                "Corresponding Author Email": "; ".join(emails)
            })
    return results
