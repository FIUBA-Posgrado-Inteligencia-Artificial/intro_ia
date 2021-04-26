import numpy as np
from metrics import BaseMetric


class QueryMeanPrecision(BaseMetric):

    def __init__(self, **kwargs):
        BaseMetric.__init__(self, **kwargs)

    def __call__(self):

        """
        Definición:
        Mean Precision obtiene la media de la precisión de cada query. La precisión de una query es la cantidad de
        documentos 'true positive' (realmente relevantes), dividido por la cantidad de documentos obtenidos. Una
        precisión de 1 significa una precisión perfecta para la query.
        """

        truth_relevance = self.parameters["truth_relevance"]
        query_ids = self.parameters["q_id"]

        # Obtener la cantidad de queries con al menos un documento relevante
        true_relevance_mask = (truth_relevance == 1)
        filtered_query_id = query_ids[true_relevance_mask]
        # en las queries con relevance, cuento
        filtered_true_relevance_count = np.bincount(filtered_query_id)
        # contar queries con 0 en queries sin documentos relevantes
        unique_query_ids = np.unique(query_ids)
        non_zero_count_idxs = np.where(filtered_true_relevance_count > 0)
        true_relevance_count = np.zeros(unique_query_ids.max() + 1)
        true_relevance_count[non_zero_count_idxs] = filtered_true_relevance_count[non_zero_count_idxs]
        # obtener el total solo para las queries existentes
        true_relevance_count_by_query = true_relevance_count[unique_query_ids]
        # obtener el total de documentos
        fetched_documents_count = np.bincount(query_ids)[unique_query_ids]
        # calcular la métrica
        precision_by_query = true_relevance_count_by_query / fetched_documents_count
        return np.mean(precision_by_query)
