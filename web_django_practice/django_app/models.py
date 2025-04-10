from django.db import models


# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name="Должность")
    objects = models.Manager()

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должность"

    def __str__(self):
        return f"{self.title}"


class Person(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, db_index=True, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=100, verbose_name="Отчество")
    tabel_num = models.CharField(max_length=100, db_index=True, unique=True, verbose_name="Табельный номер")
    position = models.ForeignKey(to=Position, on_delete=models.SET_NULL, null=True, verbose_name="Должность")
    objects = models.Manager()

    class Meta:
        verbose_name = "Сотрудники"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f"{self.tabel_num} - {self.last_name} - {self.position.title}"


class ClothCategory(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    objects = models.Manager()

    class Meta:
        verbose_name = "Категория одежды"
        verbose_name_plural = "Категория одежды"

    def __str__(self):
        return f"{self.title}"


class Cloth(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(to=ClothCategory, on_delete=models.SET_NULL, null=True)
    deadline = models.IntegerField()
    objects = models.Manager()

    class Meta:
        verbose_name = "Одежда"
        verbose_name_plural = "Одежда"

    def __str__(self):
        return f"{self.title} - {self.category.title}"


class ClothSet(models.Model):
    person = models.ForeignKey(to=Person, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    cloth_type = models.ForeignKey(to=Cloth, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    objects = models.Manager()

    class Meta:
        verbose_name = "Выдача"
        verbose_name_plural = "Выдача"

    def __str__(self):
        return f"{self.created_at} - {self.person.tabel_num} ({self.person.last_name}) - {self.is_active}"
