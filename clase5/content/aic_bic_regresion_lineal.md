# Obtención de AIC y BIC para regresión lineal

<div align="center">
  <img src="img/fiuba.png" alt="FIUBA Logo" width="15%">
  
  **Dr. Ing. Facundo Adrián Lucianna | CEIA - FIUBA**
</div>

---

En la teoría vimos el **Criterio de Información de Akaike (AIC)** y el **Criterio de Información Bayesiano (BIC)**, que se utilizan para seleccionar modelos. En ambos criterios aparece la **verosimilitud**. Ahora que sabemos cómo se calcula la verosimilitud para el caso de la regresión lineal, podemos obtener ambos índices.

## 📐 Criterio de Información de Akaike (AIC)

Comencemos con el AIC, cuya fórmula es:

$$AIC = 2k - 2\ln(\hat{L})$$

donde $k$ es la cantidad de parámetros del modelo y $\hat{L}$ es la verosimilitud máxima. En la regresión lineal con $d$ atributos, los parámetros son los $d$ coeficientes más la ordenada al origen, es decir, $k = d + 1$.

> [!NOTE]
> Algunos autores también cuentan a $\sigma$ como parámetro, y usan $k = d + 2$. Esto suma la misma constante al AIC de todos los modelos, así que no cambia cuál es el mejor.

Para el caso de la regresión lineal, la log-verosimilitud se expresa como:

$$\ln\left(L(b, \mathbf{W})\right) = -N\ln(\sigma) - \frac{N}{2}\ln(2\pi) - \frac{1}{2\sigma^2} \sum_{i=0}^{N-1} \left(y_{[i]} - b - \mathbf{W}^T \mathbf{X}_{[i]}\right)^2$$

> ⚠️ **Nota**: Para repasar qué significa cada elemento, consulten el apunte donde obtenemos la log-verosimilitud: [Obtención de ecuaciones normales mediante máxima verosimilitud](./ecuaciones_normales_maxima_verosimilitud.md).

A partir de esto, podemos reemplazar en la fórmula del AIC:

$$AIC = 2k - 2\ln\left(L(b, \mathbf{W})\right)$$

$$AIC = 2k + 2N\ln(\sigma) + N\ln(2\pi) + \frac{1}{\sigma^2} \sum_{i=0}^{N-1} \left(y_{[i]} - b - \mathbf{W}^T \mathbf{X}_{[i]}\right)^2$$

---

## 🔍 Estimando σ

Además, tenemos que la suma de los residuos al cuadrado es:

$$S_{res} = \sum_{i=0}^{N-1} \left(y_{[i]} - b - \mathbf{W}^T \mathbf{X}_{[i]}\right)^2$$

Nos falta conocer $\sigma$. Su estimador de máxima verosimilitud se obtiene igual que los coeficientes, derivando el negativo de la log-verosimilitud con respecto a $\sigma$ e igualando a cero:

$$\frac{\partial\left(-\ln L\right)}{\partial \sigma} = \frac{N}{\sigma} - \frac{S_{res}}{\sigma^3} = 0 \quad \Rightarrow \quad \sigma = \sqrt{\frac{S_{res}}{N}}$$

Este valor es muy parecido al desvío estándar residual $s_{res} = \sqrt{S_{res} / (N - d - 1)}$ que vimos en la teoría: ambos coinciden cuando $N \gg d$.

---

## ✅ El AIC para regresión lineal

Ahora reemplazamos $\sigma$ en la fórmula:

$$AIC = 2k + 2N\ln\left(\sqrt{\frac{S_{res}}{N}}\right) + N\ln(2\pi) + \frac{1}{S_{res}/N} S_{res}$$

Por lo tanto, el Criterio de Información de Akaike para el caso de la regresión lineal es:

$$AIC = 2k + N\ln\left(\frac{S_{res}}{N}\right) + N\ln(2\pi) + N$$

---

## 📏 Criterio de Información Bayesiano (BIC)

De manera similar, podemos obtener el BIC:

$$BIC = k\ln(N) - 2\ln(\hat{L})$$

Reemplazando:

$$BIC = k\ln(N) + N\ln\left(\frac{S_{res}}{N}\right) + N\ln(2\pi) + N$$

Con estas fórmulas, en la notebook de [Selección de modelo](./jupyter_notebooks/03%20-%20seleccion%20de%20modelo.ipynb) hacemos la selección de atributos de una regresión lineal múltiple usando el AIC.
