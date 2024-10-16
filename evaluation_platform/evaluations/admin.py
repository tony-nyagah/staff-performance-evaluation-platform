from django.contrib import admin
from .models import Evaluation, UserEvaluation, Section, UserSection, Goal, UserGoal


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('year', 'start_date', 'submission_deadline')
    search_fields = ('year',)


@admin.register(UserEvaluation)
class UserEvaluationAdmin(admin.ModelAdmin):
    list_display = ('staff_member', 'evaluation')
    search_fields = ('staff_member__full_name', 'evaluation__year')
    list_filter = ('evaluation__year',)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'weight')
    search_fields = ('name',)


@admin.register(UserSection)
class UserSectionAdmin(admin.ModelAdmin):
    list_display = ('user_evaluation', 'section')
    search_fields = ('user_evaluation__staff_member__username', 'section__name')


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('description', 'kpi', 'staff_comment', 'staff_score', 'supervisor_comment', 'supervisor_score')
    search_fields = ('description', 'kpi')


@admin.register(UserGoal)
class UserGoalAdmin(admin.ModelAdmin):
    list_display = ('user_section', 'goal')
    search_fields = ('goal__description', 'user_section__user_evaluation__staff_member__username')
