import pandas as pd
import chardet
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


"""
1.	Создайте Python-ноутбук, загрузите в него данные из csv-файла.  + 

2.	Изучите выбранный набор данных — определите количество столбцов, 
    названия столбцов, типы данных столбцов, использование памяти, 
    индекс диапазона и количество ячеек в каждом столбце (ненулевые значения). +

3.	Определите, содержатся ли в данных пропущенные значения и строки-дубликаты.  +


4.	Изучите функции библиотеки Pandas для работы с объектом DataFrame.
    Подумайте, какие из них могли бы пригодиться при предобработке данных, 
    попробуйте применить их к выбранному набору данных.

По каждому пункту задания сделайте выводы и отразите их в созданном Python-ноутбуке. В качестве решения задания прикрепите ссылку на свой ноутбук.
"""


def find_correct_encoding():
    global encoding
    with open("Worlds Best 50 Hotels.csv", 'rb') as rawdata:
        result = chardet.detect(rawdata.read(10000))  # Читаем первые 10000 байт
    print(result)  # Выведет словарь с информацией о кодировке (encoding, confidence)
    encoding = result['encoding']


if __name__ == '__main__':
    #0. Preparing for work with data
    find_correct_encoding()
    #1. reading csv file
    path_to_file = 'Worlds Best 50 Hotels.csv'
    df = pd.read_csv(path_to_file, sep=',', encoding=encoding)
    print(df.head())
    #2. number of columns, column data types,
        # memory usage, range index, and number of cells in each column (non-zero values).
    print(df.info())
    # column names
    print(df.columns)
    #3. Determine if your data contains missing values and duplicate rows
    print(df.isnull)
    print(df.isnull().sum())
    print(df.duplicated())
    print(df.duplicated().sum)
    #4. Explore the Pandas library functions for working with the DataFrame object.
        #Think about which of them might be useful for data preprocessing,
        # try applying them to the selected data set.
    print(df.head())
    print(df.tail())
    print(df.info())
    print(df.describe())
    print(df.isnull)
    print(df.isnull().sum())
    columns_list = df.columns
    df.dropna(inplace=True)
    print(df.info())









