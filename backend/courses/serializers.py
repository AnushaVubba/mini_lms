from rest_framework import serializers
from .models import Course
from .models import Assignment, Submission


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'instructor']
        read_only_fields = ['instructor']

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = [
            'id',
            'assignment',
            'student',
            'content',
            'submitted_at',
            'grade',
            'feedback'
        ]
        read_only_fields = ['student', 'submitted_at', 'grade', 'feedback']

class GradeSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['grade', 'feedback']
