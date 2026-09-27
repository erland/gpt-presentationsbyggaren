# Rendering och visuell kvalitetsgate

## Syfte

Rendering ska ge en professionell presentation och en tekniskt giltig leverans. När användaren inte kräver objektredigerbarhet är **visual-first** standard: visuellt resultat prioriteras framför PowerPoints interna objektmodell.

## Två huvudspår

### Visual-first

Använd när visuell kvalitet är viktigare än objektredigering.

- varje slide får renderas till en färdig helslidebild,
- PowerPoint används som presentationsskal,
- PDF ska när möjligt motsvara samma visuella rendering,
- exakt copy ska kontrolleras separat från bildgenereringen,
- speaker notes bevaras när presentationsformatet stöder det.

### Copilot-handoff

Använd när användaren vill ha en redigerbar presentation från ett presentationsverktyg som Microsoft Copilot.

- `presentation-plan.md` är sanningskälla,
- `copilot-handoff.docx` är primärt överlämningsformat,
- PDF kan följa med som stabil referens,
- en kort `copilot-prompt.md` instruerar verktyget att följa dokumentet och skapa redigerbar presentation.

## Visual-first pipeline

1. Validera `presentation-plan.md`.
2. Fastställ visual system.
3. Välj 1–2 anchor slides.
4. Generera och godkänn anchor-assets.
5. Generera återstående assets normalt en slide i taget; använd högst små batcher när det är lämpligt.
6. Komponera korrekt rubrik, etiketter och övrig presentationscopy.
7. Rendera högupplösta slides.
8. Paketera till PPTX och PDF.
9. Granska faktisk preview av alla slides.
10. Leverera först efter teknisk och visuell gate.

## Visuell ambitionsnivå

En färdig presentation ska visa:

- tydligt dominant fokus,
- storlek och kontrast som fungerar på presentationsavstånd,
- varierad komposition när slides gör olika jobb,
- avsiktlig whitespace,
- konsekvent formspråk utan identisk layout,
- visuella metaforer eller illustrationer där de stärker budskapet,
- rytm mellan lugna, informativa och starka slides.

Blockerande varningssignaler:

- wireframe-känsla,
- upprepade små boxar och tunna pilar,
- standardikoner som huvudsakligt visuellt språk,
- allt innehåll samlat i små objekt mitt på en stor canvas,
- generisk mallkänsla utan koppling till budskapet,
- bildgenererad text med felstavning eller felaktiga siffror.

## Bildgenerering

Följ `knowledge/visual-first-workflow.md`.

Bildmodellen ska normalt skapa scen, illustration, bakgrund eller metafor. Presentationscopy läggs separat när exakthet krävs.

Anchor-resultat ska styra senare generationer när runtime kan använda referensbilder.

## PPTX-paketering

Canonical metoden ska inte handskriva rå Open XML.

Vid programmatisk PPTX-generering ska en etablerad presentationsrenderer eller bibliotek användas. För visual-first kan varje slide bestå av en helslidebild; detta minskar behovet av komplex PowerPoint-layout.

## Teknisk PPTX-validering

Före leverans ska PPTX när runtime medger det passera:

1. ZIP-integritet.
2. Obligatoriska delar: `[Content_Types].xml`, `_rels/.rels`, `ppt/presentation.xml`.
3. Alla Content-Type Overrides pekar på delar som finns.
4. Interna relationship-targets kan resolvas.
5. Filen kan öppnas/renderas med en oberoende Office-kompatibel motor när sådan finns.
6. Preview kan skapas.

Fel i 1–4 är alltid blockerande. Fel i 5 blockerar påstådd PowerPoint-kompatibilitet.

## Preview-gate

Granska det användaren faktiskt kommer att se:

- textklippning,
- överlapp,
- oläslig copy,
- låg kontrast,
- oproportionerligt små objekt,
- oavsiktligt tomrum,
- visuella artefakter,
- wireframe- eller mallkänsla,
- inkonsekvent visual system.

I visual-first granskas normalt **alla slides**, eftersom previewn är den slutliga visuella sanningen.

## Leveransformat

När visual-first valts:

1. `presentation-plan.md` – återupptagningsbar masterplan,
2. `presentation.pptx` – bildbaserad PowerPoint för framförande,
3. `presentation.pdf` – visuellt stabil representation.

När redigerbarhet via Copilot önskas:

1. samma `presentation-plan.md`,
2. `copilot-handoff.docx`,
3. `copilot-handoff.pdf` när möjligt,
4. `copilot-prompt.md`.

HTML är fortsatt ett möjligt alternativ för webbpresentation men inte huvudspår i 0.3.

## Leveransgate

Leveransen är klar när:

- presentation-planen är komplett,
- anchor/style-gate är godkänd,
- alla visual-first-slides har granskats som preview,
- inga blockerande visuella problem återstår,
- PPTX-integritet är godkänd om PPTX levereras,
- PDF motsvarar avsedd rendering när PDF levereras,
- Copilot-handoff bevarar samma kärnbudskap och slide-specifikation när det spåret används.
