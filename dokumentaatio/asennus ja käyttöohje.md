# Juoksuovelluksen käyttö- ja asennusohje

## Asennus

Sovellus tarvitsee toimiakseen Poetryn sekä Python 3:n

1. Kloonaa projekti omalle koneelle

git clone https://github.com/AnnaKivekass/ot-harjoitustyo.git

2. Siirry projektikansioon komennolla

cd ot-harjoitustyo

3. Asenna riippuvuudet komennolla

poetry install

--- 

## Sovelluksen käynnistäminen

käynnistä sovellus komennolla:

poetry run invoke start

### Juoksun tarkemmat tiedot
- Tuplaklikkaamalla juoksua avautuu uusi ikkuna, jossa näkyy:
    - matka
    - aika
    - päivämäärä
    - vauhti (min/km)
    - nopeus (km/h)

--- 

Sovellus tallentaa juoksujen tiedot SQLite tietokantaan, jossa ne säilyvät ohjelman sulkemisen jälkeen
