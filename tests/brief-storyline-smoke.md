# Smoke tests – Presentation Brief och storyline

## Test 1: Idé till brief

**Input:**
"Jag ska presentera för ledningsgruppen varför vi behöver gå från manuellt AI-arbete till AI-assistenter. Jag har 15 minuter."

**Förväntat:**
- Brief kan skapas utan följdfråga.
- audience.primary = ledningsgruppen.
- length.target_minutes = 15.
- content style rekommenderas/infereras som executive eller strategy med motivering.
- `assumptions` används för okända men icke-blockerande detaljer.

## Test 2: Dokument till brief

**Input:**
En rapport med nuläge, målbild, identifierade gap och rekommenderade initiativ. Användaren vill presentera rapporten för en styrgrupp.

**Förväntat:**
- Brief utgår från användarens presentationsmål, inte dokumentets kapitelstruktur.
- `source_material.available=true`.
- eventuella luckor anges i `source_material.gaps`.
- strategy rekommenderas eller infereras som innehållsstil om inget annat krav väger tyngre.

## Test 3: Brief till storyline

**Input:**
Validerad brief för en transformationspresentation med önskad effekt: förstå nulägets problem, acceptera målbilden och besluta om nästa steg.

**Förväntat:**
- `core_message` uttrycker presentationens huvudtes/slutsats.
- `pattern.name` är exempelvis nuläge→målbild→gap→åtgärder eller motsvarande.
- minst två narrative points finns.
- varje punkt har roll och `supports_core_message=true` om den hör till huvudflödet.
- detaljer som inte behövs för huvudflödet flyttas till `appendix_candidates`.

## Test 4: Fråga endast när väsentligt

**Input:**
"Gör en presentation om vårt nya API för antingen utvecklare eller ledningsgruppen. Jag vet inte ännu vem som ska se den."

**Förväntat:**
- GPT:n ställer en fråga om målgrupp, eftersom valet leder till tydligt olika presentationer.
- GPT:n frågar inte om reversibla detaljval som typsnitt eller exakt antal ikoner.
