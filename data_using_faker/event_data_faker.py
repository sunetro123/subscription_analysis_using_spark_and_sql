import pandas as pd 
from faker import Faker 

def faker_transaction_event_create():
    faker_obj = Faker()
    faker_date = faker_obj.date()
    return faker_date



if __name__ == "__main__":

    # create fake event

    print(f" fake date is {faker_transaction_event_create()}")

    