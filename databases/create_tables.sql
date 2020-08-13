DROP TABLE IF EXISTS Complexes;
DROP TABLE IF EXISTS Buildings;
DROP TABLE IF EXISTS Apartments;
DROP TABLE IF EXISTS AptTenants;
DROP TABLE IF EXISTS Requests;
DROP TABLE IF EXISTS Tenants;


CREATE TABLE IF NOT EXISTS Complexes (
	ComplexID 	int PRIMARY KEY,
	ComplexName	varchar(40)
);
CREATE TABLE IF NOT EXISTS Buildings (
	BuildingID	int PRIMARY KEY,
	ComplexID 	int,
	BuildingName	varchar(40),
	Address		varchar(50)
);
CREATE TABLE IF NOT EXISTS Apartments (
	AptID	int PRIMARY KEY,
	UnitNumber	varchar(10),
	BuildingID int
);
CREATE TABLE IF NOT EXISTS AptTenants (
	TenantID int,
	AptID int,
	PRIMARY KEY (TenantID, AptID)
);
CREATE TABLE IF NOT EXISTS Requests (
	RequestID int PRIMARY KEY,
	Status varchar(50),
	AptID int,
	Description varchar(60)
);
CREATE TABLE IF NOT EXISTS Tenants (
	TenantID	int PRIMARY KEY,
	TenantName	varchar(80)
);

INSERT INTO Buildings VALUES
(11, 1, 'Cloudy Building', '666 Devil Street'),
(12, 1, 'Wow Building', '111 Bevil Street');
INSERT INTO Complexes VALUES 
(1, 'Sunny Homes'),
(2, 'Ocean Hills');
INSERT INTO Apartments VALUES
(1, '1A', 11),
(2, '1B', 11),
(3, '1C', 12);
INSERT INTO AptTenants VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 8),
(3, 5),
(4, 9),
(4, 11);
INSERT INTO Requests VALUES 
(1, 'Open', 1, 'Ganj'),
(2, 'Open', 2, 'Blaze'),
(3, 'Open', 3, 'Juice');
INSERT INTO Tenants VALUES
(1, 'Blaze Juicer'),
(2, 'Ganj Lighter'),
(3, 'George Dinger');
