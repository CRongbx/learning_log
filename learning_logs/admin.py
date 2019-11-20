from django.contrib import admin

# Register your models here.
#导入要注册的模型Topic
from learning_logs.models import Topic,Entry
#让Django通过管理网站管理模型

class TopicAdmin(admin.ModelAdmin):
	#需要显示的字段信息
	list_display = ('id','text')

class EntryAdmin(admin.ModelAdmin):
	list_display = ('id','text')


admin.site.register(Topic,TopicAdmin)
admin.site.register(Entry,EntryAdmin)


