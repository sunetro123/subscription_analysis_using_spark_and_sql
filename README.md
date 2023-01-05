# SUMMARY
Data Engineering Repo to Show Data Analysis on Subscription Transactions


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

