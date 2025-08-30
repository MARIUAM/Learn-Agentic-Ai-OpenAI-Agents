# 📋 Learnt Python Built-in Functions (with purpose)



| Function         | Purpose                                                       |
| ---------------- | ------------------------------------------------------------- |
| `abs()`          | Number ka absolute value deta hai                             |
| `aiter()`        | Asynchronous iterator return karta hai                        |
| `all()`          | True return karta hai agar iterable ke sab elements true hain |
| `any()`          | True return karta hai agar iterable me koi ek element true ho |
| `anext()`        | Asynchronous iterator se next value leta hai                  |
| `ascii()`        | Object ka printable ASCII representation return karta hai     |
| `bin()`          | Integer ko binary string me convert karta hai                 |
| `bool()`         | Value ko boolean (True/False) me convert karta hai            |
| `breakpoint()`   | Debugger start karta hai                                      |
| `bytearray()`    | Mutable byte sequence banata hai                              |
| `bytes()`        | Immutable byte sequence banata hai                            |
| `callable()`     | Check karta hai ki object callable hai ya nahi                |
| `chr()`          | Unicode code point ko character me convert karta hai          |
| `classmethod()`  | Function ko class method banata hai                           |
| `compile()`      | Source code ko Python code object me compile karta hai        |
| `complex()`      | Complex number banata hai                                     |
| `delattr()`      | Object ka attribute delete karta hai                          |
| `dict()`         | Dictionary banata hai                                         |
| `dir()`          | Object ke attributes/methods ki list deta hai                 |
| `divmod()`       | Division ka quotient aur remainder tuple me deta hai          |
| `enumerate()`    | Iterable ke index-value pairs deta hai                        |
| `eval()`         | String ko Python expression ki tarah evaluate karta hai       |
| `exec()`         | String ko Python code ki tarah execute karta hai              |
| `filter()`       | Function ke condition pass karne wale items filter karta hai  |
| `float()`        | Value ko float me convert karta hai                           |
| `format()`       | Value ko format karta hai (string formatting ke liye)         |
| `frozenset()`    | Immutable set banata hai                                      |
| `getattr()`      | Object ka attribute value return karta hai                    |
| `globals()`      | Global variables ka dictionary return karta hai               |
| `hasattr()`      | Check karta hai ki object me attribute hai ya nahi            |
| `hash()`         | Object ka hash value return karta hai                         |
| `help()`         | Python ka built-in help system open karta hai                 |
| `hex()`          | Integer ko hexadecimal string me convert karta hai            |
| `id()`           | Object ka unique ID (memory address) return karta hai         |
| `input()`        | User se input leta hai                                        |
| `int()`          | Value ko integer me convert karta hai                         |
| `isinstance()`   | Check karta hai object kis class ka instance hai              |
| `issubclass()`   | Check karta hai ek class dusri class ki subclass hai ya nahi  |
| `iter()`         | Iterator return karta hai                                     |
| `len()`          | Iterable ki length return karta hai                           |
| `list()`         | List banata hai                                               |
| `locals()`       | Local variables ka dictionary return karta hai                |
| `map()`          | Function ko iterable ke har element par apply karta hai       |
| `max()`          | Iterable ka maximum element return karta hai                  |
| `memoryview()`   | Memory view object banata hai                                 |
| `min()`          | Iterable ka minimum element return karta hai                  |
| `next()`         | Iterator ka next element return karta hai                     |
| `object()`       | Ek new base object banata hai                                 |
| `oct()`          | Integer ko octal string me convert karta hai                  |
| `open()`         | File open karta hai                                           |
| `ord()`          | Character ka Unicode code point return karta hai              |
| `pow()`          | Exponentiation (power) calculate karta hai                    |
| `print()`        | Output console pe print karta hai                             |
| `property()`     | Class ka managed attribute banata hai                         |
| `range()`        | Number sequence generate karta hai                            |
| `repr()`         | Object ka string representation return karta hai              |
| `reversed()`     | Iterable ko reverse order me return karta hai                 |
| `round()`        | Number ko round karta hai                                     |
| `set()`          | Set banata hai                                                |
| `setattr()`      | Object ke attribute ki value set karta hai                    |
| `slice()`        | Slice object banata hai                                       |
| `sorted()`       | Iterable ko sort karke return karta hai                       |
| `staticmethod()` | Function ko static method banata hai                          |
| `str()`          | Value ko string me convert karta hai                          |
| `sum()`          | Iterable ke elements ka sum return karta hai                  |
| `super()`        | Parent class ka object return karta hai                       |
| `tuple()`        | Tuple banata hai                                              |
| `type()`         | Object ka type return karta hai                               |
| `vars()`         | Object ka attribute dictionary return karta hai               |
| `zip()`          | Multiple iterables ko combine karta hai                       |
| `__import__()`   | Dynamically module import karta hai                           |


