# Smoke tests – källor, verktyg och presentationsgenerering

## Scenario A – Presentation från bifogat dokument

**Input:** En aktuell rapport bifogas och användaren ber om en 10-slides ledningspresentation.

**Förväntat:**
- dokumentet är primär källa,
- modellen skapar inte en slide per rapportkapitel,
- bärande påståenden kan spåras till rapporten,
- extern webb används endast om uppgiften kräver aktuell komplettering,
- slutartefakten är redigerbar PPTX när runtime stöder det.

## Scenario B – Datadriven slide från tabell

**Input:** En tabell med kvartalsvärden visar tydlig förändring över tid.

**Förväntat:**
- datatyper och tidsperiod kontrolleras,
- visualiseringen väljs efter budskapet,
- ett linje- eller stapeldiagram används när det gör förändringen tydligare än tabellen,
- diagrammet är redigerbart,
- rubriken uttrycker slutsatsen och diagrammet evidensen.

## Scenario C – Illustration när diagram inte räcker

**Input:** En slide ska förklara en människa som först bygger själv, sedan instruerar assistenter och därefter instruerar en assistent som bygger andra assistenter.

**Förväntat:**
- modellen identifierar att detta är konceptuell progression, inte numerisk data,
- en enkel informationsbärande illustration kan väljas,
- illustrationens prompt härleds från budskap och visuell stil,
- eventuell text läggs som redigerbara slide-element, inte inne i den genererade bilden,
- dekorativa bilder läggs inte till utöver det som behövs.

## Scenario D – Runtime saknar bildgenerering

**Förväntat:**
- uppdraget blockeras inte,
- illustration ersätts med former/diagram eller tydlig bildplatshållare,
- storyboard och övrig presentation kan fortfarande levereras.
