# Visual-first workflow

## Mål

Visual-first är standardspåret när användaren prioriterar visuell kvalitet. Slutprodukten ska se ut som en färdig designerpresentation, inte som ett diagramverktyg eller wireframe. När endast texten behöver vara redigerbar används normalt `hybrid-slide`: grafiken ligger i en bildbaserad bakgrund och presentationscopy ligger som native PowerPoint-text ovanpå.

## Output

Primära leveranser:

- `presentation.pptx` – PowerPoint där `image-slide` kan vara en färdigrenderad helslidebild och `hybrid-slide` använder bildbaserad grafik med redigerbar text ovanpå,
- `presentation.pdf` – samma visuella resultat för stabil distribution,
- `presentation-plan.md` – kanonisk plan som gör arbetet återupptagningsbart.

PPTX behöver inte ha redigerbar grafik i visual-first. När användaren vill kunna ändra text ska texten däremot bevaras som separata redigerbara textobjekt på `hybrid-slide`.

## Renderingspipeline

1. Läs `presentation-plan.md`.
2. Fastställ visual system.
3. Välj 1–2 anchor slides.
4. Generera och kvalitetsgranska anchor-assets.
5. Generera övriga slide-assets med anchor-resultaten som stilreferens när runtime stöder det.
6. För `hybrid-slide`: generera bildbaserad grafik utan presentationscopy och reservera de textytor som planen anger.
7. Lägg exakt presentationscopy som native PowerPoint-textobjekt ovanpå bakgrunden. För `image-slide`: komponera och rendera hela sliden till högupplöst bild.
8. Paketera hybrid- och bildslides i samma PPTX och skapa PDF från den visuella slutrenderingen.
9. Granska faktisk preview av alla slides samt kontrollera textoverflow och kontrast på hybrid-slides.
10. Leverera endast när teknisk, visuell och – när relevant – redigerbarhetsgate passerar.

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

Bildverktyget kan avsluta turen direkt efter genereringen. Därför ska Presentationsbyggaren ge användaren arbetsinstruktionen **innan den första slidebilden skapas**.

Visa kort:

> Jag skapar presentationen en slide i taget. Efter varje bild:
> - om du är nöjd, skriv t.ex. **"Det ser bra ut. Skapa slide 2 enligt planen."**
> - om du vill justera bilden, skriv t.ex. **"Ändra slide 1: gör illustrationen större."**
> - om den ska göras om, skriv t.ex. **"Gör om slide 1 enligt planen, men utan ikoner."**

Mellan bildgenerationer ska `Gör nästa steg` **inte** vara den rekommenderade kontrollsignalen.

När användaren skriver `Det ser bra ut. Skapa slide X enligt planen.`:

1. bind den senast genererade bildfilen till sliden som `Approved asset`,
2. markera den senast genererade sliden som `approved`,
3. läs specifikationen för slide X ur `presentation-plan.md`,
4. markera slide X som `next`,
5. generera exakt en slutlig bild för slide X,
6. lämna övriga slides oförändrade.

Om användaren ber om ändring eller omgenerering ska samma slide behållas som aktiv tills användaren uttryckligen godkänner den.

Efter sista godkända slide ska nästa arbetssteg vara paketering till PPTX/PDF. Paketeringen får endast starta när alla `image-slide` och `hybrid-slide` är markerade `approved` i `Rendering status` och varje godkänd slide har en explicit `Approved asset`. `next`, `pending`, `generated`, `redo` eller saknad assetbindning är blockerande.

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

På `hybrid-slide` komponeras exakt copy som separata native PowerPoint-textobjekt ovanpå asseten och får inte rasteriseras in i bakgrundsbilden. På `image-slide` får copy komponeras kontrollerat före helslidebilden exporteras.

## Hybrid-slide

Använd `hybrid-slide` när texten ska kunna ändras utan att den visuella grafiken behöver vara objektredigerbar.

### Obligatoriskt promptkontrakt

För `hybrid-slide` ska bildprompten **inte innehålla presentationscopy från `Visible text`**. Copy används först senare när native PowerPoint-textlagret skapas.

Bildprompten ska byggas från slide-specifikationens visuella delar: `Visual concept`, `Composition`, `Must show`, `Must avoid` och `Text-safe area`. Följande regel ska alltid ingå ordagrant eller semantiskt lika starkt:

> Ingen läsbar text, inga bokstäver, inga ord, inga siffror, inga etiketter, ingen pseudo-text och inga textliknande symboler i bilden.

Om bakgrundsbilden trots detta innehåller läsbar text, teckenrader eller pseudo-text ska bilden underkännas, sliden sättas till `redo` och samma slide genereras om. Den får inte bindas som `Approved asset`.

- Bildasseten får innehålla illustrationer, färgfält, boxar, linjer, pilar, diagram och dekorativa element.
- Bildasseten ska inte innehålla rubriker, brödtext, etiketter, källor eller annan presentationscopy som ska vara redigerbar.
- `presentation-plan.md` ska ange en `Text layout` och bildprompten ska reservera motsvarande text-safe area.
- Textytan ska vara visuellt lugn och ha tillräcklig kontrast för den avsedda textstilen.
- Preview ska bedöma den sammansatta sliden, inte bakgrundsbilden isolerat.

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
- inga oavsiktliga objekt eller visuella artefakter,
- på `hybrid-slide`: ingen läsbar text, inga bokstäver/ord/siffror/etiketter eller pseudo-text i bakgrundsbilden; presentationscopy får endast finnas i overlay-lagret och ingen textoverflow får finnas där.

En slide som ser ut som en skiss, ett flödesschema av standardboxar eller en generisk AI-mall ska göras om.
