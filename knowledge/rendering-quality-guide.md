# Rendering och visuell kvalitetsgate

## Syfte

Rendering ska ge en professionell presentation och en tekniskt giltig leverans. **Visual-first** prioriterar visuellt resultat framför full objektredigerbarhet, men kan samtidigt bevara texten som redigerbara PowerPoint-objekt när användaren behöver det.

## Två huvudspår

### Visual-first

Använd när visuell kvalitet är viktigast. Två render modes stöds:

- `hybrid-slide` – bildbaserad grafik med native, redigerbar PowerPoint-text ovanpå; normalval när texten ska kunna ändras,
- `image-slide` – färdigrenderad helslidebild; används när redigerbar text inte krävs eller som runtime-fallback.

I båda fallen ska PDF när möjligt motsvara samma visuella slutrendering, exakt copy kontrolleras separat från bildgenereringen och speaker notes bevaras när presentationsformatet stöder det.

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
6. För hybrid-slides: lägg korrekt rubrik, etiketter och övrig presentationscopy som native text ovanpå textfri grafik. För image-slides: komponera copy före helslide-rendering.
7. Rendera faktisk preview av den sammansatta sliden.
8. Paketera till PPTX och PDF.
9. Granska alla previews samt textoverflow, kontrast och textplacering på hybrid-slides.
10. Leverera först efter teknisk, visuell och relevant redigerbarhetsgate.

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

Bildmodellen ska normalt skapa scen, illustration, bakgrund eller metafor. På `hybrid-slide` läggs presentationscopy alltid separat som native PowerPoint-text och bildasseten ska reservera text-safe area.

Anchor-resultat ska styra senare generationer när runtime kan använda referensbilder.

## PPTX-paketering

Canonical metoden ska inte handskriva rå Open XML.

Vid programmatisk PPTX-generering ska en etablerad presentationsrenderer eller bibliotek användas. En `image-slide` kan bestå av en helslidebild. En `hybrid-slide` ska bestå av en bildbaserad bakgrund plus separata textshapes; grafiska objekt behöver inte rekonstrueras som PowerPoint-former.

## Teknisk PPTX-validering

Före leverans ska PPTX när runtime medger det passera:

1. ZIP-integritet.
2. Obligatoriska delar: `[Content_Types].xml`, `_rels/.rels`, `ppt/presentation.xml`.
3. Alla Content-Type Overrides pekar på delar som finns.
4. Interna relationship-targets kan resolvas.
5. Filen kan öppnas/renderas med en oberoende Office-kompatibel motor när sådan finns.
6. Preview kan skapas.
7. När hybrid-slides levereras: presentationscopy finns som textshapes i slide-XML och inte enbart i rasterbilden.

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
- collage/kontaktkarta/thumbnail-grid i stället för en enda slidekomposition,
- wireframe- eller mallkänsla,
- inkonsekvent visual system,
- på hybrid-slides: text som ser påklistrad ut, overflow, otillräcklig kontrast eller presentationscopy som råkat hamna i bakgrundsbilden.

I visual-first granskas normalt **alla slides**, eftersom previewn är den slutliga visuella sanningen.

## Leveransformat

När visual-first valts:

1. `presentation-plan.md` – återupptagningsbar masterplan,
2. `presentation.pptx` – visual-first PowerPoint; normalt hybrid med redigerbar text när det efterfrågas, annars bildbaserad,
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
- redigerbar text verifieras på hybrid-slides när sådan utlovas,
- PDF motsvarar avsedd rendering när PDF levereras,
- Copilot-handoff bevarar samma kärnbudskap och slide-specifikation när det spåret används.
