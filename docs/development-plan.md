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


---

## Förbättringscykel 0.2 – Rendering och visuell kvalitet

Bakgrund: praktisk RC1-testning visade två blockerande problem: en genererad PPTX hade ogiltiga Open XML-referenser och presentationens visuella resultat blev wireframe-likt och repetitivt trots fungerande storyline.

### Steg 14 – Kommunikationskvalitet före native-redigerbarhet

**Mål:** Korrigera designpolicyn så att native PowerPoint-former inte automatiskt prioriteras framför bättre visuella lösningar.

**Leveranser**
- Uppdaterad canonical instruktion
- Reviderad guide för visuell generering
- Blockerande kvalitetskriterium för genomgående wireframe-lik design

**Klart när**
- Kommunikationskvalitet är uttrycklig förstaprincip
- Native, designed-composition, generated-visual och hybrid är jämbördiga renderingsstrategier

### Steg 15 – PPTX-integritet och kontrollerad rendering

**Mål:** Förhindra att en syntaktiskt skrivbar men strukturellt trasig PPTX levereras.

**Leveranser**
- Rendering/quality guide
- Deterministisk Open XML-validator
- Tool-kontrakt för PPTX-validering
- Regressionstest för saknade Content-Type-delar och relationship-targets

**Klart när**
- Fel motsvarande RC1-testets saknade slide masters upptäcks deterministiskt
- Teknisk validering är en blockerande leveransgate

### Steg 16 – Preview och visuell kvalitetsgate

**Mål:** Bedöma den renderade sliden, inte bara storyboard eller objektmodell.

**Leveranser**
- Preview-gate
- Kontroller för overflow, små objekt, repetitiv komposition och oavsiktligt tomrum
- Presentation-generation-kontrakt med teknisk och visuell valideringsstatus

**Klart när**
- En presentation kan inte kallas färdig utan visuell kontroll när preview-rendering finns

### Steg 17 – PDF och HTML som kompletterande format

**Mål:** Ge robustare leverans och högre visuell frihet utan att överge PowerPoint.

**Leveranser**
- PDF som rekommenderad visuell följeslagare
- HTML som valfritt alternativ för webbpresentation/hög visuell frihet
- Artifact- och generation-kontrakt uppdaterade

**Klart när**
- PPTX är fortsatt huvudformat när PowerPoint/redigering krävs
- PDF och HTML kan väljas utan att ändra canonical presentationsmetod

### Steg 18 – Regression, parity och 0.2 readiness

**Mål:** Säkerställa att förändringen inte bryter runtime-paritet eller Custom GPT-gränser.

**Leveranser**
- Deterministiska PPTX-validator-tester
- Uppdaterad projektstatus och release notes
- CI-validering av projekt, tester och distributioner

**Klart när**
- CI passerar
- Canonical instruktion ryms inom 8 000 tecken
- Chat och Custom bygger från samma canonical källa
- Praktisk presentationstestning är nästa rekommenderade aktivitet


---

## Förbättringscykel 0.3 – Presentation Plan, visual-first och Copilot-handoff

Bakgrund: 0.2 löste PPTX-integritet men praktisk testning visade att native/hybrid rendering fortfarande blev för wireframe-lik. Användaren prioriterar nu visuell kvalitet framför objektredigerbarhet och vill samtidigt ha ett separat underlag för att skapa en redigerbar presentation i Microsoft Copilot.

### Steg 19 – Presentation Plan som kanonisk artefakt

**Mål:** Skapa ett sparbart Markdown-format som kan återanvändas som direkt indata vid en senare körning.

**Leveranser**
- `knowledge/presentation-plan-format.md`
- `templates/presentation-plan.md.tpl`
- `tests/presentation-plan-example.md`
- deterministisk plan-validator

**Klart när**
- planen bär brief, storyline, design direction, visual system och slide-för-slide-specifikation,
- en sparad plan kan återupptas utan att brief/storyline görs om.

### Steg 20 – Copilot-handoff

**Mål:** Projicera samma plan till ett strukturerat underlag för redigerbar presentation i Copilot eller motsvarande presentationsverktyg.

**Leveranser**
- `knowledge/copilot-handoff-guide.md`
- DOCX/PDF-kontrakt
- `copilot-prompt.md`-mall

**Klart när**
- handoff kan skapas utan att duplicera planeringslogik,
- slideordning, budskap, exakt text och design direction bevaras.

### Steg 21 – Visual-first som huvudspår utan redigerbarhetskrav

**Mål:** Optimera slutpresentationen för visuell kvalitet och tillåta helslide-rendering.

**Leveranser**
- `knowledge/visual-first-workflow.md`
- uppdaterad canonical instruktion
- uppdaterad rendering-quality guide
- generation-kontrakt med `visual-first`

**Klart när**
- visual-first kan leverera bildbaserad PPTX + PDF,
- objektredigerbarhet är inte ett implicit krav.

### Steg 22 – Anchor-slide och bildgenereringsstrategi

**Mål:** Säkerställa hög kvalitet och visuell konsistens utan att försöka generera hela presentationen i en prompt.

