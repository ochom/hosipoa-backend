from django.contrib import admin

# Register your models here.
from accounts.models import User, Group
from bugs.models import Replies, Bug
from common.models import Organization


class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone', 'organization']


class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'organization']


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['organization_name', 'physical_address', 'email', 'phone']


class RepliesInline(admin.TabularInline):
    model = Replies
    exclude = ('updated_by',)


class BugAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status', 'replies']
    inlines = [RepliesInline]
    exclude = ('updated_by',)

    def status(self, obj):
        return 'Resolved' if obj.is_resolved else 'Pending'

    def replies(self, obj):
        return obj.replies.count()


admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Bug, BugAdmin)
