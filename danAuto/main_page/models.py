from django.db import models


class NewOrder(models.Model):
    date_create_order = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')

    # Информация о клиенте
    name = models.CharField(max_length=255, verbose_name='Имя')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    middle_name = models.CharField(max_length=255, verbose_name='Отчество')

    # Контактная информация
    telephone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    email = models.EmailField(max_length=255)
    link_messenger = models.CharField(max_length=255, default='Ссылка не обязательна', blank=True,
                                      verbose_name='Ссылка на мессенджер')

    # Информация о заказе
    info_order = models.TextField(verbose_name='Информация о заказе')
    car_brand = models.CharField(max_length=255, verbose_name='Марка авто')
    car_model = models.CharField(max_length=255, verbose_name='Модель авто')
    car_year = models.CharField(max_length=4, verbose_name='Год авто')
    car_horsepower = models.CharField(max_length=255, verbose_name='Кол-во лошадиных сил')
    car_vin = models.CharField(max_length=255, verbose_name='VIN-код')

    class Meta:
        verbose_name = 'Заказы'
        ordering = ['date_create_order']

    def __str__(self):
        return f'ФИО: {self.name} {self.last_name} {self.middle_name} ' \
               f'VIN: {self.car_vin} ' \
               f'НОМЕР: {self.telephone_number} ' \
               f'МАШИНА: {self.car_brand} {self.car_model} '
