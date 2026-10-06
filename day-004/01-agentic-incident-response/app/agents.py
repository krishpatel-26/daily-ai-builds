from .models import Alert, Evidence

class Specialist:
    def __init__(self, name: str): self.name = name
    def analyze(self, alerts: list[Alert], recent_deploy: bool) -> Evidence:
        services = ', '.join(sorted({a.service for a in alerts}))
        if self.name == 'reliability':
            finding = f'Observed {len(alerts)} alert(s) across {services}; validate blast radius and dependency health.'
        elif self.name == 'release':
            finding = 'A recent deployment is a plausible change-correlated factor; compare rollout timing and error-rate deltas.' if recent_deploy else 'No recent deployment signal was supplied.'
        else:
            finding = 'Inspect saturation, latency, and error-budget impact before selecting remediation.'
        return Evidence(agent=self.name, finding=finding, confidence=.82)

AGENTS = [Specialist('reliability'), Specialist('release'), Specialist('performance')]
