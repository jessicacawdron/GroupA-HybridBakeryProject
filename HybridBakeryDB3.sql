USE hybrid_bakery;

DROP TABLE customer;
DROP TABLE order_details;
DROP TABLE order_items;

CREATE TABLE customer(
id INT PRIMARY KEY AUTO_INCREMENT,
first_name VARCHAR(35) NOT NULL,
last_name VARCHAR(35) NOT NULL,
email VARCHAR(100) NOT NULL,
pass_word VARCHAR(12) NOT NULL,
phone_number VARCHAR(11) NOT NULL,
home_address_id INT NOT NULL,
billing_address_id INT NOT NULL,
FOREIGN KEY(home_address_id) REFERENCES address(id),
FOREIGN KEY(billing_address_id) REFERENCES address(id));

CREATE TABLE order_detail(
id INT PRIMARY KEY AUTO_INCREMENT,
customer_id INT NOT NULL,
order_value DECIMAL(10,2) NOT NULL,
order_date DATE NOT NULL,
order_status ENUM('processing', 'confirmed', 'despatched', 'delivered'),
delivery_address_id INT NOT NULL,
delivery_recipient VARCHAR(100) NOT NULL,
FOREIGN KEY(customer_id) REFERENCES customer(id),
FOREIGN KEY(delivery_address_id) REFERENCES address(id));

CREATE TABLE order_item(
id INT PRIMARY KEY AUTO_INCREMENT,
order_id INT NOT NULL,
product_id INT NOT NULL,
quantity INT NOT NULL,
product_price DECIMAL(10,2),
FOREIGN KEY(order_id) REFERENCES order_detail(id),
FOREIGN KEY(product_id) REFERENCES product(id));