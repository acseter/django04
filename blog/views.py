from django.shortcuts import render, render_to_response, get_object_or_404,render
from django.core.paginator import Paginator
from .models import Blog, BlogType


# Create your views here.
def blog_list(request):

    blog_all_list = Blog.objects.all()
    paginator = Paginator(blog_all_list,4)
    page_num = request.GET.get('page',1)
    page_of_blogs = paginator.get_page(page_num)
    context = {}
    context['page_of_blogs'] = page_of_blogs
    context['blog_type'] = Blog.objects.all().count()


    # context = {}
    # context['blogs'] = Blog.objects.all()
    # context['blog_count'] = Blog.objects.all().count()

    return render_to_response('blog_list.html',context)


#
# def blog_detail(request,blog_pk):
#     context = {}
#     context['blog'] = get_object_or_404(Blog, pk=blog_pk)
#     return render_to_response('blog_detail.html',context)


def blog_detail(request,blog_pk):


    context = {}
    context['blog'] = get_object_or_404(Blog, pk = blog_pk)
    context['blog'].readed_num+=1
    context['blog'].save()
    context['user']=request.user

    # response = render_to_response('blog_detail.html',context)
    response = render(request,'blog_detail.html',context)
    return response

# def blogs_with_type(request,blog_type_pk):
#     context = {}
#     blog_type = get_object_or_404(BlogType,pk=blog_type_pk)
#     context['blogs'] = Blog.objects.filter(blog_type=blog_type)
#     context['blog_type']=blog_type
#     return render_to_response('blog_with_type.html',context)
#
def blogs_with_type(request,blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType,pk= blog_type_pk)
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_type']=blog_type
    return render_to_response('blog_with_type.html',context)

