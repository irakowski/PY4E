"""Exercise 7: Rewrite the grade program from the previous chapter 
using a function called computegrade that takes a score as its parameter 
and returns a grade as a string."""

print('Program Execution:')
score = input("Enter Score: ")

def computegrade(score):
    try:
        score = float(score)
    except:
        print("Bad Score")
        quit()
    if score > 1:
        print("Bad Score")
        quit()
    elif score < 0.6:
        return "F"
    elif score >= 0.6 and score < 0.7:
        return "D"
    elif score >= 0.7 and score < 0.8:
        return "C"
    elif score >= 0.8 and score < 0.9:
        return "B"
    else: 
        return "A"

print(computegrade(score))
