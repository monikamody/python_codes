#!/root/Desktop/python
import os
'''
menu
'''



print "press 1:to check current date and time"
print "press 2:to create a file"
print "press 3:to create directory"
print "press 4:to search something on google"
print "press 5:logout system"
print "press 6:shutdown OS"
print "press 7:to check internet cnnection"
print "press 8:to login whatsapp in browser"
print "press 9:to check all connected IP in your network"

choice=raw_input("enter your choice")
if int(choice)==1:
	os.system('date')
elif int(choice)==2:
	name=raw_input("enter the file name")
	os.system('touch name.txt')
elif int(choice)==3:
	named=raw_input("enter the name of directory")
	os.system('mkdir named')
elif int(choice)==4:
	os.system('firefox')
elif int(choice)==7:
	os.system('netstat')
elif int(choice)==8:
	os.system('firefox web.whatsapp.com')
elif int(choice)==9:
	os.system('ifconfig')
elif int(choice)==6:
	os.system('shutdown -h now')
elif int(choice)==5:
	os.system('pkill -KILL -u root')
else:
	print "invalid choice"

	




