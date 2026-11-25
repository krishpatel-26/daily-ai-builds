from functools import lru_cache
from .experiment import one_trial,benchmark
from .dataset import split_dataset
from .monitor import monitor
@lru_cache(maxsize=1)
def report():
    data=split_dataset()
    return {'project':'VisionShift','example':one_trial(),'benchmark':benchmark(),
            'monitor':monitor(data['train'],data['shifted_pool']),
            'scope':'Synthetic features and labels. Not images, a trained deep vision model or validated defect detector.',
            'method':'Logistic regression trained from scratch; PSI drift; uncertainty/diversity/random active labeling.'}
