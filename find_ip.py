import time
import commands

print "finding connected ip"

time.sleep(2)

print commands.getoutput("arp -a | cut -d'(' -f2 | cut -d')' -f1")

