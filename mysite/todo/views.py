from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.parsers import FileUploadParser
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
import csv
import codecs

from rest_framework import views

from .models import Todo

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()



from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

def handle_uploaded_file(f):
    count = 0
    reader = csv.DictReader(codecs.iterdecode(f, 'utf-8'), ["title", "description", "completed"])
    for row in reader:  
        #print(row['name'], row['completed'])
    #while True:
    #    count += 1
    
        # Get next line from file
    #    line = f.readline()
    
        # if line is empty
        # end of file is reached
        #if not line:
        #    break
        #print("Line{}: {}".format(count, line.decode("utf-8")))
        title = ""
        desc = ""
        completed = False
        if row["title"] != None:
            title = row["title"]
        if row["description"]  != None:
            desc = row["description"]
        
        if row["completed"]  != None and row['completed'].lower() in ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']:
            completed = True

        todoObject = Todo(title=title, description = desc, completed=completed)
        todoObject.save()

    """
        for chunk in read_in_chunks(f):
            lines  = map(lambda x: x.decode("utf-8").strip('\n'), f.readlines())
            for line in lines:
                print (line)
    """

@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        #form = UploadFileForm(request.POST, request.FILES)
        #if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            #return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return HttpResponse("OK")