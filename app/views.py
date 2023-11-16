from django.shortcuts import render

# Create your views here.
def data_render(request):
    date='This data is our assumption'
    d={"assumption":date}

    return render(request,'data_render.html',context=d)

def login(request):
    d={"username":"manju","age":15}
    return render(request,'login.html',context=d)


