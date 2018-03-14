import pandas as pd

# route_a = input('Source: ')

test = {'route': ['KLIT-KFDW', 'KFDW-KLIT', 'AAAA-BBBB', 'BBBB-AAAA'], 'n': [35, 45, 50, 10]}

df = pd.DataFrame(data=test)
total_df = []

print(df)

source = df.route.str.split('-')
# print(source)

for i, val in source.items():
    for j, sub_val in source.items():
        if (val[0] == sub_val[1]):
            total_df.append({'route': df['route'][i], 'total': df['n'][i] + df['n'][j]})

pd_total = pd.DataFrame(total_df)

print(pd_total)
