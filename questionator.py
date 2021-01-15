import random
from gtts import gTTS 
import os 

#link: https://pypi.org/project/mpyg321/
questions = [
    "Tell Me About Yourself.",
    "How Did You Hear About This Position?",
    "Why Do You Want to Work at This Company?",
    "Why Do You Want This Job?",
    "Why Should We Hire You?",
    "What Are Your Greatest Strengths?",
    "What Do You Consider to Be Your Weaknesses?",
    "What Is Your Greatest Professional Achievement?",
    "Tell Me About a Challenge or Conflict You’ve Faced at Work, and How You Dealt With It.",
    "Tell Me About a Time You Demonstrated Leadership Skills.",
    "What’s a Time You Disagreed With a Decision That Was Made at Work?",
    "Tell Me About a Time You Made a Mistake.",
    "Tell Me About a Time You Failed.",
    "Why Are You Leaving Your Current Job?",
    "Why Were You Fired?",
    "Why Was There a Gap in Your Employment?",
    "Can You Explain Why You Changed Career Paths?",
    "What’s Your Current Salary?",
    "What Do You Like Least About Your Job?",
    "What Are You Looking for in a New Position?",
    "What Type of Work Environment Do You Prefer?",
    "What’s Your Management Style?",
    "How Would Your Boss and Coworkers Describe You?",
    "How Do You Deal With Pressure or Stressful Situations?",
    "What Do You Like to Do Outside of Work?",
    "Are You Planning on Having Children?",
    "How Do You Prioritize Your Work?",
    "What Are You Passionate About?",
    "What Motivates You?",
    "What Are Your Pet Peeves?",
    "How Do You Like to Be Managed?",
    "Where Do You See Yourself in Five Years?",
    "What’s Your Dream Job?",
    "What Other Companies Are You Interviewing With?",
    "What Makes You Unique?",
    "What Should I Know That’s Not on Your Resume?",
    "What Would Your First 30, 60, or 90 Days Look Like in This Role?",
    "What Are Your Salary Requirements?",
    "What Do You Think We Could Do Better or Differently?",
    "When Can You Start?",
    "Are You Willing to Relocate?",
    "How Many Tennis Balls Can You Fit Into a Limousine?",
    "If You Were an Animal, Which One Would You Want to Be?",
    "Sell Me This Pen.",
    "Is There Anything Else You’d Like Us to Know?",
    "Do You Have Any Questions for Us?"]

def question(opt):
    text = "error"
    if opt == '1':
        index = random.randint(1, len(questions))
        index = index -1
        print("Question "+ str(index)+ ": ")
        question = questions[index]
        print("="*len(question))
        print(question)
        print("="*len(question))
        text = question
    elif opt == '0':
        print("Bye!")
        text = "Bye! Have a nice day."
    
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False) 
    myobj.save("question.mp3")         
    os.system("mpg321 question.mp3") 

def startQuestion():
    option = '0'
    option = input('\n0. Exit; 1. Next question: ') 
    question(option)
    while option != '0':
        option = input('\n0. Exit; 1. Next question: ') 
        question(option)

startQuestion()