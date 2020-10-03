from datetime import datetime
from django_extensions.db.fields import AutoSlugField
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="категории")
    slug = AutoSlugField(max_length=50, unique=True, populate_from='name')
    description = models.TextField()

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


SALT_CHOICES = {
    ('YES', "Да"),
    ('NO', "Нет"),
}

ACCESSORIES_CHOICES = {
    ('IS', "Испарители"),
    ('CRT', "Картриджи"),
    ('MND', "Мундштуки"),
    ("NMK", "Намотки"),
    ("VTA", "Вата")
}


def titleToSlug(title):
    return "-".join(str(title).split(" "))


class Product(models.Model):
    __name__ = "Товары"

    class Meta:
        abstract = True

    objects = models.Manager()

    id = models.AutoField(auto_created=True, unique=True, primary_key=True)
    new = models.BooleanField(default=False, verbose_name="Добавить в категорию новые?")
    title = models.CharField(max_length=255, verbose_name="Наименование")
    slug = AutoSlugField(max_length=50, unique=True, populate_from='title')
    image = models.ImageField(upload_to='images', verbose_name="Изображение")
    #image2 = models.ImageField(upload_to='images', verbose_name="Изображение")
    brand = models.CharField(max_length=255, default='другие', verbose_name="Бренд")
    description = models.TextField(verbose_name="Описание", null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")
    sale = models.DecimalField(null=True, max_digits=10, decimal_places=2, verbose_name="Скидка")
    add_time = models.TimeField(default=datetime.now(), verbose_name="Время добавления")
    add_date = models.DateField(default=timezone.now, verbose_name="Дата добавления")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# def save(self):
#     super(Product, self).save()
#     if not self.slug.endswith('-' + str(self.title)):
#         self.slug += '-' + str(self.title)
#         super(Product, self).save()


class Liquid(Product):
    taste = models.CharField(max_length=255, default="другие", verbose_name="Вкус")
    volume = models.DecimalField(max_digits=9, decimal_places=2, null=True, verbose_name="Объем")
    salt = models.CharField(max_length=255, choices=SALT_CHOICES, verbose_name="SALT")
    vg_to_pg = models.CharField(max_length=255, null=True, verbose_name="ВГ на ПГ")
    nicotine = models.DecimalField(max_digits=9, decimal_places=2, null=True, verbose_name="Содержание никотина")
    country = models.CharField(max_length=255, default="другие", verbose_name="Страна производитель")

    class Meta:
        verbose_name = 'Жидкость'
        verbose_name_plural = 'Жидкости'

    def __str__(self):
        return self.title


class Accessory(Product):
    type_category = models.CharField(choices=ACCESSORIES_CHOICES, max_length=255, null=True, verbose_name="Подтверди название категории")
    # color = models.CharField(max_length=100, null=False, default='другие')

    class Meta:
        verbose_name = 'Аксессуар'
        verbose_name_plural = 'Аксессуары'


class Crate(Product):

    class Meta:
        verbose_name = 'Набор'
        verbose_name_plural = 'Наборы'


TABLE_CHOICES = {
    ("Accessory", "Accessory"),
    ("Liquid", "Liquid"),
    }


class Slider(models.Model):

    objects = models.Manager()

    id = models.AutoField(auto_created=True, unique=True, primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Наименование", default='')
    table = models.CharField(max_length=255, choices=TABLE_CHOICES, null=True, verbose_name="Категория") # can delete this shit
    category = models.ForeignKey(Category, verbose_name="Категория", null=True, on_delete=models.CASCADE)
    slug = AutoSlugField(max_length=50, unique=True, populate_from='title')
    image = models.ImageField(upload_to='images', verbose_name="Изображение", default='')
    description = models.TextField(verbose_name="Описание", null=True)
    add_time = models.TimeField(default=datetime.now(), verbose_name="Время добавления")
    add_date = models.DateField(default=timezone.now, verbose_name="Дата добавления")

    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдеры'


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    comment = models.TextField()
    event_time = models.TimeField(default=datetime.now(), verbose_name="Время добавления")
    event_date = models.DateField(default=timezone.now, verbose_name="Дата добавления")
    created = models.TimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    sale = models.DecimalField(max_digits=9, decimal_places=2, null=False, default=0.0)
    pre_price = models.DecimalField(max_digits=9, decimal_places=2, null=False, default=0.0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, null=False, default=0.0)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    # product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.order)

    def get_cost(self):
        return self.price * self.quantity


class Producted(models.Model):
    objects = models.Manager()

    id = models.AutoField(auto_created=True, unique=True, primary_key=True)
    new = models.BooleanField(default=False, verbose_name="Добавить в категорию новые?")
    title = models.CharField(max_length=255, verbose_name="Наименование")
    slug = AutoSlugField(max_length=50, unique=True, populate_from='title')
    image = models.ImageField(upload_to='images', verbose_name="Изображение")
    # image2 = models.ImageField(upload_to='images', verbose_name="Изображение")
    brand = models.CharField(max_length=255, default='другие', verbose_name="Бренд")
    description = models.TextField(verbose_name="Описание", null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")
    sale = models.DecimalField(null=True, max_digits=10, decimal_places=2, verbose_name="Скидка")
    add_time = models.TimeField(default=datetime.now(), verbose_name="Время добавления")
    add_date = models.DateField(default=timezone.now, verbose_name="Дата добавления")
    category = models.ForeignKey(Category, verbose_name="Категория", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Desktop(Producted):
    taste = models.CharField(max_length=255, default="другие", verbose_name="Вкус")
    volume = models.DecimalField(max_digits=9, decimal_places=2, null=True, verbose_name="Объем")
    salt = models.CharField(max_length=255, choices=SALT_CHOICES, null=True, verbose_name="SALT")
    vg_to_pg = models.CharField(max_length=255, null=True, verbose_name="ВГ на ПГ")
    nicotine = models.DecimalField(max_digits=9, decimal_places=2, null=True, verbose_name="Содержание никотина")
    country = models.CharField(max_length=255, default="другие", verbose_name="Страна производитель")

    def __str__(self):
        return self.title


class Monitor(Producted):
    type_category = models.CharField(choices=ACCESSORIES_CHOICES, max_length=255, null=True, verbose_name="Подтверди название категории")

