from django.shortcuts import render

# Create your views here.
def logout(request):
    request.user = None
    return render(request, 'oauth/index.html')

def index(request):
    context = {}

    return render(request, 'oauth/index.html', context)

