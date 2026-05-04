## Testausdokumentti

Sovelluksen toimivuutta on testattu automatisoidulla yksikkö- ja integraatiotesteillä.

### Testauksen toteutus

Testaus on toteutettu Pythonin kirjastolla **Unittest**

Testit voidaan suorittaa komennolla:
```
poetry run invoke test
```

Testikattavuusraportti voidaan luoda komennolla:

```
poetry run invoke coverage-report
```
--- 
### Testauksen rakenne

Testit sijaitsevat hakemistossa src/tests.

Testeissä käytetään erillistä testitietokantaa, etteivät testit vaikuta sovelluksen oikeaan dataan.
---

### Yksikkö- ja integraatiotestaus

#### Sovelluslogiikka

Sovelluslogiikkaa testataan `RunApp`-luokan kautta. Testeissä käytetään erillistä testitietokantaa, jotta testaus ei vaikuta varsinaiseen sovelluksen dataan.

Testeissä tarkastellaan seuraavia toiminnallisuuksia:
- juoksun lisääminen, poistaminen ja päivittäminen
- juoksujen listaaminen
- kokonaismatkan ja keskiarvojen laskeminen
- nopeimman ja pisimmän juoksun tunnistaminen
- haku päivämäärän perusteella
- lajittelu matkan ja päivämäärän mukaan
- testataan myös tilanteita, joissa ei ole dataa

---
### Järjestelmätestaus

Sovellusta on testattu manuaalisesti käyttöliittymän kautta ja testauksessa on varmistettu että:

- sovellus toimii normaalikäytössä
- juoksujen lisääminen, poistaminen ja muokkaaminen toimii
- tiedot tallentuvat oikein tietokantaan

---

### Testikattavuus

Sovelluksen testikattavuus on noin 86 %

Keskeiset osat sovelluslogiikasta on testattu kattavasti. Sovelluksen käyttöliittymä on jätetty automatisoidun testauksen ulkopuolelle, mutta sitä on testattu manuaalisesti.

---

### Sovellukseen jääneet laatuongelmat

- tietokantaan voi päätyä virheellisiä päivämääriä jos validointi ohitetaan
- käyttöliittymä ei käsittele kaikkia mahdollisia virhetilanteita kuten esimerkiksi tietokantavirheitä

---