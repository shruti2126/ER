-- Find the number of users from New York

with TotalID(UserID, Location) as (select distinct UserID, Location
                                   from Bid
                                   where Location = "New York"
                                   union
                                   select distinct UserID, Location
                                   from Seller
                                   where Location = "New York")
select distinct count(UserID)
from TotalID;