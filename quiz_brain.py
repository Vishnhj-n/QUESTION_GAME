class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score =0
        
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"Q.{self.question_number} (True/False)")
        self.check_answer(user_answer,current_question.answer)
        
    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            False
            
    def check_answer(self,user_answer,correct_answer): 
       if correct_answer == user_answer.lower():
           print("correct answer")
           self.score+=1
       else:
           print("That's wrong")
       print(f"the correct answer: {correct_answer} ")
       print(f"your current:{self.score}/{self.question_number}")
       print("\n")
     
       
       
     
    
        
        