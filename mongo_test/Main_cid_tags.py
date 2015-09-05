from readfile import readfile
from getfakedata import getfakedata 
import pymongo
import random
import json

class MainTagIds(object):

	conn = pymongo.Connection('192.168.1.160',27017)
	db = conn.mydb
	tag_cid = db.tag_cid
	tag_id = db.tag_id
	
	def gettagids(self,list,obj):
		tagids = []
		for tag in list:
			data = obj.tag_id.find({"tag":tag},{"_id":1})
			print ("==========")
			print (data)
			in_json = json.dumps(data)
			print ("-----------")
			print (in_json)
			id = json.loads(in_json)["_id"]
			tagids.append(id.rstrip())
			print ("id=" + id + ",tagids=" + tagids)
		return tagids	
		
		

if __name__ == '__main__':
	obj = MainTagIds()
	list_tag = readfile.readtext("tags")
	list_appkey = readfile.readtext("android_appkey.txt")
	
	for i in range(10000000):
		tagids = []
		num = random.randint(0,41)
		tags = getfakedata.gettags(list_tag,num)
		cid = getfakedata.getcid()
		deviceid = getfakedata.getdeviceid()
		appkey = getfakedata.getappkey(list_appkey)
                obj.tag_cid.save({"tags":tags,"cid":cid,"appkey":appkey,"deviceid":deviceid})
		#tagids = obj.gettagids(tags,obj)
		#print (appkey)
		#print (deviceid)
		#print (tags)
		print (cid)
		#print (tag)
		#print (getfakedata.getcids(10))
	
	pass
