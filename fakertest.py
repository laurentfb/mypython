from faker import Faker
import sqlite3


faker = Faker('fr_FR')

c = sqlite3.connect('myDB.db')

#c.execute("INSERT INTO ...")

for _ in range(30):

    name = faker.name()
    address = faker.address()
    phone = faker.phone_number()
    job = faker.job().capitalize()


    print(f'{name}, {address}, {phone}\n{job}\n-------------------------')

c.close()