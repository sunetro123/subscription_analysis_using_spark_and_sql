# SUMMARY
An end to end workflow for analyzing memebership and financial health of a content subscription company

## The Story

**Windenflix** is a company offering subscription service for streaming digital content in **5** different tiers. 
As a new kid in the block **Windenflix** set up a basic streaming transaction system that captures events such as:
   - event1: First (7 day trial) sign-up of an user
   - event2: Upgrade/Downgrade action of an user
   - event3: Auto-renew toggle event of an user
   - event4: Scheduled automatic payment for an user ( if auto renewal is '**On**')

## The Questions:

 - Total active customers across different tiers in a month or quarter
 - How many new Acquistion in a month ?
 - How many Cancellation in a month ?
 - How many customers downgraded or upgraded tier in a month ?
 - How many customers got reacquired in a month ?

## Start with -> `Data Model`

### Input Payload

### Tables and How They Tie Up 

## Design Consideration
   

## Enter the -> Data Engineer

### Infrastructure

### Set Up

## Think about -> `Scale`

per geography

## 

## Transaction Table:
- event_date
- customer_id
- sku_id
- event_action ENUM('Start Trial', 'Start Sub', 'Cancel Sub', 'Start Autopay', 'Stop Autopay')

## DWH Tables:

### sub_sku_dim

- sku_id (PK)
- sku_name
- sku_price
- sku_validity_period

### sub_member_dim

- member_id (PK)
- member_state

### sub_member_daily_state_master
- sku_id
- member_id
- active_sku_flag
- latest_aquistion_date
- previous_aqusition_date
- latest_sku_start_date
- latest_sku_end_date
- previous_sku_id
- previous_sku_start_date
- previous_sku_end_date
- is_churned_flag
- churn_start_date


### sub_member_monthly_revenue_dwh

- month_id,
- month_name,
- sku_id,
- member_id,
- total_billed_end_of_month
- total_billed_last_month

