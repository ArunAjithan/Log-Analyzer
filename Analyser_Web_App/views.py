from django.shortcuts import render


# Create your views here.
def getfile(request):

    return Log_Analysis(request)



def Log_Analysis(request):

    return render(request, 'html/Log_Analysis.html')



def Graph_analysis(request):

    return render(request, 'html/Graph_analysis.html')


def Log_options(request):

    return render(request, 'html/Log_options.html')