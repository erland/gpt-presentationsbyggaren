# Release notes – 0.2.0-rc.1

## Rendering och visuell kvalitet

0.2 adresserar fynd från praktisk testning av 0.1 RC1: en PPTX kunde innehålla ogiltiga Open XML-referenser och den visuella designen blev för ofta wireframe-lik.

### Viktiga ändringar

- Kommunikationskvalitet går före automatisk native-redigerbarhet.
- Fyra renderingsstrategier: native, designed composition, generated visual och hybrid.
- Ny rendering/visual-quality guide med explicit ambitionsnivå.
- Deterministisk PPTX-validator för ZIP/Open XML, Content Types och relationship-targets.
- Trasig PPTX och genomgående wireframe-lik design är blockerande kvalitetsproblem.
- Preview-baserad visuell kvalitetsgate när runtime kan rendera slides.
- PDF är rekommenderad visuellt stabil följeslagare.
- HTML kan användas när webbpresentation och visuell frihet väger tyngre än PowerPoint-redigerbarhet.
- Presentation-generation-kontraktet bär teknisk valideringsstatus och visuell ambitionskontroll.
- Regressionstester täcker den felklass som observerades i 0.1-testet.

## Kvalificering

GitHub Actions CI passerar för PR #2 med projektvalidering, lint, deterministiska tester, hygiene, distributionsbuild och distributionsvalidering.

Kvar före slutlig 0.2 releasekandidat är praktiskt end-to-end-test: skapa en verklig presentation, öppna PPTX i Microsoft PowerPoint och jämför mot PDF/preview.

## Kända begränsningar

- Projektet innehåller en deterministisk paketvalidator men ingen egen generell presentationsrenderer. Runtime ska använda en etablerad presentationsrenderer och får inte handbygga rå Open XML.
- Oberoende Office-rendering och preview kräver att aktuell runtime har motsvarande verktyg.
- Live cross-model-kvalificering kvarstår från 0.1-planen.

---

# Release notes – 0.1.0-rc.1

## Första releasekandidat

Presentationsbyggaren 0.1.0-rc.1 är den första kompletta releasekandidaten. Den hjälper användaren från presentationsbehov och källmaterial till storyline, storyboard, stilval, visuell design, redigerbar PowerPoint och kvalitetsgranskning.

## Viktig funktionalitet

- Styrt flöde: Brief → Storyline → Storyboard → Design → Presentation → Kvalitetsgranskning.
- 8 innehållsstilar och 6 visuella stilar som kan kombineras oberoende.
- 20 slide patterns och 7 storytelling patterns.
- Runtime-neutral storyboard- och genereringsmodell.
- Transformationsflöden för att korta, byta målgrupp/stil och göra presentationer mer visuella.
- Separata distributioner för ChatGPT Chat och ChatGPT Custom, byggda från samma canonical källa.
- CI, release-build, checksummor, hygiene och runtime-paritetskontroll.

## Kända begränsningar

- Live cross-model-kvalificering mot separat enklare och starkare modell har inte kunnat köras i den aktuella byggmiljön.
- Faktisk PPTX-kvalitet beror på presentationsförmågan i den runtime där GPT:n körs.
