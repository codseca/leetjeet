# Write your MySQL query statement below
select round(100* sum(CASE WHEN order_date= customer_pref_delivery_date THEN 1 
            ELSE 0
            END )/count(*),2) as immediate_percentage from delivery d where d.order_date=
            (select min(order_date) from delivery where d.customer_id=customer_id) ;


