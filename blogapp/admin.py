from django.contrib import admin
from .models import Post, Aboutus, ContactUs
from django.contrib.auth import get_user_model
User = get_user_model()
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    # prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

class AboutusAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email','created_on')

admin.site.register(Post, PostAdmin)
admin.site.register(Aboutus, AboutusAdmin)
admin.site.register(User)
admin.site.register(ContactUs, ContactUsAdmin)