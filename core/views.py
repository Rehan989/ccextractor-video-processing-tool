from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import tasks
from django.core.files.storage import default_storage
import re

# Create your views here.
def index(request):
    if request.method == "GET":
        context = {}
        return render(request, "index.html", context=context)
    elif request.method == "POST":
        videoFile = request.FILES['file']
        filename = default_storage.save(videoFile.name, videoFile)
        tasks.processFile.delay(filename)
    
        return HttpResponseRedirect(f'/search?filename={filename}')
    
def search(request):
    if request.method == "GET":
        keyword = request.GET.get('keyword')

        filename = request.GET.get('filename')
        timestamp = ""
        if(keyword):
            filename = f"{filename.split('.')[0]}.srt"
            line_number = 0

            with open(filename, 'r') as file:

                for line in file:
                    line_number += 1
                    pattern = re.compile(keyword.lower())
                    matches = re.findall(pattern, line.lower())
                    if matches:
                        line_number
                        break
            
            timestamp = line_number-4
            line_number = 0
            with open(filename, 'r') as file:

                for line in file:
                    line_number += 1

                    if(line_number==timestamp):

                        pattern = re.compile('-->')
                        matches = re.findall(pattern, line.lower())
                        if matches:
                            timestamp = line
                            print(line_number)
                            break
                        
                        timestamp += 1
            
            timestamp = timestamp.split(',')[0]

        return render(request, "search.html", context={'filename':filename, 'timestamp':timestamp, 'keyword':keyword})

# @csrf_exempt
# def uploadFile(request):
#     # print(request.FILES)
#     # 
#     print(request.POST)
    