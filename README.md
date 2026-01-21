# Python OOP – Inheritance (Single Inheritance)

This project demonstrates the concept of **Inheritance in Python** using a
real-world **Company and Employee** example.

## What is Inheritance?
Inheritance allows a child class to reuse the properties and methods of a parent class.
It helps in code reusability and creates a clear relationship between classes.

## Example Used
- **Parent Class:** Company  
  - Stores company-related information such as name and role.
- **Child Class:** Employee  
  - Inherits from Company and stores employee-specific information.

## Key Concepts Implemented
- Single Inheritance
- Constructor (`__init__`)
- Parent–child relationship
- Using `super()` to call the parent constructor

## Implementation Details
- The `Company` class defines common company details.
- The `Employee` class inherits from `Company`.
- `super()` is used to initialize parent class attributes.
- Child class adds its own attributes without duplicating parent logic.

## Sample Output
