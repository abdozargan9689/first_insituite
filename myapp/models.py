from django.db import models
from django.db.models import Sum
from django.utils import timezone
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Admin(models.Model):
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.username

class Student(models.Model):
    id_card = models.CharField(max_length=50, unique=True)
    rank = models.CharField(max_length=50, blank=True, null=True)
    fullname = models.CharField(max_length=100)
    img_report = models.CharField(max_length=255, blank=True, null=True)
    total_degree = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.fullname} ({self.id_card})"
    
    def update_total_degree(self):
        """Update the student's total degree based on all related courses"""
        # Get all courses for this student
        courses = self.courses_set.all()
        
        total = 0
        
        for course in courses:
            # Sum subject degrees
            subject_sum = course.subjects_set.aggregate(Sum('owner_degree'))['owner_degree__sum'] or 0
            
            # Sum quiz degrees
            quiz_sum = course.quizzes_set.aggregate(Sum('owner_degree'))['owner_degree__sum'] or 0
            
            # Sum behavior degrees
            behavior_sum = course.behavior_set.aggregate(Sum('owner_degree'))['owner_degree__sum'] or 0
            
            total += subject_sum + quiz_sum + behavior_sum
        
        self.total_degree = total
        self.save(update_fields=['total_degree'])

class Courses(models.Model):
    name = models.CharField(max_length=100)
    id_name = models.CharField(max_length=50, unique=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} ({self.id_name})"
    
    class Meta:
        verbose_name_plural = "Courses"

class Subjects(models.Model):
    name = models.CharField(max_length=100)
    full_degree = models.DecimalField(max_digits=10, decimal_places=2)
    pass_degree = models.DecimalField(max_digits=10, decimal_places=2)
    owner_degree = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.course.name}"
    
    class Meta:
        verbose_name_plural = "Subjects"

class Quizzes(models.Model):
    name = models.CharField(max_length=100)
    full_degree = models.DecimalField(max_digits=10, decimal_places=2)
    pass_degree = models.DecimalField(max_digits=10, decimal_places=2)
    owner_degree = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.course.name}"
    
    class Meta:
        verbose_name_plural = "Quizzes"

class Behavior(models.Model):
    full_degree = models.DecimalField(max_digits=10, decimal_places=2)
    pass_degree = models.DecimalField(max_digits=10, decimal_places=2)
    owner_degree = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Behavior - {self.course.name}"

# Signal handlers to update student total degree when related models change
@receiver(post_save, sender=Subjects)
@receiver(post_save, sender=Quizzes)
@receiver(post_save, sender=Behavior)
def update_student_degree_on_save(sender, instance, **kwargs):
    """Update student's total degree when a subject, quiz, or behavior is saved"""
    instance.course.student.update_total_degree()

@receiver(post_delete, sender=Subjects)
@receiver(post_delete, sender=Quizzes)
@receiver(post_delete, sender=Behavior)
def update_student_degree_on_delete(sender, instance, **kwargs):
    """Update student's total degree when a subject, quiz, or behavior is deleted"""
    instance.course.student.update_total_degree()
