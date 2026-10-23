# Slutligt funktionellt acceptanstest – installerad Presentationsbyggaren

**Viktigt:** Kör testet med den **faktiskt installerade** Presentationsbyggaren i en ny tråd. Projektets källkod, exempelplaner, genererade ZIP-paket och hypotetiska assistantsvar ersätter inte en riktig installation. Använd inte en tidigare Custom GPT-variant.

## Kopiera som uppdrag till installerad plugin

> Genomför ett oberoende end-to-end-test av den faktiskt installerade Presentationsbyggaren, baserat på GPT Byggaren Engine 1.6.28. Testa och dokumentera VF-01–VF-07 och EXP-01–EXP-03 enligt `docs/visual-first-acceptance.md`. Använd testplanen `tests/presentation-plan-example.md` från projektet som indata. Läs installerade Skills och kontrollera deras faktiska tillgång till resurser och exekveringsförmågor. Om filen inte kan läsas i installationen ska du begära själva planfilen, inte simulera åtkomst. Skapa en slidebild åt gången, visa arbetsinstruktionen före första bilden, uppdatera och bevara `presentation-plan.md` vid varje steg och invänta explicit godkännande. Efter godkänd sista slide, skapa verklig PPTX och PDF när verktygsstöd finns och verifiera filerna med `scripts/validate_pptx.py` samt `scripts/validate_export_pair.py --slides 3` eller likvärdigt. Redovisa för varje ID status PASS/PARTIAL/FAIL/NOT_RUN, verklig indata, observerad output, artefakter och evidens. Sätt aldrig PASS utan faktisk observation. Skilj tekniskt öppningsbara filer från god visuell rendering och objektredigerbarhet. Genomför ingen full omgenerering eller godkännande automatiskt på användarens vägnar. Redovisa separata värdmiljöbegränsningar och krav på cross-model-kvalificering.

## Särskilt om godkännande

Mellan enskilda bildgenereringar krävs användarens verkliga beslut. Automatisera inte godkännanden i ett verktygstest, och använd inte `Gör nästa steg` som godkännandesignal. Vid blockerad interaktion kan bara redan genomförda steg bedömas och resten ska vara NOT_RUN.

## Evidenskrav

Varje PASS måste kunna härledas till en faktisk körning: verktygsanrop/installerad Skills-version, skapad bild eller tillståndsfil, genererad PPTX/PDF, en teknisk validatorutskrift eller en faktisk visuell bedömning. Paritet eller byggresultat från GitHub Actions får inte användas som substitut för funktionellt resultat.

Registrera resultat i `reports/installed-plugin-acceptance.json` enligt `schemas/installed-plugin-acceptance.schema.json` (mall i `tests/fixtures/installed-plugin-acceptance.template.json`). `NOT_RUN` får användas utan evidens och får aldrig presenteras som PASS.
