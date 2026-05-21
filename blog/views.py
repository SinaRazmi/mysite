from django.shortcuts import render

# Create your views here.
def blog_view(request):
    return render(request, 'blog/blog-home.html')


def blog_single(request):
    context = {'title':'Bitcoin crashed again', 'content':'bitcoint was flying but now grounded as always...' , 'author':'Sina Razmi'}
    return render(request, 'blog/blog-single.html', context)