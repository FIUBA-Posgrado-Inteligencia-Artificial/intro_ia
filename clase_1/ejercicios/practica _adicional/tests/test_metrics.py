import numpy as np
import pytest
from basic_metrics import Precision, Recall, Accuracy
from avg_q_precision import QueryMeanPrecision
from metrics_iteration import IterateMetrics


@pytest.fixture(scope='module')
def example_data():
    predictions = np.array([1, 1, 0, 1, 0, 1, 0, 0])
    truth = np.array([0, 1, 1, 0, 1, 1, 0, 1])
    q_id = np.array([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4])
    truth_relev = np.array([1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1])
    data = {"predictions": predictions, "truth": truth, "q_id": q_id,
            "truth_relevance": truth_relev}
    return data


def test_individual(example_data):
    data = example_data
    metrics_options = [Precision, Recall, Accuracy, QueryMeanPrecision]
    validations = [0.5, 0.4, 0.375, 0.5, 0.5]
    for i, metric in enumerate(metrics_options):
        aux = metric(**data)
        assert aux() == validations[i]


def test_loop_metrics(example_data):
    data = example_data
    iterator = IterateMetrics(**data)
    assert iterator.get_metrics() == {"Precision": 0.5, "Recall": 0.4, "Accuracy": 0.375,
                                    "QueryMeanPrecision": 0.5}
