from django.shortcuts import render
from .models import BlogPost, BlogCategory
# Create your views here.
def blog(request):
	template_name = "blog.html"
	blogs = BlogPost.objects.all() #queryset
	category = BlogCategory.objects.all()
	context = {'blogs':blogs,'category':category}
	return render(request, template_name, context)

def blogdetails(request, id):
	category = BlogCategory.objects.all()
	return render(request, "blog-post.html", {'blog':BlogPost.objects.get(pk=id),'cat':category})

def blogcategories(request, id):
	category = BlogCategory.objects.all()
	blogcat = BlogCategory.objects.get(id=id)
	return render(request, 'blog.html', {'blogs':blogcat.cat.all()		,'category':category })
	