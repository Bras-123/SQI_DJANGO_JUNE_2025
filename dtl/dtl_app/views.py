from django.shortcuts import render

# Create your views here.
def practice_dtl(request):
    context = {
        'username': 'bras1234',
        'no_of_messages' : 5,
        'messages': ['hello', 'free to chat?', 'when can we talk?'],
        'is_logged_in' : True,
    }
    return render(request, 'dtl/practice-dtl.html', context)