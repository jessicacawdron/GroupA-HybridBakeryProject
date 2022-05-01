USE hybrid_bakery;

INSERT INTO order_detail(customer_id, order_value, order_date, order_status, delivery_address_id, delivery_recipient) 
VALUES (9, 32.60, '2021-09-03', 'delivered', 1, 'Rachel Green'),
(12, 19.10, '2021-12-10', 'delivered', 6, 'Mr Smith'), 
(13, 47.20, '2022-03-14', 'delivered', 5, 'Miles Davis'), 
(14, 63.00, '2022-05-04', 'processing', 2, 'Hayley Taylor'),
(12, 43.50, '2022-05-04', 'processing', 4, 'Kath Woodhouse'),
(1, 71.35, '2022-05-03', 'confirmed', 3, 'Miss Brown'),
(14, 31.85, '2022-05-03', 'despatched', 4, 'Miss Brown'), 
(2, 29.95, '2022-04-27', 'delivered', 3, 'Jon Martin');

SELECT * FROM customer;

