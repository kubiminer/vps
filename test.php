import pandas as pd
import numpy as np
d = np.random.normal(100, 30, (10, 3)).astype(np.int)
df = pd.DataFrame(columns=list('ABC'), data=d)
print(df)
