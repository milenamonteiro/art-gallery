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
    user_id = models.ForeignKey(User)          # need to create user_id field

    class User(object):
        """user model"""
        
        user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        name = models.CharField(max_length=30,null=False,blank=False)
        email = models.EmailField(max_length=254,unique=True)
        GENDER_CHOICES = (
            ('M', 'Male'), 
            ('F', 'Female'), 
            ('O', 'Other'))
        gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
        date_of_birth = models.DateField(max_length=8)
        created_at = models.DateTimeField(auto_now_add=True)
