from django.shortcuts import render

# Create your views here.

def hello_world(request):

    if request.method == 'POST':
        temp = request.POST.get('hello_world_input')
        hello_world_new = HelloWorld()

    return render(request,'accountapp/hello.html')

