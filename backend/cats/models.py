from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Achievement(models.Model):
    """Cats achievements model."""
    name = models.CharField(max_length=64, verbose_name='Название достижения')

    def __str__(self):
        """Return string representation of the achievement."""
        return self.name


class Cat(models.Model):
    """Cats model."""
    name = models.CharField(max_length=16, verbose_name='Имя котика')
    color = models.CharField(max_length=16, verbose_name='цвет котика')
    birth_year = models.IntegerField(verbose_name='Год рождения')
    owner = models.ForeignKey(
        User, related_name='cats',
        on_delete=models.CASCADE,
        verbose_name='Владелец'
        )
    achievements = models.ManyToManyField(
        Achievement,
        through='AchievementCat',
        verbose_name='Достижения котика',
    )
    image = models.ImageField(
        upload_to='cats/images/',
        null=True,
        default=None,
        verbose_name='Изображение котика',
        )

    def __str__(self):
        """Return string representation of the cat's name."""
        return self.name


class AchievementCat(models.Model):
    """Many-to-many relationship between Achievement and Cat."""
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        """Return string representation of the achievement and cat."""
        return f'{self.achievement} {self.cat}'
