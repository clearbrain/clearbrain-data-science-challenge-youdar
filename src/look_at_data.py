import pandas as pd
import os
# load the file and do some basic exploration
path = '/Users/youval.dar/Documents/other_things/general/cb/data'
df = pd.read_csv(os.path.join(path, 'conversion_data.csv'))
# look at conv. rate
print(df.converted.value_counts())

conv = df.converted.value_counts().to_list()
conv_rate = round(conv[1] / sum(conv), 2)
print('\nConv rate: {}'.format(conv_rate))

print('Done...')
