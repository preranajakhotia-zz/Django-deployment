from django.shortcuts import render

# Create your views here.
def index(request):
	context = {'text':'Hello stupid!', 'number':100}
	return render(request, 'basic_app/index.html',context)


def others(request):
	return render(request, 'basic_app/others.html')


def relative(request):
	return render(request, 'basic_app/relative_url_template.html')