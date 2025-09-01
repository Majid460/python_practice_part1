"""
The match statement is used to perform different actions based on different conditions.

The Python Match Statement
Instead of writing many if..else statements, you can use the match statement.

The match statement selects one of many code blocks to be executed.

match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block

This is how it works:

The match expression is evaluated once.
The value of the expression is compared with the values of each case.
If there is a match, the associated block of code is executed.

"""
day = 3
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _:
      print("Default")
# For no match case _ will execute and it act as default case.
# Default

"""
Combine Values
Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:
"""
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")

# Today is a weekday

"""
If Statements as Guards
You can add if statements in the case evaluation as an extra condition-check:
"""
month = 5
day = 4

match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in may")
    case _:
        print("No match")
# A weekday in may

