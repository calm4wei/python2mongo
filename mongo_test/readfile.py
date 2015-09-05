
class readfile(object):
	
	@staticmethod
        def readtext(filename,folder="fakedata/"):
                f = open(folder+filename,"r")
                lines = f.readlines()
                f.close()
                l = []
                for line in lines:
			# print (line)
			l.append(line.rstrip())
		return l
		
