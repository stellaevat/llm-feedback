from django.shortcuts import render

def homepage(request):
    context_dir = {'platform_name': 'Feedback Loop'}
    return render(request, 'app/homepage.html', context=context_dir)

def about(request):
    return render(request, 'app/about.html', context={})