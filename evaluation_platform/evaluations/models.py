from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Evaluation(models.Model):
    year = models.IntegerField()
    start_date = models.DateField(blank=True, null=True)
    submission_deadline = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Evaluation for {self.year}"


class UserEvaluation(models.Model):
    staff_member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)

    def __str__(self):
        return f"Evaluation for {self.staff_member} in {self.evaluation.year}."


class Section(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField()
    weight = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        validators=[MinValueValidator(0.00), MaxValueValidator(1.00)],
    )

    def __str__(self):
        return self.name


class UserSection(models.Model):
    user_evaluation = models.ForeignKey(
        UserEvaluation, related_name="sections", on_delete=models.CASCADE
    )
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def section_score(self):
        goals = self.user_goals.all()
        supervisor_scores = [
            goal.supervisor_score for goal in goals if goal.supervisor_score is not None
        ]
        if supervisor_scores:
            avg_supervisor_score = sum(supervisor_scores) / len(supervisor_scores)
            return (avg_supervisor_score / 4) * (self.section.weight / 100)
        return 0

    def __str__(self):
        return f"{self.section.name}({self.user_evaluation.staff_member.full_name} - {self.user_evaluation.evaluation.year})"


class Goal(models.Model):
    description = models.TextField()
    kpi = models.TextField()
    staff_comment = models.TextField(blank=True, null=True)
    staff_score = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0.00), MaxValueValidator(5.00)],
    )
    supervisor_comment = models.TextField(blank=True, null=True)
    supervisor_score = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0.00), MaxValueValidator(5.00)],
    )


class UserGoal(models.Model):
    user_section = models.ForeignKey(
        UserSection, related_name="user_goals", on_delete=models.CASCADE
    )
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.goal.description}"
