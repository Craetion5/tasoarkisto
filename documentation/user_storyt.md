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
  
