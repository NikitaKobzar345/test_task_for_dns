import pandas as pandas

branches = pandas.read_csv(r'test_data\t_branches.csv')
cities = pandas.read_csv(r'test_data\t_cities.csv')
products = pandas.read_csv(r'test_data\t_products.csv')
sales = pandas.read_csv(r'test_data\t_sales.csv')

sales_sort = sales.sort_values('Количество',ascending=False)

def get_stores_by_sale():
    
    stores = branches.loc[branches['Наименование'] != 'Склад']
    return pandas.concat([stores,sales_sort],axis=1).head(10)

print(get_stores_by_sale())

def get_storage_by_sale():

    storages = branches.loc[branches['Наименование'] == 'Склад']
    return pandas.concat([storages,sales_sort],axis=1).head(10)

print(get_storage_by_sale())

def get_cities_by_products():
    return pandas.concat([cities,sales_sort]).head(10)
    
print(get_cities_by_products())


# Две нижнее функции не успел сделать
def get_products_by_storages():
    pass


def get_products_by_stores():
    pass
