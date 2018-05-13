#!/usr/bin/env python
#Vicent Dolz & Radosvet Desislavov Georgiev
import os

from whoosh.index import create_in
from whoosh.fields import Schema, ID, TEXT

schema = Schema(  #shema for index
    title=TEXT(stored=True),
    idGlobal=ID(stored=True),
    idLocal=ID(stored=True),
    content=TEXT)
idir = "index_dir"
dir = 'january'
dict = "dictIndex.dat"

f = open(dict, 'w')
countGlobal = 0
fileList = [f.name for f in os.scandir(dir) if f.is_file()]

if not os.path.exists(idir):
	os.mkdir(idir)

ix = create_in(idir, schema)
writer = ix.writer()
dictIndex = {}

for i in fileList:  #file list loop
	r = dir + '/' + str(i)
	fi = open(r, 'r')
	text = fi.read()
	splitText = text.split('<DOC>')
	countLocal = 0
	
	for j in splitText:
		writer.add_document(
		    title=i,
		    idGlobal=str(countGlobal),
		    idLocal=str(countLocal),
		    content=j)
		dictIndex[countGlobal] = j
		countGlobal += 1
		countLocal += 1
writer.commit()
f.write(str(dictIndex))
f.close()
print('Indexing done.')
