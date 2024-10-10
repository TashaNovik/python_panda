import pandas as pd
import numpy as np

fruit = np.array(["lemons", "lemons", "lemons", "lemons",
                  "apples", "apples", "apples", "apples",
                  "apples", "apples", "apples"],
                 dtype=object)

shop = np.array(["Shop A", "Shop A", "Shop A", "Shop B",
                 "Shop A", "Shop A", "Shop A", "Shop B",
                 "Shop B", "Shop B", "Shop A"],
                dtype=object)

pl = np.array(["online", "online", "offline",
               "online", "online", "offline",
               "offline", "online", "offline",
               "offline", "offline"],
              dtype=object)

df = pd.DataFrame({'fruit': fruit, 'shop': shop, 'pl': pl,
                   "Q": [1, 2, 2, 3, 3, 4, 5, 6, 7, 4, 4],
                   "P": [5, 4, 5, 5, 6, 6, 8, 9, 9, 3, 3]})
df['total'] = df['Q'] * df['P']
# далее запишите ваш код
"""
1.	Создайте сводную таблицу датафрейма df, 
    где будет выведено значение переменной total с разбиением по строкам — 
    категориям переменной shop и колонками по переменной pl. 
    Используйте сумму как метод сведения и сохраните таблицу в переменную pivot.

2.	Выведите значение для второй колонки второй строки таблицы pivot.
"""
if __name__ == '__main__':
    pivot = pd.pivot_table(df,values='total', index='shop', columns='pl', aggfunc='sum')
    row_index = pivot.index.get_loc('Shop B')
    col_index = pivot.columns.get_loc('online')
    pivot2 = pivot.iloc[row_index, col_index]
    print(pivot2)
    print(pivot)