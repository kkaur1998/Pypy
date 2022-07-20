import re
from urllib import response

from colorama import Cursor
from connection import get_sql_connection


def get_orders(cursor):
    response = []
    query = f'''select * from orders'''
    cursor.execute(query)
    for (order_id, customer, date) in cursor:
        response.append({'order_id': order_id, 'customer': customer,'order_date': date})
    return response

def get_products(cursor):
    response = []
    query = f'''select * from product'''
    cursor.execute(query)
    for (procuct_id, name, uom_id, price_per_unit) in cursor:
        response.append({'procuct_id': procuct_id, 'name': name,'uom_id': uom_id, 'price_per_unit':price_per_unit})
    return response

if __name__ == '__main__':
    cnx = get_sql_connection()
    cursor = cnx.cursor()
    print(get_products(cursor))
    print(get_orders(cursor))
    cnx.close()