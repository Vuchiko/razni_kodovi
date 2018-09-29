from django.shortcuts import render
from django.http import HttpResponse

posts = [

{
  'author':'Vukoje',
  'title':'Post#1',
  'content':'Post broj 1, kao test',
  'date_posted':'September 15, 2018',
},
{
  'author':'Maroje',
  'title':'Post#2',
  'content':'Post broj 2, jos jedan test text',
  'date_posted':'September 16, 2018',
}


]

def home(request):
	context = {
	    'posts': posts 
	}

	return render(request, 'blog_vuk/home.html', context)

def about(request):
	return render(request, 'blog_vuk/about.html', {'title': 'About'})