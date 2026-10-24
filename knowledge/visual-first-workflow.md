# Visual-first workflow

## Mål

Visual-first är standardspåret när användaren prioriterar visuell kvalitet framför objektredigerbarhet. Slutprodukten ska se ut som en färdig designerpresentation, inte som ett diagramverktyg eller wireframe.

## Output

Primära leveranser:

- `presentation.pptx` – PowerPoint-skal där varje slide kan bestå av en färdigrenderad helslidebild,
- `presentation.pdf` – samma visuella resultat för stabil distribution,
- `presentation-plan.md` – kanonisk plan som gör arbetet återupptagningsbart.

PPTX behöver inte ha redigerbara interna objekt när användaren valt visual-first.

## Renderingspipeline – AI i två steg per slide

1. Läs `presentation-plan.md` och aktuellt projekttillstånd.
2. Fastställ visual system och välj 1–2 anchor slides.
3. **Bakgrund:** generera en bild som fungerar som självständig, textfri visuell komposition. Inga textrutor, etiketter, förberedda plattor, ramar eller textplatshållare. Låt negativt utrymme uppstå naturligt.
4. Spara `slides/slide-NN-background.png`. Markera `background_ready`.
5. **Final:** skapa en NY bild från bakgrunden som **faktisk bildreferens** och ange exakt text. Låt modellen integrera typografi och eventuella skuggor, toner och grafiska textstöd i detta steg. Generera inte en ny orelaterad bakgrund från enbart prompt.
6. Kontrollera bakgrundens visuella kontinuitet och slutbildens ordalydelse, kontrast och komposition. Spara `slides/slide-NN-final.png`; markera `final_ready`.
7. Visa finalbilden för godkännande. Ändra status till `approved` först efter användarens explicita godkännande.
8. Upprepa för nästa slide. Exportera **finalbilderna** i PPTX och PDF, inspektera preview, och skapa projekt-ZIP inklusive båda bildversionerna.
9. Vid textändring: bevara bakgrunden, regenerera enbart finalbilden, återställ status till `final_ready` och begär nytt godkännande. Versionsspara ersatt finalbild där stöd finns.

När bildreferenser inte stöds: beskriv begränsningen; gör inte anspråk på referensbaserad bildgenerering. Exakt text och grafisk överensstämmelse behöver kontrolleras visuellt.

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

**Hård regel: en bildgenerering = exakt en bild av en slide. Två bildgenereringar ingår normalt per slide: bakgrund + final.**

Det gäller även enkla slides.

Varje bildprompt ska uttryckligen säga:

> Skapa exakt en 16:9-bild för detta steg (ren bakgrund eller final) av denna slide. Använd hela canvasen för en sammanhängande professionell komposition. Skapa inte collage, grid, kontaktkarta, moodboard, storyboardark, flera alternativa versioner eller flera små slidebilder på samma canvas.

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

1. markera den senast genererade sliden som `approved`,
2. läs specifikationen för slide X ur `presentation-plan.md`,
3. markera slide X som `next`,
4. generera bakgrundsbild för slide X och därefter en separat AI-finalbild med bakgrunden som bildreferens,
5. lämna övriga slides oförändrade.

Om användaren ber om ändring eller omgenerering ska samma slide behållas som aktiv tills användaren uttryckligen godkänner den.

Efter sista godkända slide ska nästa arbetssteg vara paketering till PPTX/PDF.

## Anti-collage-gate

En bild underkänns om den:

- visar flera slide-miniatyrer,
- ser ut som en kontaktkarta eller storyboard,
- innehåller ett grid av små alternativa illustrationer,
- delar canvasen i många små oberoende paneler utan att detta är själva slidebudskapet,
- återger flera designvarianter i samma bild.

Vid sådant resultat: gör om **samma slide**, inte nästa slide.

## Bakgrund kontra text i final

Bakgrundsbilden innehåller motiv, ljus och bildspråk men **ingen text och inga förberedda textrutor eller tonplattor**. Finalbilden får däremot text, textrelaterade effekter och grafisk typografi via AI-generering med bakgrundsbilden som referens. Förlita dig inte på deterministisk textoverlay som normalväg. Exakta siffror, längre text och källor kräver särskild kontroll; be användaren godkänna slutresultatet innan export.

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

## Bakgrundsgate

Innan `final_ready` måste `background_gate` ha `checked`, `text_free`, `no_text_containers` och `single_scene` satta till true samt `sha256` för bakgrundsfilens bytes. Valideraren kontrollerar metadata och hash, men inte bildens semantiska innehåll. Rapportera faktisk visuell granskning separat.
