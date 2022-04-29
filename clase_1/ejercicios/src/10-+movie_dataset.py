import numpy as np
import pickle


class Dataset(object):
    instance = None

    def __new__(cls, file_name):
        if Dataset.instance is None:
            Dataset.instance = super(Dataset, cls).__new__(cls)
            return Dataset.instance
        else:
            return Dataset.instance

    def __init__(self, file_name):
        try:
            self.structured_dataset = pickle.load(open("../data/movie_dataset.pkl", "rb"))
        except(OSError, IOError) as e:
            data = self._build_dataset(file_name)
            pickle.dump(data, open("../data/movie_dataset.pickle", "wb"))
            self.structured_dataset = pickle.load(open("../data/movie_dataset.pickle", "rb"))

    def _build_dataset(self, path):
        structure = [('userId', np.int64),
                     ('movieId', np.int64),
                     ('rating', np.float32),
                     ('timestamp', np.int64)]

        with open(path, encoding="utf8") as data_csv:
            data_gen = ((int(line.split(',')[0]), int(line.split(',')[1]),
                         float(line.split(',')[2]), int(line.split(',')[3]))
                        for i, line in enumerate(data_csv) if i != 0)
            data = np.fromiter(data_gen, structure)
        return data

    def get_first_five_rows(self):
        return self.structured_dataset[0:5]
