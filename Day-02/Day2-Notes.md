                    Day=2 Tokens, Statements, Identifiers, Comments, Keywords & Variables 
       ______________________________________________________________________________________________________                      


1. Tokens:
          tokens are the smallest individual units (building blocks) of a Python program.** Every Python program is made up of tokens. 


Types of Tokens:
_____________________________
1.Identifiers
2.Keywords
3.Literals
4.Operators
5.Punctuators

Example:
      age = 20


| Token | Type       |
| ----- | ---------- |
| age   | Identifier |
| =     | Operator   |
| 20    | Literal    |


->Statement 
____________________
               A statement is a single instruction (line of code) that performs an action. 

 Examples:
         x = 10
         print(x)
      
       Both lines are statements.

-->Types:

* Assignment Statement
* Function Call Statement
* Conditional Statement
* Loop Statement

___________________________________________
1.Identifier :
       An identifier is the **name given to variables, functions, classes, or modules.

      Examples:
            age = 20
            name = "Amani"

            def greet():
                 pass
        
Identifiers:

* age
* name
* greet


## Rules for Naming Identifiers:
_____________________________________

✅ Can contain:

* Letters
* Digits
* Underscore (_)

❌ Cannot:

* Start with a digit
* Use Python keywords
* Contain special characters (@, #, $, -, etc.)

-Python is **Case Sensitive**.

Example:

        age
        Age
        AGE
    

*All are different identifiers.

### Valid Identifiers
________________________

       name
       user_name
       score1
       _temp
  

### Invalid Identifiers
__________________________

     1name
     class
     user-name
     @value

->Comments:
_____________
       Comments explain the code. They are ignored by the Python interpreter. 

-> Single-line Comment
        # This is a comment

=> Multi-line Comment
           '''
              This is
              a multi-line
              comment
          '''

        
Uses of Comments:
_______________________

* Explain code
* Improve readability
* Debugging
* Temporarily disable code

2. Keywords:
________________
          Keywords are reserved words that have predefined meanings in Python. They cannot be used as identifiers.

      Examples:
                if
                else
                for
                while
                def
                class
                True
                False
                None
                return
                break
                continue


## How to View Keywords:
_________________________

import keyword

print(keyword.kwlist)
print(len(keyword.kwlist))


-->You cannot write
             if = 10

3.Literals:
_________________________
      Literals are the actual values stored in variables.

    Example:
      age = 21
      name = "Amani"
      price = 99.5

    Here:
       21 → Integer Literal
      "Amani" → String Literal
       99.5 → Float Literal


4.Operators:
_____________________________
   Operators are special symbols or keywords used to perform operations on variables and values.

                Common Operators:
                Arithmetic (+, -, *, /)
                Comparison (==, !=, >, <)
                Logical (and, or, not)
                Assignment (=, +=, -=)
                Membership (in, not in)
                Identity (is, is not)
                Bitwise (&, |, ^)

5.Punctuators:
___________________________
   Punctuators are symbols used to separate, group, or organize different parts of a Python program

            Common punctuators are:(),[],{},:,;,' ,



Variables:
__________________________________________
      A variable is a named memory location used to store data.

     Example
        name = "Amani"
        age = 21

## Variable Naming Rules
__________________________

✅ Must start with:

* Letter
* Underscore

✅ Can contain:

* Letters
* Numbers
* Underscore

❌ Cannot start with a number

Python is Case Sensitive.


## Variable Assignment
________________________
->using '=' operator
          price = 45000

## Multiple Assignment
_________________________
    a, b, c = 10, 20, 30

## Same Value Assignment
_________________________
       x = y = z = 100

## Reassignment
________________________

            x = 5
            x = 10
            Output:10


## Swapping Variables 
_______________________

Without temporary variable

            a = 5
            b = 10
            a, b = b, a

            Output:
            a = 10
            b = 5


## Delete Variable
_______________________

x = 100
del x

After deleting,

        print(x)
        ❌ NameError


