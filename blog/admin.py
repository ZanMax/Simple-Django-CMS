from django.contrib import admin
from .models import Post, PostStatuses, PostTypes, Author, Tags
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.conf import settings


class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'url', 'text', 'date', 'post_modified',
              'read_time', 'post_type', 'status', "author", "tags", )
    prepopulated_fields = {"url": ("title",)}
    readonly_fields = ("post_modified",)
    list_filter = ("post_type", "status", "author")
    list_display = ("title", "date", "author", "status", )


class AuthorAdmin(admin.ModelAdmin):
    list_filter = ("articles_count", "experience",)
    list_display = ("first_name", "last_name", "articles_count", "experience",)


class PostStatusesAdmin(admin.ModelAdmin):
    pass


class PostTypesAdmin(admin.ModelAdmin):
    pass


class TagsAdmin(admin.ModelAdmin):
    pass


class MyAdminSite(admin.AdminSite):
    def get_app_list(self, request):
        #ordering = settings.ORDERING_APPS

        app_dict = self._build_app_dict(request)

        app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

        """
        for app in app_list:
            app['models'].sort(key=lambda x: ordering[x['name']])
        print(app_dict)
        """
        return app_list


mysite = MyAdminSite()
admin.site = mysite


admin.site.site_header = "CMS Admin"
admin.site.site_title = "CMS Admin"
admin.site.index_title = "Welcome to CMS"

admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)

admin.site.register(PostStatuses)
admin.site.register(PostTypes)
admin.site.register(Tags)

admin.site.register(Group, GroupAdmin)
admin.site.register(User, UserAdmin)
