from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = TaggableManager()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')  # Link to the Post model
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    content = models.TextField()  # Comment content
    created_at = models.DateTimeField(auto_now_add=True)  # Auto-set creation timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Auto-update timestamp on edit

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"
