import json
import uuid

from django.shortcuts import render, redirect, get_object_or_404
from .models import Link
from django.http import JsonResponse, HttpResponse


def home(request):
	""" URLShortener home page """
	link = ""
	if request.method == "POST":
		url = request.POST.get("url")
		uid = str(uuid.uuid4())[:5]

		link, created = Link.objects.get_or_create(url= url)
		
		if created:
			link.uuid = uid	
		link.save()
		
	context = {"link": link}
		
	return render(request, "home.html", context)


def browse(request, url_uuid):
	""" Gets and parses the given id and redirects the user to the original url """
	link = get_object_or_404(Link, uuid= url_uuid)
	
	return redirect(link.url)


def page_not_found(request, exception=None):
    """ Custom 404 page handler """
    return render(request, "404_page.html")

