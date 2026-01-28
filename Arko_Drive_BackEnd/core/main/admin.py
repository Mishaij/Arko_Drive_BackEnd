from django.contrib import admin
from .models import (
    Test, Question, Answer,
    TheoryGroup, TheoryQuestion, TheoryAnswer,
    SignGroup, Sign,
    Package, PackageFeature,
    CarItem, ValueItem, HistoryItem,

)

# ----------------------------------------
# Админ для Tests / Questions / Answers
# ----------------------------------------
class AnswerInline(admin.TabularInline):
    """
    Инлайн-форма для вариантов ответов (Answer) внутри Question.
    """
    model = Answer
    extra = 1
    fields = ('text', 'is_correct')
    verbose_name = "Вариант ответа"
    verbose_name_plural = "Варианты ответов"


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """
    Админ-форма для Question:
    - dropdown для выбора Test
    - поле text, поле image
    - инлайн для Answer
    """
    list_display = ('__str__', 'test')
    list_filter = ('test',)
    search_fields = ('text',)
    inlines = [AnswerInline]
    fieldsets = (
        (None, {
            'fields': ('test', 'text', 'image')
        }),
    )


class QuestionInline(admin.TabularInline):
    """
    Инлайн-форма для вопросов (Question) внутри Test.
    Если нужно редактировать сразу все вопросы при редактировании Test.
    """
    model = Question
    extra = 1
    fields = ('text', 'image')
    show_change_link = True


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    """
    Админ-форма для Test:
    - список всех тестов
    - инлайн-форма для Question (если нужно создавать/редактировать вопросы сразу здесь)
    """
    list_display = ('title',)
    search_fields = ('title',)
    inlines = [QuestionInline]


# ----------------------------------------
# Админ для TheoryGroup / TheoryQuestion / TheoryAnswer
# ----------------------------------------
class TheoryAnswerInline(admin.TabularInline):
    model = TheoryAnswer
    extra = 1
    fields = ('text', 'is_correct')
    verbose_name = "Вариант ответа (Теория)"
    verbose_name_plural = "Варианты ответов (Теория)"


@admin.register(TheoryQuestion)
class TheoryQuestionAdmin(admin.ModelAdmin):
    """
    Админ для одиночного теоретического вопроса:
    - dropdown для выбора TheoryGroup
    - текст, картинка
    - инлайн для TheoryAnswer
    """
    list_display = ('__str__', 'group')
    list_filter = ('group',)
    search_fields = ('text',)
    inlines = [TheoryAnswerInline]
    fieldsets = (
        (None, {
            'fields': ('group', 'text', 'image')
        }),
    )


class TheoryQuestionInline(admin.TabularInline):
    model = TheoryQuestion
    extra = 1
    fields = ('text', 'image')
    show_change_link = True


@admin.register(TheoryGroup)
class TheoryGroupAdmin(admin.ModelAdmin):
    """
    Админ для TheoryGroup:
    - в списке отображается title и order
    - инлайн для TheoryQuestion
    """
    list_display = ('title', 'order')
    ordering = ('order', 'title')
    inlines = [TheoryQuestionInline]


# ----------------------------------------
# Админ для SignGroup / Sign
# ----------------------------------------
class SignInline(admin.TabularInline):
    model = Sign
    extra = 1
    fields = ('number', 'image', 'title')
    verbose_name = "Знак"
    verbose_name_plural = "Знаки"


@admin.register(SignGroup)
class SignGroupAdmin(admin.ModelAdmin):
    """
    Админ для группы знаков. В список выводится name и order.
    Инлайн для Sign, чтобы прямо тут добавлять/редактировать знаки.
    """
    list_display = ('name', 'order')
    ordering = ('order', 'name')
    inlines = [SignInline]


@admin.register(Sign)
class SignAdmin(admin.ModelAdmin):
    """
    Если нужно иметь отдельный админ для знаков, но обычно будет достаточно
    редактирования через SignGroupAdmin с инлайнами.
    """
    list_display = ('number', 'title', 'group')
    list_filter = ('group',)
    search_fields = ('number', 'title')


# ----------------------------------------
# Админ для Package / PackageFeature
# ----------------------------------------
class PackageFeatureInline(admin.TabularInline):
    model = PackageFeature
    extra = 1
    fields = ('description',)
    verbose_name = "Пункт пакета"
    verbose_name_plural = "Пункты пакета"


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    """
    Админ для пакета. Поля: name, price, category.
    Инлайн для PackageFeature, чтобы добавлять пункты прямо на странице пакета.
    """
    list_display = ('name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name',)
    inlines = [PackageFeatureInline]


@admin.register(PackageFeature)
class PackageFeatureAdmin(admin.ModelAdmin):
    """
    Отдельный админ для пунктов пакета (если потребуется).
    """
    list_display = ('description', 'package')
    list_filter = ('package',)
    search_fields = ('description',)


# ----------------------------------------
# Админ для About (CarItem / ValueItem / HistoryItem)
# ----------------------------------------
@admin.register(CarItem)
class CarItemAdmin(admin.ModelAdmin):
    """
    Админ для блока 'Наши автомобили'.
    """
    list_display = ('id', 'order', 'short_description')
    list_editable = ('order',)
    ordering = ('order',)

    def short_description(self, obj):
        return obj.description[:50]
    short_description.short_description = "Описание (первые 50 символов)"


@admin.register(ValueItem)
class ValueItemAdmin(admin.ModelAdmin):
    """
    Админ для блока 'Ценности'.
    """
    list_display = ('title', 'order')
    list_editable = ('order',)
    ordering = ('order',)


@admin.register(HistoryItem)
class HistoryItemAdmin(admin.ModelAdmin):
    """
    Админ для блока 'История и ценности'.
    """
    list_display = ('__str__', 'order')
    list_editable = ('order',)
    ordering = ('order',)


