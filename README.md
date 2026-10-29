# Partits de la setmana

Pàgina amb el calendari de partits d’Ainet i Roc. El calendari de Roc s’actualitza sol; el d’Ainet es canvia a mà.

## Posar-la en marxa (una sola vegada)

1. Crea un compte a [github.com](https://github.com) i un **repositori públic nou** (per exemple `partits`).
2. Puja-hi aquests fitxers amb *Add file → Upload files*. Si el sistema amaga la carpeta `.github`, crea el fitxer a mà amb *Add file → Create new file*, escrivint com a nom `.github/workflows/update.yml` i enganxant-hi el contingut.
3. **Settings → Pages**: *Source* = *Deploy from a branch*, branca `main`, carpeta `/ (root)`.
4. **Settings → Actions → General → Workflow permissions**: tria *Read and write permissions* i desa.
5. Pestanya **Actions → Actualitza partits → Run workflow**. Això crea el fitxer `data.json`.
6. La pàgina serà a `https://EL-TEU-USUARI.github.io/partits/` (triga uns minuts la primera vegada).

## Com s’actualitza

- **Roc:** una tasca automàtica llegeix el calendari (`data/teams/roc.json`, camp `ics`) dos cops al dia i cada hora de divendres a diumenge. Si hi ha canvis o resultats nous, es reescriu `data.json` i la pàgina es posa al dia.
- **Ainet:** edita `data/teams/ainet.json` des de GitHub (icona del llapis). En desar, la tasca s’executa sola. Cada partit té `d` (data), `t` (hora), `h` (`true` si juga a casa), `rival`, `place`, `addr` i `blurb` (la frase).
- **Un altre equip:** copia un d’aquests fitxers a `data/teams/` i canvia’n les dades. Si té enllaç `.ics`, posa’l al camp `ics` i no cal escriure partits.

## A tenir en compte

- Si la tasca falla (per exemple, si canvia l’enllaç del calendari), GitHub t’envia un correu i la pàgina conserva les últimes dades.
- GitHub pot aturar les tasques programades si el repositori passa 60 dies sense activitat. Es reactiven a la pestanya *Actions*.
- El repositori i la pàgina són públics: només hi ha noms de pila i horaris. No hi posis cognoms ni dades de contacte.

## Autor: Albert Saragossa Alòs
