from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import views

schema_view = get_schema_view(
    openapi.Info(
        title="Contacts Book API",
        default_version='v1',
        description="All the contacts details available",
        contact=openapi.Contact(email="saqiba@sqcodes.com"),
        license=openapi.License(name="SQ License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    
)

def documentation(request):
    pass



urlpatterns = [
    path('', views.home, name="home"),
    path('documentation', views.documentation,name="documentation"),
    path('contact', views.contact,name="contact"),
    path('blog', views.blog,name="blog"),
    path('register', views.register,name="register"),
    path('login', views.signin,name="signin"),
    path('api', views.api,name="api"),
    path('logout', views.signout,name="signout"),
    path('contact_delete/<int:id>/', views.delete_contact, name="delete_contact"),
    path('contacts/', views.post_contact, name="post_contact"),
    path('contacts_all/', views.list_contacts, name="list_contacts"),
    path('contact_get/<int:id>/', views.get_contact, name="get_contact"),
    path('contact_edit/<int:id>/', views.update_contact, name="update_contact"),
    
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('openapi.json', schema_view.without_ui(cache_timeout=0), name='schema-json')

]


# urlpatterns = [
#     path('', views.home, name="home"),
#     path('contacts', views.post_contact, name="post_contact"),
#     path('contacts_all', views.list_contacts, name="list_contacts"),
#     path('contact_get/<int:id>', views.get_contact, name="get_contact"),
#     path('contact_edit/<int:id>', views.update_contact, name="update_contact"),
#     path('contact_delete/<int:id>', views.delete_contact, name="delete_contact"),
# ]
