from django.contrib import admin
from .models import  (Home,About,About_skills,Portfolio,Categories,Services,
                      Experience,Education,Clients,Resume_photo,Blog_posts,
                      Contact,Footer)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','update_date','read']
    list_filter = ['update_date','read']
    search_fields = ['name','email']
admin.site.register(About)
admin.site.register(About_skills)
admin.site.register(Portfolio)
admin.site.register(Categories)
admin.site.register(Services)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Clients)
admin.site.register(Resume_photo)
admin.site.register(Blog_posts)
admin.site.register(Contact,ContactAdmin)

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ("id", "is_published", "about_title", "contact_title")
    list_filter = ("is_published",)
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['name','job','is_active']
    list_editable = ('is_active',)