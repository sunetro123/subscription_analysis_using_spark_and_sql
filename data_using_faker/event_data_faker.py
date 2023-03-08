from faker import Faker
import random
import datetime 

# Set the seed value
random.seed(1234)

# Create an instance of the Faker class
fake = Faker()
Faker.seed(0)

# A dictionary mapping customer_id to name

customer_name_dict = {
    1: "Syd",
    2: "Roger",
    3: "David",
    4: "Nick",
    5: "Richard"
}

product_sku_dict = {
    1: "TRIAL_00",
    2:  "BASIC_9_99",
    3: "PREMIUM_14_99",
    4: "AD_SUPRT_5_99"
}
# TODO Learning - faker date_time_between takes datetime.date
# TODO Learning using customer_name from dict 
start_date = datetime.date(year=2023, month=1, day=1)
end_date = datetime.date(year=2023, month=1, day=31)
# Generate a list of tuples with fake data
dataset = [(fake.uuid4(),  customer_name_dict[x],  product_sku_dict[fake.random_int(min=1, max=4)], fake.date_time_between(start_date=start_date, end_date=end_date)) for x in range(1,6)]

# Print the generated dataset
print(dataset)
    