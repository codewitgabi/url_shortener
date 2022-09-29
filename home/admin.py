from django.contrib import admin
from .models import Link


class LinkAdmin(admin.ModelAdmin):
	list_display = ["url", "uuid"]
	search_fields = ["url"]

admin.site.register(Link, LinkAdmin)