select     id                                                           as txn_id
         , adjusted_transaction_date
         , amount
         , (jsonb_array_elements(items) ->> 'sku'):: varchar            as sku
         , (jsonb_array_elements(items) ->> 'description'):: varchar    as name
from receipts.transactions
where merchant_id in (select id
                      from merchants.merchants
                      where lower(name) like '%pure%')
