#!/usr/bin/env python3

import csv
import MySQLdb
import sys

# CSV输出文件的路径和文件名
output_file = sys.argv[1]

# 连接MySQL数据库
con = MySQLdb.connect(host='localhost', port=3306, db='my_suppliers', user='root', passwd='cch20010406')
c = con.cursor()

# 创建写文件的对象，并写入标题行
filewriter = csv.writer(open(output_file, 'w', newline=''), delimiter=',')
header = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
filewriter.writerow(header)

# 查询Suppliers表，并将结果写入CSV输出文件
c.execute("""SELECT *
             FROM Suppliers
             WHERE Cost > 700.0;""")
rows = c.fetchall()
for row in rows:
    filewriter.writerow(row)
