from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
# Create your views here.



class Register_user(APIView):


     def post(self,request):
          serializers = Userserializer(data = request.data)

          if not serializers.is_valid():
               return Response({'status': 403, 'errors': serializers.errors, 'message': 'some went wrong'})
          serializers.save()

          user = User.objects.get(username = serializers.data['username'])
          token_obj , _ = Token.objects.get_or_create(user=user)

          return Response({'status': 200, 'payload':serializers. data,'token': str(token_obj),'message': 'you set'})














class Facebookapi(APIView):


     def get(self,request):
          student_obj = Facebook.objects.all()
          serializer = FacebookSerializers(student_obj, many=True)
          return Response({'status': 200, 'payload': serializer.data})


     def post(self,request):
          data=request.data
          if request.data ['age'] < 18:
               return Response({'status':403 , 'message':'age must be 18'})
          serializers=FacebookSerializers(data=request.data)

          if not serializers.is_valid():
               print(serializers.errors)
               return Response({'status':403,'errors':serializers.errors,'message':'some went wrong'})
          serializers.save()
          return Response({'status':200,'payload':data,'message':'you set'})




     def put(self,request):
               try:
                    student_obj=Facebook.objects.get(id = request.data['id'])
                    serializers = FacebookSerializers(student_obj,data=request.data)

                    if not serializers.is_valid():
                         print(serializers.errors)
                         return Response({'status': '403', 'errors': serializers.errors, 'message': 'some went wrong'})
                    serializers.save()
                    return Response({'status': '200', 'payload':serializers.data, 'message': 'you set'})
               except Exception as e:
                    print(e)
                    return Response({'status':'403','message':'invalid id'})





     def delete(self,request):
          try:
               id = request.GET.get('id')
               students_obj=Facebook.objects.get(id=id)
               students_obj.delete()
               return Response({'status:200',})
          except Exception as e:
               print(e)
               return  Response({'status':403,'message':'invalid id'})
























# @api_view(['GET'])
# def home(request):
#      student_obj=Facebook.objects.all()
#      serializer=FacebookSerializers(student_obj,many=True)
#      return Response({'status':200,'payload':serializer.data})
#
#
# @api_view(['POST'])
# def student_post(request):
#      data=request.data
#      if request.data ['age'] < 18:
#           return Response({'status':403 , 'message':'age must be 18'})
#      serializers=FacebookSerializers(data=request.data)
#
#      if not serializers.is_valid():
#           print(serializers.errors)
#           return Response({'status':403,'errors':serializers.errors,'message':'some went wrong'})
#      serializers.save()
#      return Response({'status':200,'payload':data,'message':'you set'})
#
#
# @api_view(['PUT'])
# def update_post(request,id):
#      try:
#           student_obj=Facebook.objects.get(id = id)
#           serializers = FacebookSerializers(student_obj,data=request.data)
#
#           if not serializers.is_valid():
#                print(serializers.errors)
#                return Response({'status': 403, 'errors': serializers.errors, 'message': 'some went wrong'})
#           serializers.save()
#           return Response({'status': 200, 'payload':serializers.data, 'message': 'you set'})
#      except Exception as e:
#           return Response({'status':'403','message':'invalid id'})
#
#
#
#
# @api_view(['DELETE'])
# def delete_post(request,id):
#      try:
#           students_obj=Facebook.objects.get(id=id)
#           students_obj.delete()
#           return Response({'status:200',})
#      except Exception as e:
#           print(e)
#           return  Response({'status':403,'message':'invalid id'})
