from django.contrib import admin

from snippets.models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    list_display = ("name", "is_html", "is_active", "changed_on")
    list_filter = ("is_html", "is_active",)
    readonly_fields = ( "created_on", "changed_on", "last_user")
    fields = ("name", "content", "is_html", "is_active",)
    
    def save_model(self, request, obj, form, change):
        obj.last_user = request.user
        obj.save()


admin.site.register(Snippet, SnippetAdmin)
    
    
