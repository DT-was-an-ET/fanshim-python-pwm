# Standard library imports
from subprocess import call as subprocess_call
from utility import fileexists
from time import sleep as time_sleep
from datetime import datetime

mount_try = 1
not_yet = True
done = False
start_time = datetime.now()
if fileexists("/home/rpi4-sftp/usb/drive_present.txt"):
	when_usba = 0
else:
	when_usba = -1
if fileexists("/home/duck-sftp/usb/drive_present.txt"):
	when_usbb = 0
else:
	when_usbb = -1
if fileexists("/home/pi/mycloud/drive_present.txt"):
	when_mycloud = 0
else:
	when_mycloud = -1

while (mount_try < 30) and not_yet:
	try:
		usba_mounted = fileexists("/home/rpi4-sftp/usb/drive_present.txt")
		usbb_mounted = fileexists("/home/duck-sftp/usb/drive_present.txt")
		mycloud_mounted = fileexists("/home/pi/mycloud/drive_present.txt")
		if not(usba_mounted and usbb_mounted and mycloud_mounted):
			print("Something Needs mounting this is try number: ", mount_try)
			subprocess_call(["sudo", "mount", "-a"])
			mount_try += 1
		usba_mounted_after = fileexists("/home/rpi4-sftp/usb/drive_present.txt")
		usbb_mounted_after = fileexists("/home/duck-sftp/usb/drive_present.txt")
		mycloud_mounted_after = fileexists("/home/pi/mycloud/drive_present.txt")
		if not(usba_mounted) and usba_mounted_after:
			when_usba = round((datetime.now() - start_time).total_seconds(),2)
		if not(usbb_mounted) and usbb_mounted_after:
			when_usbb = round((datetime.now() - start_time).total_seconds(),2)
		if not(mycloud_mounted) and mycloud_mounted_after:
			when_mycloud = round((datetime.now() - start_time).total_seconds(),2)
		if usba_mounted_after and usbb_mounted_after and mycloud_mounted_after:
			print("Success at :",when_usba,when_usbb,when_mycloud, " secs from start")
			not_yet = False
			done = True
	except:
		print("Count: ", count,"  error")
	time_sleep(1)

if done:
	print("Great!")
else:
	print("Failed to do all or drive_present.txt file not present; Times :",when_usba,when_usbb,when_mycloud)
while True:
	time_sleep(20000)
