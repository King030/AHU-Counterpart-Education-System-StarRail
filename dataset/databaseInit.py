import csv
import pymysql
import os
#更改成自己的密码
#更改成自己的路径（下面的csv路径）
db = pymysql.connect(host='localhost',
                     user='root',
                     password='Whw,030205',
                     port=3306,
                     db='StarRail_AHU_EduSys')
cursor = db.cursor()
# 删除 colleges 表中的数据
delete_majors_data = "DELETE FROM students;"
cursor.execute(delete_majors_data)

delete_colleges_data = "DELETE FROM colleges;"
cursor.execute(delete_colleges_data)

# 删除 grades 表中的数据
delete_grades_data = "DELETE FROM grades;"
cursor.execute(delete_grades_data)

# 删除 majors 表中的数据
delete_majors_data = "DELETE FROM majors;"
cursor.execute(delete_majors_data)

delete_majors_data = "DELETE FROM projects;"
cursor.execute(delete_majors_data)

delete_majors_data = "DELETE FROM teachers;"
cursor.execute(delete_majors_data)

delete_majors_data = "DELETE FROM users;"
cursor.execute(delete_majors_data)
db.commit()

#更改成自己的路径
with open(r'C:\Users\10168\Desktop\学生选课系统v1.2\学生选课系统\dataset\users.csv', 'r', encoding='utf-8') as f:
    read = csv.reader(f)

    # 一行一行地存，除去第一行和第一列
    for each in list(read)[1:]:
        i = tuple(each)
        # 使用SQL语句添加数据
        sql = "INSERT INTO users VALUES" + str(i)  # db_top100是表的名称
        cursor.execute(sql)  # 执行SQL语句
db.commit()
with open(r'C:\Users\10168\Desktop\学生选课系统v1.2\学生选课系统\dataset\colleges.csv', 'r', encoding='utf-8') as f:
    read = csv.reader(f)

    # 一行一行地存，除去第一行和第一列
    for each in list(read)[1:]:
        i = tuple(each)
        # 使用SQL语句添加数据
        sql = "INSERT INTO colleges VALUES" + str(i)  # db_top100是表的名称
        cursor.execute(sql)  # 执行SQL语句
db.commit()
with open(r'C:\Users\10168\Desktop\学生选课系统v1.2\学生选课系统\dataset\grades.csv', 'r', encoding='utf-8') as f:
    read = csv.reader(f)

    # 一行一行地存，除去第一行和第一列
    for each in list(read)[1:]:
        i = tuple(each)
        # 使用SQL语句添加数据
        sql = "INSERT INTO grades VALUES" + str(i)  # db_top100是表的名称
        cursor.execute(sql)  # 执行SQL语句
db.commit()
with open(r'C:\Users\10168\Desktop\学生选课系统v1.2\学生选课系统\dataset\majors.csv', 'r', encoding='utf-8') as f:
    read = csv.reader(f)

    # 一行一行地存，除去第一行和第一列
    for each in list(read)[1:]:
        i = tuple(each)
        # 使用SQL语句添加数据
        sql = "INSERT INTO majors VALUES" + str(i)  # db_top100是表的名称
        cursor.execute(sql)  # 执行SQL语句
db.commit()
with open(r'C:\Users\10168\Desktop\学生选课系统v1.2\学生选课系统\dataset\projects.csv', 'r', encoding='utf-8') as f:
    read = csv.reader(f)

    # 一行一行地存，除去第一行和第一列
    for each in list(read)[1:]:
        i = tuple(each)
        # 使用SQL语句添加数据
        sql = "INSERT INTO projects VALUES" + str(i)  # db_top100是表的名称
        cursor.execute(sql)  # 执行SQL语句
db.commit()
with open(r'C:\Users\10168\Desktop\学生选课系统v1.2\学生选课系统\dataset\students.csv', 'r', encoding='utf-8') as f:
    read = csv.reader(f)

    # 一行一行地存，除去第一行和第一列
    for each in list(read)[1:]:
        i = tuple(each)
        # 使用SQL语句添加数据
        sql = "INSERT INTO students VALUES" + str(i)  # db_top100是表的名称
        cursor.execute(sql)  # 执行SQL语句
db.commit()
with open(r'C:\Users\10168\Desktop\学生选课系统v1.2\学生选课系统\dataset\teachers.csv', 'r', encoding='utf-8') as f:
    read = csv.reader(f)

    # 一行一行地存，除去第一行和第一列
    for each in list(read)[1:]:
        i = tuple(each)
        # 使用SQL语句添加数据
        sql = "INSERT INTO teachers VALUES" + str(i)  # db_top100是表的名称
        cursor.execute(sql)  # 执行SQL语句

db.commit()
cursor.close()
db.close()

