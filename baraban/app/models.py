from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=24,
                            verbose_name='название',
                            help_text='напишите название товара')
    product_category = models.ForeignKey('Category',
                                         verbose_name='категория',
                                         help_text='выберите категорию',
                                         on_delete=models.CASCADE,
                                         blank=True,
                                         null=True)
    is_published = models.BooleanField(default=False,
                                       verbose_name='публикация')

    def __str__(self):  # строковое представление
        return self.name

    class Meta:
        db_table = 'app_categories'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('-name', 'is_published')


class Product(models.Model):
    class Status(models.TextChoices):
        NEW = 'NEW'
        OLD = 'OLD'

    title = models.CharField(max_length=36,
                             verbose_name='заголовок')
    storage_device_and_ram = models.CharField(max_length=10,
                                              verbose_name='введите 6/128GB',
                                              help_text='Выберите характеристику')
    status = models.CharField(max_length=3,
                              choices=Status.choices,
                              help_text='состояние')
    description = models.TextField(blank=True,
                                   null=True,
                                   verbose_name='описание товара',
                                   help_text='подробная информация')
    price = models.DecimalField(max_digits=7,
                                decimal_places=2,
                                default=0,
                                verbose_name='цена')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category',
                                 on_delete=models.PROTECT,
                                 verbose_name='категория')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'app_products'
        verbose_name = 'товар'
        verbose_name_plural = 'товары'
        ordering = ('-title', 'price', 'created_at')



