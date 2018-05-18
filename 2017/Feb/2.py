import os

userid = 'caseym@taxbot.com'
password = 'Brandontaxbot11'
account = "610472"
types = " Sales "
vendor = " 85333504 "
command = " getFinancialReport" + vendor + "US 2016 01"



x = os.system("python reporter.py -u " + userid + " -P " + password + " -a " + account + command)
