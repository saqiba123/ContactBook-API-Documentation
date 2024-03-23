from django.http import HttpResponse
from django.shortcuts import redirect, render
from .serializers import ContactSerializer
from .models import Contacts
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    show_logout_button = False  # Set to False for the home page
    return render(request, 'contacts/home.html', {'show_logout_button': show_logout_button})
    
def register(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        email = request.POST.get("email")
        pswd = request.POST.get("password")
        print(uname,email,pswd)
        myuser = User.objects.create_user(username=uname,email=email,password=pswd)
        myuser.save()

        return redirect("signin") 

    return render(request, "contacts/register.html")
   

def signin(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        pwd = request.POST.get("password")

        auth_user = authenticate(request, username = uname, password = pwd)
        if auth_user is not None:
            login(request,auth_user)
            return redirect("api")

    return render(request, "contacts/login.html")
  
@login_required(login_url="signin")
def api(request):
    show_logout_button = True  # Set to True for the API Web page
    return render(request, 'contacts/api_web.html', {'show_logout_button': show_logout_button})
 

def signout(request):
    logout(request)
    return redirect("home")


# # Create contact
@api_view(["POST"])
def post_contact(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# views.py
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .forms import ContactForm

# @api_view(['POST'])
# def add_record(request):
#     if request.method == 'POST':
#         form = YourModelForm(request.data)
#         if form.is_valid():
#             form.save()
#             return Response({'message': 'Record added successfully'}, status=201)
#         return Response(form.errors, status=400)



#Get all contacts
@api_view(["GET"])
def list_contacts(request):
    records = Contacts.objects.all()
    serializer = ContactSerializer(records, many =True)
    return Response(serializer.data)

#Get a contact
@api_view(["GET"])
def get_contact(request,id):
    try:
        records = Contacts.objects.get(pk=id)
    except:
        return Response({"message:Record Not Exist!"},status=status.HTTP_404_NOT_FOUND)
    
    serializer = ContactSerializer(records)
    return Response(serializer.data, status=status.HTTP_200_OK)


#Update a contact
@api_view(["PUT"])
def update_contact(request,id):
    try:
        records = Contacts.objects.get(pk=id)
    except:
        return Response({"message:Record Not Exist!"},status=status.HTTP_404_NOT_FOUND)
    
    serializer = ContactSerializer(records, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

#delete a contact
@api_view(["DELETE"])
def delete_contact(request,id):
    try:
        records = Contacts.objects.get(pk=id)
    except:
        return Response({"message:Record Not Exist!"},status=status.HTTP_404_NOT_FOUND)
    
    records.delete()
    
    return Response({"message":"Record deleted successfully!"}, status=status.HTTP_200_OK)



def documentation(request):
    pass

def contact(request):
    pass

def blog(request):
    pass

