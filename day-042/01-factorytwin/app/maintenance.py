def recommend(level,causes):
 h={"HIGH":4,"MEDIUM":24,"LOW":72}[level]
 return {"urgency":{"HIGH":"Controlled inspection within 4 hours","MEDIUM":"Plan inspection within 24 hours","LOW":"Continue condition monitoring"}[level],"recommended_window_hours":h,"checks":causes,"requires_human_approval":True}