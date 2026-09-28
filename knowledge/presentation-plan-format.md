# Presentation Plan – kanoniskt återupptagningsformat

## Syfte

`presentation-plan.md` är den sparbara, runtime-neutrala masterartefakten för en presentation. Den ska vara tillräckligt komplett för att Presentationsbyggaren senare ska kunna skapa presentationen utan att göra om brief, storyline eller storyboard.

När planen färdigställs ska den normalt **skrivas till en faktisk Markdown-fil och erbjudas som nedladdningsbar artefakt**. Hela planens innehåll ska inte dumpas i chatten om användaren inte uttryckligen ber om det. Chatten bör bara sammanfatta planen kort och länka till/visa filen.

Planen är sanningskälla för:

- syfte och målgrupp,
- kärnbudskap och narrativ båge,
- innehålls- och visuell stil,
- visuellt system och art direction,
- slideordning,
- exakt synlig text,
- huvudbudskap per slide,
- speaker notes,
- visual intent och renderingsstrategi,
- källreferenser,
- Copilot-handoff och visual-first rendering.

## Format

Använd Markdown med YAML-frontmatter.

Obligatoriskt frontmatter:

```yaml
---
schema_version: 1
title: Presentationens titel
language: sv
target_slides: 10
primary_output: visual-first
status: planned
---
```

Tillåtna `primary_output`:

- `visual-first`
- `copilot-handoff`
- `both`

## Obligatoriska huvudsektioner

1. `# Presentation Plan`
2. `## Brief`
3. `## Storyline`
4. `## Design direction`
5. `## Visual system`
6. `## Rendering status`
7. `## Slides`
8. `## Sources and assumptions`

## Brief

Dokumentera minst:

- syfte,
- primär målgrupp,
- önskad effekt,
- presentationssituation,
- ungefärlig tid/längd,
- viktiga begränsningar.

## Storyline

Dokumentera:

- kärnbudskap,
- berättelsemönster,
- narrativ båge i ordning,
- eventuella appendixkandidater.

## Design direction

Dokumentera:

- innehållsstil,
- visuell stil,
- tonalitet,
- ambitionsnivå,
- vad presentationen ska kännas som,
- vad som uttryckligen ska undvikas.

## Visual system

Detta är gemensam art direction för alla bildgenereringar:

- färgkaraktär,
- kontrast,
- illustrationstyp,
- perspektiv,
- material/känsla,
- typ av människor/objekt om relevant,
- bakgrundsprincip,
- kompositionsprincip,
- förbjudna element,
- textregel: genererade bilder ska normalt inte innehålla presentationscopy.

Visual system ska fastställas **före** massgenerering av slide-assets.

## Rendering status

Planen ska bära produktionsstatus så att arbetet kan återupptas efter varje separat bildgenerering.

Exempel:

```markdown
## Rendering status

- Phase: anchors
- Next slide: 01
- Slide 01: next
- Slide 02: pending
- Slide 03: pending
```

Tillåtna slide-statusar:

- `pending` – ännu inte genererad,
- `next` – exakt den slide som ska genereras vid nästa `Gör nästa steg`,
- `generated` – bild finns men är ännu inte uttryckligen godkänd,
- `approved` – godkänd för paketering,
- `redo` – behöver göras om innan den kan godkännas,
- `not-applicable` – ingen bildgenerering behövs.

Regler:

- högst en slide får vara `next`,
- om någon bildslide återstår ska normalt exakt en vara `next`,
- `next` behöver inte automatiskt flyttas till numeriskt följande slide; användarens explicita kommando `Skapa slide X enligt planen` avgör vilken slide som blir nästa,
- om användaren underkänner bilden sätts samma slide till `redo` och görs om innan flödet går vidare,
- när alla relevanta slides är `approved` eller `not-applicable` går nästa steg till paketering.

## Slide-format

Varje slide dokumenteras så här:

```markdown
### Slide 07 — Människans roll förändras från utförare till designer av arbete

**Purpose:** explain
**Message:** Förflyttningen sker i tre nivåer.
**Pattern:** three-pillars
**Render mode:** hybrid-slide
**Visual priority:** hero

**Visible text**
- Label 1: Bygg själv
- Label 2: Bygg assistenter
- Label 3: Bygg med en assistent

**Text layout**
- Label 1: x=7%, y=12%, width=24%, height=10%, style=label-large
- Label 2: x=38%, y=12%, width=24%, height=10%, style=label-large
- Label 3: x=69%, y=12%, width=24%, height=10%, style=label-large

**Visual concept**
Tre tydliga scener med stigande abstraktionsnivå ...

**Image asset**
- Needed: yes
- Generation group: anchor-2
- Prompt intent: ...
- Must show: ...
- Text in image: no
- Text-safe area: three calm label zones across the upper part of the slide
- Must avoid: readable text, pseudo-text, ...

**Composition**
Rubrik överst, tre stora scener över hela canvasen ...

**Speaker notes**
...

**Sources**
- ...
```

## Render mode

Planen använder i första hand:

- `image-slide` – färdig visuell slide där raster/SVG/PDF-komposition är huvudytan och text kan vara rasteriserad,
- `hybrid-slide` – bildbaserad grafik plus separat native PowerPoint-text; normalval när texten ska vara redigerbar men grafik, boxar, linjer, pilar och diagram inte behöver vara det,
- `native-slide` – endast när native diagram/tabell/teknisk struktur faktiskt är bättre,
- `copilot-only` – renderas inte lokalt; används bara i Copilot-handoff.

När redigerbar text efterfrågas är `hybrid-slide` normalfallet för visuellt drivna presentationer. När redigerbarhet inte är krav kan `image-slide` användas.

## Text layout för hybrid-slide

Varje `hybrid-slide` som har synlig text ska innehålla sektionen `**Text layout**`.

Text layout ska minst ange en placeringsregel för den redigerbara copy som finns under `**Visible text**`. Positioner kan uttryckas som procent av slideytan eller som semantiska zoner när runtime kan lösa dem deterministiskt. Föredra gemensamma stilreferenser, exempelvis `title-large`, framför duplicerade fontvärden på varje slide.

`**Image asset**` på hybrid-slides ska dessutom ange:

- `Text in image: no`,
- en `Text-safe area` som motsvarar textlayouten,
- `Must avoid` som förbjuder läsbar text eller pseudo-text i bakgrundsasseten.

Text layout beskriver endast textlagret. Boxar, linjer, pilar, diagram och annan grafik får ingå i bakgrundsbilden.

## Återupptagning

När användaren lämnar in en befintlig `presentation-plan.md`:

1. behandla den som senast fastställda planeringsartefakt,
2. gör inte om brief/storyline utan anledning,
3. kontrollera endast om planen är komplett för önskad output,
4. fortsätt direkt med rendering, Copilot-handoff eller begärd transformation,
5. uppdatera planen om användaren gör innehålls- eller designändringar.

## Gate

Planen är redo för rendering när:

- kärnbudskap och narrativ båge är tydliga,
- varje slide har ett huvudbudskap,
- synlig text är separat från speaker notes,
- varje slide har render mode och visual concept,
- varje hybrid-slide med synlig text har `Text layout` och en textfri `Image asset` med `Text-safe area`,
- visual system är definierat,
- renderingsstatus finns och pekar ut högst en nästa slide,
- varje bildgeneration avser exakt en slide,
- inga centrala fakta behöver hittas på under renderingen.
