#!/usr/bin/env python
#Vicent Dolz & Radosvet Desislavov Georgiev
import ast
import re
from whoosh.index import open_dir
from whoosh.qparser import QueryParser

# use ANDNOT to combine a word with a not one: valencia ANDNOT salenko
# use AND to combine search: "Los Angeles" AND Aeroflot
def cleanhtml(raw):
	cleanr = re.compile('<.*?>')
	cleantext = re.sub(cleanr, '', raw)
	return cleantext


fi2 = open('dictIndex.dat', 'r')
dic = ast.literal_eval(fi2.read())
ix = open_dir("index_dir")

with ix.searcher() as searcher:
	while True:
		text = input("\n\nsearcher:")
		if len(text) == 0:
			break
		query = QueryParser("content", ix.schema).parse(text)
		results = searcher.search(query, limit=None)
		#        print(dir(results))
		#        print(results.docs)
		idList = []
		for r in results:
			key = r['idGlobal']
			idList.append(cleanhtml(dic[int(key)]))
			print('file: '+r['title']+' \ndoc global ID: '+r['idGlobal']
			      +' \ndoc local ID: '+r['idLocal']+'\n\n')

		if len(results) < 4:
			for l in idList:
				print('\n\n')
				print(str(l))
