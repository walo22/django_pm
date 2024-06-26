from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL # لاستخدام خواص اليوزر 
from django.utils.translation import gettext as _

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

#تحويل نيم لسلسه نصيه 
    def __str__(self):
        return self.name


    class Meta :
        verbose_name = _('Category')
        verbose_name_plural = _('Category')
    

#تصريح عن الحالات 
class ProjectStatus(models.IntegerChoices): #عباره عن صنف او نمودج مساعد لتمثيل حاجه المشروع
    PENDING = 1, _('Pending') #قيد التنفيد
    COMPLETED = 2,_('Completed') #
    POSTPONED = 3, _('Postponed') # موجل 
    CANCELED= 4, _('Canceled') # ملغى


class Project(models.Model):
    title = models.CharField(max_length=255) #العنوان 
    description = models.TextField()          #الوصف 
    status = models.IntegerField(     #يعبر عن الحاله 
        choices=ProjectStatus.choices,
        default=ProjectStatus.PENDING
    )
    created_at= models.DateTimeField(auto_now_add=True)   #تاريخ البدء
    updated_at=models.DateTimeField(auto_now=True)        #تحديث التاريخ 
    category = models.ForeignKey(Category, on_delete=models.PROTECT) #تحديد العلاقات بين التصنيفات مع المشروع 
    user = models.ForeignKey(    #تحديد العلاقات بين النمودج والمشروع 
        AUTH_USER_MODEL,
        on_delete=models.CASCADE ,   #لحدف مشاريع المتخدم عند الحدف
        null=True
     )

#تحويل العنوان لسلسه نصيه 
    def __str__(self):
        return self.title
    


    class Meta :
        verbose_name = _('Project')
        verbose_name_plural = _('Project')
    

class Task(models.Model):
    description =models.TextField()
    is_completed = models.BooleanField(default=False) # المهمه ادا اكتمل او لا 
    project = models.ForeignKey(Project, on_delete=models.CASCADE) #تحديد العلاقات 
     
    def __str__(self) :
        return self.description
    


    class Meta :
        verbose_name = _('Task')
        verbose_name_plural = _('Task')