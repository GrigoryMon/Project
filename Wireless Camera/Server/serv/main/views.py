from django.shortcuts import render
from django.views import View
from django.http import Http404, HttpResponse, HttpResponseServerError,JsonResponse
from rest_framework.views import APIView
import json
from .models import Images, Camera, Userc

class MainRequest(APIView):

    def get(self, request):
        data= {'content':[]}
        imgs = Images.objects.all()
        if imgs:
            for img in imgs:
                data['content'].append({'user': img.user.telegram_id, 'image': img.image})
                Images.objects.all().delete()
        return JsonResponse(data)

    def post(self, request):
        json_data = json.loads(request.body)
        try:
            data = json_data['data']
            cam = Camera.objects.get(camera_id = data['camera'] )
            users = cam.user.all()
            for user in users:
                Images.objects.create( user = user , camera = cam, image = data['image'])
            return HttpResponse('ok')
        except KeyError:
            return HttpResponseServerError("Malformed data!")
        
class Register(APIView):

    def post(self, request):
        json_data = json.loads(request.body)
        try:
            data = json_data
            
            if list(data.keys())[0] == 'user':
                Userc.objects.create(telegram_id =data['user']['telegram_id'])
            elif list(data.keys())[0] == 'camera':
                Camera.objects.create(camera_id = data['camera']['camera_id'])
            return HttpResponse('ok')
        except KeyError:
            return HttpResponseServerError("Malformed data!")

class AddCamera(APIView):

    def post(self, request):
        json_data = json.loads(request.body)
        try:
            data = json_data['data']
            print(data)
            o = Camera.objects.get(camera_id = data['camera'])
            o.user.add(Userc.objects.get(telegram_id = data['user']))
            o.save()
            return HttpResponse('ok')
        except KeyError:
            return HttpResponseServerError("Malformed data!")

class Test(APIView):

    def get(self, request):
        data= {'content': 'ok'}
        return JsonResponse(data)

    def post(self, request):
        json_data = json.loads(request.body)
        try:
            data = json_data['data']
            print(data)
            return HttpResponse('ok')
        except KeyError:
            return HttpResponseServerError("Malformed data!")