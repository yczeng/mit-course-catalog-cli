import urllib
from lxml import etree
from pyquery import PyQuery as pq

def myprint(link, tag, x):
	string = tag+":eq("+str(x)+")"
	print(link(string).text())

def getMenu():
	link = pq("http://student.mit.edu/catalog/index.cgi")

	link("LI").each(lambda x: myprint(link, "li", x))
	return

def getSubject(subject):
	url = "http://student.mit.edu/catalog/search.cgi?search=" + str(subject)
	link = pq(url)
	link.xhtml_to_html()

	html = str(link)
	html = html.replace("<br />", "\n")

	if "Please try something more specific" in html:
		link("DT").each(lambda x: myprint(link, "a", x))

	else:
		link = pq(html)
		print(link("h3").text())
		print(link("blockquote").text())
	return