# -*- coding: utf-8 -*-


import json
# if you are using python 3, you should 
import urllib.request 
import urllib

#Additional code for taking queries from the query file
with open('/home/deboshree/testqueries.txt','r') as file_q:
	for line in file_q:
		query = line.replace(':', ' ').split(' ', 1)
		print (query[0])
		print (query[1])

		query_args = {'q':query[1]}
		print (query_args)
		encoded_args = urllib.parse.urlencode(query_args)
		print (encoded_args)

		# change the url according to your own corename and query
		inurl = 'http://localhost:8983/solr/core-dfr/select?q='+encoded_args+'&fl=id%2Cscore&wt=json&indent=true&rows=20'
		print(inurl)
		outfn = '/home/deboshree/output_dfr.txt'


		# change query id and IRModel name accordingly
		qid = query[0]		
		IRModel='DFR'
		outf = open(outfn, 'a+')
		#data = urllib2.urlopen(inurl)
		# if you're using python 3, you should use
		data = urllib.request.urlopen(inurl)
		print (data)

		docs = json.load(data)['response']['docs']
		# the ranking should start from 1 and increase
		rank = 1
		for doc in docs:
		    outf.write(qid + ' ' + 'Q0' + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
		    rank += 1
		outf.close()
