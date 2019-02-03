## Static Method

    * Methods that are bound to class rather than it's object.
    * They don't require a class instance creation. 
        * (So not dependent on state of
  the object)

Difference b/w **Static Method** and a **Class Method**:
    
    * Static method - knows nothing about the class and just deals with the
      parameters. 
    * Class method - works with the class since it's params is always the class
      itself.

Implementation:

```python
class.staticmethodFunc()
# or even
class().staticmethodFunc()
```

**Example**: Creating a static method using staticmethod()

```python
class Mathematics:
  def addNumber(x, y):
    return x + y

# create addNumbers static method
Mathematics.addNumbers = staticmethod(Mathematics.addNumbers)

print("The sum is: ", Mathematics.addNumbers(5, 10))
```  
