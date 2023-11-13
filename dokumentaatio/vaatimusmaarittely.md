 Vaatimusmäärittely
## Sovelluksen tarkoitus
Sovelluksen avulla käyttäjä voi pitää kirjaa päivän onnistumisista ja 
epäonnistumisista sekä antaa päiville arvosanoja. Sovellusta voi käyttää 
useampi rekisteröitynyt käyttäjä, joilla jokaisella on omat päiväkirjamerkintänsä.
Sovelluksessa pystyy tekemään ainostaan yhden merkinnän päivässä.

## Käyttäjät
Alkuvaiheessa sovelluksessa on vain yksi käyttäjärooli eli *normaali* 
käyttäjä. Myöhemmin on mahdollista lisätä *ylläpitäjän* rooli, jolla 
on laajemmat käyttöoikeudet.

## Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista
* Käyttäjä voi luoda käyttäjätunnuksen
	-Käyttäjätunnuksen tulee olla uniikki ja pituudeltaan 
	vähintään yksi merkki.
* Käyttäjä voi kirjautua järjestelmään
	-Jos käyttäjä syöttää olemassaolevan käyttäjätunnuksen ja 
	salasana on oikein, käyttäjä pääsee kirjautumaan sisään.
	-Jos käyttäjätunnusta ei ole tai salasana on väärin, 
	järjestelmä ilmoittaa tästä käyttäjälle,

### Kirjautumisen jälkeen
* Käyttäjä pystyy lisäämään uuden päväkirjamerkinnän ja tarkastelemaan 
mahdollisia vanhempia merkintöjä. Jokaiseen merkintään voi lisätä kolme asiaa:
päivän onnistuminen, epäonnistuminen ja päivän arvosana (asteikolla 1-5). 
Yhdelle päivälle voi tehdä vain yhden merkinnän.
* Merkintöjä pystyy muokkaamaan ja poistamaan jälkikäteen.
* Käyttäjä pystyy myös tarkastelemaan tilastoja annetulla aikavälillä, 
eli pystyy listaamaan kaikki onnistumiset, epäonnistumiset ja/tai arvosanat tietyltä aikaväliltä 
sekä näkemään päivien arvosanojan keskiarvon tietyltä aikaväliltä.

## Jatkokehitysideoita
* Käyttäjä pystyy tekemään monipuolisempia päiväkirjamerkintöjä.
* Ylläpitäjä voi tarkastella sovelluksen käyttöä sekä poistaa käyttäjiä.
* Oman päiväkirjamerkinnän voi jakaa "julkisesti", eli kaikille muille 
rekisteöityneille käyttäjille tai valituille käyttäjille.


