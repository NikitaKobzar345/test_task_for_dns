import pandas as pandas

branches = pandas.read_csv(r'test_data\t_branches.csv')
cities = pandas.read_csv(r'test_data\t_cities.csv')
products = pandas.read_csv(r'test_data\t_products.csv')
sales = pandas.read_csv(r'test_data\t_sales.csv')

def get_stores_by_sale():
    
    stores = branches.loc[branches['Наименование'] != 'Склад']
    concat_data = pandas.concat([stores,sales],axis=1)

    return concat_data.sort_values('Количество',ascending=False).dropna().head(10)


def get_storage_by_sale():

    storages = branches.loc[branches['Наименование'] == 'Склад']
    concat_files = pandas.concat([storages,sales],axis=1)

    return concat_files.sort_values('Количество',ascending=False).head(10)


def get_cities_by_products():
    sort_sales = sales.sort_values('Количество',ascending=False)
    conc = pandas.concat([cities,sort_sales])
    return conc.head(10)
    

# Две нижнее функции не успел сделать
def get_products_by_storages():
    pass


def get_products_by_stores():
    pass
