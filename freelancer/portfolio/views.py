from django.shortcuts import render

# Create your views here.
# portfolio/views.py

def services(request):
    services_list = [
        "Custom Web Application Development",
        "E-commerce Solutions",
        "Mobile-First Responsive Design",
        "API Integration and Development",
        "Database Design and Optimization",
        "SEO and Performance Audits"
    ]
    return render(request, 'portfolio/services.html', {'services': services_list})

def testimonials(request):
    testimonials_data = {
        "Jane Doe, CEO of TechCorp": "Working with this freelancer was a game-changer for our business. The final product exceeded all expectations.",
        "John Smith, Founder of Innovate LLC": "Incredibly professional, punctual, and talented. The communication was excellent from start to finish.",
        "Emily White, Marketing Director": "Our website traffic has doubled since the redesign. The attention to detail and user experience was outstanding."
    }
    return render(request, 'portfolio/testimonials.html', {'testimonials': testimonials_data})

def case_studies(request):
    return render(request, 'portfolio/case_studies.html')

def blog(request):
    # In a real app, you would fetch blog posts from the database
    blog_posts = [
        {'title': 'The Top 5 Python Frameworks in 2025', 'date': 'May 28, 2025', 'excerpt': 'A deep dive into the frameworks shaping modern web development.'},
        {'title': 'Why a Mobile-First Approach is Non-Negotiable', 'date': 'June 04, 2025', 'excerpt': 'Exploring the data and user behavior trends that make mobile-first design essential.'}
    ]
    return render(request, 'portfolio/blog.html', {'posts': blog_posts})


def pricing(request):
    pricing_data = {
        "Basic Website Package": "$1,500",
        "E-commerce Store Setup": "$3,500",
        "Custom Web Application": "Starting at $8,000",
        "Monthly Maintenance & SEO": "$400/month"
    }
    return render(request, 'portfolio/pricing.html', {'pricing_data': pricing_data})