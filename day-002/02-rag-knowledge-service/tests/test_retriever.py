from app.retriever import search
def test_relevant_document_ranks_first():
    rows=[(1,'Auth','OAuth tokens expire after rotation.'),(2,'Billing','Invoices are generated monthly.')]
    assert search(rows,'OAuth rotation')[0]['document_id']==1
def test_empty_result_for_unknown_term():
    assert search([(1,'Billing','Invoices only.')],'webhooks')==[]