# Juoksuovelluksen käyttö- ja asennusohje

## Asennus

Sovellus tarvitsee toimiakseen Poetryn sekä Python 3:n

1. Kloonaa projekti omalle koneelle
```
git clone https://github.com/AnnaKivekass/ot-harjoitustyo.git
```

2. Siirry projektikansioon komennolla
```
cd ot-harjoitustyo
```

3. Asenna riippuvuudet komennolla
```
poetry install
```
--- 

## Sovelluksen käynnistäminen

käynnistä sovellus komennolla:

```
poetry run invoke start
```
aja sovelluksen testit komennolla:
```
poetry run invoke test
```
generoi testikattavuusraportti komennoilla:
```
poetry run invoke coverage

poetry run invoke coverage-report
```

aja pylint raportti komennolla:
```
poetry run invoke lint
```


---

# Sovelluksen käyttö

Sovelluksen avulla käyttäjä voi:

- lisätä uusia juoksusuorituksia
- muokata ja poistaa suorituksia
- tarkastella tilastoja 
- hakea  päivämäärällä suorituksia
- lajitella suorituksia päivämäärän ja matkan perusteella
- tarkastella graafeja

### Juoksusuorituksen lisääminen

Syötä kenttiin:
- matka (kilometreinä)
- aika (minuutteina)
- päivämäärä muodossa `dd.mm.yyyy`

**Add Run**

---

### Juoksusuorituksen muokkaaminen

1. Valitse suoritus listasta  
2. **Load Selected**  
3. Muokkaa tietoja  
4. **Update Run**

---

### Juoksusuorituksen poistaminen

1. Valitse suoritus listasta  
2. **Delete Selected**

---

### Juoksun tarkemmat tiedot

Tuplaklikkaamalla juoksua listasta avautuu uusi ikkuna, jossa näkyy

- matka
- aika
- päivämäärä
- vauhti (min/km)
- nopeus (km/h)

---

## Tietojen tallennus

Sovellus tallentaa juoksut SQLite-tietokantaan (`runs.db`)

Tallennetut tiedot säilyvät ohjelman sulkemisen jälkeen

---

## Mahdolliset virhetilanteet

- Jos syötteet ovat virheellisiä sovellus näyttää virheilmoituksen
- Päivämäärän tulee olla muodossa `dd.mm.yyyy`