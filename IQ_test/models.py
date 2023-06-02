from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'IQ_test'
    players_per_group = 4
    num_rounds = 1
    payment_per_correct_answer = 1
    correct_answer1 = 1
    correct_answer2 = 1
    correct_answer3 = 1
    correct_answer4 = 1
    correct_answer5 = 1
    correct_answer6 = 1
    correct_answer7 = 1
    correct_answer8 = 1
    correct_answer9 = 1
    correct_answer10 = 1

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    correct_answer = models.IntegerField()
    combined_score = models.IntegerField(initial=0)
    answer_entered1 = models.IntegerField(label="Q1 Please select your answer", choices=[1, 2, 3, 4, 5, 6, 7, 8])
    answer_entered2 = models.IntegerField(label="Q2 Please select your answer", choices=[1, 2, 3, 4, 5, 6, 7, 8])
    answer_entered3 = models.IntegerField(label="Q3 Please select your answer", choices=[1, 2, 3, 4, 5, 6, 7, 8])
    answer_entered4 = models.IntegerField(label="Q4 Please select your answer", choices=[1, 2, 3, 4, 5, 6, 7, 8])
    answer_entered5 = models.IntegerField(label="Q5 Please select your answer", choices=[1, 2, 3, 4, 5, 6, 7, 8])
    answer_entered6 = models.IntegerField(label="Q6 Please select your answer", choices=[1, 2, 3, 4, 5, 6, 7, 8])
    answer_entered7 = models.IntegerField(label="Q7 Please select your answer", choices=[1, 2, 3, 4, 5, 6, 7, 8])
    answer_entered8 = models.IntegerField(label="Q8 Please select your answer", choices=[1, 2, 3, 4, 5, 6, 7, 8])
    answer_entered9 = models.IntegerField(label="Q9 Please select your answer", choices=[1, 2, 3, 4, 5, 6, 7, 8])
    answer_entered10= models.IntegerField(label="Q10 Please select your answer", choices=[1, 2, 3, 4, 5, 6, 7, 8])
    score1 = models.IntegerField(initial=0)
    score2 = models.IntegerField(initial=0)
    score3 = models.IntegerField(initial=0)
    score4 = models.IntegerField(initial=0)
    score5 = models.IntegerField(initial=0)
    score6 = models.IntegerField(initial=0)
    score7 = models.IntegerField(initial=0)
    score8 = models.IntegerField(initial=0)
    score9 = models.IntegerField(initial=0)
    score10 = models.IntegerField(initial=0)
    result = models.IntegerField(initial=0)
    noisy_feedback1 = models.IntegerField(initial=0)
    noisy_feedback2 = models.IntegerField(initial=0)
    noisy_feedback3 = models.IntegerField(initial=0)
    current_player = models.IntegerField(initial=0)
    NFresult1 = models.IntegerField(initial=0)
    NFresult2 = models.IntegerField(initial=0)
    NFresult3 = models.IntegerField(initial=0)
    gender = models.StringField(
        label="Please state your gender",
        choices=["Male", "Female", "Other", "Prefer not ot say"])
    age = models.StringField(
        label="Please select your age bracket",
        choices=["18-24", "25-30", "30-49", "larger than 49", "Prefer not ot say"])
    education = models.StringField(
        label="Please state your highest obtained level of education",
        choices=["High school or lower", "Bachelor degree", "Master degree", "PhD degree", "Other",
                 "Prefer not ot say"])
    employment = models.StringField(
        label="Please state your current state of employment",
        choices=["Employed", "Unemployed", "Student", "Prefer not ot say"])
    marriage = models.StringField(
        label="Please state your current marital status",
        choices=["Single", "Married", "Other", "Prefer not ot say"])
