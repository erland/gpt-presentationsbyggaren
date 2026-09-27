# Custom GPT runtime – konceptuellt end-to-end-test

## Syfte
Verifiera att Custom GPT-distributionen behåller samma canonical presentationsmetodik som ChatGPT Chat.

## Scenario A – idé till presentation
**Indata:** "Skapa en 8-slides presentation för en ledningsgrupp om varför vi bör införa ett gemensamt API-managementlager."

**Förväntat:**
1. Brief skapas eller implicit fastställs.
2. Lämplig innehållsstil och visuell stil rekommenderas.
3. Storyline föregår storyboard.
4. Varje slide har ett huvudbudskap.
5. Slutsatsdrivna rubriker används där lämpligt.
6. Synligt innehåll separeras från speaker notes.
7. Presentation genereras först efter storyboard/design-gate.
8. Slutresultatet kvalitetsgranskas före leverans.

## Scenario B – "Gör nästa steg"
Efter en godkänd brief ska "Gör nästa steg" fortsätta till storyline, inte hoppa direkt till PPTX.

## Scenario C – runtimebegränsning
Om en rekommenderad capability inte är tillgänglig ska GPT:n använda deklarerad fallback och beskriva reducerad funktion utan att ändra canonical metodik.

## Paritetskrav
De centrala beteendereglerna ska ge samma konceptuella resultat i ChatGPT Chat och Custom GPT. Skillnader får endast bero på faktisk runtime-capability och ska dokumenteras i `COMPATIBILITY.md`.
