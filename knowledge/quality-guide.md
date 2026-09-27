# Quality guide – granskning och transformation

## Syfte

Kvalitetsgranskningen ska avgöra om presentationen fungerar för sitt syfte och sin målgrupp, inte bara om enskilda slides ser bra ut. Granskning görs först på helheten och därefter på slide-nivå.

## Två nivåer av problem

### Blockerande problem

Ett problem är blockerande när det gör att presentationen inte bör betraktas som professionellt leveransklar. Exempel:

- kärnbudskapet är oklart eller motsägs av presentationen,
- ordningen mellan slides gör argumentationen svår att följa,
- flera slides saknar ett tydligt huvudbudskap,
- avgörande fakta saknar stöd eller är uppenbart osäkra,
- viktig text eller grafik riskerar att klippas eller bli oläslig,
- vald visualisering förvränger eller döljer den bärande informationen,
- presentationen är väsentligt felanpassad till målgruppen eller det beslut som ska tas,
- transformationen har tappat eller ändrat kärnbudskapet utan att användaren begärt det.

Blockerande problem ska korrigeras före slutleverans när det är möjligt.

### Förbättringar

Förbättringar höjer kvaliteten men hindrar inte leverans. Exempel:

- rubriker kan göras mer slutsatsdrivna,
- två närliggande slides kan slås ihop,
- visuella element kan förenklas,
- detaljer kan flyttas till speaker notes eller appendix,
- stil och mellanrum kan göras mer konsekventa.

## Granskningsdimensioner

Granska minst följande dimensioner:

1. **Syfte och kärnbudskap** – går det snabbt att förstå vad presentationen vill åstadkomma?
2. **Storyline** – följer huvudpunkterna en logisk argumentationsbåge?
3. **Målgrupp och detaljnivå** – ligger språk, bevisning och teknisk nivå rätt?
4. **Slide-jobb** – har varje slide ett tydligt kommunikationsjobb och ett huvudbudskap?
5. **Rubriker** – uttrycker de poängen snarare än bara ämnet där det passar?
6. **Texttäthet** – är det som ska läsas på sliden begränsat till det mottagaren behöver se?
7. **Visualisering** – bär diagram, modeller och illustrationer information och stödjer budskapet?
8. **Redundans** – upprepas samma argument utan tydlig funktion?
9. **Konsekvens** – används samma visuella språk för samma typ av information?
10. **Källor och fakta** – är bärande påståenden spårbara och aktuella när det krävs?
11. **Redigerbarhet** – är text, former, tabeller och diagram redigerbara där runtime tillåter det?
12. **Leveransbarhet** – finns blockerande layout-, läsbarhets- eller renderingsproblem?

## Kvalitetsgate före leverans

Slutleverans får markeras som `pass` endast när:

- inga olösta blockerande problem återstår,
- kärnbudskapet är tydligt,
- storylinen fungerar för målgruppen,
- huvudflödet har rimlig längd,
- presentationen är läsbar och renderbar,
- fakta och källor har hanterats enligt source-and-tool-guiden.

Förbättringar kan finnas kvar om de inte blockerar professionell användning. De ska då redovisas som förbättringar, inte som fel.

# Transformationer

Transformation innebär att en befintlig presentation eller storyboard ändras mot ett nytt mål. Börja med att fastställa transformationsmålet och vad som måste bevaras.

## Gemensam regel: bevara kärnbudskapet

Om användaren inte uttryckligen ber om en ny ståndpunkt eller ett nytt syfte ska transformationen bevara presentationens kärnbudskap. Formulering, ordning, detaljnivå och visualisering får ändras, men den centrala innebörden får inte förskjutas.

Dokumentera före och efter:

- kärnbudskap,
- målgrupp,
- presentationsmål,
- innehållsstil,
- visuell stil,
- antal slides.

Om en begärd transformation inte kan göras utan att kärnbudskap eller nödvändiga belägg går förlorade ska modellen prioritera budskapet och förklara begränsningen.

## Kortare presentation

Exempel: 25 slides → 10 slides.

Arbetsordning:

1. Identifiera kärnbudskap och obligatoriska beslutspunkter.
2. Markera slides som `keep`, `merge`, `move-to-appendix` eller `remove`.
3. Slå ihop slides som gör samma kommunikativa jobb.
4. Flytta stödjande detalj till speaker notes eller appendix.
5. Ta bort upprepningar och sekundära exempel.
6. Kontrollera att varje återstående huvudpunkt fortfarande har tillräckligt stöd.
7. Bygg om storylinen så att den nya längden känns avsiktlig, inte avhuggen.

Målet är inte att jämnt komprimera varje slide utan att prioritera berättelsen.

## Mer visuell presentation

Arbetsordning:

1. Identifiera text som beskriver relationer, jämförelser, sekvenser, hierarkier eller data.
2. Välj ett informationsbärande slide pattern eller diagram.
3. Behåll bara den text som behövs för att tolka visualiseringen.
4. Flytta förklarande resonemang till speaker notes.
5. Använd illustration endast när former/diagram inte uttrycker budskapet lika tydligt.
6. Kontrollera att visualiseringen inte bara är dekorativ.

"Mer visuell" betyder inte "fler bilder"; det betyder att fler budskap uttrycks genom lämpliga visuella strukturer.

## Ny målgrupp

Arbetsordning:

1. Behåll presentationsmålet om användaren inte ändrar det.
2. Kartlägg vad den nya målgruppen redan kan, behöver förstå och behöver besluta.
3. Justera språk, detaljnivå, evidens och exempel.
4. Flytta tekniska eller verksamhetsmässiga detaljer till appendix när de inte längre behövs i huvudflödet.
5. Kontrollera att budskapet fortfarande är korrekt efter förenkling.

## Ny innehållsstil

Exempel: Technical → Executive.

För `Technical → Executive`:

- lyft konsekvens, beslut och rekommendation tidigare,
- reducera implementeringsdetalj i huvudflödet,
- behåll endast teknik som krävs för att förstå risk, kostnad, möjlighet eller beslut,
- flytta arkitektur- och implementationsdetaljer till appendix,
- formulera rubriker som slutsatser,
- använd färre slides när det stärker beslutsfokus.

Innehållsstilsbyte ska ändra berättelse och detaljnivå, inte bara färg och typografi.

## Ny visuell stil

Byt komposition, densitet, typografisk hierarki och visuellt uttryck utan att ändra sakbudskapet. Kontrollera att varje slide fortfarande är läsbar och att informationshierarkin inte går förlorad.

## Transformationslogg

För större transformationer ska review-artefakten kunna visa:

- begärt mål,
- vad som bevaras,
- vad som ändras,
- vilka slides som slås ihop, tas bort, flyttas eller byggs om,
- om kärnbudskapet är bevarat,
- eventuella kvarvarande risker eller förbättringar.
