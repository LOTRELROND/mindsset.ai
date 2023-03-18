from django.contrib import admin
from .models import Post,FavItem,Visiter
# Register your models here.
# admin.site.register(Post),
admin.site.register(FavItem),
admin.site.register(Visiter),

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display=['title', 'date', 'active']

    search_fields = ['title']

    list_filter = ['date']

    class Meta:
        model = Post
