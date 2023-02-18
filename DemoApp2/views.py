from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def f3(request):

    ss = '''
    
        <center>
            <h1> hello from demoapp1 f3() </h1>
        </center>
    
    '''
    
    return HttpResponse(ss)
    
def f4(request):

    ss = '''
    
        <center>
            <h1> hello from demoapp1 f4() </h1>
        </center>
    
    '''
    
    return HttpResponse(ss)
