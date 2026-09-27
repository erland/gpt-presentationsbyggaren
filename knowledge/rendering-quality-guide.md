# Rendering och visuell kvalitetsgate

## Syfte

Den här guiden styr övergången från validerat storyboard till levererbar presentation. Målet är tvådelat:

1. presentationen ska se designad ut, inte som ett wireframe,
2. PPTX-filen ska vara tekniskt giltig och kunna öppnas i PowerPoint-kompatibla program.

## Designprincip

**Kommunikationskvalitet först, redigerbarhet där det är rimligt.**

Redigerbarhet är en viktig egenskap men inte det överordnade målet. En slide med primitiva boxar och linjer är inte bättre bara för att varje objekt går att redigera.

Välj för varje slide en renderingsstrategi:

- `native` – text, tabeller, enkla diagram, processer och strukturer som tjänar på fortsatt redigering,
- `designed-composition` – större typografi, färgfält, former, lager, asymmetri och grafisk rytm byggd med presentationsobjekt,
- `generated-visual` – informationsbärande illustration, konceptbild eller metafor när native objekt skulle ge märkbart svagare kommunikation,
- `hybrid` – illustration eller bild kombinerad med redigerbar rubrik, etiketter, data eller källor.

## Visuell ambitionsnivå

En färdig presentation ska normalt visa flera av följande egenskaper:

- tydlig variation i komposition mellan slides som gör olika jobb,
- stark skala: minst ett tydligt dominant element på viktiga slides,
- genomtänkt typografisk hierarki,
- avsiktlig användning av whitespace,
- visuella ankare som hjälper minnet,
- illustrationer eller starkare grafiska kompositioner på hero-/aha-slides när det passar,
- konsekvent men inte mekaniskt gridsystem,
- tydlig rytm mellan lugna, informativa och starka slides.

Följande är varningssignaler:

- samma låda-med-linje-komposition upprepas genom stora delar av presentationen,
- alla objekt är små i relation till canvasen,
- stor tom yta saknar avsikt,
- ikoner används som ersättning för faktisk visualisering,
- varje slide ser ut som ett storyboard snarare än en slutdesign.

## Rendererstrategi

Canonical metoden ska inte själv konstruera rå Open XML.

När runtime erbjuder en etablerad presentationsrenderer ska den användas. Vid programmatisk PPTX-generering ska en renderer med etablerat stöd för PowerPoint/Open XML användas i stället för handskrivna ZIP/XML-delar.

Renderingen ska följa presentation-generation-specifikationen och bevara:

- slideformat,
- typsnittsfallback,
- speaker notes när det stöds,
- text som separata element där den rimligen behöver redigeras,
- källor och etiketter som redigerbara element,
- bilder i tillräcklig upplösning.

## Teknisk PPTX-validering

Före leverans ska PPTX, när runtime medger det, passera:

1. **ZIP-integritet** – filen är ett läsbart ZIP-paket.
2. **Obligatoriska delar** – minst `[Content_Types].xml`, `_rels/.rels` och `ppt/presentation.xml` finns.
3. **Content Types** – varje explicit Override-part pekar på en del som faktiskt finns.
4. **Relationships** – interna relationship-targets går att resolva till befintliga delar.
5. **Oberoende rendering** – filen kan öppnas eller renderas i en separat Office-kompatibel motor när sådan finns.
6. **Preview** – slides renderas till bilder/PDF för visuell kontroll.

Ett fel i steg 1–4 är alltid blockerande. Fel i steg 5 är blockerande för påstådd PowerPoint-kompatibilitet.

## Visuell preview-gate

Granska renderade slides som faktisk bild, inte bara objektmodellen.

Kontrollera:

- textklippning och overflow,
- element utanför canvas,
- oläslig text,
- överlapp,
- oproportionerligt små objekt,
- repetitiv wireframe-känsla,
- oavsiktligt tomma ytor,
- låg kontrast,
- visuella element som inte stödjer slide-budskapet.

Minst titel/öppning, en typisk innehållsslide, en komplex slide och avslutning bör granskas; vid liten presentation granskas alla slides.

## Leveransformat

För full presentationsleverans prioriteras:

1. **PPTX** – huvudformat när fortsatt redigering eller PowerPoint krävs.
2. **PDF** – rekommenderad följeslagare som visuellt stabil referens.
3. **HTML** – alternativ när hög visuell frihet, animation eller webbpresentation är viktigare än PowerPoint-redigering.

PDF och HTML ersätter inte PPTX när användaren uttryckligen behöver PowerPoint, men kan vara bättre primärformat när redigering inte är ett krav.

## Leveransgate

En leverans får kallas färdig först när:

- storyboard- och designgate är godkända,
- teknisk PPTX-validering är godkänd för PPTX,
- preview har granskats när rendering är möjlig,
- inga blockerande visuella problem återstår,
- PDF har skapats som följeslagare när runtime kan göra det och uppgiften motiverar det,
- eventuella valideringsbegränsningar redovisas uttryckligt.
