# -*- coding: utf-8 -*-
"""
Created on Tue Jul 07 11:27:05 2015

@author: BergemJE
"""


#Pandas
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)


def by_three(x):
    return x % 3 == 0

for x in my_list:
    print by_three(x)
    
import pandas as pd
import pylab
import inspect

#Import an excel sheet. pd.read_csv is for csvs
animals = pd.read_excel('I:\Training\STATA Training\STATA Training 2013\Practice Data\practicedata.xlsx')
animals
animals['animal']
animals[3:9]
#.ix is used for slicing by row and column is has both label based and positional based access
animals.ix[3:9, ['animal', 'delicious']]
animals.ix[3:9, 0:4]

animals.iloc[:,1:]



animals['animal']=='cat'
cats = animals[animals['animal']=='cat']
cats


animals[1:]
#Delete row 0
animals = animals[1:]
animals.head()
#delete dogs .loc is label based access
animals = animals.loc[animals['animal']!='dog']
#Delete column 5 .iloc is positional based access
animals = animals.iloc[:, :5]
#or
animals.drop(['Unnamed: 5'], axis=1, inplace=True)
#Or
#del df.ColumnName
#Or
animals.drop(animals.columns[[5]], axis=1, inplace=True)

#Two ways to drop columns 3 and 4
animals.drop(animals.columns[[3,4]], axis=1, inplace=True)
animals.drop(animals.columns[[range(3,5)]], axis=1, inplace=True)

animals.drop_duplicates(['animal', 'leg_num'])



#come back to this
#Create list, add as columns (cbind) (rbind is append)
count = DataFrame(data=count, index=index)

animals = pd.concat([animals,count], axis = 1)

#Create column
animals['perLeg'] = animals['price']/animals['leg_num']


#Boolean mask for nulls
animals.isnull()

#List column names
list(animals.columns.values)
animals.columns
#rename column either of the below
animals = animals.rename(columns={'price':'dollars', 'delicious':'isTasty'})
animals.rename(columns={'price':'dollars', 'delicious':'isTasty'}, inplace=True)




#describe
animals.describe()

#sort
animals.sort('leg_num')
animals.sort('leg_num', ascending = False)
animals.sort(['leg_num', 'sub_animal'], ascending = [False, True])



moods = pd.read_excel('G:\Python\practicemerge.xlsx')
a1 = animals[0:8]
a2 = animals[8:]
combinethis = [a1, a2]
#These four lines do the same thing, append to data frames
animals2 = pd.concat([a1, a2], axis = 0)
animals2 = pd.concat(combinethis)
animals2 = pd.concat([a1, a2], axis = 0, ignore_index=True)
animals2 = a1.append(a2)

#Merging
animalmoods = pd.merge(animals, moods, how='outer', on='animal' )


#
byanimal = animals.groupby('animal')
byanimal['price'].describe()


#tkinter
import Tkinter as Tk
from Tkinter import *
#from Tkinter import *  #This would make it so you don't have to start a bunch of stuff with Tk.

root = Tk.Tk()

w = Tk.Label(root, text="Hello, world!")
w.pack()

root.mainloop()

###
"""
class App:

    def __init__(self, master):

        frame = Tk.Frame(master)
        frame.pack()

        self.button = Tk.Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=Tk.LEFT)

        self.hi_there = Tk.Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=Tk.LEFT)

    def say_hi(self):
        print "hi there, everyone!"
"""



root = Tk.Tk()

app = App(root)

root.mainloop()
root.destroy()



a = raw_input('Choose a number: ')
a
print a


def callback():
    print "clicked!"

b = Button(text="click me", command=callback)
b.pack()

mainloop()


def addup():
    num1 = raw_input('Choose a number: ')
    num2 = raw_input('Choose another number: ')
    print float(num1) + float(num2)

b = Button(text="Calculate", command=addup)
b.pack()

mainloop()


addup()


root = Tk.Tk()
root.title("Calculator")
root.geometry("500x500")
w = Tk.Frame(root)
w.pack()
button1 = Tk.Button(w, text = "Calculate", command = addup())
button1.pack()

root.mainloop()
root.destroy()




def button(master):
    frame = Tk.Frame(master)
    frame.pack()
    w.button = Tk.Button(frame, text="QUIT", fg="red", command=frame.quit            )
    w.button.pack(side=Tk.LEFT)


####Dates
import datetime as dt

