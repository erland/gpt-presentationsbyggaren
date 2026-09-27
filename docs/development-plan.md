# Utvecklingsplan – Presentationsbyggaren

**Profil:** `workflow_research_heavy`  
**Modellrobusthet:** `guided`  
**Aktiverade runtimes:** ChatGPT Chat, ChatGPT Custom  
**Huvudartefakt:** redigerbar PowerPoint (`.pptx`)

## Målbild

Presentationsbyggaren ska hjälpa användaren från idé eller källmaterial till en genomarbetad presentation genom ett styrt men lättviktigt flöde: **brief → storyline → storyboard → stil/design → presentation → kvalitetsgranskning**. Samma canonical projekt ska bygga både ChatGPT Chat- och ChatGPT Custom-distributioner.

Planen är persistent och vägledande. Vid varje körning ska faktisk projektstatus, blockerare och valideringsresultat styra vilket steg som utförs härnäst.

## Genomförandesteg

### Steg 1 – Bootstrap projekt och canonical kontrakt

**Mål:** Skapa projektets minsta kompletta canonical struktur och första återupptagningsbara projekt-ZIP.

**Varför nu:** Alla senare steg behöver en stabil projektmodell, status och gemensamma kontrakt.

**Leveranser**
- Projektstruktur
- gpt-project.yaml
- project-status.yaml
- README.md
- PROJECT.md
- STATUS.md
- docs/development-plan.md
- capability-, artifact-, workspace/state- och tool-kontrakt
- Första kompletta projekt-ZIP

**Förväntade filer**
- `gpt-project.yaml`
- `project-status.yaml`
- `README.md`
- `PROJECT.md`
- `STATUS.md`
- `docs/development-plan.md`
- `contracts/capabilities.yaml`
- `contracts/artifacts.yaml`
- `contracts/workspace-state.yaml`
- `contracts/tools.yaml`

**Validering**
- Validera projektmetadata och runtime-targets
- Verifiera att ChatGPT Chat och ChatGPT Custom finns i build targets
- Verifiera att projekt-ZIP kan byggas komplett

**Hygiene**
- Inga duplicerade canonical källor
- Inga genererade distributionsfiler i canonical mappar

**Klart när**
- Canonical grundstruktur finns
- Strukturerad status finns
- Utvecklingsplanen ingår i projektet
- Första projekt-ZIP är byggbar och komplett

### Steg 2 – Canonical instruktion och operativ kärna

**Mål:** Definiera Presentationsbyggarens kärnbeteende från behovsanalys till kvalitetsgranskad presentation.

**Leveranser**
- assistant/instructions.md
- Tydligt stegflöde
- Gates mellan brief, storyline, storyboard och generering

**Förväntade filer**
- `assistant/instructions.md`

**Validering**
- Kritiska regler finns i canonical instruktion och kräver inte Knowledge-hopp
- Instruktionen beskriver ett huvudbudskap per slide, slutsatsdrivna rubriker och separering av slideinnehåll från talarstöd

**Tester**
- Instruction-adherence smoke test

**Klart när**
- Operativ kärna är kort, entydig och runtime-neutral
- Modellen ska inte hoppa direkt från råmaterial till slides när storyline/storyboard behövs

**Beroenden:** steg 1

### Steg 3 – Presentation Brief, storyline och arbetsflöde

**Mål:** Införa strukturerade mellanartefakter för att göra presentationsarbetet reproducerbart och redigerbart.

**Leveranser**
- Presentation Brief-kontrakt
- Storyline-kontrakt
- Regler för Auto-rekommendation av stil
- Regler för när frågor ska ställas respektive härledas

**Förväntade filer**
- `schemas/presentation-brief.schema.json`
- `schemas/storyline.schema.json`
- `knowledge/presentation-method.md`

**Validering**
- Schemas validerar exempelartefakter
- Arbetsflödet fungerar både från kort idé och större källmaterial

**Tester**
- Idé till brief
- Dokument till brief
- Brief till storyline

**Klart när**
- Brief och storyline är maskinellt validerbara
- Auto-läget kan rekommendera presentationsstil utan onödiga frågor

**Beroenden:** steg 2

### Steg 4 – Innehållsstilar och visuella stilar

**Mål:** Skapa ett kombinerbart stilssystem där innehållsstil och visuell stil väljs oberoende.

**Leveranser**
- Innehållsstilar: auto, executive, strategy, consulting, technical, teaching, workshop, visual-storytelling
- Visuella stilar: minimal-light, minimal-dark, corporate, editorial, bold-visual, diagram-heavy
- Deklarativa stilregler

