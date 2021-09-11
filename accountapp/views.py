from django.shortcuts import render

# Create your views here.
from accountapp.models import Helloworld


def hello_world(request):

    if request.method == 'POST':
        temp = request.POST.get('hello_world_input')
        hello_world_new = Helloworld()
        hello_world_new = temp
        hello_world_new.save()

        hello_world_list = Helloworld.objects.all()


        return render(request, 'accountapp/hello.html', context={'hello_world_list': hello_world_list});
    else:

        hello_world_list = Helloworld.objects.all()
        return render(request,'accountapp/hello.html',context={'hello_world_list': hello_world_list});

