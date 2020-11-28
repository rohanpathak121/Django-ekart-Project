from django.http import HttpResponse
from django.shortcuts import render
import datetime

def about_page(request):
  context={

    'msg':'About Us',
    'bdy':'We are data science Student'

  }
  return render(request,"home.html",context)


def contact_us(request):
  context1={

    'msg':'contact Us',
    'bddy':'807929290'

  }
  return render(request,"home.html",context1)  

def home_page(request):
  h=datetime.datetime.now().hour
  if h<12 and h>=4:
    msg="Good Morning...!"
  elif h>=12 and h<=16:
    msg="Good Afternoon..." 
  elif h>=17 and h<=21:
    msg="Good Evening...!"
  else:
    msg="Go to sleep"

       
  return render(request,"home.html",{'msg':msg} )


def home_page4(request):
    return render(request,"home.html")    

def home_page3(request):
    _html="""<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">

    <title>Hello, world!</title>
  </head>
  <body>
    <i><h1 class="text-center">Hello, world!</h1></i>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
  </body>
</html>"""
    return HttpResponse(_html)


def home_page2(request):
    return HttpResponse("<i><h1>Hello World</h1></i>")

def home_page1(request):
    return HttpResponse("Hello World")    
    
