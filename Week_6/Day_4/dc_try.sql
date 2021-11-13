/*
create table items (
	item_id serial primary key,
	item_name varchar (50) not null,
	price decimal default 0
)
*/
/*
create table orders (
	order_id serial primary key,
	order_number bigint not null,
	item_id bigint references items(item_id),
	unique(item_id)
);
*/
/*
create table users (
	user_id serial primary key,
	user_name varchar (50) not null,
	order_id bigint references orders(order_id),
	unique(order_id)
);
*/
--insert into items(item_name, price)
--values ('pen', 3), ('note book', 20),('TV', 3400), ('wireless cable', 10000)

--insert into orders(order_number, item_id)
--values (1,4), (1, 3), (2, 1), (2,2)

--insert into users(user_name, order_id)
--values ('Marta', 1), ('Frida', 2), ('Moshe', 3)

drop function total_price(int);

CREATE or REPLACE FUNCTION total_price(x int) 
RETURNS decimal AS $total$
BEGIN
   RETURN(
   select sum(items.price) 
	FROM orders 
	join items on items.item_id = orders.item_id
	join users on users.user_id = orders.item_id
	where orders.order_number = x
   );
END;
$total$ LANGUAGE plpgsql;

select*from total_price(1)
