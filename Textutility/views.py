from django.http import HttpResponse
from django.shortcuts import render

def first(request):
    return render(request,'index.html')

def AboutUs(request):
    return render(request,'testing.html')

def help(request):
    return render(request,'help.html')

def analyze(request):
    get_text=request.POST.get('text','default')
    get_option=request.POST.get('optradio','default')

    if get_option=='removepunc':
        punclist=set([".",";",":","!","?","/","\\",",","#","@","$","&",")","(","\""])
        result=''
        for i in get_text:
            if i not in punclist:
                result+=i

    elif get_option=='remwhitespace':
        result=str(get_text[0])
        for i in range(1,len(get_text)):
            if get_text[i]!=' ':
                result+=get_text[i]
            else:
                if get_text[i-1]!=' ':
                    result+=get_text[i]
        print(result)


    elif get_option=='lower':
        result=get_text.lower()

    elif get_option=='upper':
        result=get_text.upper()

    mydict={'alpha':result}
    return render(request,'xerox.html',mydict)