--ex1--
--1--
--select * from language
--2--
--select film.title, film.description, language.name
--from film
--left join language on film.language_id = language.language_id
--select film.title, film.description, language.name
--from film
--right join language on film.language_id = language.language_id
--3--
--create table new_film (id serial primary key, name varchar(50))
--insert into new_film (name) values ('Jango unchained'), ('12 years a slave'), ('pulp fiction')
--4--
/*
create table customer_review (
	review_id serial primary key NOT NULL,
	film_id int references new_film(id) not null,
	language_id int references language(language_id) not null,
	title varchar(50) not null,
	score smallint,
	review_text text,
	last_update date
)*/
--5--
--insert into customer_review(film_id,language_id,title,score,review_text,last_update)
--values(1, 1, 'review by Norman', 7, 'This film is recommandable', '2000-02-20'), 
--	(2, 3, 'review by Dafna', 9, 'Just awesome', '2021-10-12')
--6--
--got an error and deleted the customer_review to delete the new_film
--delete from customer_review where film_id in (1, 2)
--delete from new_film where id in(1, 2)

--ex2---------------------------------------------------------------------------------------
--1--
--update film set language_id = 3 where title = 'Ace Goldfinger'
--2--
--store_id, adress_id both are required to insert a new item
--3--
--drop table customer_review
--4--
--select count(*) from rental where return_date is NULL
--5--
/*
select film.title, payment.amount
from rental
join payment on rental.rental_id = payment.rental_id 
join inventory on inventory.inventory_id = rental.inventory_id
join film on inventory.film_id = film.film_id
where return_date is Null
order by payment.amount desc
limit 30 
*/
--6--
select *
from film
join film_actor on film.film_id = film_actor.film_id
join actor on film_actor.actor_id = actor.actor_id
where actor.first_name = 'Penelope' and actor.last_name = 'Monroe'
and film.description like '%Sumo Wrestler%'

