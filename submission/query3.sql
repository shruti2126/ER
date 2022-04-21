-- Find the number of auctions belonging to exactly four categories

with catcount as (select ItemId, count(CategoryName) as totalCategories
                  from Category
                  group by ItemID)
select count(ItemID)
from catcount
where totalCategories = 4;