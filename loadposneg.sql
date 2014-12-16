DROP TABLE IF EXISTS posneg;
CREATE TABLE posneg (
	id VARCHAR(50),
	posneg INT,
	PRIMARY KEY (id)	
);

LOAD DATA LOCAL INFILE 'output.txt' INTO TABLE posneg;