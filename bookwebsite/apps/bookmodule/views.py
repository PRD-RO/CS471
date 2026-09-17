from django.shortcuts import render
from django.http import HttpResponse


def index(request):
  name = request.GET.get("name") or "World"
  return render(request, "bookmodule/index.html", {"name":name})



def index2(request, val1=0):
  try:
        val1 = int(val1)
        return HttpResponse(f"value1 = {val1}")
  except ValueError:
        return HttpResponse("error,expected val1 to be integer", status=400)