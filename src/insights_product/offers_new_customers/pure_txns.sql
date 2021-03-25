with receipts as (
    select customer_id
         , account_id
         , id                                                       as receipt_id
         , (jsonb_array_elements(items) ->> 'itemId'):: uuid        as item_id
         , jsonb_array_elements(items) -> 'unitAmount'->> 'amount'  as item_price
         , updated_date
         , location_id
         , total_amount
    from analytics.int_receipts_without_bank
    where merchant_id in (select id
                          from merchants.merchants
                          where lower(name) like '%pure%')
)
select r.*
     , i.sku
     , i.name
from receipts r
left join items.items i
    on r.item_id = i.id
where r.updated_date between '01-SEP-20'::date and '31-DEC-20'::date