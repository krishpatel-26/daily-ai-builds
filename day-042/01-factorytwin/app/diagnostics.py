def diagnose(f):
 c=[]
 if f["temperature"]["slope"]>.08:c.append("Rising thermal load: inspect cooling, lubrication and duty cycle.")
 if f["vibration"]["latest"]>1.9:c.append("Elevated vibration: inspect alignment, bearings and mounting.")
 if f["pressure"]["slope"]<-.01:c.append("Pressure decay: inspect leaks, seals and supply stability.")
 if f["throughput"]["slope"]<-.12:c.append("Throughput degradation: inspect tool wear, jams and cycle parameters.")
 if f["current"]["latest"]>10.5:c.append("High electrical current: inspect motor load and mechanical resistance.")
 return c or ["No dominant threshold signature. Validate sensors and continue monitoring."]