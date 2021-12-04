from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.authentication import TokenAuthentication

from django.contrib.auth.models import User

@api_view(['GET', 'POST'])
# @permission_classes([AllowAny,])
def firstAPI(request):
    if request.method=="POST":
        name = request.data['name']
        age = request.data['age']
        return Response({'name': name, 'age': age})
    context={
        'name': 'Imran Hossain',
        'university': 'DIU'
    }
    return Response(context)


@api_view(['POST',])
def registerAPI(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if User.objects.filter(username = username).exists():
            return Response({'error': 'This usernamne is already exists!'})
        elif password1 != password2:
            return Response({'error':"Both password didn't match!"})

        user = User(
            username = username,
            first_name = first_name,
            last_name = last_name,
            email = email
        )
        user.set_password(password1)
        user.save()
        return Response({'success': 'Registration successfull'})
