from uuid import uuid4; from questguard.validate import validate
def inspect(s,p):
 c,m=validate(s,p);return {"accepted":c=="ACCEPTED","code":c,"reason":m,"audit_id":str(uuid4()),"action":p.model_dump() if c=="ACCEPTED" else None}