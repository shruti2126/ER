-- Find the number of users who are both sellers and bidders

select count(distinct b.UserID)
from Bid b
inner join Seller s on b.UserID=s.UserID
order by b.UserID;