#!/usr/bin/env python3

import csv
import sqlite3
import sys

# CSV输入文件的路径和文件名
input_file = sys.argv[1]

# 创建SQLite3内存数据库
# 创建带有5个属性的Suppliers表
con = sqlite3.connect('E:\\python_pycharm\\Python数据分析基础\\第4章 数据库\\Suppliers.db')
c = con.cursor()
create_table = """CREATE TABLE IF NOT EXISTS Suppliers
                  (Supplier_Name VARCHAR(20),
                  Invoice_Number VARCHAR(20),
                  Part_Number VARCHAR(20),
                  Cost FLOAT,
                  Purchase_Date DATE);"""
c.execute(create_table)
con.commit()

# 读取CSV文件
# 向Suppliers表中插入数据
file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(row[column_index])
    print(data)
    c.execute("INSERT INTO Suppliers VALUES (?, ?, ?, ?, ?);", data)
con.commit()
print('')

# 查询Suppliers表
output = c.execute("SELECT * FROM Suppliers")
rows = output.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)
