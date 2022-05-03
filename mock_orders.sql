USE hybrid_bakery;
INSERT INTO order_detail(customer_id, order_value, order_date, order_status, delivery_address_id, delivery_recipient) 
VALUES (6, 48.00, '2022-04-29', 'delivered', 4, 'Prue Leith'),
(6, 32.60, '2022-04-24', 'delivered', 1, 'Matt Lucas'),
(6, 25.00, '2022-04-30', 'delivered', 3, 'Paul Hollywood');
SELECT * FROM order_detail;
