class SimpleCalculator():
    
    # Polymorphic function to perform arithmetic calculations
    def calculate(self, operation, num1, num2):
        # Write function description
        # Calculates the numbers with an operation that are given by the user

        # Code below this line vvvvv vvvvv vvvvv vvvvv vvvvv
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
                return "Invalid input: num1 and num2 must be numbers"
        # Addition    
        if operation == 'add':
                return num1 + num2
        
        # Subtraction
        elif operation == 'subtract':
                return num1 - num2
        
        # Multiplication
        elif operation == 'multiply':
                return num1 * num2
        
        # Division
        elif operation == 'divide':
            if num2 == 0:
                return "Cannot divide by zero"
            else:
                return num1 / num2

        # Modulus    
        elif operation == 'modulus':
            return num1 % num2
        
        # Code above this line ^^^^^ ^^^^^ ^^^^^ ^^^^^ ^^^^^ 

# Instructor's test cases
# ===== ===== ===== ===== =====

calculator = SimpleCalculator()

print(calculator.calculate('add', 5, 3))          # Expected Output: 8
print(calculator.calculate('subtract', 10, 4))    # Expected Output: 6
print(calculator.calculate('multiply', 6, 7))     # Expected Output: 42
print(calculator.calculate('divide', 8, 2))       # Expected Output: 4
print(calculator.calculate('divide', 9, 2))       # Expected Output: 4.5
print(calculator.calculate('divide', 8, 0))       # Expected Output: Cannot divide by zero
print(calculator.calculate('modulus', 8, 3))      # Expected Output: 2
print(calculator.calculate('add', 5, 'three'))    # Expected Output: Invalid input: num1 and num2 must be numbers