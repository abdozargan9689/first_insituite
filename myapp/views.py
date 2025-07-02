from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student, Courses, Subjects, Quizzes, Behavior
from django.db.models import Sum, Count

def home(request):
    # Get some stats for the dashboard
    student_count = Student.objects.count()
    course_count = Courses.objects.count()
    subject_count = Subjects.objects.count()
    quiz_count = Quizzes.objects.count()
    
    return HttpResponse(f"""
    <html>
    <head>
        <title>Student Management System</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f5f5f5; }}
            .container {{ max-width: 1000px; margin: 0 auto; }}
            h1 {{ color: #2c3e50; text-align: center; margin-bottom: 30px; }}
            .success {{ color: #27ae60; }}
            .info {{ background: #ecf0f1; padding: 20px; border-radius: 5px; margin-bottom: 20px; }}
            .stats {{ display: flex; justify-content: space-between; margin-bottom: 30px; }}
            .stat-card {{ background: white; padding: 20px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); width: 22%; }}
            .stat-card h3 {{ margin-top: 0; color: #3498db; }}
            .stat-card p {{ font-size: 24px; font-weight: bold; margin-bottom: 0; }}
            .links {{ margin-top: 30px; }}
            .links a {{ display: inline-block; margin-right: 15px; background: #3498db; color: white; padding: 10px 15px; 
                      text-decoration: none; border-radius: 5px; }}
            .links a:hover {{ background: #2980b9; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎓 Student Management System</h1>
            
            <div class="stats">
                <div class="stat-card">
                    <h3>Students</h3>
                    <p>{student_count}</p>
                </div>
                <div class="stat-card">
                    <h3>Courses</h3>
                    <p>{course_count}</p>
                </div>
                <div class="stat-card">
                    <h3>Subjects</h3>
                    <p>{subject_count}</p>
                </div>
                <div class="stat-card">
                    <h3>Quizzes</h3>
                    <p>{quiz_count}</p>
                </div>
            </div>
            
            <div class="info">
                <h3>System Overview:</h3>
                <p>This Student Management System allows you to:</p>
                <ul>
                    <li>Manage student records and academic performance</li>
                    <li>Track courses, subjects, quizzes, and behavior</li>
                    <li>Calculate and monitor student grades</li>
                    <li>Generate reports on student performance</li>
                </ul>
            </div>
            
            <div class="links">
                <a href="/admin/">Admin Dashboard</a>
                <a href="/students/">View Students</a>
                <a href="/courses/">View Courses</a>
                <a href="/about/">About System</a>
            </div>
        </div>
    </body>
    </html>
    """)

def about(request):
    return HttpResponse("""
    <html>
    <head>
        <title>About - Student Management System</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f5f5f5; }
            .container { max-width: 800px; margin: 0 auto; }
            h1 { color: #2c3e50; }
            .content { background: white; padding: 20px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
            .back-link { margin-top: 20px; }
            .back-link a { color: #3498db; text-decoration: none; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>About Student Management System</h1>
            
            <div class="content">
                <h2>System Overview</h2>
                <p>The Student Management System is a comprehensive solution for educational institutions to manage student records, courses, and academic performance.</p>
                
                <h2>Features</h2>
                <ul>
                    <li><strong>Student Management:</strong> Store and manage student information including ID cards, ranks, and total degrees.</li>
                    <li><strong>Course Management:</strong> Create and manage courses assigned to students.</li>
                    <li><strong>Subject Tracking:</strong> Track subjects within courses, including full degrees, passing degrees, and earned degrees.</li>
                    <li><strong>Quiz Management:</strong> Create and grade quizzes for each course.</li>
                    <li><strong>Behavior Monitoring:</strong> Track student behavior as part of the overall grading system.</li>
                    <li><strong>Automatic Grade Calculation:</strong> System automatically calculates total degrees based on subjects, quizzes, and behavior.</li>
                </ul>
                
                <h2>Technical Details</h2>
                <p>Built with Django 5.2.3, this system uses a relational database to store and manage all educational data with proper relationships between entities.</p>
            </div>
            
            <div class="back-link">
                <a href="/">← Back to Home</a>
            </div>
        </div>
    </body>
    </html>
    """)

def students(request):
    students_list = Student.objects.all()
    
    html_content = """
    <html>
    <head>
        <title>Students - Management System</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f5f5f5; }
            .container { max-width: 1000px; margin: 0 auto; }
            h1 { color: #2c3e50; text-align: center; margin-bottom: 30px; }
            table { width: 100%; border-collapse: collapse; background: white; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
            th, td { padding: 12px 15px; text-align: left; border-bottom: 1px solid #ddd; }
            th { background-color: #3498db; color: white; }
            tr:hover { background-color: #f5f5f5; }
            .back-link { margin-top: 20px; }
            .back-link a { color: #3498db; text-decoration: none; }
            .empty { text-align: center; padding: 30px; background: white; border-radius: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Students Directory</h1>
    """
    
    if students_list:
        html_content += """
            <table>
                <thead>
                    <tr>
                        <th>ID Card</th>
                        <th>Full Name</th>
                        <th>Rank</th>
                        <th>Total Degree</th>
                        <th>Created At</th>
                    </tr>
                </thead>
                <tbody>
        """
        
        for student in students_list:
            html_content += f"""
                    <tr>
                        <td>{student.id_card}</td>
                        <td>{student.fullname}</td>
                        <td>{student.rank or '-'}</td>
                        <td>{student.total_degree}</td>
                        <td>{student.created_at.strftime('%Y-%m-%d')}</td>
                    </tr>
            """
        
        html_content += """
                </tbody>
            </table>
        """
    else:
        html_content += """
            <div class="empty">
                <p>No students found in the system.</p>
            </div>
        """
    
    html_content += """
            <div class="back-link">
                <a href="/">← Back to Home</a>
            </div>
        </div>
    </body>
    </html>
    """
    
    return HttpResponse(html_content)

def courses(request):
    courses_list = Courses.objects.all()
    
    html_content = """
    <html>
    <head>
        <title>Courses - Management System</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; background-color: #f5f5f5; }
            .container { max-width: 1000px; margin: 0 auto; }
            h1 { color: #2c3e50; text-align: center; margin-bottom: 30px; }
            table { width: 100%; border-collapse: collapse; background: white; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
            th, td { padding: 12px 15px; text-align: left; border-bottom: 1px solid #ddd; }
            th { background-color: #3498db; color: white; }
            tr:hover { background-color: #f5f5f5; }
            .back-link { margin-top: 20px; }
            .back-link a { color: #3498db; text-decoration: none; }
            .empty { text-align: center; padding: 30px; background: white; border-radius: 5px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Courses Directory</h1>
    """
    
    if courses_list:
        html_content += """
            <table>
                <thead>
                    <tr>
                        <th>Course Name</th>
                        <th>ID Name</th>
                        <th>Student</th>
                        <th>Created At</th>
                    </tr>
                </thead>
                <tbody>
        """
        
        for course in courses_list:
            html_content += f"""
                    <tr>
                        <td>{course.name}</td>
                        <td>{course.id_name}</td>
                        <td>{course.student.fullname}</td>
                        <td>{course.created_at.strftime('%Y-%m-%d')}</td>
                    </tr>
            """
        
        html_content += """
                </tbody>
            </table>
        """
    else:
        html_content += """
            <div class="empty">
                <p>No courses found in the system.</p>
            </div>
        """
    
    html_content += """
            <div class="back-link">
                <a href="/">← Back to Home</a>
            </div>
        </div>
    </body>
    </html>
    """
    
    return HttpResponse(html_content)