**Förväntade filer**
- `knowledge/content-styles.md`
- `knowledge/visual-styles.md`

**Validering**
- Varje stil beskriver syfte, principer, önskad täthet, föredragna mönster och sådant som ska undvikas
- Kombinationer ska inte kräva separata mallar för varje par

**Tester**
- Samma brief med Executive + Minimal Light respektive Technical + Diagram Heavy ger tydligt olika storyboard

**Klart när**
- Alla v1-stilar är definierade och konsekventa
- Auto kan välja eller föreslå en kombination

**Beroenden:** steg 3

### Steg 5 – Bibliotek med slide- och berättelsemönster

**Mål:** Ge GPT:n ett begränsat men uttrycksfullt visuellt språk för att välja rätt typ av slide efter budskap.

**Leveranser**
- Slide patterns
- Storytelling patterns
- Regler för när mönster ska och inte ska användas

**Förväntade filer**
- `knowledge/slide-patterns.md`
- `knowledge/storytelling-patterns.md`

**Validering**
- Mönster beskriver kommunikationssyfte, inte bara layout
- Dubbletter och överlapp reduceras

**Tester**
- Problem→konsekvens→lösning
- Nuläge→målbild→gap→åtgärd
- Teknisk arkitektur med beroenden

**Klart när**
- GPT:n kan välja relevanta slide patterns utifrån budskap
- Biblioteket är litet nog att vara begripligt och konsekvent

**Beroenden:** steg 4

### Steg 6 – Storyboard och slide design-specifikation

**Mål:** Definiera den interna presentationsmodell som översätter storyline till konkreta, renderbara slides.

**Leveranser**
- Storyboard-schema
- Slide-specifikation
- Regler för layout, visual_intent, innehåll och speaker notes

**Förväntade filer**
- `schemas/storyboard.schema.json`
- `knowledge/slide-design-guide.md`

**Validering**
- Storyboard kan valideras deterministiskt
- Varje slide har title, message, purpose och visual_intent

**Tester**
- En storyline genererar komplett storyboard
- För mycket text flyttas till speaker notes eller appendix

**Klart när**
- Storyboard är tillräcklig som indata till presentationgenerering
- Ett huvudbudskap per slide kan kontrolleras

**Beroenden:** steg 5

### Steg 7 – Källor, verktyg och presentationsgenerering

**Mål:** Definiera hur GPT:n använder filer, webb, dataanalys, bildgenerering och presentationsverktyg utan att låsa canonical beteende till en runtime.

**Leveranser**
- Tool-policy
- Källhanteringsregler
- Regler för diagram och bildgenerering
- Genereringskontrakt för PPTX

**Förväntade filer**
- `knowledge/source-and-tool-guide.md`
- `knowledge/visual-generation-guide.md`

**Validering**
- Verktyg används endast när de förbättrar presentationen
- Dekorativa AI-bilder prioriteras inte framför informationsbärande visualisering
- Aktuella faktapåståenden kan kräva webbkällor

**Tester**
- Presentation från bifogat dokument
- Datadriven slide från tabell
- Illustrationsslide när diagram inte räcker

**Klart när**
- Tool-beteendet är runtime-neutralt definierat
- PPTX är huvudartefakt och storyboard kan bevaras som stödartefakt

**Beroenden:** steg 6

### Steg 8 – Kvalitetsgranskning och transformationsflöden

**Mål:** Göra GPT:n lika bra på att förbättra presentationer som på att skapa nya.

**Leveranser**
- Quality guide
- Review-checklista
- Transformationsflöden för kortare, mer visuell, annan målgrupp och annan stil

**Förväntade filer**
- `knowledge/quality-guide.md`
- `schemas/presentation-review.schema.json`

**Validering**
- Review skiljer blockerande problem från förbättringar
- Transformation bevarar kärnbudskap där inte användaren begär annat

**Tester**
- 25 slides till 10 slides
- Technical till Executive
- Texttung presentation till mer visuell version

**Klart när**
- GPT:n kan granska och refaktorera en presentation systematiskt
- Kvalitetsgates används före slutleverans

**Beroenden:** steg 7

### Steg 9 – ChatGPT Chat-distribution

**Mål:** Bygga en komplett ZIP-runtime för ChatGPT Chat från canonical projektet.

**Leveranser**
- Chat ZIP
- START-HERE för Chat
- Runtime-specifik dokumentation

**Validering**
- Distributionen byggs från canonical källor
- Obligatoriska beroenden håller sig få
- ZIP:en kan återupptas som projekt

**Tester**
- End-to-end: idé → storyline → storyboard → presentationsartefakt i ChatGPT Chat

