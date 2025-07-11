from pubmed_fetcher.fetcher import fetch_pubmed_ids

def test_fetch_pubmed_ids_returns_list():
    ids = fetch_pubmed_ids("covid", retmax=2)
    assert isinstance(ids, list)
    assert all(isinstance(i, str) for i in ids)
