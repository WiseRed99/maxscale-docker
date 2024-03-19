# William Grainger
# CNE 370 at RTC
# 3/19/2024
# Pythone-Script that gets largest zipcode from zipecode one, All zipcodes where state = KY, all zipcodes between 40000 and 41000, and TotalWages column where state = PA.

import mysql.connector

con = mysql.connector.connect(user = "maxuser", password = "maxpwd", host = "127.0.0.1", port = "4000")

cursor = con.cursor()




cursor.execute("SELECT * FROM zipcodes_one.zipcodes_one")

first = cursor.fetchall()

print("first data")

for row in first:
	print(row)
	break




cursor.execute("SELECT * FROM zipcodes_two.zipcodes_two")

second = cursor.fetchall()

print("second data")

for row in second:
	print(row)
	break












cursor.close()
con.close()