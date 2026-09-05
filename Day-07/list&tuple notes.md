
                               Day 6 PYTHON LISTS & TUPLES 
                _______________________________________________________________
   
LISTS:
Whatis a List?
         A List is an ordered, mutable collection used to store multiple values in a single variable.
          
### Syntax
```python
list1 = []
list2 = list()
```
Example:
```python
numbers = [10, 20, 30]
names = ["Ravi", "Teja", "Ankit"]
mixed = [10, "Python", 5.5, True]
```
Real-Life Example:
Think of a **shopping cart**.
```python
cart = ["Milk", "Bread", "Eggs"]
```
You can:
* Add items
* Remove items
* Change items

# ⭐ List Properties
_______________________________                      
 
 Ordered : Maintains insertion order    
 Mutable :Can modify elements          
 Indexed :Access using index           
 Iterable:Can use loops                
 Allows Duplicates: Duplicate values are allowed 
 Dynamic Size : Can grow or shrink           
 Heterogeneous: Different data types allowed 

# 🔹 List Operations
___________________________________

## 1. Concatenation (+)
Joins two lists.
```python
a=[1,2]
b=[3,4]
print(a+b)
```
Output:
```python
[1,2,3,4]
```
## 2. Repetition (*)
Repeats list elements.
```python
print([1,2]*3)
```
Output
```python
[1,2,1,2,1,2]
```
## 3. Indexing
Access one element.
```python
data=[10,20,30,40]
print(data[0])
print(data[-1])
```
Output
```python
10
40
```
## 4. Slicing
Extract multiple elements.
```python
data=[10,20,30,40,50]
print(data[1:4])
print(data[::-1])
```
Output
```python
[20,30,40]
[50,40,30,20,10]
```
### Remember
* Start → Included
* End → Excluded
* Step → Jump

## 5. Membership Operators
```python
data=[10,20,30]
print(20 in data)
print(100 not in data)
```
Output
```python
True
True
```
# 🔹 Built-in Functions
_______________________________

 `len()` : Number of elements        
 `max()` : Largest element           
 `min()` :  Smallest element          
 `sum()` : Sum of numbers            
 `sorted()`: Returns new sorted list   
 `list()` :Converts iterable to list 

# 🔹 List Methods
____________________________________________

## Adding
 Method      Purpose                  
 `append()`  Add one element          
 `extend()`  Add multiple elements    
 `insert()`  Add at specific position 

## Removing
 Method      Purpose                
 `remove()`  Remove by value        
 `pop()`     Remove by index        
 `clear()`   Remove all elements    
 `del`       Delete element or list 


## Searching
 Method     Purpose            
 `index()`  Returns position   
 `count()`  Counts occurrences 


## Sorting
 Method       Purpose                 
 `sort()`     Sorts original list     
 `reverse()`  Reverse original list   
 `sorted()`   Returns new sorted list 

## sort() vs sorted()

sort()                 sorted()               
Changes original list  Doesn't change original 
Returns None           Returns new sorted list 

## Copy
_____________

```python
copy()
```
Creates a **shallow copy**.

# Nested List
    List inside another list.
```python
marks=[[90,85],[88,92]]
print(marks[0])
print(marks[1][1])
```
Output
```python
[90,85]
92
```
# TUPLES
__________________________________

What is a Tuple?
       A **Tuple** is an **ordered, immutable collection** used to store multiple values in one variable.

### Syntax:
```python
t=()
t=tuple()
```
### Example:
```python
numbers=(10,20,30)
names=("Ravi","Teja")
mixed=(10,"Python",5.5,True)
```
### 💡 Real-Life Example
______________________________
A person's **Date of Birth** never changes.
```python
dob=(15,8,2003)
```
# ⭐ Tuple Properties
_________________________

 Ordered                :     Maintains order                        
 Immutable              :    Cannot modify                          
 Iterable               :    Can use loops                          
 Allows Duplicates      :   Duplicate values allowed               
 Heterogeneous          :    Different data types                   
 Supports Nested Objects :    Can contain lists, tuples, etc.        
 Mutable Objects Can Change :  Mutable objects inside can be modified 
 Faster                    :  Faster than lists                      
 Less Memory               : Uses less memory                       


