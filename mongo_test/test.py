from readfile import readfile
from getfakedata import getfakedata
import random

if __name__ == '__main__':
	tag_list = readfile.readtext("tags")
	num = random.randint(1,20)
	tags = getfakedata.gettags(tag_list,num)
	print (tags)
