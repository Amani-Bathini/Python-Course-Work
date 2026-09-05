                                    Day 7 Sets & Dictionaries 
                              ______________________________________

  SET:
___________________________________
    A set is an unordered, mutable collection that stores unique values.

* Created using {} (with values) or set()
* Automatically removes duplicate values.

### Syntax:
```python
numbers = {10, 20, 30}
names = {"Ravi", "Teja", "Ankit"}
mixed = {10, "Python", 5.5, True}
print(numbers)
```
# Set Properties:
_________________________

                        Property                     Meaning                                                 
                        
                        Unordered                    Elements have no fixed order.                           
                        Mutable                      Can add or remove elements.                             
                        Unindexed                    Cannot access using indexes like `s[0]`.                
                        Iterable                     Can be used in loops.                                   
                        Unique                       Duplicate values are removed automatically.             
                        Heterogeneous                Can store different data types.                         
                        Dynamic Size                 Size changes during execution.                          
                        Supports Immutable Objects   Can store tuples and frozensets.                        
                        Mutable Objects Not Allowed  Cannot store lists, dictionaries, or sets inside a set. 


# Creating Sets
_________________________

## Empty Set:
```python
s = set()
```
> Note: `{}` creates an empty dictionary, not an empty set.

## Duplicate Values
__________________________
```python
data = {10, 20, 30, 20, 10}
print(data)
```
Output:
```python
{10, 20, 30}
```
Duplicates are removed automatically.

# Set Operations
__________________________

## 1. Membership:
Checks whether an element exists.

```python
data = {10, 20, 30}
print(20 in data)
print(100 not in data)
```
Output
```python
True
True
```

## 2. Union ( | )
Combines all unique elements.
```python
a = {1,2,3}
b = {3,4,5}
print(a | b)
```
Output:
```python
{1,2,3,4,5}
```

## 3. Intersection ( & )
Returns common elements.
```python
a = {1,2,3}
b = {2,3,4}
print(a & b)
```
Output:
```python
{2,3}
```

## 4. Difference ( - )
Returns elements present in first set only.
```python
a = {1,2,3}
b = {2,3,4}
print(a - b)
```
Output:
```python
{1}
```

## 5. Symmetric Difference ( ^ )
Returns elements that are in either set but not both.
```python
a = {1,2,3}
b = {2,3,4}
print(a ^ b)
```
Output
```python
{1,4}
```

## 6. Subset ( <= )
Checks whether one set is inside another.

```python
a = {1,2}
b = {1,2,3,4}
print(a <= b)
```
Output:
```python
True
```

## 7. Superset ( >= )
Checks whether one set contains another.

```python
a = {1,2,3,4}
b = {1,2}
print(a >= b)
```
Output:
```python
True
```

# Built-in Functions
_____________________________

                    Function    Purpose                             Example                       
                    
                    `len()`     Number of elements                  `len({1,2,3})` → 3            
                    `max()`     Largest element                     `max({10,20,5})` → 20         
                    `min()`     Smallest element                    `min({10,20,5})` → 5          
                    `sum()`     Sum of numbers                      `sum({1,2,3})` → 6            
                    `sorted()`  Returns sorted list                 `sorted({3,1,2})` → `[1,2,3]` 
                    `set()`     Converts iterable into set          `set("hello")`                
                    `any()`     True if at least one value is True  `any({0,1})`                  
                    `all()`     True if all values are True         `all({1,2,3})`                

# Set Methods
_____________________________
## Adding Methods
-> add():
Adds one element.

```python
s = {10,20}
s.add(30)
```

->update():
Adds multiple elements.

```python
s.update([40,50])
```

## Removing Methods
->remove():
Raises an error if element is absent.

```python
s.remove(20)
```

-> discard():
No error if element is absent.

```python
s.discard(100)
```

->pop():
Removes a random element.

```python
s.pop()
```

->clear():
Removes everything.

```python
s.clear()
```

## Copy
```python
new_set = s.copy()
```
Creates a shallow copy.

## Relation Methods
```python
a.union(b)
a.intersection(b)
a.difference(b)
a.symmetric_difference(b)
```
## Subset & Superset Methods
```python
a.issubset(b)
a.issuperset(b)
a.isdisjoint(b)
```

# Frozenset
_______________
A frozenset is an immutable set.