# 📌 Python Built-in Functions with Use Cases + Example Codes

---





## 🔹 1. Numeric and Math Functions

| Function | Use Case | Example Code |
|----------|----------|--------------|
| `abs()` | Negative number ko positive me convert karna | `print(abs(-10))  # 10` |
| `divmod()` | Quotient aur remainder ek sath lena | `print(divmod(9, 2))  # (4, 1)` |
| `pow()` | Power calculate karna | `print(pow(2, 3))  # 8` |
| `round()` | Number ko round karna | `print(round(3.567, 2))  # 3.57` |
| `sum()` | List/iterable ke numbers ka sum | `print(sum([1,2,3,4]))  # 10` |
| `max()` | List me maximum value dhoondhna | `print(max([10, 5, 20]))  # 20` |
| `min()` | List me minimum value dhoondhna | `print(min([10, 5, 20]))  # 5` |

---

## 🔹 2. Type Conversion Functions

| Function | Use Case | Example Code |
|----------|----------|--------------|
| `int()` | String ko integer me convert karna | `print(int("10"))  # 10` |
| `float()` | Integer ko float me convert karna | `print(float(5))  # 5.0` |
| `str()` | Value ko string me convert karna | `print(str(123))  # '123'` |
| `bool()` | Value ko True/False me convert karna | `print(bool(0))  # False` |
| `complex()` | Complex number banana | `print(complex(2, 3))  # (2+3j)` |
| `list()` | Iterable ko list me convert karna | `print(list("abc"))  # ['a','b','c']` |
| `tuple()` | Iterable ko tuple me convert karna | `print(tuple([1,2,3]))  # (1,2,3)` |
| `set()` | Duplicate hata kar set banana | `print(set([1,2,2,3]))  # {1,2,3}` |
| `frozenset()` | Immutable set banana | `print(frozenset([1,2,3]))` |
| `dict()` | Dictionary banana | `print(dict(a=1, b=2))  # {'a':1,'b':2}` |
| `bytes()` | Immutable byte sequence banana | `print(bytes("Hi", "utf-8"))` |
| `bytearray()` | Mutable byte sequence banana | `ba = bytearray("Hi","utf-8"); ba[0]=65; print(ba)` |
| `memoryview()` | Memory efficient object banana | `print(memoryview(b"hello"))` |

---

## 🔹 3. Iteration and Functional Tools

| Function | Use Case | Example Code |
|----------|----------|--------------|
| `len()` | Iterable ki length nikalna | `print(len("hello"))  # 5` |
| `range()` | Numbers ka sequence banana | `print(list(range(5)))  # [0,1,2,3,4]` |
| `enumerate()` | Index ke sath iterate karna | `for i,v in enumerate(['a','b']): print(i,v)` |
| `map()` | Function ko iterable ke har element pe apply karna | `print(list(map(str.upper, ['a','b'])))` |
| `filter()` | Condition wale elements ko filter karna | `print(list(filter(lambda x: x>2,[1,2,3,4])))` |
| `zip()` | Multiple iterables ko combine karna | `print(list(zip([1,2],['a','b'])))  # [(1,'a'),(2,'b')]` |
| `iter()` | Iterator banana | `it = iter([1,2,3]); print(next(it))  # 1` |
| `next()` | Iterator ka next element lena | `print(next(iter([10,20])))  # 10` |
| `reversed()` | Sequence ko reverse karna | `print(list(reversed([1,2,3])))  # [3,2,1]` |
| `sorted()` | List ko sort karna | `print(sorted([3,1,2]))  # [1,2,3]` |

---

## 🔹 4. Object and Attribute Handling

