# Smoke test – slide- och berättelsemönster

## Syfte
Verifiera att Presentationsbyggaren väljer patterns efter kommunikationssyfte, skiljer närliggande patterns åt och inte reducerar patterns till layoutmallar.

## Fall A – Problem → konsekvens → lösning

**Brief:** En ledningsgrupp behöver förstå varför manuellt och personberoende AI-arbete bör ersättas av återanvändbara assistenter och besluta om en pilot.

**Förväntat storytelling pattern:** `problem-consequence-solution`.

**Rimlig sekvens av slide patterns:**
`problem` → `numbers-kpi` eller `key-message` → `before-after` → `recommendation` → `decision`.

**PASS om:** problemet och konsekvensen etableras före lösningen, rekommendationen inte presenteras som ett neutralt jämförelseobjekt och sista sliden uttrycker ett faktiskt beslut eller nästa steg.

## Fall B – Nuläge → målbild → gap → åtgärd

**Brief:** En IT-ledning ska förstå vägen från dagens fragmenterade applikationsarkitektur till en definierad målarkitektur.

**Förväntat storytelling pattern:** `current-target-gap-actions`.

**Rimlig sekvens av slide patterns:**
`architecture` eller `problem` → `before-after`/`architecture` → `comparison` eller `three-pillars` → `roadmap`.

**PASS om:** nuläge och målbild hålls isär, gapet beskrivs explicit och roadmapen visar prioriterad framtida progression snarare än bara kronologi.

## Fall C – Teknisk arkitektur med beroenden

**Brief:** Seniora arkitekter behöver förstå hur en orkestrerande AI-assistent samverkar med specialiserade assistenter och externa verktyg.

**Förväntat huvud-pattern:** `architecture`.

**Sekundärt pattern vid behov:** `process` för ett separat exekveringsflöde.

**PASS om:** arkitekturvyn fokuserar på komponenter, gränser och beroenden; exekveringsordning bryts ut till `process` om den annars skulle göra arkitektursliden överlastad; samma slide försöker inte visa alla detaljnivåer samtidigt.

## Konfliktkontroller

PASS endast om följande skillnader respekteras:
- `before-after` = samma objekt över förändring; `comparison` = olika alternativ samtidigt.
- `timeline` = kronologi; `roadmap` = avsiktlig framtida progression.
- `process` = ordning/överföring; `architecture` = struktur/relationer.
- `recommendation` = föreslagen riktning; `decision` = explicit val som mottagaren ska fatta.

## Helhetskriterier

PASS om:
1. patterns väljs från budskap och kommunikativ funktion,
2. storytelling pattern och slide pattern hålls isär,
3. biblioteket använder en begränsad uppsättning tydligt avgränsade patterns,
4. visuell stil kan ändras utan att patternets kommunikationsjobb förändras.
