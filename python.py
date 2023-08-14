from django.db import models

class Post(models.Model):
    username = models.CharField(max_length=50)
    caption = models.TextField()
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.username} - {self.caption}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()

    def __str__(self):
        return f"{self.post.username} - {self.text}"