**Klart när**
- Chat-distributionen validerar utan blockerande fel
- Kärnflödet kan följas med 'Gör nästa steg'

**Beroenden:** steg 8

### Steg 10 – ChatGPT Custom-distribution

**Mål:** Kompilera canonical projektet till en Custom GPT med rätt instruktion, Knowledge och konfigurationsgränser.

**Leveranser**
- Custom GPT instructions
- Knowledge bundle
- README för installation/configuration

**Validering**
- Instruktion och Knowledge ryms inom runtimebegränsningar
- Kritiska beteenderegler ligger inte enbart i Knowledge
- Funktionsskillnader mot Chat dokumenteras

**Tester**
- Samma centrala eval-fall körs konceptuellt mot Custom GPT-distributionen

**Klart när**
- Custom GPT-distributionen kan byggas automatiskt
- Den behåller samma canonical presentationsmetodik

**Beroenden:** steg 8

### Steg 11 – Modellrobusthet och evals

**Mål:** Verifiera att samma canonical workflow fungerar på både enklare och starkare modeller utan separata instruktioner.

**Leveranser**
- Eval-manifest
- Model-compatibility cases
- Instruction-adherence cases
- Regression cases

**Förväntade filer**
- `tests/evals/`
- `tests/test-manifest.yaml`

**Validering**
- Guided gates följs
- Modellen hoppar inte över brief/storyline/storyboard i komplexa uppgifter
- Enkla uppgifter överorkestreras inte

**Tester**
- Kort enkel presentation
- Stor rapport
- Stilbyte
- Förbättring av befintlig presentation
- Otydligt underlag där modellen ska härleda rimliga val

**Klart när**
- Blockerande evals passerar
- Samma instruktion används över modellnivåer

**Beroenden:** steg 9, steg 10

### Steg 12 – CI, build, hygiene och runtime parity

**Mål:** Automatisera kontroll av projektets kvalitet och säkerställa att aktiverade runtimes hålls synkroniserade.

**Leveranser**
- Build scripts
- Lint/validation
- GitHub Actions CI
- GitHub Release build
- Runtime parity report
- Project hygiene report

**Förväntade filer**
- `scripts/`
- `.github/workflows/ci.yml`
- `.github/workflows/release.yml`

**Validering**
- Lint passerar
- Schemas passerar
- Evals passerar
- Båda distributioner byggs
- Runtime parity saknar blockerande avvikelser

**Hygiene**
- Inga överflödiga filer
- Ingen drift mellan canonical och distribution
- Releaseartefakter byggs från taggversion

**Klart när**
- CI kan validera projektet från ren checkout
- Release-workflow kan bygga projekt-ZIP och båda distributionerna

**Beroenden:** steg 11

### Steg 13 – Release readiness och första releasekandidat

**Mål:** Sammanställa en releaseklar v1-kandidat med dokumenterade begränsningar och installationsvägar.

**Leveranser**
- Release readiness report
- Compatibility/runtime parity documentation
- Projekt-ZIP
- Chat ZIP
- Custom GPT bundle
- Release notes

**Validering**
- Project status grön
- Lint/test/build/distributionsvalidering passerar
- Final hygiene passerar
- Blockerande runtime-avvikelser saknas

**Klart när**
- Första releasekandidaten är reproducerbart byggd
- Alla användarleveranser finns
- Nästa rekommenderade steg kan vara stabil release eller konkret korrigering

**Beroenden:** steg 12

## Planerade kvalitetsgates

- Canonical beteende ska vara runtime-neutralt och vara enda sanningskälla för kärnmetodiken.
- Brief, storyline och storyboard ska användas som mellanartefakter när uppgiften är tillräckligt komplex.
- Kritiska beteenderegler får inte ligga enbart i Knowledge.
- Ett huvudbudskap per slide och slutsatsdrivna rubriker ska kontrolleras före leverans.
- Aktiverade runtimes ska valideras mot samma kärnfall och ingå i runtime parity.
- Projektstatus uppdateras först efter att relevant validering passerat.
- Komplett projekt-ZIP byggs om efter varje genomfört utvecklingssteg från och med steg 1.
- Release kräver lint, tester, build, distributionsvalidering, final hygiene och runtime-paritet utan blockerande fel.

## Första genomförandesteg

Nästa gång användaren säger **”Gör nästa steg”** ska faktisk projektstatus först kontrolleras. Eftersom projektet ännu inte är bootstrappat blir den förväntade rekommendationen **Steg 1 – Bootstrap projekt och canonical kontrakt**. I det steget skapas den första kompletta projekt-ZIP:en och denna plan läggs in som `docs/development-plan.md`.
