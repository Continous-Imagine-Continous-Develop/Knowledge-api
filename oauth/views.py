from django.shortcuts import render

# Create your views here.
def logout(request):
    return 'logout success'

def index(request):
    context = {}

    return render(request, 'oauth/index.html', context)

