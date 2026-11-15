from app.data import generate
class Store:
 def __init__(self):self.rows=generate();self.orders=[]
 def ingest(self,row):self.rows.append(row);return row
 def history(self,m):return [x for x in self.rows if x.machine_id==m]
store=Store()