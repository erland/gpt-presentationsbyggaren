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

## En slide per bildgenerering

**Hård standardregel: en bildgenerering = exakt en slutlig slidebild.**

Det gäller även enkla slides.

Varje bildprompt ska uttryckligen säga:

> Skapa exakt en slutlig 16:9-slidebild för denna slide. Använd hela canvasen för en sammanhängande professionell komposition. Skapa inte collage, grid, kontaktkarta, moodboard, storyboardark, flera alternativa versioner eller flera små slidebilder på samma canvas.

Om sliden innehåller flera steg eller perspektiv får de visas inom samma slide, men som **få stora integrerade delar**. Tre steg kan exempelvis vara tre stora scener över bredden; de ska inte bli thumbnails.

Generera inte flera slides i samma verktygsanrop även om runtime tekniskt kan skapa flera bilder. Produktionsflödet behöver ett separat kvalitetsbeslut för varje slide.

## Interaktion mellan generationerna

När bildverktyget avslutar turen efter generering ska Presentationsbyggaren göra fortsättningen tydlig **före** verktygsanropet.

Före varje slidebild ska användaren få en kort statusrad:

> Jag skapar nu slide X av Y. När bilden är klar, skriv **"Gör nästa steg"** så fortsätter jag med slide Z.

Efter att användaren skriver **"Gör nästa steg"**:

1. läs renderingsstatusen,
2. behandla föregående generering som `generated` om den inte uttryckligen underkänts,
3. välj exakt den slide som är markerad `next`,
4. uppdatera nästa slide till `next`,
5. generera endast den valda sliden.

Efter sista slide ska nästa steg vara paketering till PPTX/PDF, inte ännu en bildgeneration.

## Anti-collage-gate

En bild underkänns om den:

- visar flera slide-miniatyrer,
- ser ut som en kontaktkarta eller storyboard,
- innehåller ett grid av små alternativa illustrationer,
- delar canvasen i många små oberoende paneler utan att detta är själva slidebudskapet,
- återger flera designvarianter i samma bild.

Vid sådant resultat: gör om **samma slide**, inte nästa slide.

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
