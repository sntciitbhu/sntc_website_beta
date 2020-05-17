from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .services import superuser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import GroupAdmin


import csv

adminUser = superuser()


class MyAdminSite(admin.AdminSite):

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path('students/',self.admin_view(self.student_view)),
            path('messages/',self.admin_view(self.messages_view)),

        ]
        return new_urls + urls
        print("geturls")

    def student_view(self,request):
        heads, vals = adminUser.allStudents()

        if(request.method == "GET"):
            if 'action' in request.GET:
                do = request.GET["action"]
                if do=="sort":
                    sortby = request.GET["sortby"]
                    i = heads.index(sortby)
                    print(i)
                    vals = sorted(vals, key=lambda x: x[i])

                elif do=="download":
                    sortby = request.GET["sortby"]
                    i = heads.index(sortby)
                    vals = sorted(vals, key=lambda x: x[i])

                    response = HttpResponse(content_type='text/csv')
                    response['Content-Disposition'] = 'attachment; filename="students.csv"'
                    writer = csv.writer(response)
                    writer.writerow(heads)
                    writer.writerows(vals)
                    return response

                else:
                    vals = sorted(vals, key=lambda x: x[0])
            else:
                vals = sorted(vals, key=lambda x: x[0])

                

        context = dict(
            self.each_context(request),
            data = vals,
            heads = heads,
        )
        return TemplateResponse(request, "admin/student.html", context)


    def messages_view(self,request):
        heads, vals = adminUser.allStudents()

        if(request.method == "GET"):
            if 'action' in request.GET:
                do = request.GET["action"]
                if do=="sort":
                    sortby = request.GET["sortby"]
                    i = heads.index(sortby)
                    print(i)
                    vals = sorted(vals, key=lambda x: x[i])

                elif do=="download":
                    sortby = request.GET["sortby"]
                    i = heads.index(sortby)
                    vals = sorted(vals, key=lambda x: x[i])

                    response = HttpResponse(content_type='text/csv')
                    response['Content-Disposition'] = 'attachment; filename="students.csv"'
                    writer = csv.writer(response)
                    writer.writerow(heads)
                    writer.writerows(vals)
                    return response

                else:
                    vals = sorted(vals, key=lambda x: x[0])
            else:
                vals = sorted(vals, key=lambda x: x[0])

                

        context = dict(
            self.each_context(request),
            data = vals,
            heads = heads,
        )
        return TemplateResponse(request, "admin/student.html", context)

    

admin.site = MyAdminSite(name = "admin")
admin.site.site_header = 'Office Bearer Portal'
admin.site.site_title = 'SNTC Administraion'
admin.site.index_title = 'Components'
admin.site.index_template = 'admin/sidebar.html'
admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)




from .models import Profile
admin.site.register(Profile)




