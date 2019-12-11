'''modules'''
from model_utils import Choices
from django.db import models

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
    description = models.CharField()
    created_at = models.DateTimeField()
    category = models.PositiveSmallIntegerField(
        choices=CATEGORY,
    )
    # need to create user_id field
