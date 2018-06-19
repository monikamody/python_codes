#commands in python
import commands
print "enter choice"
print "1.date"
print "2.calender"
value=raw_input("enter your choice")
if int(value)==1:
	value1 = commands.getoutput("date")
	print value1
elif int(value)==2:
	value2 = commands.getoutput("cal")
	print value2
else:
	print "wrong choice"

