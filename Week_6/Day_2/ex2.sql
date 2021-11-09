--1--
--SELECT * FROM items ORDER BY price ASC
--SELECT * FROM items WHERE price >= 80 ORDER BY price DESC
--SELECT * FROM costumers ORDER BY l_name ASC FETCH FIRST 3 ROWS ONLY ;
--SELECT SUBSTR FROM costumers ORDER BY l_name DESC 
--SELECT l_name FROM costumers ORDER BY l_name DESC
--select * from costumers

--2--
--DROP TABLE purchases;
--CREATE TABLE purchase (item_id int, costumer_id int,
						--foreign key (item_id) references items(item_id),
						--foreign key(costumer_id)
						--references costumers(costumer_id))
--INSERT INTO purchase (item_id, costumer_id) VALUES (2, 1), (1, 2), (1, 3), (3, 5), (3, 4)

--3--
--SELECT*FROM items JOIN purchase
--ON items.item_id = purchase.item_id;
--SELECT costumers.f_name, costumers.l_name, items.item_id, items.price
--FROM costumers
--inner join purchase on purchase.costumer_id = costumers.costumer_id
--inner join items on purchase.item_id = items.item_id
--where costumers.costumer_id = 4
--INSERT INTO purchase (item_id, costumer_id) VALUES (2, 4), (1, 2)

--4--
--select * from costumers
--INSERT INTO items (item, price) values ('hard drive', 250)
--INSERT INTO purchase (item_id, costumer_id) VALUES (5, 3)

--5--
select costumers.f_name, costumers.l_name, items.item
FROM costumers, items, purchase WHERE purchase.costumer_id = costumers.costumer_id AND purchase.item_id = items.item_i
