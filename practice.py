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
count = 
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


#tkinter
import Tkinter as Tk
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








