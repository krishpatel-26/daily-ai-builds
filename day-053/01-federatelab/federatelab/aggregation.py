import statistics

def aggregate(updates,method='fedavg',trim=2):
    if not updates or any(len(v)!=len(updates[0]) for v in updates):raise ValueError('invalid update matrix')
    if method not in ('fedavg','median','trimmed_mean'):raise ValueError('unknown aggregator')
    out=[]
    for axis in range(len(updates[0])):
        values=sorted(row[axis] for row in updates)
        if method=='fedavg':out.append(sum(values)/len(values))
        elif method=='median':out.append(statistics.median(values))
        else:
            if len(values)<=2*trim:raise ValueError('insufficient clients to trim')
            out.append(sum(values[trim:len(values)-trim])/(len(values)-2*trim))
    return out
