from django.shortcuts import render,HttpResponse

# Create your views here.
def gadgets_we_have(request):
    return HttpResponse(
        '''<ol><li>Television</li>
        <li>Refrigerator</li>
        <li>Washing machice</li>
        <li>Blender</li>'</ol>'''
        )