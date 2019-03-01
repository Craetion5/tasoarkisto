# User storyjä

### Käyttäjä voi luoda käyttäjätunnuksen ja kirjautua sillä
* Käyttäjä painaa nappia "New user"
* Sovellus ohjaa tunnuksenluontilomakkeeseen
* Käyttäjä syöttää nimen, käyttäjätunnuksen ja salasanan, ja painaa nappia "Add new user"
* Uusi tunnus on luotu, ja käyttäjä ohjataan sisäänkirjautumislomakkeseen
* Käyttäjä syöttää luodun tunnuksen käyttäjänimen ja salasanan, ja painaa nappia "Login"
* Käyttäjä ohjataan etusivulle, ja on kirjautunut sisään
* Käyttäjä voi kirjautua ulos painamalla nappia "Logout"

### Käyttäjä voi selata tasoja
* Käyttäjä painaa nappia "View all levels"
* Käyttäjä ohjataan sivulle, jossa on listattu kaikki käyttäjien lähettämät tasot
   * Käyttäjä voi halutessaan kopioida yksittäisen tason koodin suoraan listasta
* Käyttäjä voi avata listasta yksittäistä tasoa vastaavan linkin
* Käyttäjä ohjataan sivulle, jossa hän voi tarkastella tasopostausta
* Käyttäjä voi lisätä kommentin tasoon syöttämällä sen kommenttilomakkeeseen ja painamalla nappia "Submit"
  * Käyttäjän lähettämä kommentti ilmestyy tason sivulle paitsi jos käyttäjä ei ole kirjautunut sisään jolloin hänet ohjataan     kirjautumissivulle
* Jos tarkasteltava taso on käyttäjän oma, näkyy sivulla nappi "Delete this level"
  * Käyttäjän painaessa nappia taso poistetaan, ja käyttäjä ohjataan etusivulle

### Käyttäjä voi jakaa tason ja tarkastella sitä
* Käyttäjä painaa nappia "Submit a level"
   * Jos käyttäjä ei ole sisäänkirjautunut, hänet johdetaan kirjautumissivulle
* Jos käyttäjä on sisäänkirjautunut, hänet johdetaan tasonluontisivulle
* Käyttäjä syöttää nimen, mahdollisen kuvauksen ja sovelluksella tekemän tason tekstimuotoisen koodin, ja painaa nappia "Submit"
* Tasopostaus on luotu, ja käyttäjä ohjataan tasoja listaavalle sivulle
* Käyttäjä avaa luomaansa tasoa vastaavan linkin listasta
* Käyttäjä ohjataan sivulle, jossa hän voi tarkastella tasopostaustaan

### Käyttäjä voi selata yksittäisen käyttäjän tasoja
* Käyttäjä avaa tasopostauksen
* Käyttäjä klikkaa linkkiä, jossa näkyy postauksen tekijä
* Käyttäjä ohjataan sivulle, jossa postauksen tekijän tasot on listattu

### Pääkäyttäjä voi käyttää erityisvoimiaan
* Pääkäyttäjä kirjautuu sisään
* Pääkäyttäjä avaa tasopostauksen
* Sivulla on nappi tason poistamiseen, vaikka taso ei olisi pääkäyttäjän postaama
* Sivulla on nappi "Feature"
  * Nappia painamalla taso lisätään pääkäyttäjien valitsemiin tasoihin, jotka saa näkyviin sovelluksen yläpalkin napista "View featured levels"
  * Jos taso on jo valittu, lukee napissa "Unfeature" ja sitä painamalla taso poistuu valittujen tasojen listasta
  
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

Etsi käyttäjät, joilla on ainakin yksi tasopostaus, laske käyttäjien tasojen määrä ja ryhmittele käyttäjät tasojen määrän mukaan:
  `
  select account.username, count (submission.id), account.id from account
  left join submission on submission.account_id = account.id
  group by account.id
  having count(submission.id) != 0
  order by 0 - count(submission.id)
  `
