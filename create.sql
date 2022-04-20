drop table if exists Item;
create table Item(
    ItemID int NOT NULL,
    Name varchar(255) NOT NULL,
    Currently double NOT NULL,
    First_Bid  double NOT NULL,
    SellerID varchar(255) NOT NULL,
    Number_Of_Bids int NOT NULL,
    Buy_Price double, 
    Started double NOT NULL, 
    Ends double NOT NULL, 
    Description varchar(255) NOT NULL, 
    PRIMARY KEY (ItemID),
    FOREIGN KEY (SellerID) REFERENCES Seller(UserID)
);

drop table if exists Bid;
create table Bid (
    ItemID int NOT NULL, 
    Amount double NOT NULL, 
    Bid_Time TIMESTAMP NOT NULL,
    UserID varchar(255) NOT NULL, 
    Rating int NOT NULL, 
    Location varchar(255), 
    Country varchar(255),
    Primary Key (ItemID, UserID),
    FOREIGN KEY (ItemID) REFERENCES Items(ItemID)
);

drop table if exists Seller;
create table Seller (
    UserID int NOT NULL, 
    Rating int NOT NULL, 
    PRIMARY KEY (UserID)
);

drop table if exists Category;
create table Category (
    ItemID int NOT NULL, 
    CategoryName varchar(255) NOT NULL, 
    PRIMARY KEY (ItemID),
    FOREIGN KEY (ItemID) REFERENCES Items (ItemID)
);
