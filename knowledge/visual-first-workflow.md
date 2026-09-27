# Visual-first workflow

## Mål

Visual-first är standardspåret när användaren prioriterar visuell kvalitet framför objektredigerbarhet. Slutprodukten ska se ut som en färdig designerpresentation, inte som ett diagramverktyg eller wireframe.

## Output

Primära leveranser:

- `presentation.pptx` – PowerPoint-skal där varje slide kan bestå av en färdigrenderad helslidebild,
- `presentation.pdf` – samma visuella resultat för stabil distribution,
- `presentation-plan.md` – kanonisk plan som gör arbetet återupptagningsbart.

PPTX behöver inte ha redigerbara interna objekt när användaren valt visual-first.

## Renderingspipeline

1. Läs `presentation-plan.md`.
2. Fastställ visual system.
3. Välj 1–2 anchor slides.
4. Generera och kvalitetsgranska anchor-assets.
5. Generera övriga slide-assets med anchor-resultaten som stilreferens när runtime stöder det.
6. Komponera exakt presentationscopy separat från bildgenereringen när text måste vara korrekt.
7. Rendera varje slide till högupplöst bild.
8. Paketera slidebilderna i PPTX och PDF.
9. Granska faktisk preview av alla slides.
10. Leverera endast när teknisk och visuell gate passerar.

## Anchor slides

Anchor slides används för att etablera formspråket innan resten av presentationen genereras.

Välj normalt:

- titel/öppning eller annan identitetsbärande slide,
- en central hero-/aha-slide eller representativ innehållsslide.

Anchor slides ska testa:

- illustrationstyp,
- färg/kontrast,
- skala,
- visuell densitet,
- bildspråk,
- relationen mellan illustration och text.

Om anchor-resultatet är svagt ska visual system justeras **innan** resten genereras.

## Hur många bilder per prompt?

Generera inte hela presentationen i en enda bildprompt.

Standard:

- **1 slide per generation** för hero-slides, konceptuella slides, människor/scener, komplexa metaforer och slides som är viktiga för presentationens identitet.
- **2–4 slides i en liten batch** kan användas för enklare och närbesläktade assets när runtime faktiskt kan hålla dem separata och konsekventa.
- **Aldrig hela decket i en enda bildgeneration** som standard.

Kvalitet och kontroll går före minimering av antal generationer.

## Bild kontra text

Bildmodellen ska normalt skapa:

- scen,
- illustration,
- grafisk bakgrund,
- visuella objekt,
- metafor,
- atmosfär och komposition.

Bildmodellen ska normalt **inte** skapa:

- långa rubriker,
- brödtext,
- exakta siffror,
- källhänvisningar,
- text som måste vara helt korrekt.

Exakt copy komponeras ovanpå eller tillsammans med asseten i ett kontrollerat renderingssteg före helslidebilden exporteras.

## Konsistens

Alla generationer ska få:

- samma visual-system-beskrivning,
- samma format/aspect ratio,
- samma återkommande stilbegrepp,
- relevanta anchor-referenser när runtime stöder bildreferenser,
- slide-specifik visual concept,
- tydliga `must show` och `must avoid`.

Undvik att återanvända exakt samma komposition bara för konsistens. Konsistens gäller formspråk, inte layoutidentitet.

## Kvalitetsgate

Varje slide ska granskas som bild för:

- tydligt dominant fokus,
- professionell komposition,
- rimlig textyta,
- korrekt visuell hierarki,
- frånvaro av wireframe-känsla,
- konsekvent formspråk,
- inga bildgenererade textfel,
- inga oavsiktliga objekt eller visuella artefakter.

En slide som ser ut som en skiss, ett flödesschema av standardboxar eller en generisk AI-mall ska göras om.
