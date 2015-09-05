from readfile import readfile
from getfakedata import getfakedata 
import pymongo

if __name__ == '__main__':
	conn = pymongo.Connection('192.168.1.160',27017)
	db = conn.mydb
	coll = db.tag_cid
	list_tag = readfile.readtext("tags")
	
	for i in range(20):
		tag = getfakedata.getindexdata(list_tag,i)
		cid = getfakedata.getcid()
		cids = getfakedata.getcids(100000)
                coll.insert({"tag":tag,"cids":cids})
		print (tag)
		print (cids)
		#print (tag)
		#print (getfakedata.getcids(10))
	
	pass
