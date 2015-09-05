import random

class getfakedata(object):
	
	@staticmethod
	def getrandomdata(list):
		index = random.randint(0,len(list)-1)
		return list[index]
	
	@staticmethod
	def getindexdata(list,index):
		return list[index]

	@staticmethod
	def getcid():
		sysrand = random.SystemRandom()
		cid = str(sysrand.randint(100000000,999999999))
		return cid

	@staticmethod
	def getcids(num):
		cids = []
		#index = random.randint(1,100)
		for i in range(num):
			cids.append(getfakedata.getcid().rstrip())
		return cids
		
	@staticmethod
	def gettags(list,num):
		tags = []
		for i in range(num):
			index = random.randint(0,len(list)-1)
			tag = getfakedata.getindexdata(list,index)
			#print ("--" + tag)
			if tag in tags:
				continue
			#tags.append(getfakedata.getindexdata(list,i))
			tags.append(tag)
		return tags

	@staticmethod
	def getappkey(list):
		index = random.randint(0,len(list)-1)
		return list[index]

	@staticmethod
	def getdeviceid():
		sysrand = random.SystemRandom()
		deviceid = str(sysrand.randint(10000000000, 99999999999))
		return deviceid
	
