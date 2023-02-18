from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def f1(request):

    ss = '''
    
        <center>
            <h1> ***hello from demoapp1 f1()*** </h1>
        </center>
    
    '''
    
    return HttpResponse(ss)
    
def f2(request):

    ss = '''
    
        <center>
            <h1> hello from demoapp1 f2() </h1>
        </center>
    
    '''
    
    return HttpResponse(ss)