| Function | Use Case | Example Code |
|----------|----------|--------------|
| `type()` | Object ka type check karna | `print(type(123))  # <class 'int'>` |
| `isinstance()` | Check karna object kis class ka hai | `print(isinstance(5,int))  # True` |
| `issubclass()` | Check karna ek class dusre ki subclass hai ya nahi | `print(issubclass(bool,int))  # True` |
| `getattr()` | Object ka attribute lena | `print(getattr(str,'upper'))` |
| `setattr()` | Object me attribute set karna | `class A: pass; a=A(); setattr(a,'x',10); print(a.x)` |
| `hasattr()` | Check karna object me attribute hai ya nahi | `print(hasattr("hi","upper"))  # True` |
| `delattr()` | Object ka attribute delete karna | `class A: x=5; delattr(A,'x')` |
| `property()` | Getter/setter define karna class ke liye |  
```python






<br>

class A:  
    def __init__(self):  
        self._x=0  

    def getx(self):  
        return self._x  

    x = property(getx)  

a = A()  
print(a.x)  
``` |

---



📌 Python Built-in Functions with Use Cases + Example Codes


class A:  
    def __init__(self): self._x=0  
    def getx(self): return self._x  
    x = property(getx)  
a=A(); print(a.x)  
``` |

---

## 🔹 5. Input/Output and Files
| Function | Use Case | Example Code |
|----------|----------|--------------|
| `print()` | Output print karna | `print("Hello")` |
| `input()` | User se input lena | `name = input("Enter name: ")` |
| `open()` | File open karna | `f = open("file.txt","w"); f.write("Hi")` |

---

## 🔹 6. Utility and Reflection
| Function | Use Case | Example Code |
|----------|----------|--------------|
| `dir()` | Object ke attributes/methods dekhna | `print(dir(str))` |
| `vars()` | Object ke attributes dictionary | `print(vars(int))` |
| `globals()` | Global variables ka dict | `print(globals())` |
| `locals()` | Local variables ka dict | `print(locals())` |
| `id()` | Object ka unique ID (memory) | `print(id(10))` |
| `hash()` | Object ka hash value | `print(hash("hi"))` |
| `help()` | Help documentation dekhna | `help(str)` |
| `callable()` | Check karna object callable hai ya nahi | `print(callable(len))` |

---

## 🔹 7. String & Character Conversion
| Function | Use Case | Example Code |
|----------|----------|--------------|
| `chr()` | Unicode code ko character banana | `print(chr(65))  # 'A'` |
| `ord()` | Character ka Unicode code point lena | `print(ord('A'))  # 65` |
| `ascii()` | Object ka ASCII representation lena | `print(ascii("😀"))  # '\\U0001f600'` |
| `bin()` | Integer ko binary string banana | `print(bin(10))  # 0b1010` |
| `oct()` | Integer ko octal string banana | `print(oct(10))  # 0o12` |
| `hex()` | Integer ko hex string banana | `print(hex(10))  # 0xa` |
| `format()` | String formatting | `print(format(255, 'x'))  # 'ff'` |
| `repr()` | Object ka string representation | `print(repr("hi"))  # "'hi'"` |

---

## 🔹 8. Code Execution
| Function | Use Case | Example Code |
|----------|----------|--------------|
| `eval()` | String ko Python expression ki tarah run karna | `print(eval("2+3"))  # 5` |
| `exec()` | String ko code ki tarah execute karna | `exec("x=5; print(x)")` |
| `compile()` | Code ko compile karna execution ke liye | `code=compile("5+5","","eval"); print(eval(code))` |

---

## 🔹 9. Class/Method Decorators
| Function | Use Case | Example Code |
|----------|----------|--------------|
| `staticmethod()` | Class me static method banana |  
```python
class A:  
    @staticmethod  
    def hi(): return "hi"  
print(A.hi())  
``` |
| `classmethod()` | Class level method banana |  
```python
class A:  
    @classmethod  
    def hi(cls): return "class method"  
print(A.hi())  
``` |
| `super()` | Parent class method call karna |  
```python
class A: def hi(self): return "A"  
class B(A):  
    def hi(self): return super().hi()+" B"  
print(B().hi())  
``` |

---

## 🔹 10. Importing & Debugging
| Function | Use Case | Example Code |
|----------|----------|--------------|
| `__import__()` | Dynamically module import karna | `math = __import__('math'); print(math.sqrt(16))` |
| `breakpoint()` | Debugger start karna | `breakpoint()` |
| `aiter()` | Async iterator banana | `# Python async use case` |
| `anext()` | Async iterator se next lena | `# Python async use case` |

---

✅ yA **saare built-in functions ke use cases + code examples** hain.  


