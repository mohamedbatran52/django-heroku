from django.shortcuts import render
# Create your views here.

posts = [ 
    {
        'author': 'Batran',
        'title' : 'First Post',
        'content': 'First post content',
        'date_posted': 'August 27th, 2018'
    }, 
    
    {
        'author': 'Batran',
        'title' : 'Second Post',
        'content': 'Second post content',
        'date_posted': 'August 28th, 2018'
    },
    
    {
        'author': 'Batran',
        'title' : 'Third Post',
        'content': 'Third post content',
        'date_posted': 'August 29th, 2018'
    }
]


def home(request):
    context = {
    'posts' : posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
    