import mysql.connector
import random

def gemino(mycursor):
    session2 = str(random.randrange(1111, 9999))
    mycursor.execute("create table dummytable" + session2 + " as select * from mysql.proc")
    count = 0
    while True:
        count += 1
        try:
            mycursor.execute("insert into dummytable" + session2 + "  select * from dummytable" + session2)
            print("Iteration: " + str(count))
            
        except Exception as e:
            print('Something really bad happened: ' + str(e))
            if 'is full' in str(e):
                count += gemino(mycursor)
                return count
            if 'No space left on device' in str(e):
                return count

if __name__ =="__main__":
    try:
        endpoint = 'dm1pr2tvyl75put.cnygdr2psqor.us-east-1.rds.amazonaws.com'
        username = 'Admin'
        password = 'Passw0rd'

        session = str(random.randrange(1111, 9999))
        mydb = mysql.connector.connect(host=endpoint, user=username, passwd=password)
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE dummydb" + session)
        mycursor.execute("use dummydb" + session)
        
        execresponse = gemino(mycursor)
        print("Total operations : " + str(execresponse))

    except Exception as e:
        print('Something really bad happened: ' + str(e))