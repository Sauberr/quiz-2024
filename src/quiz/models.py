from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from faker import Faker

from core.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @classmethod
    def generate_instances(cls, count: int = 5):
        faker = Faker()
        for _ in range(count):
            category = cls.objects.create(
                name=faker.word(),
            )


class Quiz(models.Model):
    QUESTION_MAX_LIMIT = 20
    QUESTION_MIN_LIMIT = 3

    class LEVEL_CHOICES(models.IntegerChoices):
        BASIC = (
            0,
            "Basic",
        )
        MIDDLE = (
            1,
            "Middle",
        )
        ADVANCED = (
            2,
            "Advanced",
        )

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1024, blank=True, null=True)
    image = models.ImageField(default="default.jpg", upload_to="media/covers")
    category = models.ForeignKey("quiz.Category", related_name="quizzes", on_delete=models.CASCADE)
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES.choices, default=LEVEL_CHOICES.BASIC)

    def __str__(self):
        return self.title

    def questions_count(self):
        return self.questions.count()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    @classmethod
    def generate_instances(cls, count: int = 5):
        faker = Faker()
        for _ in range(count):
            quiz = cls.objects.create(
                title=faker.sentence(),
                description=faker.text(),
                image="default.jpg",
                category=Category.objects.first(),
                level=faker.random_int(min=0, max=2),
            )


class Result(BaseModel):
    quiz = models.ForeignKey("quiz.Quiz", related_name="results", on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quiz.title} - {self.user.email}"

    @classmethod
    def generate_instances(cls, count: int = 5):
        faker = Faker()
        for _ in range(count):
            result = cls.objects.create(
                quiz=Quiz.objects.first(),
                user=get_user_model().objects.first(),
            )


class Question(BaseModel):
    quiz = models.ForeignKey("quiz.Quiz", related_name="questions", on_delete=models.CASCADE)
    order_number = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(Quiz.QUESTION_MAX_LIMIT), MinValueValidator(Quiz.QUESTION_MIN_LIMIT)]
    )
    text = models.TextField(max_length=1024)

    def __str__(self):
        return f"{self.quiz.title} - {self.order_number}"

    @classmethod
    def generate_instances(cls, count: int = 5):
        faker = Faker()
        for _ in range(count):
            question = cls.objects.create(
                quiz=Quiz.objects.first(),
                order_number=faker.random_int(min=1, max=20),
                text=faker.text(),
            )


class Choice(BaseModel):
    question = models.ForeignKey("quiz.Question", related_name="choices", on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.text} - {self.text}"

    @classmethod
    def generate_instances(cls, count: int = 5):
        faker = Faker()
        for _ in range(count):
            choice = cls.objects.create(
                question=Question.objects.first(),
                text=faker.word(),
                is_correct=faker.boolean(),
            )
