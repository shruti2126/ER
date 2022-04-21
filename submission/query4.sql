-- Find the IDs of auction(s) with the highest current price

Select ItemID 
from Items
where Number_Of_Bids != 0 and Currently = (select max(Currently)
                                           from Items);