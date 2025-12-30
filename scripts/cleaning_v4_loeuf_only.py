import pandas as pd
import numpy as np

df = pd.read_csv("../data/gnomad_v4_1.csv") #Creating Data Frame from cvs file
df = df[['gene', 'lof.oe_ci.upper']] # Only keep gene name and upperbound confidence interval loeuf score
df = df.rename(columns={'gene': 'Gene'})


mins_constraints = df.groupby('Gene', as_index=False).agg({'lof.oe_ci.upper': 'min'}) #Multiple gene reads, take the minimum value

mins_constraints.to_csv('cleaned_v4_loeuf.csv', index=False)



