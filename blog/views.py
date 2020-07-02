from django.shortcuts import render
from blog.models import *
from django.http import HttpResponse, HttpResponseRedirect


def blog(request):
    allpost = Blog.objects.all()
    blog_dict = {"allpost": allpost}
    return render(request, 'blog/blog.html', blog_dict)


def blogPost(request, slug):
    post = Blog.objects.filter(slug=slug)

    count = 0
    for c in post:
        count = count + 1

    if (count > 0):
        post = post.first()
        post_dict = {"slug": slug, "post": post}
        return render(request, 'blog/blogsingle.html', post_dict)
    else:
        return HttpResponse("404")
        