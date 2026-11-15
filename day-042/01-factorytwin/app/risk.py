def classify(x):return "HIGH" if x>=.75 else "MEDIUM" if x>=.45 else "LOW"
def risk_index(anomaly,trend,criticality):return round(min(1,max(0,.62*anomaly+.23*min(1,abs(trend)*12)+.15*criticality)),4)
def estimate_hours(x):return None if x<.2 else round(max(2,168*(1-x)**2),1)