**Regler**
- 1–2 anchor slides först,
- viktiga/komplexa slides normalt en i taget,
- små batcher om 2–4 endast för enklare närbesläktade assets,
- aldrig hela decket i en enda bildgeneration som standard,
- exakt presentationscopy genereras normalt separat från bildasset.

**Klart när**
- reglerna finns både i Knowledge och generation-kontraktet,
- anchor-style-gate måste passera före massgenerering.

### Steg 23 – Paketering till PPTX/PDF och plan

**Mål:** Göra visual-first levererbar i vanliga presentationsformat.

**Leveranser**
- `presentation-plan.md`
- bildbaserad `presentation.pptx`
- `presentation.pdf`
- teknisk PPTX-validering och visuell preview-gate

**Klart när**
- PPTX kan fungera som presentationsskal för helslidebilder,
- PDF motsvarar samma visuella rendering.

### Steg 24 – Regression, parity och 0.3 readiness

**Mål:** Säkerställa att nya artefakter och regler fungerar i Chat och Custom utan regression.

**Validering**
- presentation-plan-validator passerar,
- generation-schema och exempel passerar,
- canonical instruktion < 8 000 tecken,
- lint, pytest, hygiene och distributionsvalidering passerar,
- Chat och Custom bygger från samma canonical källa.

**Klart när**
- CI är grön,
- nästa rekommenderade aktivitet är praktiskt A/B-test: visual-first-resultat kontra Copilot-handoff-resultat.


---

## Förbättringscykel 0.3.1 – En slide per generation och återupptagningsbar rendering

Bakgrund: praktisk visual-first-testning visade att bildmodellen kunde tolka flera slide-assets i samma generation som ett collage med många små bilder. Dessutom avslutar bildgenereringen ofta turen, vilket gjorde `Gör nästa steg` otydligt efter varje bild.

### Steg 25 – Hård en-slide-per-generation-regel

**Mål:** Förhindra collage, thumbnails och flera slides i samma bild.

**Regler**
- exakt en slutlig 16:9-slidebild per bildgenerering,
- ingen batchgenerering av flera slides,
- inga collage, kontaktkartor, moodboards, storyboardark eller designvarianter på samma canvas,
- flera delar inom en slide ska vara få, stora och integrerade i samma komposition.

**Klart när**
- generation-kontraktet har `max_batch_size = 1`,
- anti-collage är blockerande kvalitetsgate.

### Steg 26 – Persistent renderingsstatus och Gör nästa steg

**Mål:** Göra visual-first-flödet återupptagningsbart trots att bildverktyget avslutar turen efter bildgenerering.

**Leveranser**
- obligatorisk `## Rendering status` i `presentation-plan.md`,
- status per slide: pending, next, generated, approved, redo eller not-applicable,
- deterministisk validator som tillåter högst en `next`,
- före varje bildgenerering informeras användaren att skriva `Gör nästa steg` när bilden är klar,
- efter sista slide går nästa steg till PPTX/PDF-paketering.

### Steg 27 – Copilot nedgraderas och 0.3.1 readiness

**Mål:** Göra visual-first till entydig standardväg.

**Leveranser**
- Copilot-handoff dokumenteras som kompletterande/experimentellt spår,
- README/status/release notes uppdateras,
- CI validerar nya regler och regressionstester.

**Klart när**
- CI passerar,
- visual-first kan fortsätta deterministiskt slide för slide,
- praktiskt nästa test kan fokusera på bildkvalitet i stället för batchbeteende.


---

## Förbättringscykel 0.3.2 – Explicit bildgodkännande och nedladdningsbar plan

Bakgrund: praktisk testning visade att `Gör nästa steg` inte var en tillräckligt robust kontrollsignal mellan separata bildgenerationer. Däremot fungerade explicita kommandon som `Det ser bra ut. Skapa slide 3 enligt planen.`. Planeringsdokumentet visades dessutom i sin helhet i chatten i stället för att levereras som fil.

### Steg 28 – Informationssteg före bildproduktion

**Mål:** Förklara arbetsformen innan första bildgenereringen.

**Leverans**
- visa kort instruktion före första bilden:
  - godkänd bild → `Det ser bra ut. Skapa slide X enligt planen.`
  - ändring → `Ändra slide X: ...`
  - omgenerering → `Gör om slide X enligt planen, men ...`

**Klart när**
- `Gör nästa steg` inte rekommenderas mellan bildgenerationer,
- användaren explicit anger både bedömning och nästa slide.

### Steg 29 – Vänteläge för renderingsstatus

**Mål:** Låta planen vänta på användarens bedömning efter en genererad bild.

**Leverans**
- `Next slide: none` tillåts när en slide är `generated` eller `redo`,
- nästa slide väljs först av användarens explicita kommando,
- regressionstest för vänteläget.

### Steg 30 – Presentation Plan som nedladdningsbar fil

**Mål:** Göra den kanoniska planen praktiskt sparbar och återanvändbar.

**Leverans**
- `presentation-plan.md` ska skrivas till fil när runtime kan skapa filer,
- chatten visar endast kort sammanfattning och fil/länk,
- hela Markdown-planen visas inline endast på uttrycklig begäran.

**Klart när**
- canonical instruktion, artifact contract och Knowledge beskriver samma beteende,
- CI passerar.
