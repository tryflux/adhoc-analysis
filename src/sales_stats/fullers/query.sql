select id
    , account_id
    , merchant_name
    , updated_date
    , amount 
    , (metadata -> 'location' ) -> 'google_places_id'  as google_location
    , (metadata -> 'location' ) -> 'name'  as location_name
from receipts.transactions
where provider = 'STARLING'
    and source = 'BANK'
    and updated_date between '01-MAR-20'::date and '28-FEB-21'::date
;