from readfile import readfile
from getfakedata import getfakedata 
import pymongo
import random

if __name__ == '__main__':
	conn = pymongo.Connection('192.168.1.160',27017)
	db = conn.mydb
	coll = db.tag_cid
	list_tag = readfile.readtext("tags")
	
	for i in range(10000000):
		num = random.randint(1,20)
		tags = getfakedata.gettags(list_tag,num)
		cid = getfakedata.getcid()
		#cids = getfakedata.getcids(100000)
                coll.insert({"tags":tags,"cid":cid})
		print (tags)
		print (cid)
		#print (tag)
		#print (getfakedata.getcids(10))
	
	pass
