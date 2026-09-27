# Smoke tests – kvalitetsgranskning och transformation

## Scenario A – 25 slides till 10 slides

**Input:** En 25-slides presentation med fyra huvudbudskap, flera upprepningar, tekniska detaljslides och ett appendix-liknande avsnitt ska kortas till högst 10 huvudslides.

**Förväntat:**
- kärnbudskapet identifieras före transformation,
- slides klassificeras som keep, merge, remove eller move-to-appendix,
- upprepningar slås ihop i stället för att varje slide bara kortas,
- nödvändiga belägg för huvudbudskapen finns kvar,
- target_slide_count är högst 10,
- core_message_before och core_message_after har samma innebörd,
- final_gate får inte passera om ett bärande argument tappats.

## Scenario B – Technical till Executive

**Input:** En teknisk arkitekturpresentation ska användas i en ledningsgrupp.

**Förväntat:**
- content_style ändras från technical till executive,
- beslut, konsekvens, risk och rekommendation flyttas fram,
- implementation och arkitekturdetalj flyttas till appendix när de inte krävs för beslutet,
- teknisk information som påverkar risk eller beslut behålls,
- rubriker görs mer slutsatsdrivna,
- kärnbudskapet bevaras om användaren inte begärt annat.

## Scenario C – Texttung till mer visuell

**Input:** Flera slides innehåller långa punktlistor som beskriver process, jämförelser och en sekvens över tid.

**Förväntat:**
- process blir processdiagram,
- jämförelse blir comparison eller lämplig tabell/struktur,
- tidssekvens blir timeline eller roadmap efter semantiken,
- förklarande detalj flyttas till speaker notes,
- texten minskar utan att informationsinnehållet förvrängs,
- dekorativa bilder läggs inte till bara för att presentationen ska upplevas mer visuell.

## Scenario D – Blockerande problem kontra förbättring

**Input:** En presentation har både ett motsägelsefullt kärnbudskap och några inkonsekventa marginaler.

**Förväntat:**
- motsägelsefullt kärnbudskap klassas som blocker,
- marginalinkonsekvens klassas normalt som improvement,
- final_gate är fail så länge blockern är öppen,
- en öppen improvement behöver inte ensam hindra leverans.
