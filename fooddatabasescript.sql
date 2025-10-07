CREATE DATABASE food_delivery_db;
USE food_delivery_db;

-- Customers Table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(100)
);

-- Foods Table
CREATE TABLE foods (
    food_id INT AUTO_INCREMENT PRIMARY KEY,
    food_name VARCHAR(100),
    price DECIMAL(6,2)
);

-- Orders Table
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    food_id INT,
    quantity INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (food_id) REFERENCES foods(food_id)
);
INSERT INTO customers (name, city) VALUES
('Arun', 'Chennai'), ('Meena', 'Madurai'), ('Vijay', 'Coimbatore');

INSERT INTO foods (food_name, price) VALUES
('Pizza', 250), ('Burger', 150), ('Pasta', 200), ('Idli', 50);

INSERT INTO orders (customer_id, food_id, quantity, order_date) VALUES
(1, 1, 2, '2025-10-01'),
(2, 2, 3, '2025-10-02'),
(3, 4, 5, '2025-10-03'),
(1, 3, 1, '2025-10-04'),
(2, 1, 1, '2025-10-04');
