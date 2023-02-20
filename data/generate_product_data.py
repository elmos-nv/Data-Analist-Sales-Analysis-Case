'''
-- Generate Product Data --

This script will generate a product csv with the following attributes:

Date: Date of the transaction
Product: Name of the product
Category: Category of the product (e.g., clothing, accessories)
Price: Price of the product
Region: Region where the sale took place
Customer ID: Unique identifier for each customer
Quantity: Quantity of the product sold in the transaction

Ben Selleslagh - ben.selleslagh@elmos.be
'''
import pandas as pd
import requests, tqdm
from faker import Faker
fake = Faker('nl_BE')



def date_generator():
    # Generate a date between now and 1 year ago
    date = fake.date_between(start_date='-1y', end_date='today')
    return date

def price_generator():
    price = fake.pyfloat(left_digits=2, right_digits=2, positive=True)
    return price

def city_generator():
    # Only generate cities in Belgium
    city = fake.city()
    return city

def customer_id_generator():
    customer_id = fake.random_int(min=1, max=1000)
    return customer_id

def quantity_generator():
    quantity = fake.random_int(min=1, max=10)
    return quantity

def age_generator():
    age = fake.random_int(min=18, max=100)
    return age

def main(rows):
    # Now let's a DataFrame with a random products from the products DataFrame
    # and add the other attributes
    data = []
    products = pd.read_csv('ikea.csv')

    for i in tqdm.tqdm(range(rows)):

        # Print the number of the iteration
        order_id = i
        # Select a random products from the products DataFrame, between 1 and 5
        orders = products.sample(n=fake.random_int(min=1, max=5))
        orders.reset_index(drop=True)
        customer_id = customer_id_generator()
        age = age_generator()
        city = city_generator()
        date = date_generator()
        

        for index, row in orders.iterrows():
            data.append([order_id, date, row['name'], row['category'], row['price'], age, city, customer_id, quantity_generator()])
    
    data = pd.DataFrame(data, columns=['Order ID', 'Date', 'Product', 'Category', 'Price', 'Age', 'City', 'Customer ID', 'Quantity'])
    data.to_csv('sales_data.csv', index=False)

if __name__ == '__main__':
    main(rows=10000)
