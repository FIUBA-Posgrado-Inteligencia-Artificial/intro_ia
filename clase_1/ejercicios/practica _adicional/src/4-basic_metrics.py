import numpy as np


class BaseMetric:
    def __init__(self, **kwargs):
        self.parameters = kwargs

    def __call__(self, *args, **kwargs):
        pass


class Precision(BaseMetric):
    def __init__(self, **kwargs):
        BaseMetric.__init__(self, **kwargs)

    def __call__(self):
        prediction = self.parameters["predictions"]
        truth = self.parameters["truth"]
        true_pos_mask = (prediction == 1) & (truth == 1)
        true_pos = true_pos_mask.sum()
        false_pos_mask = (prediction == 1) & (truth == 0)
        false_pos = false_pos_mask.sum()
        return true_pos/(true_pos + false_pos)


class Recall(BaseMetric):
    def __init__(self, **kwargs):
        BaseMetric.__init__(self, **kwargs)

    def __call__(self):
        prediction = self.parameters["predictions"]
        truth = self.parameters["truth"]
        true_pos_mask = (prediction == 1) & (truth == 1)
        true_pos = true_pos_mask.sum()
        false_neg_mask = (prediction == 0) & (truth == 1)
        false_neg = false_neg_mask.sum()
        return true_pos/(true_pos + false_neg)


class Accuracy(BaseMetric):
    def __init__(self, **kwargs):
        BaseMetric.__init__(self, **kwargs)

    def __call__(self):
        prediction = self.parameters["predictions"]
        truth = self.parameters["truth"]
        true_pos_mask = (prediction == 1) & (truth == 1)
        true_pos = true_pos_mask.sum()
        false_pos_mask = (prediction == 1) & (truth == 0)
        false_pos = false_pos_mask.sum()
        true_neg_mask = (prediction == 0) & (truth == 0)
        true_neg = true_neg_mask.sum()
        false_neg_mask = (prediction == 0) & (truth == 1)
        false_neg = false_neg_mask.sum()
        return (true_pos + true_neg)/(true_pos + true_neg + false_pos + false_neg)
