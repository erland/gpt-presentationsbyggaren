# Slide design guide

Detta dokument definierar hur en storyline översätts till ett storyboard som är tillräckligt precist för presentationgenerering men fortfarande runtime-neutralt.

## Grundprincip

Varje slide ska göra ett tydligt kommunikationsjobb och normalt bära **ett huvudbudskap**. Storyboardet ska beskriva vad mottagaren ska förstå och hur det ska visualiseras – inte pixelplacering eller PowerPoint-specifik implementation.

## Obligatoriska slidefält

Varje slide ska ha:

- `title` – den synliga rubriken; helst en poäng eller slutsats när innehållet tillåter det.
- `message` – exakt ett huvudbudskap som sliden ska förmedla.
- `purpose` – vilket kommunikationsjobb sliden gör.
- `pattern` – ett känt slide pattern från `slide-patterns.md`.
- `visual_intent` – varför och hur informationen ska visualiseras.
- `layout` – komposition, densitet, hierarki och alignment.
- `content` – endast det som behöver finnas på sliden samt eventuella nyckeldata och källreferenser.
- `speaker_notes` – förklaringar som hjälper framförandet men inte behöver visas.
- `quality_checks` – slide-specifika gate-resultat.

## Från storyline till slides

1. Börja från storyline-punkternas funktion, inte från källmaterialets rubriker.
2. Skapa så få slides som behövs för att varje budskap ska vara tydligt.
3. Dela en storyline-punkt i flera slides endast när mottagaren behöver separata visuella eller argumentativa steg.
4. Slå ihop slides som skulle göra samma kommunikationsjobb.
5. Välj pattern utifrån budskapets form, inte efter variation för variationens skull.

## Ett huvudbudskap per slide

`message` ska vara en enkel deklarativ sats. Om den naturligt behöver innehålla två oberoende slutsatser ska innehållet delas upp i två slides eller en av slutsatserna flyttas till speaker notes/appendix.

Rubriken bör normalt uttrycka samma poäng i publikvänlig form. Undvik ämnesrubriker som "Bakgrund", "Arkitektur" och "Resultat" när sliden i stället kan säga vad publiken ska förstå.

## Textdensitet

`content.on_slide` innehåller endast text som måste synas för att visualiseringen ska förstås.

Flytta innehåll från sliden när något av följande gäller:

- texten förklarar *varför* snarare än visar *vad*;
- samma detalj redan framgår visuellt;
- fler än cirka 3–5 textpunkter behövs för en normal slide;
- en punkt kräver flera meningar för att förstås;
- detaljer är relevanta för frågor men inte huvudberättelsen.

Förklarande material flyttas i första hand till `speaker_notes`. Bevis, tabeller eller detaljer som kan behövas vid fördjupning flyttas till appendix.

## Visual intent

`visual_intent.mode` väljs efter informationsbehov:

- `text-led` – budskapet kräver främst en kort formulering eller slutsats.
- `diagram` – relationer, struktur, flöde eller beroenden är centrala.
- `data` – siffror eller jämförbara mätvärden bär argumentet.
- `image` – en informationsbärande illustration eller konkret bild är viktigast.
- `hybrid` – två uttryck behövs och båda bidrar till samma budskap.

`primary_visual` beskriver vad som faktiskt ska dominera sliden, exempelvis "trestegsprocess med tydlig riktning" eller "stapelgraf som jämför ledtid före och efter".

`elements` beskriver de viktigaste objekten som måste synas. `relationships` beskriver betydelsefulla kopplingar eller riktningar mellan objekten. Dessa fält gör storyboardet användbart som indata till diagram- eller presentationsgenerering.

Sätt `image_generation_needed: true` endast när en genererad illustration tillför information som inte kan uttryckas bättre med redigerbara former, diagram eller text.

## Layoutspecifikation

Storyboardet ska ange komposition utan att låsa renderingstekniken.

- `composition`: kort fri beskrivning, exempelvis "rubrik överst, stor process centralt, en slutsatsrad längst ned".
- `density`: `low`, `medium` eller `high`.
- `hierarchy`: ordnad lista över vad ögat ska möta först, sedan därefter.
- `alignment`: primär struktur (`left`, `center`, `grid`, `mixed`).

Innehållsstilen styr detaljnivå och berättelse. Den visuella stilen styr typografisk känsla, luft, kontrast och grafiskt uttryck. Slide-specifik layout får inte bryta mot den valda visuella stilens principer utan tydligt skäl.

## Speaker notes och appendix

Speaker notes används för:

- muntlig förklaring och övergångar;
- definitioner som talaren behöver men publiken inte måste läsa;
- metoddetaljer som inte bär huvudbudskapet;
- källförklaringar som inte måste visas.

Appendix används för:

- detaljerade tabeller;
- tekniska fördjupningar;
- extra evidens;
- alternativa vyer;
- sådant som behövs för frågor men skulle bromsa huvudberättelsen.

## Storyboard-gate

Storyboardet är redo för design/rendering först när:

- varje slide har exakt ett explicit `message`;
- alla slides har `title`, `purpose`, `pattern` och `visual_intent`;
- två slides inte gör samma jobb utan avsikt;
- varje visualisering stöder budskapet;
- texttätheten är rimlig och överflödig text har flyttats;
- slideordningen följer storylinen;
- storyboardet innehåller tillräckligt med information för att skapa presentationen utan att hitta på centralt innehåll.
