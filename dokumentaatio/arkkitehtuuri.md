# Arkkitehtuuri

```mermaid
classDiagram

class GUI {
}


class RunApp {
    +add_run(distance, minutes, date)
    +list_runs()
    +delete_run(id)
    +update_run(id, distance, minutes, date)
    +distance_total()
    +average_pace()
    +longest_run()
    +fastest_run()
    +average_distance()
    +find_date(date)
    +sort_by_distance()
    +sort_by_date()
}

class Run {
    +distance
    +minutes
    +date
    +pace()
    +speed()
}

class Database {
    +add_run()
    +get_runs()
    +delete_run()
}

GUI --> RunApp
RunApp --> Run
RunApp --> Database
```
---

## Sovelluksen rakenne

Sovellus on jaettu kolmeen pääosaan: käyttöliittymään, sovelluslogiikkaan ja tietojen tallennukseen
---

## Pakkausrakenne

Sovelluksen koodi on jaettu loogisiin osiin:

- `gui.py`: käyttöliittymä
- `run.py`: sovelluslogiikka (RunApp)
- `database`: tietokantatoiminnot
- `graphs.py`: graafien piirtäminen

Rakenne noudattaa arkkitehtuuria, jossa käyttöliittymä riippuu sovelluslogiikasta ja sovelluslogiikka riippuu tietokannasta.
---

## Käyttöliittymä GUI

Käyttöliittymä on toteutettu Tkinterillä ja se vastaa käyttäjän syötteiden vastaanottamisesta ja tulosten näyttämisestä. RunApp tarjoaa käyttöliittymälle kaikki sovelluksen toiminnot.

Käyttäjä voi käyttöliittymän kautta:

- lisätä juoksusuorituksia
- poistaa juoksusuorituksia
- tarkastella tilastoja
- hakea suorituksia päivämäärän perusteella

---
- Käyttöliittymä ei sisällä sovelluslogiikkaa, vaan kutsuu RunApp luokasta metodeja.
---

## Sovelluslogiikka RunApp

RunApp sisältää kaiken logiikan, joka liittyy juoksusuoritusten käsittelyyn.

- vastaanottaa pyynnöt käyttöliittymältä
- käsittelee dataa
- kutsut tietokannasta

Sisältää seuraavat toiminnot

- Suoritusten lisääminen ja poistaminen
- Kokonaismatkan laskeminen
- Keskimääräisen vauhdin laskeminen
- Pisimmän ja nopeimman suorituksen etsiminen
- Hakeminen päivämäärän perusteella
---

## Run luokka

Run luokka kuvaa yksittäistä juoksusuoritusta

Sisältää seuraavat toiminnot

- Matka
- Aika
- Päivämäärä

Sisältää metodit

- Vauhdin laskeminen (pace)
- Nopeuden laskeminen (speed)
---

## Tietokanta (database)

Tietojen pysyväistallennus on toteutettu tietokannalla SQLite.

Tietokantakerros:

- Tallentaa juoksusuoritukset
- Hakee suorituksia
- Poistaa suorituksia

Tietokantaan tallennetaan jokaiselle suoritukselle:

- Id
- Distance
- Minutes
- Date

---

## Sovelluksen toiminnallisuutta kuvaava sekvenssikaavio, joka esittää juoksusuorituksen lisäämisen.


```mermaid
sequenceDiagram
    participant User
    participant GUI
    participant RunApp
    participant Database

    User->>GUI: klikkaa "Add"
    GUI->>RunApp: add_run(distance, minutes, date)
    RunApp->>Database: add_run(...)
    Database-->>RunApp: ok
    RunApp-->>GUI: updated list

```
---
- Kaavio kuvaa, miten käyttäjän lisäämä suoritus kulkee käyttöliittymästä sovelluslogiikan kautta tietokantaan ja päivitetty tieto palautetaan takaisin käyttöliittymälle.
---

## Sovelluksen toiminnallisuutta kuvaava sekvenssikaavio, joka esittää juoksusuorituksen poistamisen

```mermaid
sequenceDiagram
    participant User
    participant GUI
    participant RunApp
    participant Database

    User->>GUI: poistaa suorituksen
    GUI->>RunApp: delete_run(id)
    RunApp->>Database: delete_run(id)
    Database-->>RunApp: ok
    RunApp-->>GUI: updated list
```
---
- Kaavio kuvaa, miten valittu suoritus poistetaan tietokannasta sovelluslogiikan kautta jonka jälkeen käyttöliittymä päivitetään vastaamaan muutosta.
---

## Ohjelman rakenteeseen jääneet heikkoudet: