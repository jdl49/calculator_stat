[![Build Status](https://travis-ci.com/kaw393939/calculator.svg?branch=master)](https://travis-ci.com/kaw393939/calculator)

# calculator
The calculator class is an example of encapsulation. It encapsulates all the logic of a basic calculator. 

    class Calculator:
        result = 0

        def __init__(self):
            pass

        def add(self, a, b):
            self.result = addition(a, b)
            return self.result

        def subtract(self, a, b):
            self.result = subtraction(a, b)
            return self.result
        
Using the add method, data variables a and b are past to the Addition function and return a result.
        
    def addition(a, b):
    return float(a) + float(b)


# Statistics
The same process is use when calling then mean method in statistics.
class Statistics(Calculator):

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

# Abstraction

An example of abstraction. We use this fuction in test_statistics.py to get then mean of 
random data. All you need to do is enter in random data and get the result. 

    def test_mean_calculator(self):
        mean = self.statistics.mean(self.testData)

The implementation detail's are hidden 

test_statistics ----> statistics
class Statistics(Calculator): s

    def mean(self, data):
        self.result = mean(data)
        return self.result
        
       statistics -----> Mean
        
        def mean(data):
    num_values = len(data)
    total = 0
    for num in data:
        total = addition(total, num)
    return division(num_values, total)
    
    Mean -----> Addition
    def addition(a, b):
    return float(a) + float(b)

Then back up returning the mean result.

#Polymorphism


Mean many shapes in greek. Its role in coding explains that any class can 
be inherited by multiple classes of different type but still function independently and with out conflicting
one another. 

    def test_multiple_calculators(self):
        calculator1 = Calculator()
        calculator2 = Calculator()
        self.calculator.addition(calculator1.addition(1, 2), calculator2.subtraction(3, 4))
        self.assertEqual(2, self.calculator.result)
        
As you can see here each calculator class inherits Calculator() but each do its
own operations. This is proven when they are all then added together using another calculator. 
