# import subprocess

from django.http import HttpResponse
from django.shortcuts import render
from insertion import DatabaseOperations
from django.utils.datastructures import MultiValueDictKeyError

def getfile(request):

    return Log_Analysis(request)


def Log_Analysis(request):

    return render(request, 'html/Log_Analysis.html')



def Graph_analysis(request):

    return render(request, 'html/Graph_analysis.html')


def Log_options(request):

    return render(request, 'html/Log_options.html')


def Insert_mongodb(request):
    inputValue = ''
    if request.method == "POST":
        try:

            inputValue = request.POST['myvalue']
            db_ops = DatabaseOperations()
            db_ops.db_connect()
            filespath = db_ops.db_filepaths(inputValue)
            print(filespath)
            for paths in filespath:
                try:
                    inputValue = inputValue + ('/') + paths
                    print(inputValue)
                    insert_str, f_name = db_ops.file_content(inputValue.replace('\\', '/'))
                    print('Inserted into Database: ' + str( db_ops.db_insert(insert_str, f_name)))
                    split_string = inputValue.split("/", 1)
                    inputValue = split_string[0]

                except Exception as e:

                    print('Error: {}.\nFile path not found.'.format(e))

            return HttpResponse("inserted into mongoDB")

        except MultiValueDictKeyError:
            inputValue = False
    return render(request, 'html/Insert_mongodb.html')
