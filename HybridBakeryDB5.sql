USE hybrid_bakery;

ALTER TABLE customer
ADD user_role ENUM('client', 'staff');
