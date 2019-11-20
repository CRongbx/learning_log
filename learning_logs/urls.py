"""定义learning_logs的URL模式"""

from django.urls import path	
from . import views		# . 表示当前的urls.py模块所在的文件夹

app_name='learning_logs'	#防止报错：'learning_logs' is not a registered namespace
urlpatterns = [
	#主页
	path('',views.index, name='index'),	#从起始到末尾查找字符串中是否有URL

	#显示所有的topics
	path('topics/', views.topics, name='topics'),

	#显示所有主题的详细条目
	path("topics/<topic_id>/", views.topic, name='topic'),
	#将topic_id作为该主题对应的URL

	#用于添加新主题的网页
	path("new_topic/", views.new_topic, name='new_topic'),

	#用于添加新条目的网页
	path("new_entry/<topic_id>/", views.new_entry, name='new_entry'),

	#用于编辑条目的网页
	path("edit_entry/<entry_id>/", views.edit_entry, name='edit_entry'),
]	
#这里注意是列表[]而不是{}，这样会报错：'set' object is not reversible
