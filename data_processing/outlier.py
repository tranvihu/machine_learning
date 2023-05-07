import matplotlib
import numpy as np
import pandas as pd
import seaborn as sns
from docutils.nodes import inline
from scipy.stats import zscore
import matplotlib.pyplot as plt
import pandas as pd

def kaggle():
    df = pd.read_csv('outlier.csv', nrows=500)
    # downloaded from Kaggle(https://www.kaggle.com/austinreese/craigslist-carstrucks-data?select=vehicles.csv)

    Q3 = df['price'].quantile(0.75)
    Q1 = df['price'].quantile(0.25)

    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df_IQR = df.loc[(df['price'] > lower) & (df['price'] < upper)]
    sns.boxplot(data=df_IQR, y='price')

    df['price_zscore'] = zscore(df['price'])
    df_Z = df.loc[df['price_zscore'].abs() <= 3]
    sns.boxplot(data=df_Z, y='price')


def random():

    # Some test data
    np.random.seed(33454)
    df = (
        # A standard distribution
        pd.DataFrame({'nb': np.random.randint(0, 100, 20)})
            # Adding some outliers
            .append(pd.DataFrame({'nb': np.random.randint(100, 200, 2)}))
            # Reseting the index
            .reset_index(drop=True)
    )
    Q1 = df['nb'].quantile(0.25)
    Q3 = df['nb'].quantile(0.75)
    IQR = Q3 - Q1
    filtered = df.query('(@Q1 - 1.5 * @IQR) <= nb <= (@Q3 + 1.5 * @IQR)')
    df.join(filtered, rsuffix='_filtered').boxplot()

if __name__ == '__main__':
    kaggle()
    # random()

    plt.show()
