from django.shortcuts import render,HttpResponse

# Create your views here.

def book_list(request):
    return HttpResponse("""
    <ul>
        <li>History Maker</li>
        <li>Mistborn: The Final Empire</li>
        <li>This Thing Called Purpose</li>
        <li>The Secret</li>
        <li>The Way of Kings</li>
    </ul>
    """)
    

def special_books(request):
     return HttpResponse("""
    <div>
        <h3>Featured Books of the Month</h3>
        <ul>
            <li>Project Hail Mary</li>
            <li>The Three-Body Problem</li>
        </ul>
    </div>
    """)
   