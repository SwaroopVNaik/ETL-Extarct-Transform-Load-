CREATE DATABASE etl_db;

USE etl_db;

CREATE TABLE cart_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cart_id INT,
    product_id INT,
    title VARCHAR(255),
    price FLOAT,
    quantity INT,
    total FLOAT,
    discountPercentage FLOAT,
    discountedPrice FLOAT
);

SELECT * FROM cart_details;