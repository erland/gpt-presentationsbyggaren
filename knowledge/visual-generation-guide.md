# Guide för visuell generering

## Mål

Visualisering ska minska mottagarens kognitiva arbete. Välj alltid den enklaste visuella form som tydligt visar relationen, förändringen eller slutsatsen.

## Beslutstrappa

Välj i denna ordning:

1. **Typografi och whitespace** – när ett påstående är hela poängen.
2. **Former och relationer** – för struktur, hierarki, flöde och arkitektur.
3. **Tabell** – när exakta värden behöver jämföras.
4. **Diagram** – när mönster, skillnader eller utveckling i data är budskapet.
5. **Ikoner** – som stöd för kategorier, aldrig som huvudsaklig evidens.
6. **Illustration** – när en scen, metafor eller konceptuell modell kommunicerar bättre än ovanstående.
7. **Foto** – endast när verklig miljö, person, produkt eller plats tillför relevant information.

## Diagramregler

- Stapel: jämförelse mellan kategorier.
- Linje: utveckling över ordnad tid.
- Punkt/scatter: samband mellan två numeriska variabler.
- 100 % stapel: sammansättning när relativa andelar är poängen.
- Waterfall: förklaring av hur bidrag leder från start- till slutvärde.
- Undvik cirkeldiagram när små skillnader ska jämföras eller kategorierna är många.
- Undvik 3D-effekter och visuella perspektiv som förvränger data.
- Rubriken ska uttrycka slutsatsen; diagrammet ska visa evidensen.
- Visa bara etiketter och hjälplinjer som behövs för tolkningen.

## Illustrationer

En genererad illustration ska ha ett definierat `visual_intent` i storyboardet. Prompten ska härledas från:

- budskap,
- vald visuell stil,
- komposition,
- vilka objekt och relationer som måste synas,
- vad som uttryckligen ska undvikas.

Illustrationen får inte introducera fakta som saknar stöd i materialet. Text i genererade bilder ska undvikas; lägg text som redigerbara PowerPoint-element ovanpå eller bredvid bilden.

## Redigerbarhet

Föredra inbyggda presentationsobjekt för:

- rubriker,
- etiketter,
- pilar och kopplingar,
- boxar och grupperingar,
- diagram,
- tabeller,
- enkla ikoner och symboler.

En komplex illustration kan vara en bild, men presentationens semantiska struktur ska inte låsas in i en enda rasterbild om den kan byggas redigerbart.

## Konsistens

Inom samma presentation ska följande vara konsekventa:

- typografisk hierarki,
- kant- och hörnbehandling,
- linjetjocklek,
- ikonstil,
- diagrametiketter,
- visuella metaforer,
- mängd dekorativa element.

Variation ska komma från budskap och layout, inte från slumpmässiga stilbyten.

## Tillgänglighet och robusthet

- Säkerställ läsbar kontrast.
- Lägg inte avgörande betydelse enbart i färg.
- Använd tillräckligt stor text för presentationssituationen.
- Undvik överfulla diagram och för små etiketter.
- Säkerställ att en slide fortfarande går att förstå när bilden visas på mindre skärm.

## Genereringsgate

En visuell tillgång är klar när den:

- stödjer exakt det avsedda budskapet,
- följer vald visuell stil,
- inte tillför ostyrkt information,
- inte duplicerar text utan anledning,
- kan placeras utan att förstöra informationshierarkin,
- är redigerbar där det är rimligt.
