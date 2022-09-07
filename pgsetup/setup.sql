CREATE SCHEMA pizzeria
CREATE TABLE pizzeria.orders(
    order_id SERIAL,
    customer_id INTEGER,
    pizzas_name VARCHAR,
    pizzas_price INTEGER,
    datetime VARCHAR
);
CREATE TABLE pizzeria.customer(
	customer_id INTEGER,
	first_name VARCHAR,
	last_name VARCHAR,
	datetime VARCHAR
)
