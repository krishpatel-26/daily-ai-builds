"""Illustrative thresholds; domain-specific drift alarms require calibration."""
from .drift import feature_drift

def monitor(training,observed,watch=.15,investigate=.35):
    if not 0<watch<investigate:raise ValueError('invalid monitor thresholds')
    values=feature_drift(training,observed)
    return {'features':{name:{'psi':value,'level':'investigate' if value>=investigate else 'watch' if value>=watch else 'stable'} for name,value in values.items()},
            'disclaimer':'PSI indicates feature distribution change, not measured defect-rate drift or model failure.'}
