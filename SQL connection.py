import sqlite3
a=sqlite3.connect('SQLdata.db')
b=a.cursor()
#b.execute('create table Students(rollno number,name varchar,phno number,marks number)')
'''b.execute("insert into Students values(101,'Kaliya',9865443783,35)")
b.execute("insert into Students values(102,'Dolu',9566778983,99)")
b.execute("insert into Students values(103,'Bolu',9865443783,98)")
b.execute("insert into Students values(104,'Indhumathi',9732647437,95)")'''
data=b.execute('select * from Students')
# print(data.fetchone()[1])#kaliya
#print(data.fetchmany(3)[1][1])#first 3values-->(102, 'Dolu', 9566778983, 99)--->Dolu
print(data.fetchall())
a.commit()
a.close()