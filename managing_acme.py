# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 11:47:28 2015

@author: BergemJE
"""
#1
employee_emails = ["Wile.E.Coyote@acme.com", 
"Looney.Tunes@acme.com", 
"Chuck.Jones@acme.com", 
"Road.Runner@acme.com", 
"Michael.Maltese@acme.com",
"Speedy.Gonzales@acme.com",
"Calamity.Coyote@acme.com",
"Bugs.Bunny@texavery.com"]

employee_ids = range(0, len(employee_emails))

#2
employee_emails.append("Acceleratti.Incredibilis@acme.com")
employee_ids = range(0, len(employee_emails))

#3
employee_emails[2:6]

#4
employee_emails[::2]

#5
employee_emails[1:6:2]

#6
employee_emails.remove(employee_emails[1])
employee_ids.remove(employee_ids[1])

#7
locations = ["Taos", "Phoenix", "Santa Fe", "Flagstaff"]
locations.reverse()

#8
locations = locations[::-1]