import numpy as np
from metrics import Precision, Recall, Accuracy
from avg_q_precision import QueryMeanPrecision


class IterateMetrics(object):
    def __init__(self, **kwargs):
        self.data = kwargs
        self.metrics = {}

    def get_metrics(self):
        metrics_options = [Precision, Recall, Accuracy, QueryMeanPrecision]
        for metric in metrics_options:
            aux = metric(**self.data)
            self.metrics[metric.__name__] = aux()
        return self.metrics
