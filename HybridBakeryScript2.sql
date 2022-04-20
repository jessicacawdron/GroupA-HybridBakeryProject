USE hybrid_bakery;

INSERT INTO address(first_line, second_line, town, postcode) VALUES ('3 Burley Road', 'Burley', 'Leeds', 'LS8 3CT'), ('61 Town Street', 'Greendale', 'Sheffield', 'S12 4QP');

INSERT INTO customer(first_name, last_name, email, phone_number, home_address, billing_address) VALUES ('John', 'Smith', 'john@email.com', '01234567890', 1, 1), ('Jane', 'Jones', 'jane@email.com', '02345678901', 2, 2);

INSERT INTO order_details(customer_id, order_value, order_date, order_status, delivery_address, delivery_recipient) VALUES (1, 10.00, '2022-04-18', 'confirmed', 1, 'Mr Smith'), (2, 20.00, '2022-04-19', 'despatched', 2, 'Mrs Jones');

INSERT INTO order_items(order_id, product_id, quantity) VALUES (1, 1, 2), (2, 2, 1), (2, 3, 4);

SELECT *
FROM address;

SELECT *
FROM customer;

SELECT *
FROM order_details;

SELECT *
FROM order_items;

INSERT INTO address(first_line, second_line, town, postcode) VALUES ('11 Green Rise', 'Headingley', 'Leeds', 'LS4 8FT'),('103 New Street', 'High Green', 'Sheffield', 'S12 4ND'),('95 Park Row', 'Sheepridge', 'Huddersfield', 'HD13 6TH');
INSERT INTO customer(first_name, last_name, email, phone_number, home_address, billing_address) VALUES ('Connor', 'Larkin', 'CLarkin@email.com', '07356673985', 2, 2), ('Sally','Long', 'SallyL@email.co.uk','074982762892',3,3), ('James','Ellis', 'JamesEllis@email.com','07345786211');