DROP TABLE IF EXISTS sentipolar;
CREATE TABLE sentipolar(
	id VARCHAR(50),
	sentiment DOUBLE,
	polarity DOUBLE,
	PRIMARY KEY (id)	
);

LOAD DATA LOCAL INFILE "final.txt" INTO TABLE sentipolar;

