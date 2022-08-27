import numpy as np
from movie_dataset import Dataset


def test_movie():
    dataset = Dataset('../data/ratings.csv')
    structure = [('userId', np.int64),
                 ('movieId', np.int64),
                 ('rating', np.float32),
                 ('timestamp', np.int64)]
    assert dataset.get_first_five_rows()[1] == np.array([(1, 147, 4.5, 1425942435)],
                                                        dtype=structure)
