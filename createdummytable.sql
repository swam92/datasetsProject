/* Create Dummy Table for news subreddit */
DROP TABLE IF EXISTS news;
CREATE TABLE news (
  created_utc INT,
  score INT,
  domain VARCHAR(255),
  id VARCHAR(50),
  title TEXT,
  author VARCHAR(255),
  ups INT,
  downs INT,
  num_comments INT,
  permalink VARCHAR(255),
  selftext TEXT,
  link_flair_text VARCHAR(255),
  over_18 BOOLEAN,
  thumbnail VARCHAR(10),
  subreddit_id VARCHAR(255),
  edited VARCHAR(255),
  link_flair_css_class VARCHAR(10),
  author_flair_css_class VARCHAR(10),
  is_self BOOLEAN,
  name VARCHAR(255),
  url VARCHAR(255),
  distinguished VARCHAR(10),
  PRIMARY KEY (id)
);

LOAD DATA LOCAL INFILE "news.csv" INTO TABLE news
FIELDS TERMINATED BY ',' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

/* test query to make sure we can select a range of time with the unix timestamp data type */
SELECT FROM_UNIXTIME(created_utc) as time, ups, downs, title
FROM news
WHERE created_utc > UNIX_TIMESTAMP('2013-06-12')
AND created_utc < UNIX_TIMESTAMP('2013-06-14');
