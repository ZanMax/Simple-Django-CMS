from django.contrib import admin
from .models import Post, PostStatuses, PostTypes, Author

admin.site.site_header = "CMS Admin"
admin.site.site_title = "CMS Admin"
admin.site.index_title = "Welcome to CMS"


class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'url', 'text', 'date',
              'post_modified', 'post_type', 'status')
    prepopulated_fields = {"url": ("title",)}
    readonly_fields = ("post_modified",)
    list_filter = ("author", "post_type", "status",)
    list_display = ("title", "date", "author",)


class AuthorAdmin(admin.ModelAdmin):
    list_filter = ("articles_count", "experience",)
    list_display = ("first_name", "last_name", "articles_count", "experience",)


admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)
