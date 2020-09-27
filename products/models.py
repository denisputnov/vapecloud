from django.utils import timezone

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя категории")
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


SALT_CHOICES = {
    ('YES', "Да"),
    ('NO', "Нет"),
}


class Product(models.Model):
    __name__ = "Товары"

    class Meta:
        abstract = True

    objects = models.Manager()

    id = models.PositiveIntegerField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=255, verbose_name="Наименование")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images', verbose_name="Изображение")
    #image2 = models.ImageField(upload_to='images', verbose_name="Изображение")
    brand = models.CharField(max_length=255, default='другие', verbose_name="Бренд")
    description = models.TextField(verbose_name="Описание", null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена")
    date = models.DateField(default=timezone.now, verbose_name="Дата добавления")
    sale = models.DecimalField(null=True, max_digits=10, decimal_places=2, verbose_name="Скидка")

    """connection_id = models.DecimalField()"""

    def __str__(self):
        return self.title


class Liquid(Product):
    taste = models.CharField(max_length=255, default="другие", verbose_name="Вкус")
    volume = models.DecimalField(max_digits=9, decimal_places=2, null=True, verbose_name="Объем")
    salt = models.CharField(max_length=255, choices=SALT_CHOICES, verbose_name="SALT")
    vg_to_pg = models.CharField(max_length=255, null=True, verbose_name="ВГ на ПГ")
    nicotine = models.DecimalField(max_digits=9, decimal_places=2, null=True, verbose_name="Содержание никотина")
    country = models.CharField(max_length=255, default="другие", verbose_name="Страна производитель")

    def __str__(self):
        return self.title

ACCESSORIES_CHOICES = {
    ('IS', "Испарители"),
    ('CRT', "Картриджи"),
    ('MND', "Мундштуки"),
    ("NMK", "Намотки")
}


class Accessory(Product):
    color = models.CharField(max_length=100, null=False, default='другие')
    type_category = models.CharField(choices=ACCESSORIES_CHOICES, max_length=255, null=True)


class Crate(Product):
    pass


class Utility(Product):
    class Meta:
        abstract = True


DELIVERY_METHODS = {
    ('SM', "Cамовывоз"),
    ("HMK", "Доставка курьером"),
    ('HMP', "Доставка почтой")
}

PAYMENT_METHODS = {
    ('CR', "мастеркард"),
    ("QW", "киви"),
    ('WBM', "вебмани"),
}


class CartProduct(models.Model):

    """user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)"""
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self):
        return "Продукт: {} (для корзины)".format(self.content_object.title)

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.content_object.price
        super().save(*args, **kwargs)


class Cart(models.Model):

    """owner = models.ForeignKey('Customer', null=True, verbose_name='Владелец', on_delete=models.CASCADE)"""
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, default=0, decimal_places=2, verbose_name='Общая цена')
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)


class Order(models.Model):
    order_id = models.IntegerField(auto_created=True, primary_key=True)
    phone = models.CharField(max_length=100, null=False, default='без номера, даун')
    mail = models.CharField(max_length=100, null=False, default='без номера, даун')
    full_name = models.CharField(max_length=100, null=False, default='без номера, даун')
    delivery = models.CharField(choices=DELIVERY_METHODS, max_length=255, null=True)
    city = models.CharField(max_length=100, null=False, default='без номера, даун')
    address = models.CharField(max_length=500, null=False, default='без номера, даун')
    payment_method = models.CharField(choices=PAYMENT_METHODS, max_length=255, null=True)
    sale = models.DecimalField(max_digits=9, decimal_places=2, null=False, default=0.0)
    date = models.DateField(default=timezone.now, verbose_name="Дата заказа")
    pre_price = models.DecimalField(max_digits=9, decimal_places=2, null=False, default=0.0)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, null=False, default=0.0)

    def __str__(self):
        return self.order_id


class OrderProduct(models.Model):
    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'is_ready'
    STATUS_COMPLETED = 'completed'

    BUYING_TYPE_SELF = 'self'
    BUYING_TYPE_DELIVERY = 'delivery'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Новый заказ'),
        (STATUS_IN_PROGRESS, 'Заказ в обработке'),
        (STATUS_READY, 'Заказ готов'),
        (STATUS_COMPLETED, 'Заказ выполнен')
    )

    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF, 'Самовывоз'),
        (BUYING_TYPE_DELIVERY, 'Доставка')
    )

    """customer = models.ForeignKey(Customer, verbose_name='Покупатель', related_name='related_orders',
                                 on_delete=models.CASCADE)"""
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    cart = models.ForeignKey(Cart, verbose_name='Корзина', on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=1024, verbose_name='Адрес', null=True, blank=True)
    status = models.CharField(
        max_length=100,
        verbose_name='Статус заказ',
        choices=STATUS_CHOICES,
        default=STATUS_NEW
    )
    buying_type = models.CharField(
        max_length=100,
        verbose_name='Тип заказа',
        choices=BUYING_TYPE_CHOICES,
        default=BUYING_TYPE_SELF
    )
    comment = models.TextField(verbose_name='Комментарий к заказу', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания заказа')
    order_date = models.DateField(verbose_name='Дата получения заказа', default=timezone.now)

    def __str__(self):
        return str(self.id)


