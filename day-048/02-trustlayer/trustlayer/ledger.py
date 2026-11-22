from hashlib import sha256
import json

class Ledger:
    """Tamper-evident *local* log, not an externally anchored or signed record."""
    def __init__(self):self.entries=[]
    @staticmethod
    def canonical(payload):return json.dumps(payload,sort_keys=True,separators=(',',':'),ensure_ascii=False)
    def append(self,event):
        prior=self.entries[-1]['hash'] if self.entries else 'GENESIS'
        index=len(self.entries)
        digest=sha256(f'{index}|{prior}|{self.canonical(event)}'.encode()).hexdigest()
        row={'index':index,'previous_hash':prior,'event':event,'hash':digest}
        self.entries.append(row);return row
    def verify(self):
        previous='GENESIS'
        for i,row in enumerate(self.entries):
            if row.get('index')!=i or row.get('previous_hash')!=previous:return False
            expected=sha256(f"{i}|{previous}|{self.canonical(row['event'])}".encode()).hexdigest()
            if row.get('hash')!=expected:return False
            previous=expected
        return True