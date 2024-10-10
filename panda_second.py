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
"""
1.	Сделайте срез по условию для df. Выберите все строки со значением Q больше 3, 
    для которых значение переменной Shop — это Shop A. 
    Сохраните результат в переменную subset. 
    Получите значение колонки total для второй строки получившегося среза subset и сохраните его в переменную total2.

2.	Посчитайте общую выручку в разбивке по всем фруктам (колонка total), 
    результат (объект Series) сохраните в переменную fruit_total.

3.	Посчитайте общее количество (колонка Q) всех фруктов в разбивке по названию, 
    результат (объект Series) сохраните в переменную fruit_quantity.

4.	Посчитайте среднюю цену (колонка P) лимонов, 
    результат (объект Series) сохраните в переменную lemon_average_price.

Обратите внимание: в заданиях не требуется выполнять вывод полученных результатов на экран.
"""
if __name__ == '__main__':
    #1.
    subset =  df[(df['Q'] > 3) & (df['shop'] == "Shop A")]
    #print(subset)
    total2 = subset['total'].iloc[1]
    #print(total2)
    #2.
    fruit_total = df.groupby('fruit')['total'].sum()
    #print(fruit_total)
    #3.
    fruit_quantity = df.groupby('fruit')['Q'].sum()
    #print(fruit_quantity)
    #4.
    lemon_average_price = df.groupby('fruit')['P'].mean().loc[['lemons']]
    #print(lemon_average_price)
