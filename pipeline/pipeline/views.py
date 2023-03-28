from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def Home(request):
    djtext = request.POST.get('text','default')
    RemovePunc = request.POST.get('RemovePunctuation','off')
    UpperCaseBtn =  request.POST.get('uppercase','off')
    newlineRemover = request.POST.get('newLineRemover','off')
    removespace = request.POST.get('spaceRemover','off')
    

   
    if RemovePunc == "on":
        analyzed_text = " "
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

        for char in djtext:
            if char not in punctuation:
                analyzed_text = analyzed_text +char
        params= {'analyzed_text':analyzed_text,'purpose':'Remove Punctuation'} 
        djtext = analyzed_text       

        
    if UpperCaseBtn == "on":
        analyzed_text = " "
    
        for char in djtext:
            analyzed_text=analyzed_text+char.upper()
        params= {'analyzed_text':analyzed_text,'purpose':'Changed to upper Case'}
        djtext = analyzed_text

    if newlineRemover == "on":
        analyzed_text = " "

        for char in djtext:
            if char!= "\n":
                analyzed_text=analyzed_text+char
        params= {'analyzed_text':analyzed_text,'purpose':'Remove NewLine'}
        djtext = analyzed_text

    if removespace == "on":
        analyzed_text = " "
        for index,char in enumerate(djtext):
            if djtext[index] == " " and djtext=="  ":
                pass
            else:
                analyzed_text = analyzed_text + char
        params= {'analyzed_text':analyzed_text,'purpose':'Remove space'}
        djtext = analyzed_text
        
    if RemovePunc == "off" and UpperCaseBtn == "off" and newlineRemover == "off" and removespace == "off" :
        return HttpResponse("<a href='/'>Error</a>")
    
    return render(request,'analyze.html',params)