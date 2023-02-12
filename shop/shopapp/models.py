from django.db import models

from django.urls import reverse


def get_product_url(obj, viewname):
    # ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'slug': obj.slug})


# class Category(models.Model):
#
#     name = models.CharField(max_length=255, verbose_name='Категорія')
#     slug = models.SlugField(unique=True)
#
#     def __str__(self):
#         return self.name


class Product(models.Model):
    ENTRANCE_HOUSE_DOOR = 'Двері вхідні в будинок'
    ENTRANCE_APARTMENT_DOOR = 'Двері вхідні в квартиру'
    INTERIOR_DOOR = 'Міжкімнатні двері'
    FIRE_DOORS = 'Двері протипожежні'
    ENTRANCE_DOOR = "Двері в під'їзд"
    HIDDEN_INSTALLATION = 'Прихований монтаж'

    CHOICE_GROUP = {
        (ENTRANCE_HOUSE_DOOR, 'Двері вхідні в будинок'),
        (ENTRANCE_APARTMENT_DOOR, 'Двері вхідні в квартиру'),
        (INTERIOR_DOOR, 'Міжкімнатні двері'),
        (FIRE_DOORS, 'Двері протипожежні'),
        (ENTRANCE_DOOR, "Двері в під'їзд"),
        (HIDDEN_INSTALLATION, 'Прихований монтаж'),
    }

    #category = models.ForeignKey(Category, verbose_name='Категорія', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='Назва товару')
    slug = models.SlugField(unique=True)
    price = models.PositiveIntegerField(verbose_name='Ціна')
    availability = models.BooleanField(default=True, verbose_name='Наявність')
    group = models.CharField(max_length=40, choices=CHOICE_GROUP, default=ENTRANCE_APARTMENT_DOOR, verbose_name='Категорія')
    img = models.ImageField(default='no_image.png', upload_to='product_image', verbose_name='Фото')
    description = models.TextField(max_length=1000, verbose_name='Опис')
    door_package = models.TextField(max_length=1000, verbose_name='Комплектація')
    door_size = models.TextField(max_length=255, verbose_name='Розміри дверей')
    door_leaf = models.TextField(max_length=255, verbose_name='Дверне полотно')
    threshold = models.TextField(max_length=255, verbose_name='Поріг')
    furniture = models.TextField(max_length=1000, verbose_name='Фурнітура')
    coating = models.CharField(max_length=1000, verbose_name='Покриття')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')




