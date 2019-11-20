"""定义面向用户的表单格式化"""

from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text' : ''}		#不要为text生成标签


class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['text']
		labels = {'text' : ''}
		widgets = {'text': forms.Textarea(attrs={'cols': 80})}		#设置HTML中部件大小
		