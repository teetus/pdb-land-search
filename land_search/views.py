from django.shortcuts import render

# Create your views here.
def land_search_view(request):
    context = {}
    return render(request,template_name='land_search/pages/land-search',context=context)
