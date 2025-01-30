import pandas as pd
data = {
    'id': [1, 2, 3, 4],
    'name': ['A', 'B', 'C', 'D'],
    'sex': ['m', 'f', 'm', 'f'],
    'salary': [2500, 1500, 5500, 500]
}

df = pd.DataFrame(data)

df['sex'] = df['sex'].replace({'m': 'f', 'f': 'm'})


