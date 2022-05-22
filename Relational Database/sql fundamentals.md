### A relation(table)
    is a set of Tuples(rows)

* Each element in a tuple(cell value) is a member of a data domain(set of allowed values)
* These elements are called attribute values, and are associated with an **attribute** (column name + type)

### Schema
    is the shape or structure of one's data (as opposed to values themselves)

* these are the Tables, column names, types and constraints
* Strongly connected to your data domain

### Relational Algebra
Involves no variables and is a procedural way of thinking
### Relational Calculus
Is a declarative way of thinking and stating what need to be done

### Structured Query Language
used to manage data in a relational database management system
- its declarative
- can be procedural too(PL/SQl)
- inspired by Codd's relational Model

### SQL language elements
- Select clause E.g. SELECT * FROM  Employee
- Where clause WHERE id = 123 AND is_admin = "true"
  ("true" is an expression) 
- Predicate is an expression evaluated to either true or false or undefined
- An Expression is something that produces tables or scaler values

### SELECT * FROM Employee
    SELECT
- returns a result set
- let assume results are rows
 
      FROM 
- allows one or more elements to be returned from a relation