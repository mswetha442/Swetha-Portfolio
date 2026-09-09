from django.shortcuts import render

def home(request):
    projects = [
        {
            'id': 1,
            'title': 'E-Commerce Platform',
            'description': 'A full-stack online shopping platform built with Django, featuring user authentication, product catalog, cart management, and order checkout.',
            'tags': ['Django', 'Python', 'JavaScript', 'CSS3', 'HTML5'],
            'images': [
                '/static/images/ecommerce1.png',
                '/static/images/ecommerce2.png',
                '/static/images/ecommerce3.png',
                '/static/images/ecommerce4.png',
                '/static/images/ecommerce5.png',
            ],
            'github_link': 'https://github.com/Swetha/ecommerce-django',
            'live_demo': 'https://swetha-portfolio-6.onrender.com'
        }
    ]
    
    profile = {
        'name': 'Swetha',
        'role': 'Full-Stack Developer & Software Engineer',
        'bio': 'Passionate web developer specializing in building modern, responsive, and scalable web applications using Django, Python, JavaScript, and cloud platforms like Render.',
        'profile_image': '/static/images/profile.jpg',
        'email': 'swetha@example.com',
        'github': 'https://github.com/Swetha',
        'linkedin': 'https://linkedin.com/in/swetha',
    }

    return render(request, 'main/index.html', {'projects': projects, 'profile': profile})
