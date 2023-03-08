# Task Mar-08-2023

## Unknown -- How Faker works 

https://python.plainenglish.io/generating-a-fake-database-with-python-8523bf6db9ec

Do I need table or S3:// storage ?

### Plan on Faker Working 

I want to start with 4-5 customers only for the month of Jan

I would have a dictionary that would map customer_id to name 

1 -> Syd ( Trial - acquired -- same tier long time )
2 -> Roger ( trial - acquired basic -- cancelled - came back)
3 -> David ( trial - acquired basic -- downgraded ad-supported -- upgraded basic )
4 -> Nick ( trial - acquired basic -- upgraded to premium -- downgraded to ad-supported - upgraded to basic )
5 -> Richard (trial - acquired basic - cancelled -- CHURN)

## End Goal 

**A transaction Table** 

| customer_name | sku | transaction_date |
|---------------|-----|------------------|
|               |     |                  |
|               |     |                  |
|               |     |                  |

**A Final Fact Table**

**Subscription_Master_Daily_State**

customer_name, state(trial/acquired), latest_acquired_date, cancelled_date, current_sku, sku_start_date, scu_end_date(7 if trial, 30 otherwise), prev_sku, prev_sku_start_date, prev_sku_end_date
