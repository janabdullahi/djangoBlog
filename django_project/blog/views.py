from django.shortcuts import render


# demo date

posts = [
    {
        'author' : 'hamed',
        'content' : 'first post 1',
        'title' : 'post content first',
        'date_posted' : 'August 27, 2018'
    },
    {
        'author' : 'jan',
        'content' : 'second post 2',
        'title' : 'post content second',
        'date_posted' : 'july 21, 2019'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
