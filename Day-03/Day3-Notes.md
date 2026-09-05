                     Day 3 – Data Types \& Type Conversions
         _______________________________________________________________________________
                                                                                                                                                                                                                                                                          
What is a Data Type?

A Data Type defines:

             *What type of value is stored
             *How memory is allocated
             *Whether the value can be modified (Mutable/Immutable)
             *How Python manages the data internally

             Example: x = 10
               name = "Amani"
               price = 99.5

-->Python automatically identifies:

       * `10` → `int`
       * `"Amani"` → `str`
       * `99.5` → `float`
------------------------------


Types of Data Types:
_________________________________________________
                                                                                  
1. Numeric
2. Sequence
3. Set
4. Mapping
5. Boolean
6. None

                                                                   
1.Numeric Data Types:Used to store numbers.

    a) int: Stores whole numbers.

         age = 21
         Examples:
                Age
               mProduct Quantity
               mEmployee ID

    b) float: Stores decimal numbers.

        price = 749.99 
        Examples:
              Product Price
              Temperature
              Height

    c) complex:Stores real + imaginary numbers.

          z = 5 + 2j
          Used in:
             Scientific Calculations
             Signal Processing

2.Sequence Data Types:Sequence means data stored in order.

     Characteristics:
              Ordered
              Indexed
              Can access using index

     Types:

        * String
        * List
        * Tuple

     a) String (str):Stores text.

          name = "Python"
          Examples:
                 Name
                 City
                 Email
          Properties:
                 Ordered
                 Indexed
                 Immutable


     b) List:Stores multiple values.

         fruits = ["Apple","Banana","Mango"]

         Properties:
               * Ordered
               * Indexed
               * Allows duplicates
               * Mutable
        Example:
            fruits\[0] = "Orange"
        Real-life Examples:
            * Shopping Cart
            * Student Marks
            * Employee Names


    c) Tuple:Stores fixed values.

            days = ("Mon","Tue","Wed")
            Properties:
                   * Ordered
                   * Indexed
                   * Immutable
                   * Faster than List
            Real-life Examples:
                   * Coordinates
                   * RGB Colors
                   *  Date of Birth

3.Set Data Types:Stores unique values only.

    a) Set
       colors = {"Red","Blue","Green"}
       Properties:
           * Unique values
           * Unordered
           * No Index
           * Mutable
     ->Duplicates removed automatically.
      {"A","A","B"}
      Output:{"A","B"}

    b) Frozen Set

       Immutable version of Set.
       tags = frozenset(\["Python","AI"])

       Properties:

         * Unique
         * Unordered
         * Immutable



4.Dictionary (dict):Stores data as **Key : Value** pairs.

     Example:
     student = {
          "name":"Amani",
          "age":21
          }


     Properties:

         Mutable
         Ordered (Python 3.7+)
         No duplicate keys

     Real-life Example:

          -> Student Record
           Roll No → Student
           Product ID → Product
           Username → Password


5. Boolean:

  -> Stores only

        True
        False

  -> Used in

        * Conditions
        * Decision Making
        * Comparisons

        Example:
           is    logged = True

6.None Type

      Represents **No Value**.
      Ex:name = None

      Used when:

           Value not assigned
           Placeholder
           Empty state



Mutable vs Immutable
_________________________________________________

->Mutable:Can change after creation.

     Examples
           * List
           * Set
           * Dictionary

->Immutable:Cannot change after creation.

     Examples
          * int
          * float
          * complex
          * str
          * tuple
          * frozenset
          * bool
          * NoneType


#Ordered vs Unordered
___________________________________________________

->Ordered

        * String
        * List
        * Tuple
        * Dictionary

->Unordered

        * Set
        * Frozen Set


#Indexed vs Non-Indexed

->Indexed

      * String
      * List
      * Tuple

->Non-Indexed

      * Set
      * Frozen Set
      * Dictionary (access is by keys, not index)

**Checking Data Type**
___________________________________________

      x = 10
      print(type(x))
      Output:
          <class 'int'>


Type Conversion
____________________________________________
->Converting one datatype into another.

Examples

     int("100")
     Output:100
     float(10)
     Output:10.0
     str(100)
     Output:"100"
     list("Python")
     Output:['P','y','t','h','o','n']



Type Conversions Allowed in Python:
-->int:float,complex,bool,str	   
-->float:int,float,complex,bool,str
-->complex:bool,str
-->bool:int,float,complex,string
-->str:int,float,bool,str,list,tuple,set
-->list:bool,str,list,tuple,set
-->tuple:bool,str,list,set
-->set:bool,str,list,tuple
-->dictionary:bool,str,list,tuple,set



**Boolean Rules**
______________________________________________

     These values return False:

         bool(0)
         bool(0.0)
         bool("")
         bool(\[])
         bool(())
         bool(set())
         bool({})
         bool(None)
    Everything else (non-empty values) returns True.


