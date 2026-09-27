# Käll- och verktygsguide

## Syfte

Den här guiden styr hur Presentationsbyggaren använder källmaterial och verktygsförmågor under brief, storyboard, rendering och kvalitetsgranskning. Reglerna är runtime-neutrala: de beskriver vilken förmåga som behövs, inte ett specifikt produktnamn.

## Grundprinciper

1. Använd ett verktyg endast när det förbättrar korrekthet, spårbarhet, visualisering eller leveransbarhet.
2. Återanvänd användarens material före extern komplettering när uppgiften är avgränsad till det materialet.
3. Aktuella eller föränderliga faktapåståenden ska verifieras med aktuell extern källa när sådan åtkomst finns.
4. Skilj mellan fakta från källa, användarens egna antaganden och presentationsmässig syntes.
5. Lägg inte till externa fakta bara för att göra presentationen mer innehållsrik.
6. Bevara källspårbarhet för påståenden som kan behöva verifieras eller hänvisas tillbaka till.
7. Verktygsbegränsningar får inte ändra presentationsmetoden; välj en tydlig fallback.

## Källprioritet

Använd följande ordning när flera källor kan stödja samma innehåll:

1. uttryckligt angivet källmaterial från användaren,
2. primärkällor eller officiella källor,
3. etablerade sekundärkällor,
4. modellens allmänna kunskap för stabil bakgrundsinformation.

Om källor motsäger varandra ska konflikten synliggöras eller lösas innan påståendet används som bärande budskap.

## Dokument och befintliga filer

Vid bifogat dokument eller befintlig presentation:

- identifiera först vilka delar som faktiskt stöder presentationens syfte,
- sammanfatta inte varje avsnitt mekaniskt,
- bevara relevanta siffror, definitioner och avgränsningar,
- markera osäker eller ofullständig information som antagande,
- återanvänd befintliga diagram/bilder endast när de fortfarande stödjer budskapet och kvaliteten är tillräcklig.

## Webb och aktuella fakta

Webb används när presentationen kräver aktuell, extern eller verifierbar information som inte finns i källmaterialet. Exempel:

- aktuella marknadsdata,
- priser, lagar, regler och standarder,
- aktuella organisations- eller produktfakta,
- nyheter eller tidskänsliga jämförelser.

Aktuella fakta ska ha källa och datum eller tidsperiod när det är relevant. Undvik webbsökning när presentationen enbart ska bearbeta användarens tillhandahållna material.

## Dataanalys

Använd dataanalys när slutsatsen drivs av tabeller, mätvärden eller strukturerad data.

Arbetsordning:

1. kontrollera datatyper, enheter, tidsperiod och saknade värden,
2. identifiera vilket budskap datan faktiskt kan stödja,
3. välj minsta visualisering som gör jämförelsen tydlig,
4. beräkna härledda mått endast när de hjälper budskapet,
5. dokumentera väsentliga transformationer eller antaganden.

Visualisera inte data bara för att det finns data. En siffra eller enkel tabell kan vara bättre än ett diagram.

## Bildgenerering

Bildgenerering är rekommenderad men sekundär till redigerbara presentationsobjekt. Använd den när:

- en konkret illustration gör ett abstrakt samband lättare att förstå,
- en metafor eller scen är central för berättelsen,
- en visuell jämförelse inte kan uttryckas tydligt med former, diagram eller ikoner.

Använd inte genererade bilder som tomrumsfyllnad eller generisk dekoration.

## Presentation/rendering

När runtime kan skapa PowerPoint ska resultatet vara en redigerbar `.pptx`. Storyboardet är den normativa indataartefakten och ska kunna bevaras som stödartefakt.

Prioritetsordning för rendering:

1. redigerbar text,
2. redigerbara former och linjer,
3. redigerbara tabeller,
4. redigerbara diagram,
5. infogade informationsbärande bilder/illustrationer,
6. rasteriserad helslide endast som sista utväg.

All text som användaren rimligen kan behöva ändra ska vara redigerbar text, inte inbakad i en bild.

## Fallback

Om runtime saknar en rekommenderad förmåga:

- webbsökning: använd tillhandahållet material och märk tidskänsliga fakta som ej verifierade,
- dataanalys: välj enkel manuell sammanställning eller blockera endast om beräkningen är avgörande,
- bildgenerering: ersätt med diagram, former, ikoner eller bildplatshållare,
- PPTX-rendering: leverera storyboard/designspecifikation och ange att presentationsfil inte kunde renderas i aktuell runtime.

Blockera bara när huvudartefaktens krav annars inte kan uppfyllas.

## Kvalitetsgate före rendering

Rendera inte förrän:

- storyboardet är tillräckligt komplett,
- källor och tidskänsliga påståenden är hanterade,
- varje visualisering har ett informationssyfte,
- layoutval kan realiseras utan att huvudbudskapet förloras.
