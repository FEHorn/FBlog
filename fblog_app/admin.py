from django.contrib import admin

from fblog_app.models import GroupProfile, UserProfile, Post, Tag



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile



@admin.register(GroupProfile)
class GroupProfileAdmin(admin.ModelAdmin):
    model = GroupProfile



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = (
        "id",
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )

    list_filter = (
        "published",
        "publish_date",
    )

    list_editable = (
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )

    search_fields = (
        "title",
        "subtitle",
        "slug",
        "body",
    )

    prepopulated_fields = {
        "slug": (
            "title",
            "subtitle",
        )
    }

    date_hierarchy = "publish_date"
    save_on_top = True
