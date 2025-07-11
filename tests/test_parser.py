from pubmed_fetcher.parser import is_pharma_affiliation, extract_emails

def test_is_pharma_affiliation_true():
    assert is_pharma_affiliation("XYZ Biotech Inc.")

def test_is_pharma_affiliation_false():
    assert not is_pharma_affiliation("Stanford University")

def test_extract_emails():
    text = "Contact us at john@pharma.com or info@company.org"
    emails = extract_emails(text)
    assert "john@pharma.com" in emails
    assert "info@company.org" in emails
