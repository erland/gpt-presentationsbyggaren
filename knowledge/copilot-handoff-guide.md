# Copilot handoff guide

## Syfte

Copilot-handoff är en projektion av `presentation-plan.md` för att låta ett presentationsverktyg skapa en **redigerbar** presentation. Handoff-dokumentet är inte kanonisk källa; presentation-planen är det.

## Leveranser

När runtime kan skapa dokument:

- `copilot-handoff.docx` – primärt handoff-format,
- `copilot-handoff.pdf` – stabil referens av samma underlag,
- valfritt `copilot-prompt.md` – kort startinstruktion att klistra in tillsammans med dokumentet.

## Struktur

Dokumentet ska börja med:

### Presentation objective
- titel,
- syfte,
- målgrupp,
- önskad effekt,
- ungefärligt antal slides.

### Overall design direction
- visuell stil och tonalitet,
- färgkaraktär,
- typografisk känsla,
- ambitionsnivå,
- vad som ska undvikas.

Skriv uttryckligen när wireframe-lik estetik ska undvikas, exempelvis:

> Skapa en färdig professionell designerpresentation. Undvik små boxar, standardikoner och tunna pilar som huvudsakligt visuellt språk. Variera kompositionen efter budskapet.

## Slide-by-slide

För varje slide:

- slide-nummer,
- rubrik,
- huvudbudskap,
- exakt synlig text,
- visual direction,
- önskad komposition,
- eventuell illustration/metafor,
- speaker notes,
- källor när de behövs.

Beskriv **vad mottagaren ska se och förstå**, inte hur PowerPoint-objekt ska implementeras.

## Word som primärt handoff-format

När DOCX kan skapas:

- använd riktiga Heading 1/2/3-stilar,
- en slide per tydlig sektion,
- håll exakt slide-copy separat från visual direction,
- undvik tabeller som blandar flera slides,
- placera speaker notes under egen underrubrik,
- behåll källreferenser nära respektive slide.

Det gör dokumentet både mänskligt läsbart och lätt att använda som strukturerat presentationsunderlag.

## Copilot prompt

Den korta prompten ska hänvisa till handoff-dokumentet och sammanfatta:

- målgrupp,
- önskad designnivå,
- antal slides,
- att slideordning och huvudbudskap ska följas,
- att layout får förbättras men innehållets innebörd ska bevaras,
- att resultatet ska vara redigerbart.

Prompten ska inte duplicera hela dokumentet.

## Relation till visual-first

Visual-first och Copilot-handoff ska kunna genereras från samma `presentation-plan.md`.

De får ha olika rendering men ska bevara:

- samma kärnbudskap,
- samma slideordning om inte transformationsmålet säger annat,
- samma exakta fakta,
- samma speaker notes i sak,
- samma övergripande design direction.
