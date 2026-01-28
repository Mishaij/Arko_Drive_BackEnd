from django.db import models


class Test(models.Model):
    title = models.CharField("Название теста", max_length=255)


    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"

    def __str__(self):
        return self.title


class Question(models.Model):
    test = models.ForeignKey(
        Test,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name="Тест"
    )
    text = models.TextField("Текст вопроса")
    image = models.ImageField(
        "Картинка (если нужна)",
        upload_to='questions/',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.text[:50] if len(self.text) > 50 else self.text


class Answer(models.Model):

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name="Вопрос"
    )
    text = models.CharField("Текст ответа", max_length=255)
    is_correct = models.BooleanField("Правильный?", default=False)

    class Meta:
        verbose_name = "Вариант ответа"
        verbose_name_plural = "Варианты ответов"

    def __str__(self):
        return self.text



class TheoryGroup(models.Model):
    title = models.CharField("Название группы", max_length=255)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Теоретическая группа"
        verbose_name_plural = "Теоретические группы"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title


class TheoryQuestion(models.Model):
    group = models.ForeignKey(
        TheoryGroup,
        on_delete=models.CASCADE,
        related_name='questions',
        verbose_name="Группа"
    )
    text = models.TextField("Текст вопроса")
    image = models.ImageField(
        "Картинка (если нужна)",
        upload_to='theory_questions/',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Теоретический вопрос"
        verbose_name_plural = "Теоретические вопросы"

    def __str__(self):
        return f"{self.group.title} — {self.text[:50]}"


class TheoryAnswer(models.Model):
    question = models.ForeignKey(
        TheoryQuestion,
        on_delete=models.CASCADE,
        related_name='answers',
        verbose_name="Теоретический вопрос"
    )
    text = models.CharField("Текст ответа", max_length=255)
    is_correct = models.BooleanField("Правильный?", default=False)

    class Meta:
        verbose_name = "Вариант ответа (теория)"
        verbose_name_plural = "Варианты ответов (теория)"

    def __str__(self):
        return self.text



class SignGroup(models.Model):

    name = models.CharField("Название группы", max_length=255)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Группа знаков"
        verbose_name_plural = "Группы знаков"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Sign(models.Model):

    group = models.ForeignKey(
        SignGroup,
        on_delete=models.CASCADE,
        related_name='signs',
        verbose_name="Группа"
    )
    number = models.CharField("Номер знака", max_length=20)
    image = models.ImageField("Изображение знака", upload_to='signs/')
    title = models.CharField("Название знака", max_length=255)

    class Meta:
        verbose_name = "Дорожный знак"
        verbose_name_plural = "Дорожные знаки"
        ordering = ['group__order', 'number']

    def __str__(self):
        return f"{self.number} — {self.title}"



class Package(models.Model):
    CATEGORY_CHOICES = [
        ('full', "Теория + Практика"),
        ('theory', "Только теория"),
        ('practical', "Только практика"),
    ]

    name = models.CharField("Название пакета", max_length=255)
    price = models.DecimalField("Цена (в ₧)", max_digits=10, decimal_places=2)
    category = models.CharField(
        "Тип пакета",
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='full'
    )

    class Meta:
        verbose_name = "Пакет"
        verbose_name_plural = "Пакеты"

    def __str__(self):
        return f"{self.name} — {self.price}֏"


class PackageFeature(models.Model):

    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
        related_name='features',
        verbose_name="Пакет"
    )
    description = models.CharField("Описание пункта", max_length=255)

    class Meta:
        verbose_name = "Пункт пакета"
        verbose_name_plural = "Пункты пакета"

    def __str__(self):
        return self.description



class CarItem(models.Model):

    image = models.ImageField("Изображение автомобиля", upload_to='cars/')
    description = models.TextField("Описание")
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"
        ordering = ['order']

    def __str__(self):
        return f"Авто #{self.pk}"


class ValueItem(models.Model):

    icon = models.ImageField("Иконка", upload_to='values/')
    title = models.CharField("Заголовок", max_length=255)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Значение"
        verbose_name_plural = "Ценности"
        ordering = ['order']

    def __str__(self):
        return self.title


class HistoryItem(models.Model):

    title = models.CharField("Заголовок раздела", max_length=255, blank=True)
    content = models.TextField("Текст")
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        verbose_name = "Пункт истории"
        verbose_name_plural = "История и ценности"
        ordering = ['order']

    def __str__(self):
        return self.title if self.title else self.content[:30]


