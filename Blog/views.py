from django.shortcuts import render
import random

# Global lists for blogs and images
BLOGS = [
    "The journey of learning Django has been incredibly rewarding. Starting from the basics of MTV architecture, I've come to appreciate how Django simplifies web development through its batteries-included philosophy.",
    "Understanding the difference between a Django project and an app was transformative. Projects contain multiple apps, each responsible for specific functionality. This modular approach makes code maintainable and scalable.",
    "Static files in Django can be confusing at first, but once you understand the static directory structure and how collectstatic works, managing CSS and JavaScript becomes straightforward and organized."
]

IMAGES = [
    "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=500&h=300&fit=crop",
    "https://images.unsplash.com/photo-1633356122544-f134ef2944f7?w=500&h=300&fit=crop",
    "https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=500&h=300&fit=crop"
]

def blog(request):
    """Display a random blog post with a random image"""
    selected_blog = random.choice(BLOGS)
    selected_image = random.choice(IMAGES)
    
    context = {
        'blog': selected_blog,
        'image': selected_image,
    }
    
    return render(request, 'blog/blog.html', context)

def show_all(request):
    """Display all blog posts and images"""
    context = {
        'blogs': BLOGS,
        'images': IMAGES,
    }
    
    return render(request, 'blog/show_all.html', context)

def about(request):
    """Display about page"""
    context = {
        'name': 'KYALIGAMBA JOEL',
        'bio': 'I am a Muni University student passionate developer learning Django and web development.',
    }
    
    return render(request, 'blog/about.html', context)
def homepage(request):
    return render(request, 'blog/homepage.html')