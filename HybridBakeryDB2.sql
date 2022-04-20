USE hybrid_bakery;

CREATE TABLE address(
id INT PRIMARY KEY AUTO_INCREMENT,
first_line VARCHAR(100) NOT NULL,
second_line VARCHAR(100),
town VARCHAR(35) NOT NULL,
postcode VARCHAR(10) NOT NULL);

CREATE TABLE customer(
id INT PRIMARY KEY AUTO_INCREMENT,
first_name VARCHAR(35) NOT NULL,
last_name VARCHAR(35) NOT NULL,
email VARCHAR(100) NOT NULL,
phone_number VARCHAR(11) NOT NULL,
home_address INT NOT NULL,
billing_address INT NOT NULL,
FOREIGN KEY(home_address) REFERENCES address(id),
FOREIGN KEY(billing_address) REFERENCES address(id));

CREATE TABLE order_details(
id INT PRIMARY KEY AUTO_INCREMENT,
customer_id INT NOT NULL,
order_value DECIMAL(10,2) NOT NULL,
order_date DATE NOT NULL,
order_status ENUM('processing', 'confirmed', 'despatched', 'delivered'),
delivery_address INT NOT NULL,
delivery_recipient VARCHAR(100) NOT NULL,
FOREIGN KEY(customer_id) REFERENCES customer(id),
FOREIGN KEY(delivery_address) REFERENCES address(id));


CREATE TABLE order_items(
id INT PRIMARY KEY AUTO_INCREMENT,
order_id INT NOT NULL,
product_id INT NOT NULL,
quantity INT NOT NULL,
FOREIGN KEY(order_id) REFERENCES order_details(id),
FOREIGN KEY(product_id) REFERENCES product(id));

