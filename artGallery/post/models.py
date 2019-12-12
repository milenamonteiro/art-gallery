'''modules'''
from model_utils import Choices
from django.db import models
from django.utils.timezone import now

class Post(models.Model):
    '''Post model
    Every post has a category, defined in the list below.
    This variable uses the module django_model_utils
    '''

    CATEGORY = Choices(
        (1, 'animation', 'Animation'),
        (2, 'cartoon', 'Cartoon'),
        (3, 'digitalart', 'Digital Art'),
        (4, 'traditional', 'Traditional'),
        (5, 'photography', 'Photography'),
        (6, 'caligraphy', 'Caligraphy'),
        (7, 'sculpture', 'Sculpture'),
        (8, 'streetart', 'Street Art'),
        (9, 'characters', 'Characters'),
        (10, 'background', 'Background'),
        (11, 'fantasy', 'Fantasy'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(default=now, blank=True, verbose_name='created at')
    category = models.PositiveSmallIntegerField(
        choices=CATEGORY,
    )
    user_id = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
