from unittest import TestCase
import numpy as np
from indexer import Indexer


class IndexerTestCase(TestCase):

    def test_indexer(self):
        a = np.array([10, 13, 14, 15], dtype=np.int64)
        indexer = Indexer(a)

        idxs, valid_idxs = indexer.get_idxs(np.array([13, 10]))
        np.testing.assert_equal(np.array([True, True]), valid_idxs)
        ids = indexer.get_ids(idxs)
        np.testing.assert_equal(np.array([13, 10]), ids)

        idxs, valid_idxs = indexer.get_idxs(np.array([13, 1, 2, 15]))
        np.testing.assert_equal(np.array([True, False, False, True]), valid_idxs)
        ids = indexer.get_ids(idxs[valid_idxs])
        np.testing.assert_equal(np.array([13, 15]), ids)
