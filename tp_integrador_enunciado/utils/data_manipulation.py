import pandas as pd
import numpy as np


def generate_outliers(
    df: pd.DataFrame,
    cols: list = None,
    extreme_outlier: bool = False,
    two_tailed: bool = False,
    percentage: float = 0.02,
) -> pd.DataFrame:
    """Con esta función vamos a poder generar outliers en ciertas columnas de nuestro
    dataset. Si le damos True a _extreme_outlier_ va a generar outliers con mucho
    peso en la regresión (puede ser bilateral o unilateral segun _two_tailed_)
    """
    seeds = np.random.randint(100, size=len(df))

    nsamples = np.math.floor(len(df) * percentage)
    idx_to_change = df.sample(n=nsamples).index

    cols = df.columns.tolist() if cols is None else cols

    result = df.copy(deep=True)

    for i, col_name in enumerate(cols):
        np.random.seed(seeds[i])

        iqr = result[col_name].quantile(0.75) - result[col_name].quantile(0.25)

        lb = result[col_name].quantile(0.25) - 1 * iqr
        ub = result[col_name].quantile(0.75) + 1 * iqr

        if two_tailed:
            outs = result[col_name].loc[
                (result[col_name] < lb) | (result[col_name] > ub)
            ]
        else:
            outs = result[col_name].loc[(result[col_name] > ub)]

        out_size = len(outs)
        if out_size < nsamples:
            nsamples = out_size

        idx_to_change = outs.sample(nsamples, replace=False).index

        if extreme_outlier:
            outlier_sign = [
                1 if np.random.random() < 0.9 else -1 for _ in range(nsamples)
            ]

            result[col_name].loc[idx_to_change] = np.multiply(
                outlier_sign,
                np.random.uniform(
                    low=result[col_name].mean(),
                    high=result[col_name].max() * 5,
                    size=nsamples,
                ),
            )
            result["target"].loc[idx_to_change] = np.multiply(
                outlier_sign,
                np.random.uniform(
                    low=result["target"].mean(),
                    high=result["target"].max() * 2,
                    size=nsamples,
                ),
            )
        else:
            samples = result[col_name].loc[idx_to_change].values
            np.random.shuffle(samples)
            result[col_name].loc[idx_to_change] = samples

    return result
