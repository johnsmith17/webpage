DROP TABLE IF EXISTS sea_data;
CREATE TABLE IF NOT EXISTS sea_data (
ID INTEGER PRIMARY KEY,
datum varchar(10) NOT NULL,
ura varchar(6) NOT NULL,
plima int(3) NOT NULL,
temp int(2,1) NOT NULL
)
