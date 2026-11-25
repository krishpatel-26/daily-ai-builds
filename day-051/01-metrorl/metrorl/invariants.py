def audit_trajectory(result,capacity=36):
    stats=result['stats'];remaining=sum(sum(q) for q in result['final_queues'])
    errors=[]
    if stats['arrivals']!=stats['exits']+stats['dropped']+remaining:
        errors.append('mass_conservation')
    if any(v<0 or v>capacity for q in result['final_queues'] for v in q):
        errors.append('queue_bounds')
    if stats['emergencies_served']>stats['emergencies']:
        errors.append('emergency_count')
    if any(f['total_queue']<0 for f in result['trace']):
        errors.append('negative_occupancy')
    return {'ok':not errors,'errors':errors}
