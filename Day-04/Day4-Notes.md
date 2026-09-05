                      Day 4 – Python Operators, Input Formatting \& Output Formatting
                    ______________________________________________________________________

What is an Operator?

An operator is a special symbol or keyword that performs an operation on values or variables.

     ex: a = 10
         b = 5
         print(a + b)
     o/p:15

Types of Operators:
__________________________________________

1. Arithmetic
2. Comparison
3. Assignment
4. Logical
5. Membership
6. Identity
7. Bitwise


1.Arithmetic Operators

   ->Used for mathematical calculations.

      | Operator | Meaning             | Example  |
      ---------------------------------------------
      | +        | Addition            | 10+5=15  |
      | -        | Subtraction         | 10-5=5   |
      | \*       | Multiplication      | 10\*5=50 |
      | /        | Division            | 10/5=2.0 |
      | //       | Floor Division      | 10//3=3  |
      | %        | Modulus (Remainder) | 10%3=1   |
      | \*\*     | Exponent            | 2\*\*3=8 |


`/` → Returns *float*

`//` → Returns *integer*

`%` → Gives *remainder*

2.Comparison Operators

   ->Compare two values and return **True** or **False**.

         | Operator | Meaning                |
         ------------------------------------   
         |  ==       | Equal                 |
         | !=        | Not Equal             |
         | >         | Greater Than          |
         | <         | Less Than             |
         | >=        | Greater Than or Equal |
         | <=        | Less Than or Equal    |


      Ex:10 > 5
      Output:True

3. Assignment Operators

    ->Assign or update values.

                  | Operator | Example |   
                 ----------------------
                  | =        | x=10    |
                  | +=       | x+=5    |
                  | -=       | x-=2    |
                  | \*=      | x\*=3   |
                  | /=       | x/=2    |
                  | //=      | x//=2   |
                  | %=       | x%=2    |
                  | \*\*=    | x\*\*=2 |

        Ex:x=10
           x+=5
           Output:15

4.Logical Operators

    ->Used to combine conditions.

         | Operator | Meaning                      |
         ------------------------------------------
         | and      | Both conditions must be True |
         | or       | At least one condition True  |
         | not      | Reverses the result          |

         Ex:10>5 and 20>15
         Output: True

-->Truth Table

         AND     
         
     | A | B | Result | 
     | - | - | ------ |  
     | T | T | T      |  
     | T | F | F      |
     | F | T | F      | 
     | F | F | F      | 

       OR            

      | A | B | Result |          
      | - | - | ------ |         
      | T | T | T      |          
      | T | F | T      |          
      | F | T | T      |        
      | F | F | F      |

        NOT

     | A | not A |
     | - | ----- |
     | T | F     |
     | F | T     |

5.Membership Operators

   ->Check whether a value exists in a sequence.

        |  Operator | Meaning     |
        --------------------------
        | in       | Present      |

        | not in   | Not Present  |

     Ex:"apple" in \["apple","banana"]
     Output:True


6.Identity Operators

    ->Check whether two variables refer to the **same object**.

          | Operator | Meaning           |
         -------------------------------=
          | is       | Same object       |
          | is not   | Different objects |

       Example :a=\[1,2]
                b=a
                print(a is b)
                Output:True

7. Bitwise Operators

     =>Work on binary numbers (0 and 1).

              | Operator | Meaning    |
              --------------------------
              | \&       | AND        |
              | |        | OR         |
              | ^        | XOR        |
              | \\\~     | NOT        |
              | <<       | Left Shift |
              | >>       | Right Shift|


Input Formatting
_____________________________________________________________

-->input():Used to take input from the user.

      input()` always returns a string

      Ex: name=input("Enter name:")

* Integer Input:

      age=int(input("Enter age:"))

* Float Input:

      price=float(input("Enter price:"))

* List of Strings:

      names=input().split()
      Output:\['A','B','C']

* Tuple of Strings:

      tuple(input().split())

* Set of Strings:

      set(input().split())
      ->Duplicates are removed automatically. 

* List of Integers:
 
    list(map(int,input().split()))

* Tuple of Integers:

        tuple(map(int,input().split()))

* Set of Integers:

        set(map(int,input().split()))

######eval():
_____________________________________________________

-Converts input into the appropriate Python datatype automatically.                                             

                          data=eval(input())

Can accept:

* List
* Tuple
* Dictionary
* Set
* Integer
* Float
* Boolean



###### **Multiple Inputs**
_____________________________________________________________

* String:

         username,password=input().split()

* Integer:

         a,b=map(int,input().split())

 Output Formatting
____________________________________________________________

1. print():Used to display output.

       Syntax: print(object, sep=' ', end='\\n')

2. sep Parameter: Changes the separator.

       print(2026,7,15,sep="-")

       Output:2026-7-15

3. end Parameter: Changes what is printed at the end.

       print("Hello",end=" ")

       print("World")

       Output:Hello World

##Escape Characters:

           | Escape | Meaning   |
           ---------------------
           | \n  | New Line     |
           | \t  | Tab Space    |
           | \\  | Backslash    |
           | '   | Single Quote |
           | "   | Double Quote |


Output Formatting Methods:
_______________________________________________________________

1. Using Commas

         print("Age:",25)

2. Using %

       print("Age:%d"%25)

3. Using f-Strings

      name="Amani"
      age=21
      print(f"Name:{name}, Age:{age}")

4. Using format()

       print("Name:{} Age:{}".format("Amani",21))








