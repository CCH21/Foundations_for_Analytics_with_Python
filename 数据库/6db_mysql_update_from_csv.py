#!/usr/bin/env python3

import csv
import MySQLdb
import sys

# CSV输入文件的路径和文件名
input_file = sys.argv[1]

# 连接MySQL数据库
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='root', passwd='cch20010406')
c = con.cursor()

# 读取CSV文件并更新特定的行
file_reader = csv.reader(open(input_file, 'r', newline=''), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
    data = []
    for column_index in range(len(header)):
        data.append(str(row[column_index]).strip())
    print(data)
    c.execute("""UPDATE Suppliers SET Cost=%s, Purchase_Date=%s WHERE Supplier_Name=%s;""", data)
con.commit()

# 查询Suppliers表
c.execute("SELECT * FROM Suppliers")
rows = c.fetchall()
for row in rows:
    output = []
    for column_index in range(len(row)):
        output.append(str(row[column_index]))
    print(output)
