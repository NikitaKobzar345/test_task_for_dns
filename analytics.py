import pandas as pandas

branches = pandas.read_csv(r'test_data\t_branches.csv')
cities = pandas.read_csv(r'test_data\t_cities.csv')
products = pandas.read_csv(r'test_data\t_products.csv')
sales = pandas.read_csv(r'test_data\t_sales.csv')


sales_sort = sales.sort_values('Количество',ascending=False)
storages = branches.loc[branches['Наименование'] == 'Склад']
stores = branches.loc[branches['Наименование'] != 'Склад']

def get_stores_by_sale():
    return pandas.concat([stores,sales_sort],axis=1).head(10)


def get_storage_by_sale():
    return pandas.concat([storages,sales_sort],axis=1).head(10)


def get_cities_by_products():
    return pandas.merge(cities,sales_sort).head(10)
    

def get_products_by_storages():
    return pandas.concat([products,storages]).head(10)


def get_products_by_stores():
    return pandas.concat([products,stores]).head(10)


def get_max_sale():
    return sales['Период'].max()
