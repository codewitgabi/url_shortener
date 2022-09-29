from django.shortcuts import render, redirect
from .models import Link
from django.http import JsonResponse, HttpResponse
import json
import uuid


def home(request):
	if request.method == "POST":
		url = request.POST.get("url")
		uid = str(uuid.uuid4())[:5]

		link, created = Link.objects.get_or_create(url= url)
		
		if not link.uuid:
			link.uuid = uid	
		link.save()
		
		context = {"link": link}
		return render(request, "home.html", context)
	return render(request, "home.html")


def browse(request, id):
	link = Link.objects.get(uuid= id)
	return redirect(link.url)