from django.db import models

# Create your models here.
class UserInfo(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=32,verbose_name='用户名')
    pwd=models.CharField(max_length=32,verbose_name='密码')

    def __str__(self):
        return self.name

class Music(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=32,default='MilkMusic')
    path=models.FileField(upload_to='music/')
    user=models.ForeignKey(to='UserInfo',to_field='id',related_name='music')

    def __str__(self):
        return self.name

class Book(models.Model):

    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=32,default='MilkBook')
    path=models.FileField(upload_to='book/')
    user=models.ForeignKey(to='UserInfo',to_field='id',related_name='book')

    def __str__(self):
        return self.name

class Movie(models.Model):

    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=32,default='MilkMovie')
    path=models.FileField(upload_to='movie/')
    user=models.ForeignKey(to='UserInfo',to_field='id',related_name='movie')

    def __str__(self):
        return self.name

class CollectionMusic(models.Model):

    id=models.AutoField(primary_key=True)
    music=models.ForeignKey(to='Music',to_field='id',related_name='collection_music')
    user=models.ForeignKey(to='UserInfo',to_field='id',related_name='collection_music')

    def __str__(self):
        return self.music.name+'-'+self.user.name


class CollectionBook(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(to='Book', to_field='id', related_name='collection_book')
    user = models.ForeignKey(to='UserInfo', to_field='id', related_name='collection_book')

    def __str__(self):
        return self.book.name+'-'+self.user.name


class CollectionMovie(models.Model):
    id = models.AutoField(primary_key=True)
    movie = models.ForeignKey(to='Movie', to_field='id', related_name='collection_movie')
    user = models.ForeignKey(to='UserInfo', to_field='id', related_name='collection_movie')

    def __str__(self):
        return self.movie.name + '-' + self.user.name


class Token(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(to='UserInfo',to_field='id',related_name='token')
    token_msg=models.CharField(max_length=32,verbose_name='携带token')

    def __str__(self):
        return self.user.name+':'+self.token_msg