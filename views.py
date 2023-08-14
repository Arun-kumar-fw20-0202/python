from django.shortcuts import render
from django.http import JsonResponse
from .models import Post, Comment

def create_post(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        caption = request.POST.get('caption')
        post = Post(username=username, caption=caption)
        post.save()
        return JsonResponse({'message': 'Post created successfully'})
    return JsonResponse({'error': 'Invalid request method'})

def view_posts(request):
    posts = Post.objects.all()
    data = [{'id': post.id, 'username': post.username, 'caption': post.caption, 'likes': post.likes} for post in posts]
    return JsonResponse(data, safe=False)

def delete_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return JsonResponse({'message': 'Post deleted successfully'})
    except Post.DoesNotExist:
        return JsonResponse({'error': 'Post not found'})

def like_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        post.likes += 1
        post.save()
        return JsonResponse({'message': 'Post liked successfully'})
    except Post.DoesNotExist:
        return JsonResponse({'error': 'Post not found'})

def comment_post(request, post_id):
    if request.method == 'POST':
        try:
            post = Post.objects.get(id=post_id)
            comment_text = request.POST.get('comment')
            comment = Comment(post=post, text=comment_text)
            comment.save()
            return JsonResponse({'message': 'Comment added successfully'})
        except Post.DoesNotExist:
            return JsonResponse({'error': 'Post not found'})
    return JsonResponse({'error': 'Invalid request method'})
