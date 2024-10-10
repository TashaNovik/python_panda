import numpy as np
import pandas as pd

df = pd.DataFrame(np.nan, index=[0, 1, 2, 3], columns=['I', 'II', 'III'])
df.loc[0,"I"] = 1
df.loc[1,"I"] = 2
df.loc[2,"I"] = 3
df.loc[3,"I"] = 4
df.loc[0,"II"] = 5
df.loc[1,"II"] = 6
df.loc[2,"III"] = 7
df.loc[3,"III"] = 6
# далее запишите ваш код

if __name__ == '__main__':
    #1. Замените индексы строк на последовательность чисел от 1 до 4, используя соответствующий метод библиотеки Pandas.
    new_indexes =  df.set_axis([1, 2, 3, 4], axis='index')
    # проверка аутпута:
    #print(new_indexes)
    """
    I   II  III
1  1.0  5.0  NaN
2  2.0  6.0  NaN
3  3.0  NaN  7.0
4  4.0  NaN  6.0
    """
    #2.	Переименуйте названия колонок в последовательность букв A, B, C ,
    # используя соответствующий метод библиотеки Pandas.
    new_columns_naming = new_indexes.set_axis(['A', 'B','C'], axis='columns')
    # проверка аутпута:
    #print(new_columns_naming)
    """
     A    B    C
1  1.0  5.0  NaN
2  2.0  6.0  NaN
3  3.0  NaN  7.0
4  4.0  NaN  6.0
    """
    #3. Замените пропущенные значения числом 55.
    replace_null_elements = new_columns_naming.fillna('55')
    # проверка аутпута:
    #print(replace_null_elements)
    """
     A    B    C
1  1.0  5.0   55
2  2.0  6.0   55
3  3.0   55  7.0
4  4.0   55  6.0
    """