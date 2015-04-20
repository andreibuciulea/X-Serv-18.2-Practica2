from django.shortcuts import render
from models import datos
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt


formulario = "<html><body><form method=post>\
       URL: <input type=text name=fname><br>\
       <input type=submit value=Submit>\
       </form></body></html>"

@csrf_exempt
def form(request):

    lista = datos.objects.all()
    salida = ""
    for fila in lista:
        salida += "<br>"
        salida += str(fila.id) + "-----" + fila.acortada + "-----" + fila.url
        salida += "<br/>"
    formulario = "<html><body><form method=post>\
       URL: <input type=text name=fname><br>\
       <input type=submit value=Submit>\
       </form>" + salida + "</body></html>"
    
    if request.method == "GET":
        return HttpResponse(formulario)
    elif request.method == "POST":
        acortada = request.body.split("=")[1]

        try:
            esta = datos.objects.get(acortada = acortada)
            return HttpResponse(formulario)
        except datos.DoesNotExist:
            acortada = request.body.split("=")[1]
            comienzo = acortada.split("//")[0]
            if comienzo == "http:" or comienzo == "https:":
                numero = 1
                direccion = datos(acortada = acortada,url = acortada)
                direccion.save()
                return HttpResponse(formulario)
            else:
                url = "http://" + acortada
                numero = 1
                direccion = datos(acortada = acortada,url = url)
                direccion.save() 
                return HttpResponse(formulario)
      

def acortar(request,recurso):

    try:
        fila = datos.objects.get(id=recurso)
        #salida = str(fila.id) + " " + str(fila.numero) + " " + fila.acortada + " " + fila.url
        salida = "<html><head><META http-equiv=refresh\
                 content=1;URL=" + fila.url + "></head></html>\r\n"   
        return HttpResponse(salida)
    except:
        return HttpResponseNotFound("Not Found")
