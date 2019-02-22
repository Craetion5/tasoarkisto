## Sovelluksen asentaminen

Lataa projektin zip-tiedosto Githubista tai kloonaa projekti git clonella.
Mene projektin juurikansioon, ja
* luo Python-virtuaaliympäristö komennolla `python3 -m venv venv`
* käynnistä virtuaaliympäristö komennolla `source venv/bin/activate`
* asenna projektin riippuvuudet komennolla `pip install -r requirements.txt`

Näiden vaiheiden jälkeen sovelluksen voi käynnistää paikallisesti komennolla `python3 run.py`

## Sovelluksen käyttäminen

Apua sovelluksen käyttämiseen löytyy tiedostoista 
[user_storyt](https://github.com/Craetion5/tasofoorumi/blob/master/documentation/user_storyt.md)
ja [README](https://github.com/Craetion5/tasofoorumi/blob/master/README.md)

## SQL CREATE TABLE-lauseet

CREATE TABLE account (

	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	admin BOOLEAN NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (admin IN (0, 1))
  
);

CREATE TABLE submission (

	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	code VARCHAR(1440) NOT NULL, 
	description VARCHAR(1440) NOT NULL, 
	featured BOOLEAN NOT NULL, 
	account_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	CHECK (featured IN (0, 1)), 
	FOREIGN KEY(account_id) REFERENCES account (id)
  
);

CREATE TABLE comment (

	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	text VARCHAR(1440) NOT NULL, 
	account_id INTEGER NOT NULL, 
	submission_id INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id), 
	FOREIGN KEY(submission_id) REFERENCES submission (id)
  
);

## SQL komentoesimerkkejä

Näytä tasopostausten data: `select * from submission;`

Näytä tietyn käyttäjän tasot: `select * from submission where submission.account_id = 1;`

Tee käyttäjästä pääkäyttäjä: `update account set admin = 1 where username = 'test';`

