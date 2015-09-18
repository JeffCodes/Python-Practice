# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:27:21 2015

@author: BergemJE
"""
import string

f = open("G:\Python\katrina_advisory\katrina_advisory.txt")
text = f.read()
f.close()

#1
text = text.lower()

#2
sum(map(text.count, ("killed","destroyed","death",'devastating')))

#3


is_urgent = text.startswith('urgent')

#4
#remove puntuation
replace_punctuation = string.maketrans(string.punctuation, ' '*len(string.punctuation))
text = text.translate(replace_punctuation)
tlist = text.split()
#remove other non-words
words = [x for x in tlist if x.isalpha()]
ratio =round((sum(map(text.count, ("killed","destroyed","death",'devastating'))))/float(len(tlist)),3)




