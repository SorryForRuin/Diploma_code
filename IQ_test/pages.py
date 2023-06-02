from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class IQ_test1(Page):
    form_model = "player"
    form_fields = ["answer_entered1"]


    def before_next_page(self):
        if Constants.correct_answer1 == self.player.answer_entered1:
            self.player.score1 = Constants.payment_per_correct_answer

class IQ_test2(Page):
    form_model = "player"
    form_fields = ["answer_entered2"]

    def before_next_page(self):
        if Constants.correct_answer2 == self.player.answer_entered2:
            self.player.score2 += Constants.payment_per_correct_answer

class IQ_test3(Page):
    form_model = "player"
    form_fields = ["answer_entered3"]

    def before_next_page(self):
        if Constants.correct_answer3 == self.player.answer_entered3:
            self.player.score3 += Constants.payment_per_correct_answer

class IQ_test4(Page):
    form_model = "player"
    form_fields = ["answer_entered4"]

    def before_next_page(self):
        if Constants.correct_answer4 == self.player.answer_entered4:
            self.player.score4 += Constants.payment_per_correct_answer

class IQ_test5(Page):
    form_model = "player"
    form_fields = ["answer_entered5"]

    def before_next_page(self):
        if Constants.correct_answer5 == self.player.answer_entered5:
            self.player.score5 += Constants.payment_per_correct_answer

class IQ_test6(Page):
    form_model = "player"
    form_fields = ["answer_entered6"]

    def before_next_page(self):
        if Constants.correct_answer6 == self.player.answer_entered6:
            self.player.score6 += Constants.payment_per_correct_answer

class IQ_test7(Page):
    form_model = "player"
    form_fields = ["answer_entered7"]

    def before_next_page(self):
        if Constants.correct_answer7 == self.player.answer_entered7:
            self.player.score7 += Constants.payment_per_correct_answer

class IQ_test8(Page):
    form_model = "player"
    form_fields = ["answer_entered8"]

    def before_next_page(self):
        if Constants.correct_answer8 == self.player.answer_entered8:
            self.player.score8 += Constants.payment_per_correct_answer

class IQ_test9(Page):
    form_model = "player"
    form_fields = ["answer_entered9"]

    def before_next_page(self):
        if Constants.correct_answer9 == self.player.answer_entered9:
            self.player.score9 += Constants.payment_per_correct_answer

class IQ_test10(Page):
    form_model = "player"
    form_fields = ["answer_entered10"]

    def before_next_page(self):
        if Constants.correct_answer10 == self.player.answer_entered10:
            self.player.score10 += Constants.payment_per_correct_answer

