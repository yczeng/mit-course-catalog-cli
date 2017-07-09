import urllib
from lxml import etree
from pyquery import PyQuery as pq

def myprint(link, x):
	string = "li:eq("+str(x)+")"
	print(link(string).text())

def getMenu():
	link = pq("http://student.mit.edu/catalog/index.cgi")

	r = link("LI").each(lambda x: myprint(link, x))
	return

def getSubject(subject):
	url = "http://student.mit.edu/catalog/search.cgi?search=" + str(subject)
	link = pq(url)
	
	print(link("blockquote").text())
	return
