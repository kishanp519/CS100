"""
Kishan Patel
CS 100 - Section 019, Fall 2019
HW 01, September 10th 2019
"""

# 5b) - My Birthday
month = 5
day = 19
year = 1999

# 5c) - College GPAs
sbu = 3.40
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
     - Input: 'print colleges)' -- Returned error above.
   - When you leave out both of the parenthesis, you get a "SyntaxError: Missing parentheses in call to 'print'" error.
     - Input: 'print colleges' -- Returned error above.

2) - When you leave out one of the quotation marks, you get a "SyntaxError: EOL while scanning string literal" error.
     - Input: print("Hello World) -- Returned error above
   - When you leave out both of the quotation marks, you get a "SyntaxError: invalid syntax" error.
     - Input: print(Hello World) -- Returned error above.

3) - If you put a plus before a number it will just negate the + and leave the number as positive.
     - Input: '+2' -- Returned 2.
   - If you put two +'s between a number it assumes that the second number is positive and continues to perform the
     addition of the two numbers.
    - Input: '2++2' -- Returned 4.
    
4) - If you add a leading zero to a number, you get a "SyntaxError: invalid token" error.
     - Input: '011' -- Returned error above.
     
5) - If you have two values with no operator between them, you get a "SyntaxError: invalid syntax" error.
     - Input: '2 2' -- Returned error above.
------------------------------------------------------------------------------------------------------------------------
** Exercise 1.2 **

1) - There are 2562 seconds in 42 minutes and 42 seconds.
     - Input: '(42 * 60) + 42' -- Returned 2562.
     
2) - There are 6.21 miles in 10 kilometers.
     - Input: '10 / 1.61' -- Returned 6.21.
     
3) - Average pace per mile is 6 minutes and 53 seconds.
   - Input: '(2562 / 6.21) / 60' -- Returned  6.876.
            '0.876 * 60' -- Returned 52.56.

------------------------------------------------------------------------------------------------------------------------
    1
"""