####Grab a wikipedia table
from bs4 import BeautifulSoup
import urllib2
from urllib2 import urlopen

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")


site= "https://en.wikipedia.org/wiki/List_of_sovereign_states"
hdr = {'User-Agent': 'Firefox/35.0;DOJ3jx7bf'}
req = urllib2.Request(site,headers=hdr)
soup = make_soup(site)

area = ""
district = ""
town = ""
county = ""

table = soup.find("table", { "class" : "sortable wikitable" })
print table

for row in table.findAll("tr"):
    cells = row.findAll("td")


#<table class="sortable wikitable" style="background:white; text-align:left;">
d = [[1,2,3],[4,5,6]]
d[1][1]







#################################
def damerau_levenshtein_distance(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in xrange(-1,lenstr1+1):
        d[(i,-1)] = i+1
    for j in xrange(-1,lenstr2+1):
        d[(-1,j)] = j+1
 
    for i in xrange(lenstr1):
        for j in xrange(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i,j)] = min(
                           d[(i-1,j)] + 1, # deletion
                           d[(i,j-1)] + 1, # insertion
                           d[(i-1,j-1)] + cost, # substitution
                          )
            if i and j and s1[i]==s2[j-1] and s1[i-1] == s2[j]:
                d[(i,j)] = min (d[(i,j)], d[i-2,j-2] + cost) # transposition
 
    return d[lenstr1-1,lenstr2-1]
    

damerau_levenshtein_distance("Cat", "Catching")

a = ['sit','orange','taco']
b = ['oatmeal','ORanfge','taceo']
close = []
for x in a:
    for y in b:
        if damerau_levenshtein_distance(x.upper(),y.upper())<=2:
            close.append([x,y,damerau_levenshtein_distance(x,y)])
close        


#Python for Data Science notes
#List available variables
%whos
#Deletes variables from namespace
%reset
#Delete one variable from namespace
a = 630
del a #del also works for deleting an element from a list
#Displays a log
%hist
#Join is the opposite of split
a = "What a wacky adventure"
wd_lst = a.split()
mysep = '-'
b = mysep.join(wd_lst)
#Adding Line Breaks
print """hello
world"""
print "hello\nworld"
#A few string functions
a = 'Mercury, Venus, Earth, Mars'
#Replace
a = a.replace('Earth','Home')
#Upper
a = a.upper()
#Remove Whitespace
a = a + "     \n\n"
a = a.strip()
#Replacement fields
a = '{0} are writing {1}'
a.format('we', 'code')
a = '{zero} are writing {one}'
a.format(one='we', zero='code')
#List comprehension
x = [1,2,3]
x = [y+1 for y in x]
x[-3:-1]
#Does it contain?
a = [1,2,3,4,5]
13 in a
13 not in a
#A few more list things
a.append(5) #Add a five
a.count(5) #How many fives?
a.extend([5,4,3]) #add three numbers to a list, not add one element which is a list
a.index(3) #First occurence of
a.insert(5,22) #Insert the number 22 so that is becomes index 5
a.pop(5) #Remove element at index 5 and return it
a.remove(3) #Remove the first occurence of the number 3.
a.sort() #This sorts the list. You Do not need a = a.sort()
a.reverse() #Reverse order of the list
#Strings are immutable, unlike lists, so to add something to the middle of a string...
s = 'kjfojs'
s = s[:1] + ' abcd ' + s[1:]
#Tuples are also immutable
a = (3,4,5)
list(a) #convert to list
#A few dictionary things
a = {'food':'carrot', 'drink':'water','shelter':'house'}
b = {'food':'half-carrot', 'companion':'dog'}
a.update(b) #Update a dictionary with another dictionary
#Reference part of a dictionary by key.
a.get('food', 'none') # Second argument is return value if key does not exist
a['food']
c = a.pop('companion') #pop works here too
a.keys() #List keys
a.values() #List values
a.items() #List of key value pairs as tuples






def quad(a,b,c):
    x = (-b + (b**2 - 4*a*c)**(0.5))/(2*a)
    return x

quad(-1,3,5)


#Download a file
import urllib
testfile = urllib.URLopener()
testfile.retrieve("http://fmwww.bc.edu/repec/bocode/l/labmask.ado", "C:\ADO\labmask.ado")
testfile.retrieve("http://fmwww.bc.edu/repec/bocode/l/labmask.hlp", "C:\ADO\labmask.hlp")

