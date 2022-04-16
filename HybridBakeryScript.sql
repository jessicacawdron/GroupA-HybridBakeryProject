show databases;

create database if not exists hybrid_bakery;

use hybrid_bakery;

insert into product (id, product_name, price, product_description) values (1, 'Brookie', '5.00', 'Brookies are bars made from marbled layers of fudgy brownie batter and cakey chocolate chip cookie dough.');
insert into product (id, product_name, price, product_description) values (2, 'Cronut', '6.00', 'The Cronut is a croissant-doughnut pastry. It resembles a doughnut and is made from croissant-like dough which is filled with flavored cream and fried in grapeseed oil. The Cronut in its current form was invented in 2013 by French-American pastry chef Dominique Ansel.');
insert into product (id, product_name, price, product_description) values (3, 'Cruffin', '8.00', 'A Cruffin is made from a buttery croissant pastry that has been moulded into a muffin shape and packed with a tasty filling. Once baked, the Cruffin has the crispy, flaky exterior of a croissant, but the doughy centre of a muffin.');
insert into product(product_name, price, product_description) values ("Duffin", 3.70, "Muffin meets doughnut with a raspberry filling"), 
("Cragel", 3.25, "Bagel shaped, croissant-style pastry");
insert into product(product_name, price, product_description) values ("Townie", 4.50, "A Tart-Brownie hybrid"), ("Cretzel",3.99, "A croissant - pretzel mix");
INSERT INTO product VALUES (8, 'Wonut', 2.75, 'We\'ve combined two breakfast favourites to create these decadent waffle donuts! Fluffy, deep-fried and covered in a powdered sugar glaze.'), (9, 'Crookie', 2.50, 'A croissant filled with crushed cookie pieces and topped with a melted, chocolate cream cookie. The crunchy cookie and pillow-soft croissant dough are a winning combination.'), (10, 'Biskie', 3.00, 'The sandwiched dessert of your dreams is a cross between a cake and a cookie. Two chewy dark chocolate cookies are filled with cream and handmade salted caramel sauce.');

select * from product;

insert into allergen(allergen_type) values ("Tree Nuts"), ("Gluten"), ("Milk"), ("Eggs"), ("Peanuts");

select * from allergen;

UPDATE product
SET product_description = 'Brookies are bars made from marbled layers of fudgy brownie batter and cakey chocolate chip cookie dough. These are also gluten free!' 
WHERE id = 1;

insert into product_allergen(product_id, allergen_id) values (1,3), (1,4), (2,2), (2,3), (2,4), (3,2), (3,3),(3,4), (4,2),(4,3),(4,4), (5,2),(5,3),(5,4),(6,1), (6,2),(6,3),(6,4), (7,2),(7,3),(7,4), (8,2),(8,3),(8,4), (9,2),(9,3),(9,4),(9,5), (10,2),(10,3),(10,4);

select * from product_allergen;

UPDATE product
SET product_description = 'Townies are a tart-brownie cross. The outside is a tart case, crispy, buttery and delicious, with a brownie centre that is indulgently nutty.'  
WHERE id = 6;

UPDATE product
SET product_description = 'A cretzel is a croissant crossed with a pretzel. It combines the perfectly chewy bite of a pretzel with the buttery, flaky pastry of a croissant.'  
WHERE id = 7;