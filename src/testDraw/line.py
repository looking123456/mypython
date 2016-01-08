import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy.linalg import svdvals
import matplotlib.pyplot as plt

df = pd.DataFrame({'X': np.arange(10), 'Y': np.arange(10) + np.random.randn(10)})
print(df)
mod = sm.OLS.from_formula("Y ~ X", df)
res = mod.fit()
print(res.summary())
exog = pd.DataFrame({"X": np.linspace(0, 10, 100)})
print(exog)
res.predict(exog)
fig = plt.figure()
 
exog.plot(ax=fig, style='k-') 
fig.show()