from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext,Context, Template
from forex.models import DocumentCSV
from forex.forms import DocumentForm
import csv # first we need import necessary lib:csv
def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def redir(request):
    thefile = open('StockPrice_HTML.data', 'r')
    return HttpResponse(thefile)

def home(request):
    data=None
    a=[]
    b=[]
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = DocumentCSV(docfile = request.FILES['docfile'])
            #newdoc#.save()
            file = request.FILES['docfile']
            #file.seek(0)
            #data = file.read()
            data=csv.reader(file,delimiter=' ', quotechar='|')
#now the testReader is an array,so we can iterate it
            for row in data:
                a.insert(0,[row[0].split(",")[0]+row[0].split(",")[1],float(row[0].split(",")[2]),float(row[0].split(",")[3]),float(row[0].split(",")[4]),float(row[0].split(",")[5]),float(row[0].split(",")[6]),0.2])
                b.insert(0,[row[0].split(",")[0]+row[0].split(",")[1],float(row[0].split(",")[2]),float(row[0].split(",")[3]),float(row[0].split(",")[4]),float(row[0].split(",")[5]),float(row[0].split(",")[6]),0.2])
            c=[0]*len(a)
            m=8
            for i in range(len(a)-m):
                for j in range(len(b)-m):
            	    flag=1
                    for k in range(0,m):
			if(abs(abs(a[i+k][4]-a[i+k][1])-abs(b[j+k][4]-b[j+k][1]))>0.0005):
			    flag=0
                    if(flag):
			c[i]=c[i]+1
            #d=[0]*len(a)
	    for i in range(len(a)-m):
		flag=1
		for k in range(0,m):
			if(abs(abs(a[i+k][4]-a[i+k][1])-abs(a[c.index(max(c))+k][4]-a[c.index(max(c))+k][1]))>0.0005):
				flag=0
		if(flag):
			for z in range(0,m):
				a[i+z][6]=1
	    print a
	    data=a
	    thefile = open('StockPrice_HTML.data', 'w')
            thefile.write("[")
	    for item in a:
                thefile.write("%s,\n" % item)
            thefile.write("]")
            # Redirect to the document list after POST
            #return HttpResponseRedirect(reverse('myapp.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form
        
    return render_to_response('index.html',{'form': form,'data':data},context_instance=RequestContext(request))
    #return HttpResponse("Hello, world. You're at the poll index.")
# Create your views here.
