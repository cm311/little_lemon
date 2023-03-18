from django.http import HttpResponse

#here is where you put error handlers

#override these
#def handler400
#def handler403
#def handler404
#def handler500

def handler404(request, exception):
    return HttpResponse('<h4>404 ya lunkhead!</h4>')