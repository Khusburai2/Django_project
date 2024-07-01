from django.test import TestCase

# Create your tests here.
import MySQLdb

conn = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="admin",
    db="lunar"
)

print("Connection successful")
conn.close()
