# -*- coding: utf-8 -*-
# time: 2023/9/8 16:04
# file: con_mysql.py
# author: wht

'''
1、如果系统重装后，mysql服务没有了，想继续用以往的data数据，就先修改别名data_old,再初始化mysql
    mysqld -install  (安装服务)
    mysqld   (启动mysql服务)
    mysqld --initialize --console   (初始化用户，生成密码)
    net start mysql     (启动服务)
    mysql -u root -p    (登录)
    net stop mysql    (结束服务)

    (重置密码)：
    ALTER USER 'root'@'localhost' IDENTIFIED BY '123' PASSWORD EXPIRE NEVER;  //注意大小写
2、修改完密码后，退出root操作，再结束mysql服务；将data_old全部复制到新的data内进行覆盖
3、再启动mysql，即可看到原来的databases
'''

import pymysql


flag = 1
if flag == 1:
    ...

    mysql = pymysql.connect(host='localhost',
                            user='root',
                            password='123',
                            port=3306,
                            database='study')
    cour = mysql.cursor()
    print(cour,type(cour))
    # 展示所有表
    cmd = 'show tables;'
    cour.execute(cmd)
    print(cour.fetchall())
    # 查询s1表数据
    cmd = 'select * from s1;'
    cour.execute(cmd)
    print(cour.fetchone())
    print(cour.fetchmany(2))
    print(cour.fetchall())
    cour.close()

flag = 1
if flag == 11:
    ...
    '''通过虚拟机进行连接：
    1、先关闭防火墙 getenforce
        systemctl stop firewalld.service
        systemctl disable firewalld.service
    2、在配置远程连接host：use mysql; update user set common='%' where user='root'; select common from user where user='root';
    3、重启mysql服务： systemctl restart mysqld.service
    '''
    mysql = pymysql.connect(host='192.168.64.128',
                            user='root',
                            password='123',
                            port=3306,
                            database='study')
    cour = mysql.cursor()
    print(cour, type(cour))
    # 展示所有表
    cmd = 'show tables;'
    cour.execute(cmd)
    print(cour.fetchall())
    # 查询s1表数据
    cmd = 'select * from s1;'
    cour.execute(cmd)
    print(cour.fetchall())



