#! /usr/bin/env python3

''' Test program:

Description of behavior:
The program should keep status and tstamp column in the
"test" db "test" table in mysql database updated.
It also checks request column for the STOP command.

Requirements:
It assumes there is MySQL database present on "localhost" with "root" user
and "1234" password (it can be changed in settings below).
The database "test" with table "test" with columns "request", "status"
and "timestamp" should be present in database.
The module "pymysql" should be installed 
(https://github.com/PyMySQL/PyMySQL).

More details about instalation and database settings: install.txt
'''


import pymysql
from time import sleep

#database settings
db_host  = 'localhost'
db_user  = 'root'
db_pass  = '1234'
db_name  = 'test'
db_table = 'test'

def main():
    ''' Open table and read request and set timestamp (periodically) while request is not STOP '''
    #connect to db
    conn = pymysql.connect(host=db_host,user=db_user,passwd=db_pass)
    conn.autocommit(True)
    cur = conn.cursor()

    #first write
    cur.execute('''UPDATE {}.{} SET request='', status='STARTING', tstamp=current_timestamp;'''.format(db_name,db_table))

    while True:

        #read test table
        cur.execute('SELECT * FROM {}.{}'.format(db_name,db_table))
        testdb = cur.fetchall()[0]

        #check if stop request .. if not, update timestamp
        if testdb[0]=='STOP':
            #say 'stopped' and break the loop
            cur.execute('''UPDATE {}.{} SET request='', status='STOPPED';'''.format(db_name,db_table))
            break
        else:
            #say 'running' and update timestamp
            cur.execute('''UPDATE {}.{} SET status='RUNNING', tstamp=current_timestamp;'''.format(db_name,db_table))

        #wait a while
        sleep(5)

    #close db
    cur.close()
    conn.close()

#run main if this is stand alone module
if __name__ == "__main__":
    main()