```python
data = frozenset({10,20,30})
print(data)
```

### Properties

* Immutable
* Unordered
* Unique
* Hashable
* Can be used as dictionary keys
* Can be stored inside another set

# Why Use Sets?

* Remove duplicates
* Fast searching
* Mathematical set operations
* Store unique values
* Efficient comparisons

### Real-life Examples
```python
unique_ids = {101,102,103}

available_sizes = {"S","M","L","XL"}

visited_pages = {"Home","Products","Cart"}
```

# DICTIONARIES
_______________________________________________
        A dictionary stores data in key : value pairs.

Created using {} or dict().

```python
student = {
    "id":101,
    "name":"Ravi",
    "course":"Python"
}
```

# Dictionary Properties
_________________________

                        Property               Meaning                                          
                        
                        Ordered                Maintains insertion order (Python 3.7+)          
                        Mutable                Can add, update and remove items                 
                        Indexed by Keys        Access values using keys                         
                        Iterable               Can loop through keys and values                 
                        Unique Keys            Duplicate keys are not allowed                   
                        Duplicate Values       Allowed                                         
                        Heterogeneous          Mixed data types supported                      
                        Dynamic Size          Can grow or shrink                               
                        Nested Structures      Can contain lists, tuples, sets and dictionaries 
                        Keys Must Be Hashable  Keys should be immutable                         


# Creating Dictionaries
__________________________

## Empty Dictionary

```python
d = {}
```
or

```python
d = dict()
```

## With Values

```python
student = {
    "id":101,
    "name":"Ravi",
    "course":"Python"
}
```

## Using dict():
```python
student = dict(
    id=101,
    name="Ravi",
    course="Python"
)
```

# Dictionary Operations
____________________________

## Access Values

```python
student = {
    "name":"Ravi",
    "age":22
}

print(student["name"])
print(student["age"])
```

## Update Values

```python
student["age"] = 23
```

## Add New Item

```python
student["course"] = "Python"
```

## Remove Item

```python
del student["age"]
```

## Membership:
Checks only **keys**.

```python
print("name" in student)
print("course" not in student)
```

# Built-in Functions
________________________________

                    Function    Purpose                   
                    
                    `len()`     Number of key-value pairs 
                    `max()`     Largest key               
                    `min()`     Smallest key              
                    `sorted()`  Sorted keys               
                    `dict()`    Creates dictionary        
                    `any()`     True if any key is True   
                    `all()`     True if all keys are True 


# Dictionary Methods
____________________________________
## Access Methods

```python
d.get("name")
d.keys()
d.values()
d.items()
```

## Add & Update

```python
d.update({"age":25})
d.setdefault("city","Hyd")
```

## Remove Methods

```python
d.pop("age")
d.popitem()
d.clear()
```

## Copy:

```python
new_dict = d.copy()
```

## Create Dictionary
______________________

```python
dict.fromkeys(["a","b"],0)
```

Output:
```python
{'a': 0, 'b': 0}
```

# Nested Dictionary
_______________________

```python
students = {
    "s1":{
        "name":"Ravi",
        "age":22
    },
    "s2":{
        "name":"Teja",
        "age":21
    }
}

print(students["s1"]["name"])
```
Output:

```python
Ravi
```

# Mutable Values Inside Dictionary
_____________________________________

```python
student = {
    "marks":[90,85,88]
}
student["marks"].append(95)
print(student)
```

Output:
```python
{'marks':[90,85,88,95]}
```

# Valid Dictionary Keys

```python
data = {
    101:"Ravi",
    3.14:"Pi",
    True:"Yes",
    "name":"Python",
    (1,2):"Tuple Key"
}
```
# Why Use Dictionaries?

* Store related information
* Fast lookup using keys
* Represent real-world objects
* Flexible data structure
* Used in JSON, APIs, databases and applications

### Real-life Examples

```python
student = {
    "id":101,
    "name":"Ravi",
    "course":"Python"
}

product = {
    "name":"Laptop",
    "price":50000
}
```

## Set vs Dictionary
_____________________________

                        Set                           Dictionary                    
                        
                        Stores only values            Stores key-value pairs        
                        Unique elements               Unique keys                   
                        Uses `{1,2,3}`                Uses `{"name":"Ravi"}`        
                        No indexing                   Access using keys             
                        Best for removing duplicates  Best for storing related data 



