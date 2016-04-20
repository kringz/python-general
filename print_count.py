#!/usr/bin/python
#
#
#
## Original code by Stephen Krings
#
#
#
#import subprocess

import urllib2
import re
import os

#dot38 = urllib2.urlopen('http://10.10.221.38/sys_count.html')

copier_lh = urllib2.urlopen('http://10.10.240.10/sys_count.html')
copier_wc2 = urllib2.urlopen('http://10.10.230.30/machine_status.html')
copier_wc1 = urllib2.urlopen('http://10.10.230.31/machine_status.html')
copier_wc3 = urllib2.urlopen('http://10.10.230.175/machine_status.html')
copier_rw1 = urllib2.urlopen('http://10.11.210.39/sys_count.html')
copier_hw1 = urllib2.urlopen('http://10.10.9.137/sys_count.html')
copier_hw2 = urllib2.urlopen('http://10.10.9.136/sys_count.html')


page_content0 = copier_wc3.read()
page_content1 = copier_lh.read()
page_content2 = copier_wc2.read()
page_content3 = copier_wc1.read()
page_content4 = copier_rw1.read()
page_content5 = copier_hw1.read()
page_content6 = copier_hw2.read()




###############
#### 23686 ####
###############


with open ('page_content0.html', 'w') as fid:
        fid.write(page_content0)

fp = open('page_content0.html')
print "#####################################"
print "ID: 23686, 10.10.240.175, (Walnut Creek)"
print "#####################################"
print ""
for i, line in enumerate(fp):
        if i == 82:
#                print "Total Count"
                line = re.sub(r'<h2[^>]*>', '', line)
#               line = re.sub(r'[/<>td]', '', line)
                print line.strip()
                print ""







###############
#### 85030594  ####
###############


with open ('page_content1.html', 'w') as fid:
        fid.write(page_content1)

fp = open('page_content1.html')
print "#####################################"
print "ID: 85030594, 10.10.240.10, (Laguna Hills)"
print "#####################################"
print ""
for i, line in enumerate(fp):
        if i == 133:
                print "Black & White"
                line = re.sub(r'[/<>td]', '', line)
                print line.strip()
                print ""
        if i == 136:
                print "Full Color"
                line = re.sub(r'[/<>td]', '', line)
                print line.strip()
                print ""

	

###############
#### 20951 ####
###############

with open ('page_content2.html', 'w') as fid:
        fid.write(page_content2)

fp = open('page_content2.html')
print "#####################################"
print "ID: 20951, 10.10.230.30, AR-M455N (Walnut Creek)"
print "#####################################"
print ""
for i, line in enumerate(fp):
        if i == 86:
#                print "Total Count"
                line = re.sub(r'<h2[^>]*>', '', line)
#               line = re.sub(r'[/<>td]', '', line)
                print line.strip()
                print ""



###############
#### 24409 ####
###############

with open ('page_content3.html', 'w') as fid:
        fid.write(page_content3)

fp = open('page_content3.html')
print "#####################################"
print "ID: 24409, 10.10.230.31, MX-M550U (Walnut Creek)"
print "#####################################"
print ""
for i, line in enumerate(fp):
        if i == 82:
#                print "Total Count"
		line = re.sub(r'<h2[^>]*>', '', line)
#               line = re.sub(r'[/<>td]', '', line)
                print line.strip()
                print ""

###############
#### 23145 ####
###############

with open ('page_content4.html', 'w') as fid:
        fid.write(page_content4)

fp = open('page_content4.html')
print "#####################################"
print "ID: 23145, 10.11.210.39, Exec (Redwood)"
print "#####################################"
print ""
for i, line in enumerate(fp):
        if i == 133:
                print "Black & White"
                line = re.sub(r'[/<>td]', '', line)
                print line.strip()
                print ""
        if i == 137:
                print "Full Color"
                line = re.sub(r'[/<>td]', '', line)
                print line.strip()
                print ""


###############
### 24971 #####
###############

with open ('page_content5.html', 'w') as fid:
        fid.write(page_content5)

fp = open('page_content5.html')
print "#####################################"
print "ID: 24971, 10.10.9.137, HQ (Howard Rear)"
print "#####################################"
print ""
for i, line in enumerate(fp):
        if i == 133:
                print "Black & White"
                line = re.sub(r'[/<>td]', '', line)
                print line.strip()
                print ""
        if i == 137:
                print "Full Color"
                line = re.sub(r'[/<>td]', '', line)
                print line.strip()
                print ""
	



#		print "Total Count"
#                line = re.sub(r'[:!TCs/totalcount-]', '', line)
#                line = line.replace("<h2>", "")
#                line = line.replace("< >", "")
#                print line.strip()
#		print ""
#		print "#####################################"

###############
#### 24619 ####
###############

with open ('page_content6.html', 'w') as fid:
        fid.write(page_content6)

fp = open('page_content6.html')
print "#####################################"
print "ID: 24619, 10.10.9.136, Corp (Howard Front)"
print "#####################################"
print ""
for i, line in enumerate(fp):
        if i == 136:
                print "Black & White"
                line = re.sub(r'[/<>td]', '', line)
                print line.strip()
                print ""
        if i == 139:
                print "Full Color"
                line = re.sub(r'[/<>td]', '', line)
                print line.strip()
                print ""

		
os.remove("./page_content0.html")
os.remove("./page_content1.html")
os.remove("./page_content2.html")
os.remove("./page_content3.html")
os.remove("./page_content4.html")
os.remove("./page_content5.html")
os.remove("./page_content6.html")

