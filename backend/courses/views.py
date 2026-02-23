from rest_framework import generics, permissions
from .models import Course
from .serializers import CourseSerializer
from .permissions import IsInstructor
from .models import Assignment, Submission
from .serializers import AssignmentSerializer, SubmissionSerializer
from .permissions import IsStudent
from rest_framework.generics import ListAPIView
from .models import Submission
from .serializers import SubmissionSerializer
from .permissions import IsInstructor
from rest_framework.generics import UpdateAPIView
from .serializers import GradeSubmissionSerializer
from .permissions import IsCourseInstructor
from rest_framework.permissions import IsAuthenticated


class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsInstructor()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)

# Instructor creates assignment
class AssignmentCreateView(generics.CreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsInstructor]


# List assignments
class AssignmentListView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.AllowAny]


# Student submits assignment
class SubmissionCreateView(generics.CreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [IsStudent]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

class InstructorSubmissionListView(ListAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [IsInstructor]

    def get_queryset(self):
        # Only submissions of instructor's courses
        return Submission.objects.filter(
            assignment__course__instructor=self.request.user
        )

class GradeSubmissionView(UpdateAPIView):
    queryset = Submission.objects.all()
    serializer_class = GradeSubmissionSerializer
    permission_classes = [IsInstructor, IsCourseInstructor]

class StudentSubmissionListView(ListAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Submission.objects.filter(student=self.request.user)
