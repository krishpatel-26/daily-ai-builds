class LocalProvider:
 name='local'; model='deterministic-v1'
 def complete(self,prompt,max_tokens): return 'Local model response: '+' '.join(prompt.strip().split()[:max_tokens])
class ReasoningProvider(LocalProvider):
 name='local-reasoning'; model='reasoning-sim-v1'
 def complete(self,prompt,max_tokens): return 'Plan: identify constraints -> analyze evidence -> produce answer. Input: '+prompt[:max_tokens*3]
