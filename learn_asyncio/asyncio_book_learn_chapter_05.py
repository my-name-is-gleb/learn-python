import asyncio
import asyncpg
from util import password
from asyncpg import Record
from asyncpg import Connection # мы импортируем этот класс чтобы обозначит переменую подключения как объект этого класса
                               # для того чтобы vscode понимал что за объект, переменая подключения, если убрать его то 
                               # vscode не будет подсказывать методы к нашей переменной
                               # это происходит из-за того что разработчики asyncpg написали код так,
                               # что типы данных генерируются динамически во время работы программы.

# Объявляем SQL-запросы в виде текстовых переменных
# CREATE_BRAND_TABLE =\
#       """
# CREATE TABLE IF NOT EXISTS brand(
#     brand_id SERIAL PRIMARY KEY,
#     brand_name TEXT NOT NULL
# );"""
# 
# CREATE_PRODUCT_TABLE = \
#     """
# CREATE TABLE IF NOT EXISTS product(
#     product_id SERIAL PRIMARY KEY,
#     product_name TEXT NOT NULL,
#     brand_id INT NOT NULL,
#     FOREIGN KEY (brand_id) REFERENCES brand(brand_id)
# );"""
# 
# CREATE_PRODUCT_SIZE_TABLE = \
#     """
# CREATE TABLE IF NOT EXISTS product_size(
#     product_size_id SERIAL PRIMARY KEY,
#     product_size_name TEXT NOT NULL
# );"""
# 
# CREATE_PRODUCT_COLOR_TABLE = \
#     """
# CREATE TABLE IF NOT EXISTS product_color(
#     product_color_id SERIAL PRIMARY KEY,
#     product_color_name TEXT NOT NULL
# );"""
# 
# CREATE_SKU_TABLE = \
#     """
# CREATE TABLE IF NOT EXISTS sku(
#     sku_id SERIAL PRIMARY KEY,
#     product_id INT NOT NULL,
#     product_size_id INT NOT NULL,
#     product_color_id INT NOT NULL,
#     FOREIGN KEY (product_id) 
#     REFERENCES product(product_id),
#     FOREIGN KEY (product_size_id) 
#     REFERENCES product_size(product_size_id),
#     FOREIGN KEY (product_color_id) 
#     REFERENCES product_color(product_color_id)
# );"""
# 
# COLOR_INSERT = \
#     """
# INSERT INTO product_color VALUES (1, 'Blue');
# INSERT INTO product_color VALUES (2, 'Black');
# """
# 
# SIZE_INSERT = \
#     """
# INSERT INTO product_size VALUES (1, 'Small');
# INSERT INTO product_size VALUES (2, 'Medium');
# INSERT INTO product_size VALUES (3, 'Large');
# """

async def main():
    connection: Connection = await asyncpg.connect(host = "127.0.0.1",
                                       port=5432,
                                       user="postgres",
                                       database='products',
                                       password=password)
    
    await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Levis')")
    await connection.execute("INSERT INTO brand VALUES(DEFAULT, 'Seven')")

    brand_query = 'SELECT brand_id, brand_name FROM brand'
    result: list[Record] = await connection.fetch(brand_query)

    for brand in result:
        print(f"id: {brand['brand_id']}, name: {brand["brand_name"]}")

    await connection.close()
    """------------------------------"""
    # statment = [CREATE_BRAND_TABLE,
    #         CREATE_PRODUCT_TABLE,
    #         CREATE_PRODUCT_COLOR_TABLE,
    #         CREATE_PRODUCT_SIZE_TABLE,
    #         CREATE_SKU_TABLE,
    #         SIZE_INSERT,
    #         COLOR_INSERT]
    # 
    # for table in statment:
    #   status = await connection.execute(table)
    #   print(status)
    # await connection.close()
    """------------------------------"""
    version = connection.get_server_version()
    print(f"Подключенно! Версия Postgres равна {version}")
    """------------------------------"""
    # await connection.execute("CREATE DATABASE products")
    # print("База данных product создана")
    """------------------------------"""

asyncio.run(main())