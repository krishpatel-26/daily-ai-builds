RUNBOOKS = {
    'latency': 'Check dependency latency, saturation, and recent configuration changes; rollback only after confirming correlation.',
    'error': 'Inspect error samples and downstream dependencies; disable the failing path only after impact is confirmed.',
    'cpu': 'Check saturation and traffic shape; scale capacity before invasive remediation when the signal is sustained.'
}

def retrieve_runbooks(alerts):
    hits=[]
    for a in alerts:
        key=next((k for k in RUNBOOKS if k in a.metric.lower() or k in a.message.lower()), None)
        if key and RUNBOOKS[key] not in hits: hits.append(RUNBOOKS[key])
    return hits
