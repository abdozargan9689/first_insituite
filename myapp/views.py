from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <html>
    <head>
        <title>Django Project</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .container { max-width: 800px; margin: 0 auto; }
            h1 { color: #2c3e50; }
            .success { color: #27ae60; }
            .info { background: #ecf0f1; padding: 20px; border-radius: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎉 Django Project Created Successfully!</h1>
            <p class="success">Your Django project is up and running!</p>
            
            <div class="info">
                <h3>Project Structure:</h3>
                <ul>
                    <li><strong>myproject/</strong> - Main project directory</li>
                    <li><strong>myapp/</strong> - Sample Django app</li>
                    <li><strong>manage.py</strong> - Django management script</li>
                    <li><strong>db.sqlite3</strong> - SQLite database</li>
                </ul>
                
                <h3>Next Steps:</h3>
                <ul>
                    <li>Visit <a href="/admin/">/admin/</a> to access the Django admin</li>
                    <li>Create models in myapp/models.py</li>
                    <li>Add more views in myapp/views.py</li>
                    <li>Create templates in myapp/templates/</li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    """)

def about(request):
    return HttpResponse("<h1>About Page</h1><p>This is a sample Django application.</p>")
