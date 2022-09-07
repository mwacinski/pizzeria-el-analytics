import random
from datetime import datetime
from typing import Any, List, Tuple
from faker import Faker
import psycopg2

conn = psycopg2.connect(database="airflow", user='airflow', password='airflow', host='host.docker.internal', port= '5432')
cursor = conn.cursor()

def get_orders(cust_ids: List[int]) -> List[Tuple[int, Any, Any, str]]:
    pizzas = {
        "Margherita": 27,
        "Hawaii": 27,
        "Capriciosa": 28,
        "Chicken": 28,
        "Salami": 29,
        "Sombrero": 29,
        "Mexicana": 29,
        "Hot Retro": 30,
        "Al Capone": 31,
        "Grecos": 32,
        "Colt": 33,
        "Vegatariana": 34,
        "Western": 34,
        "Primavera": 35,
        "Curry": 36,
        "Parmese": 37,
        "Bolognese": 37,
        "Sheriff": 38,
        "Bianca": 39,
    }
    name, price = random.choice(list(pizzas.items()))
    return random.choice(cust_ids), name, price, datetime.now().strftime("%y-%m-%d %H:%M:%S"),



def get_customer_data(cust_ids: List[int]) -> List[Tuple[int, Any, Any, str]]:
    fake = Faker()

    return [
        (
            cust_id,
            fake.first_name(),
            fake.last_name(),
            datetime.now().strftime("%y-%m-%d %H:%M:%S"),
        )
        for cust_id in cust_ids
    ]


def customer_data_insert() -> str:
    return """
        INSERT INTO pizzeria.customer (
        customer_id,
        first_name,
        last_name,
        datetime

        )
        VALUES (
            %s,
            %s,
            %s,
            %s
        )
        """


def orders_data_insert() -> str:
    return """
    INSERT INTO pizzeria.orders (
    customer_id,
    pizzas_name,
    pizzas_price,
    datetime

    )
    VALUES (
        %s,
        %s,
        %s,
        %s
    )
    """


def generate_data():
    cust_ids = [x for x in range(1, 101)]
    orders_data = [get_orders(cust_ids) for _ in range(1000)]
    customer_data = get_customer_data(cust_ids)

    for cd in customer_data:
        cursor.execute(customer_data_insert(), (cd[0], cd[1], cd[2], cd[3]))
        conn.commit()

    for od in orders_data:
        cursor.execute(orders_data_insert(), (od[0], od[1], od[2], od[3]))
        conn.commit()
