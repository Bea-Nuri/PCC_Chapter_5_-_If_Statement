#simple if statement
age = 19
if age >= 18:                               #if conditiona test is true
    print("you are old enough to vote")     #proceed to this action
    print("have you registered to vote yet?") # and this action

#if - else statement
#this is for if the condition of if is not met, the we want some actions happening in else,

age = 17
if age >= 18:                               #looking at this we know that the condition is not met, means false
    print("you are old enough to vote")     #then python will SKIP this action,
    print("have you registered to vote yet?")
else:
    print('sorry you are too you to vote')
    print('please register as soon as you turn 18')
