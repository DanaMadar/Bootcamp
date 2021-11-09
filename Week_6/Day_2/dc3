
/*
create table customer(
	customer_id serial primary key,
	f_name varchar (30) not null,
	l_name varchar(30) not null
);

create table customer_profile(
	costumer_profile_id serial primary key,
	balance int default 0,
	foreign key (costumer_profile_id) references customer(customer_id)
);

insert into customer (f_name, l_name)
values ('Angi', 'Braut'), ('Paul', 'Nussbaum'), ('Dafna', 'Diamond');

insert into customer_profile(balance)
values ('1000'), ('9999'), ('7854')
*/

--select *
--from customer
--join customer_profile on customer.customer_id=customer_profile.costumer_profile_id
--left join customer_profile on customer.customer_id=customer_profile.costumer_profile_id
--right join customer_profile on customer.customer_id=customer_profile.costumer_profile_id
--full join customer_profile on customer.customer_id=customer_profile.costumer_profile_id
/*
create table product(
	product_id serial primary key,
	p_name varchar (30) not null,
	price int not null
);

create table product_order(
	product_order_id serial primary key,
	customer_id int not null,
	product_id int not null,
	foreign key (product_order_id) references customer(customer_id),
	foreign key (product_order_id) references product(product_id)
);
*/

--insert into product(p_name, price) values ('eggs', '4'), ('salad', '24'), ('ice creme', '20')
--insert into product_order (customer_id, product_id) values ('1','3'), ('2', '2'), ('3','1')

select product.p_name, customer.f_name, customer.l_name
from product_order
join customer on product_order.customer_id=customer.customer_id
join product on product_order.product_id = product.product_id