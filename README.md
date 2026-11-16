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

La FCF no permet que altres webs llegeixin el seu calendari, així que els dos equips es mantenen a mà, cadascun al seu fitxer de `data/teams/`. Per canviar-ne un: obre'l a GitHub, clica el llapis, edita i prem *Commit changes*. En uns minuts la tasca regenera `data.json` i la pàgina es posa al dia.

- **Resultat d’un partit de Roc** (`roc.json`): afegeix al final de la línia del partit els gols de Roc (`gf`) i els del rival (`gc`), per exemple: `{"d": "2026-11-07", ..., "geo": "...", "gf": 2, "gc": 1}`. Recorda la coma abans de `gf`.
- **Canvi d’hora o de pista:** modifica `d` (data), `t` (hora), `place` (pista) o `geo` (coordenades per al mapa).
- **Ainet** (`ainet.json`): cada partit té `d`, `t`, `h` (`true` si juga a casa), `rival`, `place`, `addr` i `blurb` (la frase).
- **Un altre equip:** copia un d’aquests fitxers a `data/teams/` i canvia’n les dades.
- Si algun dia hi ha una font de calendari que es pugui llegir (un `.ics` públic), es pot posar al camp `ics` del fitxer de l’equip i el script el llegirà sol.

## A tenir en compte

- El repositori i la pàgina són públics: només hi ha noms de pila i horaris. No hi posis cognoms ni dades de contacte.

---

Autoria: Albert Saragossa Alòs
