from readfile import readfile
import pymongo

class init_tagid(object):

	conn = pymongo.Connection('192.168.1.160',27017)
	db = conn.mydb

	# exist some error
	def getNextSequence(name):
		ret = db.counters.findAndModify({query:{"_id":name},update:{'$inc':{seq:1}},new:true})
		return ret.seq

if __name__ == '__main__' :

	main = init_tagid()
	coll_tagid = main.db.tag_id
	list_tag = readfile.readtext("tags")
	
	for tag in list_tag:
		#print (main.getNextSequence(tag))	
		#coll_tagid.insert({"tag":tag,"_id":main.getNextSequence(tag)})
		coll_tagid.insert({"tag":tag})
