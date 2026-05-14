from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def homePage(req):

  now = datetime.now()
  html = f"<h1>Current Date and Time (Server): {now}</h1>"

  return HttpResponse(html)