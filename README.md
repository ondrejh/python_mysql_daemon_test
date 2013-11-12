python_mysql_daemon_test
========================

Python3 script updating mysql database entry (using pymysql).
Converted to unix daemon (using python-daemon).


test.py: python mysql test scrip.
	Reads and updates mysql entry in infinite loop.
	
test_daemon.py: python unix daemon test.
	Runs test.py as unix daemon.

install.txt: instalation, setup and test notes