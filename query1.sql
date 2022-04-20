-- Find the total number of users

with allIDs(UserID) as (select UserID
                from Bid
                union
                select UserID
                from Seller)
select distinct count(UserID)
from allIDs;