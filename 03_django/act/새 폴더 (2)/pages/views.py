from django.shortcuts import render

# Create your views here.
def number(request):
    return render(request, 'number.html')

def result(request):
    number = request.GET.get('number')
    context = {'number': number,}
    return render(request, 'result.html', context)
    
