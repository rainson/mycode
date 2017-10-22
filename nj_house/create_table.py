import sqlite3

ershoufang = sqlite3.connect("ershoufang.sqlite")
create_table = "create table ershoufang (area varchar(128), house varchar(128), houseroom varchar(128), totalprice varchar(128), unitprice varchar(128))"
ershoufang.execute(create_table)
ershoufang.close()