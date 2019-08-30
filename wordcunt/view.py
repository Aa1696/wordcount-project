
from django.http import HttpResponse
from django.shortcuts import render
import operator
def homePage(request):

	return render(request,'home.html')


def count(request):
	fulltext = request.GET['fulltext']

	wordlist = fulltext.split()

	worddictionary = {}

	for word in wordlist:
		if word in worddictionary:
			worddictionary[word]  += 1

		else:

			worddictionary[word] = 1

	Sortedwords = sorted (worddictionary.items() , key = operator.itemgetter(1) , reverse = True)


	return render(request,'count.html',{'fulltext':fulltext ,'count':len (wordlist) , 'Sortedwords':Sortedwords})

def home1(request):

	return render( request,'home1.html')
	