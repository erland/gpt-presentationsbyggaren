# Acceptanstest – visual-first och export (GPT Byggaren 1.6.28)

## Syfte och bevisnivåer

Flera deterministiska tester verifierar nu `presentation-plan.md` och tillåtna tillståndsövergångar. Dessa tester **utför inte bildgenerering, PowerPoint-export eller PDF-rendering**. Funktionell acceptans i verklig värdmiljö återstår och får inte redovisas som PASS innan körning.

## Testdata

Använd `tests/presentation-plan-example.md` (tre slides) som kopierad projektplan. Låt originalfilen vara oförändrad. Kontrollera att varje mellanversion valideras av `python scripts/validate_presentation_plan.py presentation-plan.md`.

## Scenarier och förväntat utfall

| ID | Verkligt teststeg | Förväntad verifiering |
|---|---|---|
| VF-01 | Starta med planfilen i en ny konversation. | Brief/storyline återskapas inte i onödan; planen är auktoritativ och nedladdningsbar. |
| VF-02 | Instruera om visual-first och låt assistenten skapa första anchor-slide. | Användaren informeras **innan** första generationen om godkännandekommandon. Exakt en 16:9-slutslide per anrop, ingen kontaktkarta eller thumbnail-grid. |
| VF-03 | Inspektera plan direkt efter bild 1. | `Slide 01: generated`, `Next slide: none`, inga andra aktiva slides. |
| VF-04 | Skriv `Ändra slide 1: gör huvudillustrationen större.` | Samma slide revideras, inga andra slides genereras, status `redo` eller `generated` i väntan på godkännande. |
| VF-05 | Skriv `Det ser bra ut. Skapa slide 2 enligt planen.` | Slide 1 blir `approved`; exakt slide 2 genereras som en enda bild och blir `generated`, `Next slide: none`. |
| VF-06 | Försök få assistenten att skapa slide 3 innan 2 är godkänd. | Ingen hoppa-över-godkännande-övergång. Planen behåller en enda aktiv slide. |
| VF-07 | Godkänn slide 2 och slide 3 en i taget, kontrollera rendering och visual system. | Alla slides `approved`; högst en slide i `generated`/`redo` åt gången; faktisk preview bedömd. |
| EXP-01 | Exportera den godkända visuella presentationen. | Faktisk PPTX och PDF kan öppnas och granskas; PPTX-sidorna motsvarar planen, inga saknade mediarelationer. Bildbaserade slides beskrivs inte som objektredigerbara. |
| EXP-02 | Begär redigerbar PPTX. | Assistenten skiljer klart objektredigerbar export från helslidebilder och lovar inte hostförmåga utan faktisk verifiering. |
| EXP-03 | Begär Copilot-handoff. | Separat experimentellt spår från samma plan med prompt/underlag, inte en påstådd redigerbar PPTX. |

## Praktiskt protokoll

För varje ID: notera *runtime/modell, datum, indata, faktisk output, observerade artefakter, status PASS/PARTIAL/FAIL och en direkt verifierbar evidenslänk eller fil*. Ett uteblivet toolstöd är PARTIAL om kontraktet deklarerar en tillåten fallback, annars FAIL. Underkänd anti-collage-gate eller uteblivet explicit godkännande är FAIL.

PPTX-integritet: `python scripts/validate_pptx.py <genererad.pptx>`. Kontrollera samtidigt verklig rendering (öppna och granska samtliga slides) och jämför med PDF. Tekniskt giltig ZIP är inte i sig bevis på bra layout. Cross-model-beteende ska kvalificeras separat i en enklare och en starkare modell.

## Status

Deterministiska planövergångar kan köras i CI. Samtliga verkliga VF-/EXP-scenarier ovan har status **NOT RUN** tills de utförts i en riktig presentationsvärd.
