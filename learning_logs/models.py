from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
	""""用户记录的主题"""
	#主题名
	text = models.CharField(max_length=200)	#CharField用于指明该属性要在数据库预留多少空间
	#创建时间
	date_added = models.DateTimeField(auto_now_add=True)	#auto_now_add=True表示每创建一个新主题，Django会自动将该属性设置为当前系统的时间
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):
		#返回模型的字符串表示
		return self.text


class Entry(models.Model):
	"""每个主题下的记录条目"""
	topic = models.ForeignKey('Topic',on_delete=models.CASCADE)	#设置外键
	text = models.TextField()	#每条记录下的文本内容无长度限制
	date_added = models.DateTimeField(auto_now_add=True)

	class Meta:
		"""存储用于管理模型的额外信息，让Django在需要时使用entries在表示多个记录(而不是Entrys)"""
		verbose_name_plural = 'entries'

	def __str__(self):
		#返回模型的字符串表示(只显示前50个字符)
		return self.text[:50]+"..."	#...表示显示的非整个条目
