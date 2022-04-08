from django.shortcuts import render

# This is the views file on test-branch
# Create your views here.
def index(request):
    return render(request, 'pages/index.html')