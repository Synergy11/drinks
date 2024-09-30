from django.http import JsonResponse
from .models import Drinks, User
from .serializers import DrinkSerializer,UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def drink_list(request):
    # get all drinks
    if request.method == 'GET':
        drinks = Drinks.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        return JsonResponse({'drinks':serializer.data})
    
    if request.method == 'POST':
        serializer = DrinkSerializer( data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
@api_view(['GET','PUT','DELETE'])
def drink_detail(request, id):

    try:
      drink= Drinks.objects.get(pk=id)
    except Drinks.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serilalizer = DrinkSerializer(drink)
        return Response(serilalizer.data)
    
    elif request.method == 'PUT':
        serilalizer = DrinkSerializer(drink, data= request.data)
        if serilalizer.is_valid():
            serilalizer.save()
            return Response(serilalizer.data)
        return Response(serilalizer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET','POST'])
def user_list(request):
    if request.method == 'GET':
       user= User.objects.all()
       userSerializer = UserSerializer(user , many = True)
       return Response({'USER DATA':userSerializer.data})

    if request.method == 'POST':
        userSerializer = UserSerializer(data= request.data)
        if userSerializer.is_valid():
            userSerializer.save()
            return Response(status= status.HTTP_201_CREATED)
        return Response(status= status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['GET','PUT','DELETE'])
def user_detail(request, id):
    try:
        user = User.objects.get(pk=id)
    except User.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method =='GET':
        userSerializer=UserSerializer(user)
        return Response(userSerializer.data)
    
    elif request.method == 'PUT':
        update_user=UserSerializer(user, data = request.data)
        if update_user.is_valid():
            update_user.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)
