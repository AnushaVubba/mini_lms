from django.urls import path
from .views import CourseListCreateView, AssignmentCreateView, AssignmentListView, SubmissionCreateView, InstructorSubmissionListView, GradeSubmissionView, StudentSubmissionListView

urlpatterns = [
    path('', CourseListCreateView.as_view()),
    path('assignments/', AssignmentListView.as_view()),
    path('assignments/create/', AssignmentCreateView.as_view()),
    path('submissions/', SubmissionCreateView.as_view()),
    path('instructor/submissions/', InstructorSubmissionListView.as_view()),
    path('submissions/<int:pk>/grade/', GradeSubmissionView.as_view()),
    path('my-submissions/', StudentSubmissionListView.as_view()),
]
