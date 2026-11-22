# This is a conceptual allowlist. No approved action is actually executed by the prototype.
ALLOWED={'read_report':{'prefix':'report:','approval':False,'sources':{'internal'}},
         'draft_email':{'prefix':'draft:','approval':False,'sources':{'internal'}},
         'update_ticket':{'prefix':'ticket:','approval':True,'sources':{'internal'}},
         'send_email':{'prefix':'outbox:','approval':True,'sources':{'internal'}}}
DENIED={'transfer_funds','delete_database','export_secrets','disable_monitoring'}

def policy_for(action):return ALLOWED.get(action)