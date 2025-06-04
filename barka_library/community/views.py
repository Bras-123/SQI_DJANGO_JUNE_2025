from django.shortcuts import render,HttpResponse

# Create your views here.

def community_events(request):
    return HttpResponse("""
    <section>
        <h2>Upcoming Community Events</h2>
        <p><strong>June 15, 2025:</strong> Summer Reading Challenge Kick-off Party</p>
        <p><strong>July 22, 2025:</strong> Author Q&A with Nnedi Okorafor</p>
    </section>
    """)
    