class ResultsWaitPage(WaitPage):
    form_model = "player"



    # group_by_arrival_time = True
    def vars_for_template(self):
        self.player.combined_score = self.player.score1 + self.player.score2 + self.player.score3 + self.player.score4 + self.player.score5 + self.player.score6 + self.player.score7 + self.player.score8 + self.player.score9 + self.player.score10
        current_player = self.player.id_in_group

    def after_all_players_arrive(self):
        current_player = self.player.id_in_group
        player1, player2, player3, player4 = self.group.get_players()
        # player3, player4, player5, player6, player7, player8, player9, player10 = self.group.get_players()
        # for p in self.group.get_players():
        #     pass
        def getID(self):
            return self.player.id_in_group
        player_set = [player1, player2, player3, player4]
        id_set = [1, 2, 3, 4]
        for x in id_set:
            if x == getID(self):
                current_player = x
                break
        noisy_feedback1 = random.choice(player_set)
        noisy_feedback2 = random.choice(player_set)
        noisy_feedback3 = random.choice(player_set)

        while noisy_feedback1 == current_player:
            noisy_feedback1 = random.choice(player_set)

        while noisy_feedback2 == current_player or noisy_feedback2 == noisy_feedback1:
            noisy_feedback2 = random.choice(player_set)

        while noisy_feedback3 == current_player or noisy_feedback3 == noisy_feedback1 or noisy_feedback3 == noisy_feedback2:
            noisy_feedback3 = random.choice(player_set)

        # noisy feedback first round
        for x in player_set:
            if noisy_feedback1 == player1:
                if self.player.combined_score > player1.combined_score:
                    self.player.NFresult1 = 2
                if self.player.combined_score == player1.combined_score:
                    self.player.NFresult1 = 1
                if self.player.combined_score < player1.combined_score:
                    self.player.NFresult1 = 0
            if noisy_feedback1 == player2:
                if self.player.combined_score > player2.combined_score:
                    self.player.NFresult1 = 2
                if self.player.combined_score == player2.combined_score:
                    self.player.NFresult1 = 1
                if self.player.combined_score < player2.combined_score:
                    self.player.NFresult1 = 0
            if noisy_feedback1 == player3:
                if self.player.combined_score > player3.combined_score:
                    self.player.NFresult1 = 2
                if self.player.combined_score == player3.combined_score:
                    self.player.NFresult1 = 1
                if self.player.combined_score < player3.combined_score:
                    self.player.NFresult1 = 0
            if noisy_feedback1 == player3:
                if self.player.combined_score > player4.combined_score:
                    self.player.NFresult1 = 2
                if self.player.combined_score == player4.combined_score:
                    self.player.NFresult1 = 1
                if self.player.combined_score < player4.combined_score:
                    self.player.NFresult1 = 0
            if noisy_feedback2 == player1:
                if self.player.combined_score > player1.combined_score:
                    self.player.NFresult2 = 2
                if self.player.combined_score == player1.combined_score:
                    self.player.NFresult2 = 1
                if self.player.combined_score < player1.combined_score:
                    self.player.NFresult2 = 0
            if noisy_feedback2 == player2:
                if self.player.combined_score > player2.combined_score:
                    self.player.NFresult2 = 2
                if self.player.combined_score == player2.combined_score:
                    self.player.NFresult2 = 1
                if self.player.combined_score < player2.combined_score:
                    self.player.NFresult2 = 0
            if noisy_feedback2 == player3:
                if self.player.combined_score > player3.combined_score:
                    self.player.NFresult2 = 2
                if self.player.combined_score == player3.combined_score:
                    self.player.NFresult2 = 1
                if self.player.combined_score < player3.combined_score:
                    self.player.NFresult2 = 0
            if noisy_feedback2 == player4:
                if self.player.combined_score > player4.combined_score:
                    self.player.NFresult2 = 2
                if self.player.combined_score == player4.combined_score:
                    self.player.NFresult2 = 1
                if self.player.combined_score < player4.combined_score:
                    self.player.NFresult2 = 0
            if noisy_feedback3 == player1:
                if self.player.combined_score > player1.combined_score:
                    self.player.NFresult3 = 2
                if self.player.combined_score == player1.combined_score:
                    self.player.NFresult3 = 1
                if self.player.combined_score < player1.combined_score:
                    self.player.NFresult3 = 0
            if noisy_feedback3 == player2:
                if self.player.combined_score > player2.combined_score:
                    self.player.NFresult3 = 2
                if self.player.combined_score == player2.combined_score:
                    self.player.NFresult3 = 1
                if self.player.combined_score < player2.combined_score:
                    self.player.NFresult3 = 0
            if noisy_feedback3 == player3:
                if self.player.combined_score > player3.combined_score:
                    self.player.NFresult3 = 2
                if self.player.combined_score == player3.combined_score:
                    self.player.NFresult3 = 1
                if self.player.combined_score < player3.combined_score:
                    self.player.NFresult3 = 0
            if noisy_feedback3 == player4:
                if self.player.combined_score > player4.combined_score:
                    self.player.NFresult3 = 2
                if self.player.combined_score == player4.combined_score:
                    self.player.NFresult3 = 1
                if self.player.combined_score < player4.combined_score:
                    self.player.NFresult3 = 0


class Feedback(Page):
    def vars_for_template(self):
        self.player.combined_score = self.player.score1 + self.player.score2 + self.player.score3 + self.player.score4 + self.player.score5 + self.player.score6 + self.player.score7 + self.player.score8 + self.player.score9 + self.player.score10
        if self.player.NFresult1 == 2:
            return {
                "NFresult1"
            }
        return {
            "combined_payoff":self.player.combined_score
        }
class Results(Page):
    def vars_for_template(self):
        return {
            "player_ID": self.player.id_in_group
        }
class CombinedResults(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


    def vars_for_template(self):
        self.player.combined_score = self.player.score1 + self.player.score2 + self.player.score3 + self.player.score4 + self.player.score5 + self.player.score6 + self.player.score7 + self.player.score8 + self.player.score9 + self.player.score10
        return {
            "combined_payoff":self.player.combined_score
        }

class SurveyQuestions(Page):
    form_model = "player"
    form_fields = ["gender", "age", "education", "employment", "marriage"]

page_sequence = [IQ_test1, IQ_test2, IQ_test3, IQ_test4, IQ_test5, IQ_test6,
                 IQ_test7, IQ_test8, IQ_test9, IQ_test10, CombinedResults,
                 ResultsWaitPage,Feedback, Results, SurveyQuestions ]
