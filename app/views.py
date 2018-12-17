from django.shortcuts import render,HttpResponse
import json
from app.models import *
import hashlib
import time

# Create your views here.
def index(request):
    if request.method=='GET':

        response=HttpResponse(json.dumps({'state':200,'msg':"2323","data":4545}))


        return response

def user(request):
    if request.method=='GET':
        token=request.GET.get('token')
        if token :
            user=UserInfo.objects.filter(token__token_msg=token).first()
            if user:
                music_obj_list=Music.objects.filter(user__id=user.id).all()
                movie_obj_list=Movie.objects.filter(user__id=user.id).all()
                book_obj_list=Book.objects.filter(user__id=user.id).all()
                music_list=[]
                movie_list=[]
                book_list=[]
                for item in music_obj_list:
                    music_list.append(item)
                for item in movie_obj_list:
                    movie_list.append(item)
                for item in book_obj_list:
                    book_list.append(item)
                return HttpResponse(json.dumps({'code':200,"music_list":music_list,
                                                'movie_list':movie_list,'book_list':book_list}))
            else:
                return HttpResponse(json.dumps({'code':202}))
        else:
            return HttpResponse(json.dumps({'code':201}))
def register(request):
    if request.method=='POST':
        data=json.loads(request.body)
        username=data.get('name')
        pwd=data.get('pwd')
        user=UserInfo.objects.create(name=username,pwd=pwd)
        md5=hashlib.md5()
        md5.update(username.encode('utf-8'))
        timer=time.time()
        md5.update(str(timer).encode('utf-8'))
        md5_msg=md5.hexdigest()
        token=Token.objects.create(user=user,token_msg=md5_msg)
        if token:
            return HttpResponse(json.dumps({'code':200,'token':token.token_msg,'username':user.name}))
        else:
            return HttpResponse(json.dumps({'code': 201}))
    elif request.method=='OPTIONS':
        return HttpResponse('1')


def login(request):
    if request.method=='POST':
        data=json.loads(request.body)
        username=data.get('name')
        pwd=data.get('pwd')
        user=UserInfo.objects.filter(name=username,pwd=pwd).first()
        if user:
            token_object=Token.objects.filter(user=user).first()
            if not token_object:
                md5 = hashlib.md5()
                md5.update(username.encode('utf-8'))
                timer = time.time()
                md5.update(str(timer).encode('utf-8'))
                md5_msg = md5.hexdigest()
                token_object = Token.objects.create(token_msg=md5_msg, user=user)
            return HttpResponse(json.dumps({'code':200,"token":token_object.token_msg,'username':token_object.user.name}))
    if request.method=='OPTIONS':
        return HttpResponse('1')
def logout(request):
    if request.method=='GET':
        token=request.GET.get('token')
        Token.objects.filter(token_msg=token).delete()
        token=Token.objects.filter(token_msg=token).first()
        if not token:
             return HttpResponse(json.dumps({'code':200}))
        else:
            return HttpResponse(json.dumps({'code':201}))


def music(request):
    if request.method=='GET':
        token = request.GET.get('token')
        if not token:
            return HttpResponse(json.dumps({'code':201}))
        user = UserInfo.objects.filter(token__token_msg=token).first()
        music_object_list=Music.objects.filter(user=user).all()
        collection_object_list=CollectionMusic.objects.filter(user=user).all()
        MyMusicList=[]
        CollectionMusicList=[]
        for item in music_object_list:
            music_object={}
            music_object['path']=str(item.path)
            music_object['name']=item.name
            music_object['user']=item.user.name
            print(music_object)
            MyMusicList.append(music_object)
        for item in collection_object_list:
            collection_object = {}
            collection_object['path'] = str(item.music.path)
            collection_object['name'] = item.music.name
            collection_object['user'] = item.user.name
            CollectionMusicList.append(collection_object)
            print(collection_object)
        return HttpResponse(json.dumps({'code':200,'MyMusicList':MyMusicList,'CollectionMusicList':CollectionMusicList}))