# 🔹 Creating Tuples
___________________________

## Empty Tuple
```python
t=()
```
## Single Element Tuple
______________________
Correct:
```python
t=(10,)
```
Wrong:
```python
t=(10)
```
This becomes an **integer**, not a tuple.

->Why is the comma required?
Because parentheses alone are treated as grouping operators. The comma tells Python it's a tuple.

 Tuple Operations
 ______________________________

Exactly same as Lists.
## Concatenation
```python
a=(1,2)
b=(3,4)
print(a+b)
```
Output
```python
(1,2,3,4)
```
## Repetition
```python
print((1,2)*3)
```
Output
```python
(1,2,1,2,1,2)
```
## Indexing
```python
data=(10,20,30)
print(data[0])
```
## Slicing
```python
data=(10,20,30,40)
print(data[1:3])
```
Output
```python
(20,30)
```
## Membership
```python
20 in data
100 not in data
```
 Built-in Functions
 _______________________________

 len()   :  Count                     
 max()   : Largest                   
 min()   : Smallest                  
 sum()   : Total                     
 sorted(): Returns List              
 tuple() : Convert iterable to tuple 
 any()   : At least one True         
 all()   : All values True           

### any()
____________
```python
any((0,0,1))
```
Output
```python
True
```
Because one value is True.

### all()
______________
```python
all((1,2,3))
```
Output
```python
True
```
Because every value is True.

# Tuple Methods
______________________

 count() : Counts occurrences   
 index() : Finds first position 

### Why only 2?
Because tuples are **immutable**.

Tuple Packing
_________________________
Automatically creates tuple.
```python
data=10,20,30
```
Output
```python
(10,20,30)
```
Tuple Unpacking
________________________
```python
data=(10,20,30)
a,b,c=data
```
Result
```python
a=10
b=20
c=30
```
Nested Tuple
___________________________
```python
data=((1,2),(3,4))
print(data[1][0])
```
Output
```python
3
```
Immutability
_________________________
Not Allowed
```python
data=(10,20)
data[0]=100
```
Output
```python
TypeError
```
 Mutable Objects Inside Tuple
 ________________________________
Allowed
```python
data=(10,[20,30],40)
data[1].append(50)
print(data)
```
Output
```python
(10,[20,30,50],40)
```
### Why?
The tuple cannot change, but the **list inside it is mutable**.

# 🔹 Why Use Tuples?
Use tuples when:
* Data should not change
* Better memory efficiency
* Faster performance
* Fixed values
* Coordinates
* Database records
* Packing & unpacking

Example
```python
location=(17.3850,78.4867)
```

LIST vs TUPLE
_________________________

                      Feature                               List         Tuple                     
 
                        Syntax                                `[]`         `()`                      
                        Mutable                              ✅ Yes        ❌ No                      
                        Ordered                              ✅            ✅                         
                        Indexed                              ✅            ✅                         
                        Iterable                             ✅            ✅                         
                        Duplicates                           ✅            ✅                         
                        Heterogeneous                        ✅            ✅                         
                        Add Elements                         ✅            ❌                         
                        Remove Elements                      ✅            ❌                         
                        Modify Elements                      ✅            ❌                         
                        Dynamic Size                         ✅            ❌                         
                        Memory                               More           Less                      
                        Speed                               Slower        Faster                    
                        Methods                              Many         Only `count()`, `index()` 
                        sort()                             ✅ Available  ❌ Not available           
                        copy()                             ✅ Available  ❌ Not available           
                        Dictionary Key                     ❌ No         ✅ Yes (if hashable)       
