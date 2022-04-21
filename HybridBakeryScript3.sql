USE hybrid_bakery;

INSERT INTO customer(first_name, last_name, email, phone_number, home_address_id, billing_address_id) VALUES ('John', 'Smith', 'john@email.com', '01234567890', 1, 1), ('Jane', 'Jones', 'jane@email.com', '02345678901', 2, 2);

INSERT INTO order_detail(customer_id, order_value, order_date, order_status, delivery_address_id, delivery_recipient) VALUES (1, 10.00, '2022-04-18', 'confirmed', 1, 'Mr Smith'), (2, 20.00, '2022-04-19', 'despatched', 2, 'Mrs Jones');

INSERT INTO order_item(order_id, product_id, quantity) VALUES (1, 1, 2), (2, 2, 1), (2, 3, 4);

INSERT INTO customer(first_name, last_name, email, phone_number, home_address_id, billing_address_id) VALUES ('Connor', 'Larkin', 'CLarkin@email.com', '07356673985', 2, 2), ('Sally','Long', 'SallyL@email.co.uk','074982762892',3,3), ('James','Ellis', 'JamesEllis@email.com','07345786211');