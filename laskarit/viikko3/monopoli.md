## Monopoli luokkakaavio

```mermaid
classDiagram
    Monopolipeli "1" -- "2" Noppa
    Monopolipeli "1" -- "1" Pelilauta
    Pelilauta "1" -- "40" Ruutu
    Ruutu "1" -- "1" Ruutu : seuraava
    Ruutu "1" -- "0..8" Pelinappula
    Pelinappula "1" -- "1" Pelaaja
    Pelaaja "2..8" -- "1" Monopolipeli

    Monopolipeli "1" -- "1" Aloitusruutu
    Monopolipeli "1" -- "1" Vankila

    Ruutu <|-- Aloitusruutu
    Ruutu <|-- Vankila
    Ruutu <|-- Sattuma ja Yhteismaa
    Ruutu <|-- Katu

    Ruutu "1" -- "1" Toiminto

    SattumaYhteismaa "1" -- "*" Kortti
    Kortti "1" -- "1" Toiminto

    Katu "0..1" -- "1" Pelaaja : omistaja

    class Katu {
        nimi
        talot
        hotelli
    }

    class Pelaaja {
        raha
    }