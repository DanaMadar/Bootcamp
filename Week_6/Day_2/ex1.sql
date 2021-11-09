--1--

--SELECT * FROM items ORDER BY price ASC
--SELECT * FROM items WHERE price >= 80 ORDER BY price DESC
--SELECT * FROM costumers ORDER BY l_name ASC FETCH FIRST 3 ROWS ONLY ;
--SELECT SUBSTR FROM costumers ORDER BY l_name DESC 
--SELECT l_name FROM costumers ORDER BY l_name DESC
--select * from costumers

--2--
--DELETE FROM purchases;
CREATE TABLE purchases (item_id int, foreign key (item) references items,
						customers_id int primary key ,foreign key(customers)
						references customer(id))
