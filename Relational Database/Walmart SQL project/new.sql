CREATE DATABASE walmart;

CREATE TABLE walmart.products (
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    product_description VARCHAR(255) NOT NULL,
    product_price DECIMAL(10,2) NOT NULL,
    product_quantity INTEGER NOT NULL,
    product_image VARCHAR(255) NOT NULL
);

INSERT INTO walmart.products (product_id, product_name,
 product_description, product_price, product_quantity, product_image)
VALUES (1, 'Bread', 'Bread is a staple food in many cultures.', 2.99, 100, 'bread.jpg'),
       (2, 'Milk', 'Milk is a dairy product.', 3.99, 100, 'milk.jpg'),
       (3, 'Eggs', 'Eggs are a staple food in many cultures.', 4.99, 100, 'eggs.jpg'),
       (4, 'Cheese', 'Cheese is a dairy product.', 5.99, 100, 'cheese.jpg')
       
        