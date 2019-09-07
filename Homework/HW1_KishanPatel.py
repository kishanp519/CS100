"""
Kishan Patel
CS 100 - Section 019, Fall 2019
HW 01 - September 10th, 2019
"""

# 5b) - My Birthday
month = 5
day = 19
year = 1999

# 5c) - College GPAs
sbu = 3.50
bcc = 4.0
njit = 3.88

# 5d) - Attended Colleges
firstCollege = "Stony Brook University"
secondCollege = "Bergen Community College"
thirdCollege = "New Jersey Institute of Technology"

"""
------------------------------------------------------------------------------------------------------------------------
** Practice with printing information stored with appropriate syntax. **

birthday = str(month) + "/" + str(day) + "/" + str(year) + "."
gpas = str(sbu) + " (SBU), " + str(bcc) + " (BCC), and " + str(sbu) + " (NJIT)."
colleges = firstCollege + ", " + secondCollege + ", and " + thirdCollege + "."

print("My birthday is:", birthday)
print("The GPA for colleges I've attended are:", gpas)
print("The colleges I've attended are:", colleges)

------------------------------------------------------------------------------------------------------------------------
** Exercise 1.1 **

1) - When you leave out one of the parentheses, you get the "SyntaxError: Missing parentheses in call to 'print'" error. 
     - Input: 'print colleges)' -- Printed error above.
   - When you leave out both of the parenthesis, you get a "SyntaxError: Missing parentheses in call to 'print'" error.
     - Input: 'print colleges' -- Printed error above.

2) - When you leave out one of the quotation marks, you get a "SyntaxError: EOL while scanning string literal" error.
     - Input: print("Hello World) -- Printed error above.
   - When you leave out both of the quotation marks, you get a "SyntaxError: invalid syntax" error.
     - Input: print(Hello World) -- Printed error above.

3) - If you put a plus before a number it will just negate the + and leave the number as positive.
     - Input: '+2' -- Returned 2.
   - If you put two +'s between a number it assumes that the second number is positive and continues to perform the
     addition of the two numbers.
     - Input: '2++2' -- Returned 4.
    
4) - If you add a leading zero to a number, you get a "SyntaxError: invalid token" error.
     - Input: '011' -- Printed error above.
     
5) - If you have two values with no operator between them, you get a "SyntaxError: invalid syntax" error.
     - Input: '2 2' -- Printed error above.
------------------------------------------------------------------------------------------------------------------------
** Exercise 1.2 **

1) - There are 2562 seconds in 42 minutes and 42 seconds.
     - Input: '(42 * 60) + 42' -- Returned 2562.
     
2) - There are 6.21 miles in 10 kilometers.
     - Input: '10 / 1.61' -- Returned 6.21.
     
3) - Average pace per mile is 6 minutes and 53 seconds.
     - Input: '(2562 / 6.21) / 60' -- Returned  6.876.
              '0.876 * 60' -- Returned 52.56.
   - Average speed in miles per hour is 8.73 mph.
     - Input: '6.21 / ((42 / 60) + (42 / 60 / 60))' -- Returned 8.73. 

------------------------------------------------------------------------------------------------------------------------
** Exercise 2.1 **

1) - When you do '42 = n', you get a "SyntaxError: can't assign to literal" error. You can't declare a number to a
   variable in that format. It must be '[variableName = number]'.
     - Input: '42 = n' -- Printed error above.
     
2) - When you so 'x = y = 1', you set variables x and y to the value 1.
     - Input: 'x = y = 1' -- Set variables x and y both to 1.
     
3) - When you put a semi-colon at the end of a Python statement, it still runs the statement how it normally would.
     - Input: 'print("Hello World");' -- Printed 'Hello World'.
     
4) - When you put a period at the end of a Python statement, you get a "SyntaxError: invalid syntax" error.
     - Input: 'print("Hello World").' -- Printed error above.
     
5) - If you try multiplying x and y by just putting the letters next to each other, you get a "NameError: name 'xy' is 
     not defined" error because the shell assumes 'xy' is a variable.
     - Input 'xy' (initialized x = 2, and y = 3) -- Printed error above.
------------------------------------------------------------------------------------------------------------------------
** Exercise 2.2 **

1) - The volume of a sphere with radius 5 is 523.60.
     - Input: 'import math'
              '(4/3) * math.pi * math.pow(5,3)' -- Returned 523.60
            
2) - The total wholesale cost for 60 copies would be $945.45.
     - Input: '((24.95 * .60) * 60) + 3 + (.75 * 59)' -- Returned 945.45.
    
3) - After starting your run at 6:52 AM, you spent a total of 38.1 minutes running which led to you getting home at 
     7:30 AM for breakfast.
     - Input: 'timeSpentRunning = ((2 *(8 * 60 + 15)) + (3 * (7 * 60 + 12))) / 60'
              'import datetime'
              'time = datetime.timedelta(hours = 6,minutes = 52) + datetime.timedelta(minutes = timeSpentRunning)' 
              'str(time)' -- Returned 7:30:06.
------------------------------------------------------------------------------------------------------------------------   
"""
