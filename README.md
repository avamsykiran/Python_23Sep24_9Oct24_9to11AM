Python
---------------------------------------------

    Objectives
        Python Basics, 
        Logic and Conditional Flow in Python , 
        Dictionaries and Sets in Python, 
        Files and Input/Output , 
        Errors and Exceptions , 
        Functions and Modules , 
        Classes and OOP , 
        Python Library: 
            NumPy,
            SciPy,
            matplotlib,
            Pandas, 
            requests, 
            streamlit, 
            pytest
        Package Manager – Pip
        Webframework – FastApi
        AI Framework – Langchain, LlamaIndex

    Intro

        Python was developed by Guido van Rossum in the late eighties and early nineties at the National Research Institute for Mathematics and Computer Science in the Netherlands..

        Python is derived from many other languages, including ABC, Modula-3, C, C++, Algol-68, SmallTalk, and Unix shell and other scripting languages

        Easy-to-learn
        Easy-to-read
        Easy-to-maintain
        A broad standard library
        Interactive Mode
        Portable
        Extendable
        GUI Programming
        Scalable

    Lab Setup

        Python  3.13.x or above
        VSCode as an IDE 

    Characteristics

        1. case sensitive
        2. no statement terminator, but each line is assumed to be a single statement.
        3. no block statement either, the blocks are organized as indented statements.
            an indent can be of spaces of any length but 4 spaces is the general standard.
            statements belonging to the same block must have the indent of equal length.

        //java / C#
        if cond {
            statement1;
            statement2;
        }
        statement 3;

        #python

        if cond :
         statement1
         statement2
        statement3

    Tokens

        is the samllest indivisible part of a script or code.

        Identifiers
            are the names givne to program resources like variabels, classes, objects, functions ..etc.,

            1. an identifier should start with a letter or _
            2. an identifier can be of any length
            3. an identifier can not contian spaces and special character other than alphabet and digits.
            4. a class identifier is expected to start with a capital letter and all other idenfiers
                are expected start with lower case letters.
            
            5. if an identifier start with an _ (underscore), it is understood as a private resource
            6. if an identifier start with an __(dbl underscore), it is understood as a strongly private resource
            7. certtain language pre-defiend identifers start and end with __ (dbl-underscores)
                  
        Keywords
            are reserved word in any language and python keywords are lower in case .

        Operators
            Arithemtic
                    +   addition        sum
                    -   substraction    difference
                    *   multiplication  product
                    /   division        quitiont
                    %   division        reminder
                    **  exponent
                    //  floor division  quitiont

                            7/2     3.5
                            7//2    3

            Relational
                    ==  is equal to
                    !=  is not equal to
                    <   is less than
                    >   is greater than
                    <=  is less than or equal to
                    >=  is greater than or equal to

            Logical Operators
                    and         cond1 and cond2
                                    when cond1 is found false, cond2 is not evaluated at all
                                    and this is called short circuit.

                    or          cond1 or cond2
                                    when cond1 is found true, cond2 is not evaluated at all
                                    and this is called short circuit.

                    not

            Assignment Operators
                    =
                    +=      a+=b        a = a+b
                    -=
                    /=
                    *=
                    **=
                    //=
                    &=
                    |=
                    ^=
                    ~=
                    <<=
                    >>=

            Identity Operators
                is              x is Type
                is not          x is not Type

            Memebrship check operator
                in              x in obj
                not in          x not in obj

            Bitwise operators
                &       x = 4 & 7
                            0100 & 0111 = 0100
                |       x = 4 | 7
                            0100 | 0111 = 0111
                ^       x = 4 ^ 7
                            0100 ^ 0111 = 1100
                ~       x = ~4
                            ~0100 = 1011
                            
                <<      left shift              x<<3  means that the binary value of x is shifted 3 places left side
                                                if x is     1001 1001
                                                x<<3    is  1 1001 000
                                                x<<2    is  01 1001 00
                                                x<<1    is  001 1001 0

                >>      right shift             x>>3  means that the binary value of x is shifted 3 places right side
                                                if x is     1001 1001
                                                x>>3    is  000 1001 1
        
        Comments
                #to give a comment
                """
                    is a multi line string
                    but if not assigned to any variable
                    python ignores it and hence
                    can be used as a mulitline comment
                """

        Literals
                is a hard coded value in an expression.

                c = 2 * PI * r

                    PI is a constant identifier
                    r and c are variable identifiers
                    = and * are operators
                    2 is literal

                integer             0 to 9      12,3,8 
                floating point      .           3.15,5.67
                string              'is a string leteral' , " is also a string letral " 
                                    """
                                            are used for
                                            multi line string
                                    """
                boolean             False,True

    Variables and Data Types

        dynamically typed languages

        x = 56
        y = "Hello World"

        Text Type:	    str
        Numeric Types:	int, float, complex
        Sequence Types:	list, tuple, range          #Linear data structures
        Mapping Type:	dict                        #dictonaries or key-value pairs
        Set Types:	    set, frozenset              #Non Linear Dat aStructures
        Boolean Type:	bool
        Binary Types:	bytes, bytearray, memoryview

        type casting:   str(x) will convert int x into a string.

    Control Strucutres

        Branching Statements 

            simple if
                if cond:
                 statements_under_if_block.... 

            if..else
                if cond:
                 statements_under_if_block....
                else:
                 statements_under_else_block....

            if ladder
                if cond1:
                 statements_under_if_block....
                elif cond2:
                 statements_under_elif_block....
                else:
                 statements_under_else_block....

            inline if
                if cond: single_statement                

            conditional statement
                statement if cond else else_statement

        Looping Statements

            while           indefinite-loop     - number of iterations is indefinite
                                                    loop executes as long as a condition is true

                                                    while cond:
                                                        looping-block-of-statements

            for             definite-loop       - number of iterations is definite
                                                    loop executes for a given number of times/iterations.

                                                    

        Non Condition Statements

            break
            continue

    input method
        read a value from the keyboard

    assignment1: a python script to print the factors of a givne number and check if it is prime

    assignment2: a python script to print a multiplication table from 1 to 20's of a given number

    assignment3: to print only the even positioned elements of a list of strings
   
    assignment4: to accept a userName say('VAMSY') then print it as
        V
        VA
        VAM
        VAMS
        VAMSY

    assignment5: to accept a userName say('VAMSY') then print it as
        VAMSY
        VAMS
        VAM
        VA
        V

    assignment6: to accept a userName say('VAMSY') then print it as
        V
        AA
        MMM
        SSSS
        YYYYY

    Python Collections        

        Array      no concept of arrays but lists are used as arrays

                        modifiable      allows duplicates     ordered     indexed      operator
        list                YES             YES                 YES         YES       [ele1,ele2]
        tuple               NO              YES                 YES         YES       (ele1,ele2)
        set                 YES             NO                  NO          NO        {ele1,ele2}
        frozenset           NO              NO                  NO          NO        frosenset({ele1,ele2})
        dictionary          YES             NO                  YES (>3.7)  N/A       {key:value}
                                                                NO (<3.6)

        len method
            to retrive the length of a string or a list or any collection.
    
        slicing 

                                    list = ["a","b","c","d","e","f"]
            collection[lb:ub]       list[2,4]   --->    c,d
            collection[:ub]         list[:3]    --->    a,b,c
            collection[lb:]         list[4:]    --->    e,f
        
        'in' and 'not in' operators are sued to check if the element exists or not in a collection

            element in collection
            element not in collection
        
        list methods

            append()	Adds an element at the end of the list
            clear()	    Removes all the elements from the list
            copy()	    Returns a copy of the list
            count()	    Returns the number of elements with the specified value
            extend()	Add the elements of a list (or any iterable), to the end of the current list
            index()	    Returns the index of the first element with the specified value
            insert()	Adds an element at the specified position
            pop()	    Removes the element at the specified position
            remove()	Removes the item with the specified value
            reverse()	Reverses the order of the list
            sort()	    Sorts the list

        tuple methods

            count()	    Returns the number of times a specified value occurs in a tuple
            index()	    Searches the tuple for a specified value and returns the position of where it was found

        set methods

            add()	                Adds an element to the set
            clear()	                Removes all the elements from the set
            copy()	                Returns a copy of the set
            difference()	        Returns a set containing the difference between two or more sets
            difference_update()	    Removes the items in this set that are also included in another, specified set
            discard()	            Remove the specified item
            intersection()	        Returns a set, that is the intersection of two other sets
            intersection_update()	Removes the items in this set that are not present in other, specified set(s)
            isdisjoint()	        Returns whether two sets have a intersection or not
            issubset()	            Returns whether another set contains this set or not
            issuperset()	        Returns whether this set contains another set or not
            pop()	                Removes an element from the set
            remove()	            Removes the specified element
            union()	                Return a set containing the union of sets
            update()	            Update the set with the union of this set and others

        dictionary methods

            clear()	        Removes all the elements from the dictionary
            copy()	        Returns a copy of the dictionary
            fromkeys()	    Returns a dictionary with the specified keys and value
            get()	        Returns the value of the specified key
            items()	        Returns a list containing a tuple for each key value pair
            keys()	        Returns a list containing the dictionary's keys
            pop()	        Removes the element with the specified key
            popitem()	    Removes the last inserted key-value pair
            setdefault()	Returns the value of the specified key. If the key does not exist:
                             insert the key, with the specified value
            update()	    Updates the dictionary with the specified key-value pairs
            values()	    Returns a list of all the values in the dictionary

    Function

        def functionName():
            function implementation.......

        def functionName():
            function implementation.......
            return returnValueOrExpression

        def functionName(param1,param2):
            function implementation.......

        #Var len args or arbitary args
        def functionName(*args):
            function implementation.......

        def functionName(**args):
            function implementation.......

    Variable Scope

        local variables
        global variables
    
    The Zen of Python (PEP - Python Enchanment Proposal)

        Before writing a single line of code, Pythonistas embrace a set of 19 guiding 
        principles written by Tim Peters. 
        We can see them anytime by running `import this` in a Python terminal.

        The philosophy is Readability counts. 
            "Beautiful is better than ugly"
            "Explicit is better than implicit."
            "Simple is better than complex."
        
            If the code feels overly clever or hard to read, the Zen of Python gently nudges to refactor 
            it for clarity.
        
        The Blueprint: PEP 8 Styling

            PEP 8 is the official style guide for Python code. It ensures that Python code looks consistent, 
            no matter who wrote it.
            Key PEP 8 Rules:
            1. Indentation: Use exactly "4 spaces" per indentation level (no tabs!).
            2. Line Length: Limit all lines to a maximum of "79 characters".
            3. Naming Conventions:
                `snake_case` for functions, variables, and method names.
                `PascalCase` (or `CapWords`) for class names.
                `UPPER_CASE_WITH_UNDERSCORES` for constants.
            4. Whitespace:  Put spaces around operators (e.g., `x = 5`, not `x=5`), 
                            but not directly inside parentheses (e.g., `print(x)`, not `print( x )`).
        
        The Core Mechanics: Dynamic Typing & Type-Casting

            Python is dynamically typed, we need NOT to declare a variable's data type ahead of time. The interpreter figures it out at runtime.

            x = 42        # x is an integer
            x = "Hello"   # dynamically re-assigned; x is now a string

            However, Python is also strongly typed, meaning it won't let any crazy things like adding 
            a string to an integer without explicit type-casting.

            Common Type-Casting Functions:
                `int()` – Converts a value to an integer.
                `float()` – Converts a value to a floating-point number.
                `str()` – Converts a value to a string.

                age_input = "25"
                # total_age = age_input + 5  <-- This throws a TypeError!

                # Correct way using type-casting:
                total_age = int(age_input) + 5  # Returns 30

        The Engine: Arithmetic & Logical Operators

            Python uses intuitive operators to manipulate data and drive logic.

            In Arithmetic Operators, beyond standard math (`+`, `-`, `*`, `/`), Python includes a few specialized tools `//`,`%`,'**`

            In Logical Operators, Instead of cryptic symbols like `&&` or `||`, Python uses clean, readable English words `and`, `or` and 'not` 
        
        The Presentation: f-Strings (Formatted String Literals)

            Introduced in Python 3.6, f-strings are the gold standard for string formatting. 
            They are faster, cleaner, and much easier to read than old methods like `%` formatting or `.format()`.

            To use an f-string, simply prefix the string with an `f` or `F` and place the variables or expressions inside curly braces `{}`.

            Examples of f-String Power:

                name = "Alice"
                score = 94.578

                # 1. Basic interpolation
                print(f"Hello, {name}!") 

                # 2. Inline expressions/math
                print(f"Next year, you will be {20 + 6} years old.")

                # 3. Formatting floats (rounding to 2 decimal places)
                print(f"Your final score is {score:.2f}%") 

                # 4. The '=' shortcut for quick debugging (Prints: name='Alice')
                print(f"{name=}")                 

        Comprehensions

            Comprehensions provide a syntactic way to create new collections (lists, sets, or dictionaries) out of existing iterables.

            List Comprehensions
                Instead of initializing an empty list, looping, and appending, a list comprehension does it all in one shot.

                Syntax: [expression for item in iterable if condition]

                # Old way
                squares = []
                for x in range(5):                    
                    squares.append(x**2)

                # Pythonic way
                squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

            Set Comprehensions
                Exactly like list comprehensions, but they use curly braces {} and automatically handle uniqueness by stripping out duplicates.
                
                names = ["alice", "bob", "ALICE", "charlie", "bob"]

                # Creates a unique set of title-cased names
                unique_names = {name.title() for name in names}  # {'Alice', 'Bob', 'Charlie'}

            Dictionary Comprehensions
                These also use curly braces {}, but require a key: value pair definition to construct a new dictionary.
                
                users = [("id_1", "Alice"), ("id_2", "Bob")]

                # Convert a list of tuples into a quick lookup dictionary
                user_dict = {uid: name for uid, name in users}  # {'id_1': 'Alice', 'id_2': 'Bob'}

        Lambda Functions
            A lambda function is a small, anonymous (unnamed) function defined using the lambda keyword. 
            They can take any number of arguments but can only evaluate a single expression.

            Syntax: lambda arguments: expression
       
                # Standard function
                def add(x, y):
                    return x + y

                # Equivalent lambda function
                add_lambda = lambda x, y: x + y

                print(add_lambda(3, 5))  # Outputs: 8

            Per PEP 8, you shouldn't assign lambda functions to variables like add_lambda = .... If you need a named function, use def. 
            Lambdas are meant to be used as inline (throwaway) functions.

            The map function - applies a function to every item in an iterable and returns a map object
                                and the returned map object is usually casted to a list.
                prices = [10, 20, 30, 40]

                # Add 10% tax to every price inline
                taxed_prices = list(map(lambda p: p * 1.10, prices))  # [11.0, 22.0, 33.0, 44.0]

            The filter function - extracts elements from an iterable for which a function returns True.
                scores = [45, 82, 91, 58, 73, 60]

                # Filter out only passing scores (>= 60)
                passing_scores = list(filter(lambda s: s >= 60, scores))  # [82, 91, 73, 60]

            The sorted function - takes a custom key argument. 
                                This tells Python exactly how to calculate the sorting order for complex data.

                # A list of dictionaries representing products
                products = [
                    {"name": "Laptop", "price": 1200},
                    {"name": "Mouse", "price": 25},
                    {"name": "Monitor", "price": 300}
                ]

                # Sort the products based on the 'price' key inside the lambda
                sorted_by_price = sorted(products, key=lambda item: item["price"])
                sorted_by_name = sorted(products, key=lambda item: item["name"])

                print(sorted_by_price)

    Advanced Function Concepts & Decorators

        In Python, functions aren't just blocks of code that execute tasks, but they are first-class objects.
        This foundational concept unlocks two of Python’s most powerful design patterns: closures and decorators. 
        
        First-Class Functions

            In Python, functions are treated like any other variable (like integers, strings, or lists). 
            This means we can:
                1. Assign a function to a variable.

                2. Pass a function as an argument to another function.
                    
                    When a function is passed into another function, 
                    the receiving function is called a "higher-order function".

                3. Return a function from another function.
                
                def shout(text):
                    return text.upper()

                def whisper(text):
                    return text.lower()
                
                #high-order-func
                def greet(myWay):
                    greeting = myWay("Hi, I am an AI collaborator.")
                    print(greeting)
                
                greet(shout)   # Outputs: HI, I AM AN AI COLLABORATOR.
                greet(whisper) # Outputs: hi, i am an ai collaborator.

                ---------------------------------------------------------------------------
                #high-order-func
                def greet(myWay):
                    greeting = myWay("Hi, I am an AI collaborator.")
                    print(greeting)
                
                greet(lambda text:text.upper())   # Outputs: HI, I AM AN AI COLLABORATOR.
                greet(lambda text:text.lower())   # Outputs: hi, i am an ai collaborator.
        
        Closure Mechanics

            A "closure" occurs when a nested (inner) function retains access to the variables of its enclosing (outer) function, even after the outer function has finished executing.

            For a closure to happen, three criteria must be met:
                1. There must be a nested function.
                2. The nested function must refer to a value defined in the enclosing function.
                3. The enclosing function must "return" the nested function.

                def make_multiplier(factor):
                    # This is the outer function's local variable
                    
                    def multiply(number):
                        # The inner function 'remembers' the 'factor' variable
                        return number * factor
                    
                    return multiply  # Returns the inner function object

                # Create two distinct closure environments
                times_two = make_multiplier(2)  
                times_five = make_multiplier(5)

                # 'make_multiplier' has already finished running here,
                # but the inner functions still remember their respective 'factor' values!
                print(times_two(10))   # Outputs: 20
                print(times_five(10))  # Outputs: 50
        
        Decorators

            A "decorator" is essentially a wrapper. 
            It is a design pattern that allows you to modify or extend the behavior of a function 
            without permanently altering its source code.

            Architecturally, a decorator is a higher-order function that takes a function as an argument, 
            wraps it with extra logic using a closure, and returns the wrapped function.

            Manual Decorator, here is a decorator that logs when a function starts and finishes.

                def my_logger(func):
                    def wrapper():
                        print(f"--- Starting execution of {func.__name__} ---")
                        func()  # Execute the original function
                        print(f"--- Finished execution of {func.__name__} ---")
                    return wrapper

                def say_hello():
                    print("Hello, world!")

                # Manual decoration
                decorated_hello = my_logger(say_hello)
                decorated_hello()

            Using the Syntactic Sugar (`@`)
                Python provides a much cleaner way to apply decorators using the `@` symbol directly above the function definition.

                @my_logger
                def say_goodbye():
                    print("Goodbye, world!")

                say_goodbye()
                # Outputs:
                # --- Starting execution of say_goodbye ---
                # Goodbye, world!
                # --- Finished execution of say_goodbye ---

            Decorators with (Accepting `*args` and `kwargs`)
                The decorator above fails if the function it wraps accepts arguments. 
                To build a robust, universal decorator, your inner `wrapper` function must accept `*args` and `kwargs` and pass them right along to the original function.

                import time

                def timer_decorator(func):
                    def wrapper(*args, **kwargs):
                        start_time = time.time()
                        
                        # Execute the original function and capture its return value
                        result = func(*args, **kwargs)
                        
                        end_time = time.time()
                        print(f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds to run.")
                        
                        return result  # Ensure the original function's output isn't lost
                    return wrapper

                @timer_decorator
                def heavy_calculation(n):
                    return sum(i * i for i in range(n))

                # Call the decorated function
                total = heavy_calculation(5_000_000)
                print(f"Result: {total}")
    
    Classes and Object

        class is a user defiend data type to represent an entity
        in terms of its properties and behaviours.
        
        an object is a variable of class type

        class Car:                
            # The __init__ method is the constructor (not the initializer, technically, but functionally identical)
            def __init__(self, make: str, model: str):
                self.make = make        # Instance variable
                self.model = model      # Instance variable
                self.is_running = False # Instance variable

            # Standard Instance Method, and every instance method in Python must explicitly accept self as its first parameter
            def start_engine(self):
                self.is_running = True
                print(f"The {self.make} {self.model}'s engine is purring.")

        Python does not have strict encapsulation enforcement. Everything is public by default. 
        Instead, Python relies on naming conventions and a mechanism called Name Mangling.

            1. Internal Use Only (Single Underscore): A prefix of a single underscore (e.g., _secret) is a convention. It tells other developers, "This is internal; touch it at your own risk." It is still completely accessible.

            2. Private/Name Mangled (Double Underscore): A prefix of a double underscore (e.g., __secret) triggers name mangling. Python automatically rewrites the attribute name behind the scenes to prevent accidental overriding in subclasses.
        
            class BankAccount:
                def __init__(self, owner, balance):
                    self.owner = owner          # Public
                    self._routing_number = 123  # Protected/Internal by convention
                    self.__balance = balance    # Name Mangled (Private-ish)

            account = BankAccount("Alice", 5000)
            print(account.owner)            # Works: "Alice"
            print(account._routing_number)  # Works (but PEP 8 warns against it): 123

            # print(account.__balance)      # Throws AttributeError!

            # How to bypass name mangling (Don't do this in production!):
            # Syntax: _ClassName__attributeName
            print(account._BankAccount__balance)  # Works: 5000

        Getter and Setter Properties

            Python uses the @property decorator to expose methods as if they were standard attributes

            class Employee:
                def __init__(self, name, salary):
                    self.name = name
                    self.__salary = salary

                @property
                def salary(self):
                    """ The Getter """
                    return self.__salary

                @salary.setter
                def salary(self, value):
                    """ The Setter with validation """
                    if value < 0:
                        raise ValueError("Salary cannot be negative!")
                    self.__salary = value

            emp = Employee("Bob", 60000)

            # Notice that it is not called like a function 'emp.salary()'
            print(emp.salary)  # Acts like a field access -> Outputs: 60000

            emp.salary = 65000 # Triggers the setter seamlessly
        
    Inheritance And Polymorphism

        No Overloading, but averiding is possible

        # (Base)
        class Employee:
            def __init__(self, name,sal):
                self.name = name
                self.sal = sal
            
            def total_sal(self):
                return self.sal

        # Single Inheritance
        class Manager(Employee):
            def __init__(self, name,sal,ta):
                super().__init__(name,sal)
                self.sal = sal 
            
            def total_sal(self):
                return super.total_sal() + self.ta

        # Multi-Level Inheritance
        class GeneralManager(Manager):
            def __init__(self, name,sal,ta,allowence):
                super().__init__(name,sal,ta)
                self.allowence = allowence 
            
            def total_sal(self):
                return super.total_sal() + self.allowence
        
    Abstraction        

        Python practices Duck Typing (for abstraction): 
            "If it walks like a duck and quacks like a duck, it's a duck." A shared base class is not needed to achieve abstraction; you just need objects to implement methods with the same name.

        class Dog:
            def make_sound(self):
                return "Bark!"

        class Cat:
            def make_sound(self):
                return "Meow!"

        # This function doesn't care about the class type; it only cares that 'animal' has a 'make_sound' method.
        def animal_chorus(animal):
            print(animal.make_sound())

        animal_chorus(Dog()) # Outputs: Bark!
        animal_chorus(Cat()) # Outputs: Meow!

    Abstraction forced by 'abc'

        abc - abstract base class
        we have a package called abc in Python
        @abstratmethod  to be applied on a method with no-impl.
        In python, 'pass' is a keyword used to skip implementation body of any block, the
        same is used to skip the block of a abstract emthod.

        from abc import ABC, abstractmethod

        class Shape(ABC):
            @abstractmethod
            def area(self):
                pass

        class Rect(Shape):
            #assuming a proper constructor here

            def area(self):
                self.length*self.breadth

        NOTE: by combining @property and @abstractmethod decorators, we can create abstract properties too.

        class DBConnectionProvider(ABC):
            @property
            @abstracmethod
            def connection_string(self):
                pass

        class MySQLConnectionProvider(DBConnectionProvider):
            @property            
            def connection_string(self):
                return "mysql-related-connection-string"

        class SqlServerConnectionProvider(DBConnectionProvider):
            @property            
            def connection_string(self):
                return "SqlServer-related-connection-string"
    
    Dunder (Magic) Methods
        __init__(self,..)   represents constructor        
        __str__(self) Allows us to pass an object directly into Python's native str() function.
        __len__(self) Allows us to pass an object directly into Python's native len() function.

        class Book:
            def __init__(self, title, author, pages):
                self.title = title
                self.author = author
                self.pages = pages

            def __str__(self):
                # End-user view
                return f"'{self.title}' by {self.author}"

            def __len__(self):
                # Ties object into len()
                return self.pages

        book = Book("Python Basics", "Jane Doe", 320)

        print(str(book))  # Outputs: 'Python Basics' by Jane Doe
        print(len(book))  # Outputs: 320
    
    The Daimond Problem (multiple inheretence)

        In multiple inheritance, the Diamond Problem occurs when a subclass inherits from two parent classes that both inherit from a single grandparent class. If the grandparent class has a method that both parent classes override, which version of the method should the grandchild inherit?

                /--- Class B ---\
            Class A              +---> Class D
                \--- Class C ---/

        The MRO - (Method Resolution Order)

            Python uses the C3 Linearization algorithm to build a flat, ordered list of classes to search through when looking for a method or attribute.

            The MRO enforces three strict rules:

                1. Subclasses before Parents:   A child class is always checked before its parent classes.
                2. Left-to-Right Ordering:      Parent classes are checked in the exact order they are 
                                                listed in the class definition (e.g., class D(B, C) checks B before C).

                    class A:
                        def process(self):
                            print("Executing Class A")

                    class B(A):
                        def process(self):
                            print("Executing Class B")
                            super().process()  # Passes control to the next class in the MRO

                    class C(A):
                        def process(self):
                            print("Executing Class C")
                            super().process()  # Passes control to the next class in the MRO

                    class D(B, C):
                        def process(self):
                            print("Executing Class D")
                            super().process()

                    d = D()
                    d.process()

                    print(D.mro())

                    output:
                        Executing Class D
                        Executing Class B
                        Executing Class C
                        Executing Class A

                        [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]   
                                                
                3. Monotonicity:                The relative order of parent classes must be preserved across 
                                                the entire inheritance hierarchy, and if not Python will refuse to compile the code and throw a TypeError.

                    class X:
                        def someMethod(self):
                            print("Class x")

                    class Y: 
                        def someMethod(self):
                            print("Class y")

                    # X comes before Y
                    class Alpha(X, Y): 
                        def someMethod(self):
                            print("Class Alpha")

                    # Y comes before X (Contradiction!)
                    class Beta(Y, X): 
                        def someMethod(self):
                            print("Class Beta")

                    # This will crash! Python cannot build a consistent MRO list
                    class Gamma(Alpha, Beta): 
                        def someMethod(self):
                            print("Class Gamma")

                    Error Output:
                        TypeError: Cannot create a consistent method resolution order (MRO) for bases X, Y
            
    assignment7: 
        a. define a class Student with properties 
            name,maths score,phy score and computers score
        b. define a member function total to return the total Score
        c. define a member function average to return the average score
        d. define a member function grade to return grade as per the below rules

                if any one score is less than 35 then the grade is FAIL
                else if avg >=90    grade is outstanding
                else if avg between 89 and 70 grade is proficient
                else if avg between 69 and 36 grade is aspirant

    Match Case Statement
        Introduced in Python 3.10, Structural Pattern Matching (the `match-case` statement) brought a powerful, readable tool to the language that goes far beyond a simple `switch-case` found in languages like C++ or Java.

        While it looks like a switch statement on the surface, it doesn't just check for equality; it can destructure data structures (like lists, dictionaries, or objects) and extract values on the fly.

        1. Basic Matching (Like a Switch Statement)

            status_code = 404

            match status_code:
                case 200:
                    print("Success!")
                case 400:
                    print("Bad Request.")
                case 404:
                    print("Not Found.")
                case _:
                    print("Unknown status code.")  # The underscore acts as a wildcard/else block

        2. Destructuring Sequences (Lists or Tuples)

            command = ["move", "north"]

            match command:
                case ["quit"]:
                    print("Goodbye!")
                case ["move", direction]:
                    print(f"Moving the character {direction}.")
                case ["teleport", x, y]:
                    print(f"Teleporting to coordinates: ({x}, {y})")
                case _:
                    print("Unknown command format.")

            If `command` is `["move", "north"]`, Python matches the second case and binds the string `"north"` to the variable `direction`.

        3. Matching Dictionaries (Mapping Patterns)
        
            user_action = {"action": "delete", "user_id": 42, "timestamp": 162509}

            match user_action:
                case {"action": "login", "user_id": uid}:
                    print(f"User {uid} logged in.")
                case {"action": "delete", "user_id": uid}:
                    print(f"Deleting data for user {uid}.")
                case _:
                    print("Action not recognized.")
        
        4. Combining Patterns 

            day = "Saturday"

            match day:
                case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
                    print("It's a weekday. Time to work!")
                case "Saturday" | "Sunday":
                    print("Weekend mode activated!")

        5. Adding Guards (`if` clauses)

            We can append an `if` statement to a case pattern to add conditional logic (called a **guard**).

            packet = [100, 200]

            match packet:
                case [x, y] if x == y:
                    print(f"X and Y match perfectly: {x}")
                case [x, y] if x > y:
                    print(f"X ({x}) is greater than Y ({y})")
                case [x, y]:
                    print(f"Y is greater than X")

        6. Matching Object/Class Types

            class Point:
                def __init__(self, x, y):
                    self.x = x
                    self.y = y

            location = Point(0, 10)

            match location:
                case Point(x=0, y=0):
                    print("At the origin.")
                case Point(x=0, y=y_val):
                    print(f"On the Y-axis at {y_val}.")
                case Point(x=x_val, y=0):
                    print(f"On the X-axis at {x_val}.")
                case Point(x, y):
                    print(f"At coordinates ({x}, {y})")

    Modules

        is a logical section of an application code base.

        each .py file is concedered to be a module.

        the file name becomes the module name.

        import moduleName

        from moduleName import resource

    assignment8: 
        a. define and consume a modules called 'loans' having
            1. a method called simpleInterest
            2. a method called compositeInterest
            3. a method called emi

    Python inbuilt-modules
        1. System and File Operations

            os
                os.mkdir(), os.listdir(), os.environ.get(), os.remove()
                Creating/deleting directories, accessing environment variables. 

            pathlib
                Path.exists(), Path.write_text(), Path.glob(), Path.cwd()
                Modern, object-oriented way to handle file paths and I/O. 

            sys
                sys.argv, sys.exit(), sys.path, sys.platform
                Accessing command-line arguments and interpreter-specific parameters. 

            shutil
                shutil.copy(), shutil.move(), shutil.rmtree(), shutil.make_archive()
                High-level file operations (copying, moving, and zipping entire folders). 

        2. Data Structures & Logic

            collections
                Counter(), defaultdict(), namedtuple(), deque()
                Counting elements, setting default dict values, or using high-performance queues. 

            itertools
                chain(), cycle(), product(), permutations()
                Creating efficient iterators for complex loops and combinations. 

            functools
                lru_cache(), partial(), reduce()
                Optimizing code with caching or creating "pre-filled" versions of functions. 

            enum
                Enum, IntEnum, auto()
                Creating symbolic names for constant values to improve code readability. 
        
        3. Math and Statistics
            
            math
                math.sqrt(), math.ceil(), math.sin(), math.pi
                Basic trigonometry, logarithms, and constants. 

            random
                random.choice(), random.randint(), random.shuffle()
                Generating random numbers or selecting random items from a list. 

            statistics
                mean(), median(), mode(), stdev()
                Calculating basic descriptive statistics on datasets. 

            decimal
                Decimal()
                Handling high-precision floating-point arithmetic (critical for financial apps). 
        
        4. Data Formats & Serialization
            
            json
                json.loads(),json.dumps(), json.load(), json.dump()
                Converting Python dictionaries to/from JSON format.
                
            csv
                csv.reader(), csv.writer(), DictReader()
                Parsing and generating Comma-Separated Values files. 

            re
                re.search(), re.findall(), re.sub(), re.compile()
                Using Regular Expressions for complex string searching and cleaning. 

            sqlite3
                connect(), execute(), commit()
                Using a full SQL database engine without installing a separate server. 
        
        5. Datetime & Concurrency
            
            datetime
                datetime.now(), strftime(), timedelta()
                Working with dates, times, and time zone differences. 

            time
                time.sleep(), time.time()
                Measuring execution time or pausing the program. 

            threading
                Thread(), Lock()
                Running tasks concurrently (useful for I/O-bound tasks). 

            asyncio
                async def, await, asyncio.run()
                Writing single-threaded concurrent code using coroutines. 
        
        Pro-Tip: How to see all modules

            help("modules") - ON PYTHON SHELL.
    
    Exception Handling

        try:
            #code that we anticipate to raise an exception
        except:
            #alternate or exception handling code goes here..
        else:
            #this block is executed if the try completes without any exception
        finally:
            #this block executes irrespective of an exception being raised or not raised.    

        in case of no exceptions occuring in the try-block
                else block - finally block are executed

        in case of an exception occuring in the try-block
                except block - finally block are executed

    assignment9: 
        a. define a class Train having 'maxSeats' and 'seatsFilled' as fields
        b. write the script to run a managed loop that
            1. prompt for booking seats
            2. accept the number of seats needed and book them by calling 'reserve' function on the train.
            3. print seats remaning after every booking
        c. handle appropriate exceptions   

    Python Type Hints

        Python is a dynamically typed language, which means you never have to explicitly indicate what kind of variable it is. But in some cases, dynamic typing can lead to some bugs that are very difficult to debug, and in those cases, Type Hints or Static Typing can be convenient. Type Hints have been introduced as a new feature in Python 3.5.

        Example:

            def factorial(x: int) -> int:
                if x<0: return None
                if x==0: return 1
                return x * factorial(x-1)

    NumPy

        stands for 'Numerical Python', is a python library offering array operations with 50% faster
        performence than python lists.

        installing:

            pip install numpy
            pip list

        NumPy Array related Methods and Properties

            numpy.array([e1,e2,e3,...],ndim=dim,dtype='datatype')   creates an array 

                Array datatype codes
                    i - integer
                    b - boolean
                    u - unsigned integer
                    f - float
                    c - complex float
                    m - timedelta
                    M - datetime
                    O - object
                    S - string
                    U - unicode string
                    V - fixed chunk of memory for other type ( void )

            array.ndim                                              array dimenssion
            array[index1,index2,..]                                 indexing or accessing an element
            array[start:end:step]                                   slicing an array
            array[booleanExpression]                                filters an array
            array.dtype                                             array data type
            array.astype('datatype')                                convertes the datatype of an array
            array.copy()                                            creates a disconnected copy of the array
            array.view()                                            creates a reference of the array
            array.base                                              returns the base array for references
                                                                    orelse none
            array.shape                                             elements count in each dim
            array.reshape(dims)                                     convets an array dim
            numpy.concatenate(arr1,arr2,..)                         joins all given array sinto one
            numpy.stack(arr1,arr2)                                  stacks multi-dim arrays
            numpy.hstack(arr1,arr2)                                 stacks 2D array alongside rows
            numpy.vstack(arr1,arr2)                                 stacks 2D array alongside cols
            numpy.array_split(arr, arrayCount)                      splits an array into multiple arrays
            numpy.where(booleanExpression)                          search for a matching ele
            array.searchsorted(ele)                                 binary search
            numpy.sort(arr)                                         sorts the given array

        NumPy random object

            random.randint(ubound)                                  generates a random int between 0 and ubound
            random.rand()                                           generates a random float between 0 and 1
            random.randint(ubound,size=(dim))                       generates a random int array of given dims
            random.rand(dim)                                        generates a random float array of given dims
            random.choice(array)                                    generates a fandom number from the list
            random.choice(array,size=(dim))
            random.choice(array,size=(dim),p=[possibility]) 
                eg: random.choice([3, 5, 7], p=[0.1, 0.3, 0.6], size=(4))
            
            random.shuffle(array)                                   returns a shuffled copy of the array
            random.permutation(array)                               returns a permutation of eles in the array

        NumPy ufuncs - 'Universal Functions'

            numpy.frompyfunc(scalarFunc,noOfInputArgs,noOfOutputs)      VECTORIZATION

            numpy.add(arr1,arr2)
            numpy.subtract(arr1,arr2)
            numpy.multiply(arr1,arr2)
            numpy.divide(arr1,arr2)
            numpy.power(arr1,arr2)
            numpy.mod(arr1,arr2)
            numpy.divmod(arr1,arr2)
            numpy.absolute(arr1)
            numpy.trunc(arr1)           12.45 -> 12      12.69->12  (deletes the fractional part)
            numpy.around(arr1)          12.45 -> 12      12.69->13  (rounds the fractional part)
            numpy.floor(arr1)           12.45 -> 12      12.69->12  
            numpy.ceil(arr1)            12.45 -> 13      12.69->13  
            numpy.log2(arr1)
            numpy.log10(arr1)
            numpy.cumsum(arr1)          cumulative sum            
            numpy.cumprod(arr)
            numpy.prod(arr)                        
            numpy.lcm(n1,n2,n3...)
            numpy.gcd(n1,n2,n3...)
            
    SciPy

        stands for 'Scientific Python', is a python library offering scientific computation and uses numpy underneath.

        installing:

            pip install scipy
            pip list

        SciPy Methods and Properties

            scipy.constants                 is an object offering a variety of constants
            scipy.optimize.root(eqn,0)
            scipy.sparse.csr_matrix(arr)    handle sparse data in an array (csr - compress sparse row)
                .data                       gives non zero data stored
                .count_nonzero()
                .eliminate_zeros()
                .sum_duplicates()
                .tocsc()

            Interpolation is a feature of SciPy that 
            is used to generate points between a start and end point for
            a series in a chart.

    matplotlib

        is a low level graph plotting library in python that serves as a visualization utility.

        installing:

            pip install matplotlib
            pip list

        Matplotlib Pyplot

            is a submodule that offers major plotting utilities

            pyplot.show()                           displays the chart
            pyplot.plot(xpoints,ypoints)            draws a line chart for the givne curve or line
            pyplot.plot(xpoints,ypoints,marker='')  draws a line chart and marks the coordinates with
                                                    'o'	Circle	
                                                    '*'	Star	
                                                    '.'	Point	
                                                    ','	Pixel	
                                                    'x'	X	
                                                    'X'	X (filled)	
                                                    '+'	Plus	
                                                    'P'	Plus (filled)	
                                                    's'	Square	
                                                    'D'	Diamond	
                                                    'd'	Diamond (thin)	
                                                    'p'	Pentagon	
                                                    'H'	Hexagon	
                                                    'h'	Hexagon	
                                                    'v'	Triangle Down	
                                                    '^'	Triangle Up	
                                                    '<'	Triangle Left	
                                                    '>'	Triangle Right	
                                                    '1'	Tri Down	
                                                    '2'	Tri Up	
                                                    '3'	Tri Left	
                                                    '4'	Tri Right	
                                                    '|'	Vline	
                                                    '_'	Hline	

            pyplot.bar(xseries,yseries)             draws a bar chart
            pyplot.barh(xseries,yseries)            draws a bar chart horizontal
            pyplot.hist(xseries)                    draws a histogram
            pyplot.pie(xseries,labels=[])           draws a pie-chart

    Pandas

        is a python library used for 
            1. data analysis            extracting patterns from a collected dataset to support decisions.
            2. data manipulation        project the data in a new time series, 
                                        compoute dependent attributes ..etc.,
            3. data cleaning            process the data to ensure consistency and validity.
            4. data transformation      is to convert the data from one format to another
                                        like xml to json or csv to json ..et.,c
                                        or plain text to attribute-for, or semi-formatted form.

        installing:

            pip install pandas
            pip list

        Pandas Series

            A series is like an attribute or column of a table.
            We represent a series as a 1D array.
            For example, the scores of all the students in maths is one series and
            in computers is another series ...etc.,

            pandas.Series(list, index=["label1","label2",..])
                generates a series with given lables , lables are optional and when
                skipped, o based index is taken as labels

            seriesObj["label"]      access a ele for a given label

        Pandas DataFrames

            A dataFrame is a 2D array representing a table as rows and cols.

            pandas.DataFrame(dictonary,index=[labels..])
                creates a dataFrame

            dataFrameObj.loc[rowIndex]
                returns the specified row as series

            dataFrameObj.loc([row1,row2,..])
                returns the specified rows as a dataFrame

            pandas.read_csv(aCsvFilePath)
                returns a dataFrame loaded with content of the CSV file
            
            pandas.read_json(aJsonFilePath)
                returns a dataFrame loaded with content of the JSON file

            pandas.read_excel(aExcelFilePath)
                returns a dataFrame loaded with content of the XL file (needs 'openpyxl')
            
            dataFrame.to_json(aJsonFilePath)
                writes a dataFrame into a JSON file
            
            dataFrame.to_csv(aCSVFilePath)
                writes a dataFrame into a CSV file

            dataFrame.to_excel(aExcelFilePath)
                writes a dataFrame into a Excel file (needs 'openpyxl')

        Pandas Data Analysis        

            dataFrame.head(n)       returns the first 'n' records n is 5 by default
            dataFrame.tail(n)       returns the bottom 'n' records n is 5 by default
            dataFrame.discribe()    returns the complete statistics (mod, median, sum ..etc) 
            dataFrame.shape         returns the dataframe shape (rowCount,colCount)
            dataFrame.columns       returns the list of columns.
            dataFrame.info()        returns all about the dataset including mem-usage
            dataFrameObj.corr()		computes correlation between cols

            dataFrame.toString()
                prints the entire dataframe, as a dataFrame if directly printed
                prints the top 5 and last 5 rows only when the data is huge.
   	    
        Pandas Data Cleaning

            dataFrameObj.dropna()  				           removes rows with null values 
                                                            and returns a new dataframe
                                                            
            dataFrameObj.dropna(inplace=True)  			   removes rows with null values 
                                                            modifying the actual dataframe

            dataFrameObj.fillna(defaultValue,inplace=True) replaces null values with a 
                                                            default value in the dataframe

            dataFrameObj["label"].fillna(defaultVaue,inplace=True)
            dataFrameObj["lable"].mean()
            dataFrameObj["lable"].median()
            dataFrameObj["lable"].mode()

        Pandas Data Visualization (Plotting Charts)

            dataFrameObj.plot()  					                    
                Plots a curve for each series in the df

            dataFrameObj.plot(kind="scatter",x="xLabel",y="yLabel")  	
                Plots a scatter chart against choosen xseries and yseies in the dataframe

            dataFrameObj["label"].plot(kind="hist")                
                Plots a histogram chart of a choosen series 

        Data Wrangling And Transformations

            Filtering Rows:  is done using Boolean Indexing, instead of writing structural conditional blocks
                            dataFrame[booleanExpression]

            Sorting Data :  Sorting datasets relies on .sort_values(). 
                            It accepts single columns, lists of columns, and independent ascending/descending parameters for complex ordering operations.

                            dataFrame.sort_values(by="colLabel", ascending=False)
        
            Single Column Transformations
                dataFrame["new_col"] = dataFrame["col"].apply(lambdaExpression)
                dataFrame["estimatedHike"] = dataFrame["sal"].apply(lambda sx:sx*0.10)

            Multi Column Transformations
                dataFrame["new_col"] = dataFrame["col"].apply(evaluationMethod,axis=1)

            Mathematical Vectorization
                dataFrame["estimatedHike"] = dataFrame["sal"]*0.10

            String Vectorization
                dataFrame["full_name_in_upper"] = dataFrame["full_name"].str.upper()

            Logical Vectorization
                dataFrame["new_col"] = np.where(cond,true_val,false_val)
                dataFrame["new_col"] = np.select([cond1,cond2], [result1,result2], default="else value")
        
        Data Aggregations

            Summarizing Data with .groupby()
                The .groupby() method implements the classic database design pattern: Split-Apply-Combine.
                Split the DataFrame into chunks based on a specific column's unique values.
                Apply a mathematical function (like sum, mean, or count) to each chunk.
                Combine those results back into a single, summarized DataFrame.

                dataFrame.groupby("groupCol")["aggregateCol"].<aggregate>().reset_index()

                <aggregate> is sum, min, max, avg, mean, or count

                We append .reset_index() at the end because grouping shifts the target column into the DataFrame's index. Resetting it converts it back into a standard, clean column.

            Advanced Grouping: The .agg() Method

                df_sales.groupby(["groupCol1", "groupCol2"]).agg({
                    "aggCol1": [<aggregate1>,<aggregate2>],
                    "aggCol2": "<aggregate>"
                })

            Pivot Tables
            
                SalesMan        Quater      Sales
                A               Q1          12
                A               Q2          10
                A               Q3          5
                B               Q1          7                
                B               Q3          6

                            A   B      TotalSales
                Q1          12  7       19
                Q2          10  0       10
                Q3          5   6       11
                TotalSales  27  13      40

                df_sales.pivot_table(
                    values="Sales",     # The numeric data to aggregate
                    index="Quater",     # Rows
                    columns="SalesMan", # Columns
                    aggfunc="sum",      # The aggregation function (defaults to 'mean' if omitted)
                    fill_value=0        # Replace any resulting missing NaN cells with 0
                )

        Merging and Joining Datasets

            Inner Join (The Default)
                pd.merge(df1, df2, on="join_col", how="inner")

            Left Outer Join (The Default)
                pd.merge(df1, df2, on="join_col", how="left")

            Right Outer Join (The Default)
                pd.merge(df1, df2, on="join_col", how="right")

            Joins when the left and right cols-lables are not matching.
                pd.merge(df1, df2, left_on="lft_col",right_on="rt_col", how="inner")
            
        Unions

            pd.concat([df1,df2,df3])               vertical stacking
            pd.concat([df1,df2,df3],axis=1)        horizontal stacking

                join                inner or outer
                ignore_index        false           retain actual indexes
                                    or true         regerate indexes afresh      

    Requests

        is a HTTP request and Response management library.

        installing:

            pip install requests
            pip list

        API

            resp = requests.get(url)
            resp = requests.post(url)
            resp = requests.put(url)
            resp = requests.delete(url)

            resp = requests.get('url', auth = HTTPBasicAuth('userName', 'password')) 

            resp.statusCode
            resp.url
            resp.content
            resp.cookies
            resp.json()
            resp.ok

    StreamLit

        is a model deployment tool for Mechine Learning Systems.

        installing:

            pip install streamlit
            pip list

        Deploying a model

            streamlit run Prog.py

        API

            streamlit.title("")
            streamlit.header("")
            streamlit.subheader("")
            streamlit.text("")
            streamlit.markdown("")
            streamlit.success("")
            streamlit.info("")
            streamlit.warning("")
            streamlit.error("")
            streamlit.exception(expObj)
            streamlit.checkbox("checkBoxLabel")                    returns true or false
            streamlit.radio("label", (Option1, Option2,...))       returns selected option
            streamlit.selectbox("label",[options..])               returns selected option
            streamlit.multiselect("label",[options..])             returns selected options as a list
            streamlit.button("")                                   returns true when clicked
            streamlit.text_input("question", "default ans..")      returns the entered text
            streamlit.slider("label", min, max)                    returns the marked value
            
    PyTest 

        is a testing framework for python

        installing:

            pip install pytest
            pip list
        
        Test Files and Functions

            test_*.py or *_test.py in the current directory are all concedered as test files
            Pytest requires the test function names to start with 'test'
        
        Assertions

            assert booleanExpression

            for example: assert expectedValue == actualValue

        Executing test cases

            pytest -v                   executes all test cases in the current folder
            pytest filename.py -v       executes test cases in the specified file alone
            pytest -k substring -v      executes test cases whose name contains the specified substring
            pytest -m markername -v     executes test cases that marked with @pytest.mark.markername
       
        Pytest help

            pytest -h

    SQLAlchemy ORM Data Modeling

        Installation

            pip install sqlalchemy

        Connecting to the Database

            from sqlalchemy import create_engine

            # Create an Engine. For this example, Let's use an in-memory SQLite database.            
            engine = create_engine("sqlite:///:memory:", echo=True) 

            # Setting echo=True makes SQLAlchemy print every raw SQL statement it executes to the terminal.
            # Creates a physical file named 'app_data.db' in your local project root folder
            engine = create_engine("sqlite:///app_data.db", echo=True)

        Connecting to Postgres

            pip install psycopg

            postgres_url = "postgresql+psycopg://username:password@localhost:5432/my_database"
            engine = create_engine(postgres_url, echo=True) 

        Connecting to MySQL
            Option1:

                pip install pymysql

                mysql_url_pymysql = "mysql+pymysql://username:password@localhost:3306/my_database"
                engine = create_engine(mysql_url_pymysql, echo=True) 
            
            Option2
                pip install mysqlclient
                
                mysql_url_client = "mysql+mysqldb://username:password@localhost:3306/my_database"
                engine = create_engine(mysql_url_client, echo=True) 

        Modeling Tables with Declarative Base

            from typing import Optional
            from sqlalchemy import String, Integer, ForeignKey
            from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

            # Step 1: Create the Registry Base Class
            class Base(DeclarativeBase):
                pass

            # Step 2: Model a Department Table
            class Department(Base):
                __tablename__ = "depts"  # Maps directly to the SQL table name

                # Mapped[] defines the Type-Hinting layer for IDEs and type-checkers (like mypy)
                # mapped_column() configures the actual SQL constraint properties
                id: Mapped[int] = mapped_column(primary_key=True)
                name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

                # Relationship attribute (Allows OOPS-style navigation: department.employees)
                # This does NOT create a column in the DB; it tells SQLAlchemy how to join tables in Python memory.
                employees: Mapped[list["Employee"]] = relationship(back_populates="department")

            # Step 3: Model an Employee Table (with a Foreign Key)
            class Employee(Base):
                __tablename__ = "emps"

                id: Mapped[int] = mapped_column(primary_key=True)
                name: Mapped[str] = mapped_column(String(100), nullable=False)
                
                # Optional[] implies nullable=True in the database
                email: Mapped[Optional[str]] = mapped_column(String(255)) 
                
                # Defining a physical Foreign Key Column
                department_id: Mapped[int] = mapped_column(ForeignKey("departments.id"))
                
                # Bidirectional relationship link
                department: Mapped["Department"] = relationship(back_populates="employees")
        
        Emitting the Schema
            
            # Iterates through every class inheriting from 'Base' and generates tables in SQLite
            Base.metadata.create_all(engine)

        Reset / Drop the Schema
                        
            Base.metadata.drop_all(engine)

        Migration

            1. When create_all is called, the tables that do not exist in teh database are only created.
            2. If a table exists, and its shcema is not matching with the class definition, no changes
                are made to the table. (and this leads to inconsistency or run-time errors)
            3. In dev mode
                    drop all
                    then
                    create all
               In prod mode 
                    we use tools like 'alembic'

        Executing Operations with the Session

            from sqlalchemy.orm import sessionmaker

            # Create a session factory bound to our database engine
            Session = sessionmaker(bind=engine)

            # Use a context manager ('with' block) to ensure the session closes safely automatically
            with Session() as session:
                # 1. Create instances of our Python Objects
                eng_dept = Department(name="Engineering")
                
                alice = Employee(name="Alice", email="alice@company.com", department=eng_dept)
                bob = Employee(name="Bob", department=eng_dept) # Email defaults to None/NULL
                
                # 2. Stage them in the transaction pipeline
                session.add(eng_dept) # Cascades automatically and adds Alice and Bob too!

                # 3. Commit the transaction to the database
                session.commit()
        
        Querying Data Objects

            from sqlalchemy import select,insert,delete,update

            with Session() as session:
                # Build a type-safe Select statement
                statement = select(Employee).where(Employee.name == "Alice")
                                
                # Execute and fetch the first scalar result
                employee = session.scalars(statement).first() 
                #.all() instead of .first() to retrive a list of recs.
                
                print(f"Fetched Employee: {employee.name}")
                # Seamlessly cross into the joined table using our relationship property:
                print(f"Works in department: {employee.department.name}")

                delStatement = delete(Employee).where(Employee.id == 101)
                session.execute(delStatement)
                session.commit()

                updateStmt = (
                        update(Employee)
                        .where(Employee.id == 365)
                        .values(sal=78000)
                )
                session.execute(updateStmt)
                session.commit()

                insStmt = insert(Employee)
                session.execute(insStmt, empObjectsList)
                session.commit()
      
        CRUD Operations

            # Stage multiple records in the Session transaction cache
            session.add_all([rec1, rec2])

            # Retrive by id
            rec = session.get(EntityClassName, ID)
            
            # Deletion
            session.delete(rec)

            Updation
                # 1. Fetch the target entity
                rec = session.get(EntityClassName, ID)
                
                if rec:
                    # 2. Modify properties directly
                    rec.field1 = newValueForField1
                    rec.field2 = newValueForField2
                    
                    # 3. Commit tracking changes
                    session.commit()

    WebServices

        A web-service is a method offering bussiness logic and hsoted on a server.
        That method is invoked by sending a request from a ui-client.
        API is a collection of web-services

        web-serives that run on SOAP protocol are called SOAP webservices
        web-serives that run on HTTP protocol are called RESTful webservices (rest-api)

        Multi-tiered-app

            DatabaseServer      WebServer           Client
                Database            webApp              Apps (FrontEnd)
                                    webService (BE)
                                        
                                        <---------->    flipkart-react-app
                                        <---------->    flipkart-andriod-app
                        flipkart-api    <---------->    flipkart-website
                                        <---------->    flipkart-ios-app
                                        <---------->    flipkart-angular-app

    FastApi

        is a modern Python web framework, very efficient in building APIs.

        we use uvicorn as HTTP Server to host our rest api application
        we use pydantic for data validations.

        installing:
            pip install uvicorn
            pip install fastapi
            pip install pydantic
            
        Mapping Methods

            app = fastapi.FastAPI()
            
            @app.get("url")             GET Mapping     for data retrival
            @app.post("url")            POST Mapping    for insertion operations
            @app.put("url")             PUT Mapping     for updation operations
            @app.delete("url")          DELETE Mapping  for deletion operations

            URL segment marked in {} is a path parameter

        Luanching 'app' object on uvicorn server assuming the program is in app.py
            uvicorn main:app --reload   

   
   

    Langchain, LlamaIndex    

        Large Language Models (LLMs) are transforming how users approach tasks related to searching, interacting with, and generating new content. 

        LangChain,LlamaIndex are open-source frameworks that give developers the tools they need to create applications using large language models (LLMs). In its essence, LangChain is a prompt orchestration tool that makes it easier for teams to connect various prompts interactively.

        UseCases
            Content generation and summarization
            Chatbots
            Data analysis software

        Comparing LlamaIndex and Langchain
 
                         	
        Primary Function 	
            Langchain	
                LangChain is a Python-based library that enables the development of custom NLP applications using large language models. 	            
            LlamaIndex
                Formerly GPT-Index, LlamaIndex is a project consisting of data structures designed to ease the integration of extensive external knowledge bases with large language models.

        Key Features 	
            Langchain	
                Supports GPT-2, GPT-3, and T5 LLMs – Provides tokenization, text generation, and question-answering capabilities – Ideal for creating chatbots and summarizing lengthy documents. 	
            LlamaIndex
                Enables integration with external knowledge bases, including Wikipedia and Stack Overflow – Allows topic extraction from unstructured data- Supports GPT-2, GPT-3, GPT-4and T5 LLMs.
        
        Use Cases
            Langchain	
                Chatbot construction: Create a chatbot capable of answering specific subject queries using LLMs for accurate and relevant responses.
                Text summarization: Use LangChain to generate brief summaries of long documents or articles, helping users to quickly grasp the key points.
            LlamaIndex
                Question-answering system: Build a system that provides answers by connecting to external knowledge bases, using LlamaIndex to compile an index of queries and responses.

                Topic extraction: Use LlamaIndex to extract topics from unstructured data, linking it to LLMs for deeper analysis and understanding.
