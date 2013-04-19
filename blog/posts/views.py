from django.shortcuts import render_to_response
from django.http import Http404
from posts.models import Post
 
def home(request):
	return render_to_response("home.html",{
		"posts" : Post.objects.all().order_by('post_date')
	})
 
def post_specific(request, post_id):
	try:
		p = Post.objects.get(pk=post_id)
	except:
		raise Http404
 
	return render_to_response("post_specific.html",{
		"post" : p
	})
