# Visuella stilar

Detta dokument definierar Presentationsbyggarens v1-bibliotek för visuella stilar. Den visuella stilen styr **hur presentationen ser ut och hur informationen arrangeras**, medan innehållsstilen styr berättelse och prioritering.

## Gemensamma regler

- Visuell stil får inte ändra presentationens kärnbudskap.
- Samma visuella stil ska användas konsekvent genom presentationen, med begränsade undantag för titel-, sektions- och avslutningsslides.
- Läsbarhet, informationshierarki och tillgänglighet går före dekorativ effekt.
- Bilder, ikoner, diagram och former ska ha en kommunikativ funktion.
- Färg ska användas sparsamt för hierarki, kategorier eller betoning och inte vara enda bärare av betydelse.
- Undvik att skapa en separat mall för varje kombination av innehålls- och visuell stil.

## Auto-val av visuell stil

När användaren inte väljer visuell stil, rekommendera utifrån kontext:

| Signal | Primärt val | Vanliga alternativ |
|---|---|---|
| neutral professionell standard | `minimal-light` | `corporate` |
| mörk scen, teknik, hög kontrast | `minimal-dark` | `bold-visual` |
| etablerad verksamhets-/företagskommunikation | `corporate` | `minimal-light` |
| rapportkänsla, resonemang, redaktionellt uttryck | `editorial` | `minimal-light` |
| inspiration, keynote, få ord | `bold-visual` | `minimal-dark` |
| arkitektur, processer, modeller | `diagram-heavy` | `minimal-light` |

Om en organisationsmall eller explicit designprofil finns ska den normalt överordnas dessa standardstilar.

## minimal-light

**Syfte:** Ge en ren, modern och neutral presentation med mycket luft och tydlig hierarki.

**Principer**
- ljus bakgrund,
- hög andel whitespace,
- stor tydlig rubrikhierarki,
- få samtidiga visuella element,
- strikt alignment och konsekvent grid.

**Önskad täthet:** låg till medel.

**Föredragna mönster**
- stora slutsatsrubriker,
- enkel tvåkolumnslayout,
- enskilda diagram,
- processer med få steg,
- luftiga jämförelser.

**Undvik**
- tunga ramar runt allt,
- flera accentfärger utan funktion,
- små texter för att få plats med mer innehåll,
- dekorativa bakgrunder.

## minimal-dark

**Syfte:** Skapa ett fokuserat, modernt uttryck med hög kontrast, lämpat för skärm och scen.

**Principer**
- mörk bakgrund,
- ljus typografi med tydlig kontrast,
- begränsad accentanvändning,
- stora huvudbudskap,
- enkel geometri.

**Önskad täthet:** låg.

**Föredragna mönster**
- key-message,
- en stor visualisering,
- få datapunkter,
- tydliga sektioner,
- före/efter.

**Undvik**
- stora textmängder,
- tunna linjer med låg kontrast,
- många små diagram,
- stora ljusa ytor som bryter stilen utan syfte.

## corporate

**Syfte:** Ge ett stabilt, professionellt och organisationsnära uttryck som fungerar för verksamhets- och ledningskommunikation.

**Principer**
- konsekvent grid,
- återhållsam typografi,
- tydliga standardlayouter,
- kontrollerad användning av organisationsfärger,
- hög förutsägbarhet mellan slides.

**Önskad täthet:** medel.

**Föredragna mönster**
- titel + innehåll,
- KPI-kort,
- tabell/jämförelse,
- roadmap,
- process,
- sammanfattning.

**Undvik**
- trendig estetik som konkurrerar med budskapet,
- överdrivna effekter,
- inkonsekvent ikonografi,
- avsteg från befintlig organisationsmall när sådan finns.

## editorial

**Syfte:** Ge presentationen ett mer redaktionellt och berättande uttryck med stark typografisk identitet och varierad komposition.

**Principer**
- tydlig typografisk kontrast,
- asymmetri kan användas kontrollerat,
- citat, korta textstycken och bilder får större roll,
- varje slide kan ha mer individuell komposition men följer gemensamt grid och typografisystem.

**Önskad täthet:** låg till medel.

**Föredragna mönster**
- citat,
- bild + resonemang,
- stora siffror,
- sektionsöppnare,
- redaktionella jämförelser.

**Undvik**
- traditionella bulletväggar,
- för många boxar,
- stereotyp magasinestetik utan koppling till innehållet,
- inkonsekvent typografi.

## bold-visual

**Syfte:** Maximera genomslag och minne i presentationer som framförs muntligt och där varje slide ska kunna uppfattas snabbt.

**Principer**
- mycket stora rubriker,
- ett dominerande visuellt element,
- stark skala och kontrast,
- korta texter,
- tydlig rytm mellan slides.

**Önskad täthet:** mycket låg.

**Föredragna mönster**
- helbild/illustration med kort budskap,
- en stor siffra,
- statement-slide,
- before-after,
- call-to-action.

**Undvik**
- små etiketter,
- komplexa tabeller,
- flera likvärdiga visuella fokus,
- generiska bilder som bara fyller yta.

## diagram-heavy

**Syfte:** Göra komplexa relationer, processer, arkitektur och modeller centrala och lättare att läsa genom ett konsekvent diagramspråk.

**Principer**
- diagram är primär informationsbärare när relationer är kärnan,
- använd konsekvent symbolik, former, linjer och nivåer,
- skapa tydlig läsriktning,
- reducera modellen till den detaljnivå presentationens syfte kräver,
- komplettera diagram med en tydlig slutsatsrubrik.

**Önskad täthet:** medel till hög, men strukturerad.

**Föredragna mönster**
- architecture,
- process,
- hierarchy,
- timeline,
- roadmap,
- 2x2-matrix,
- system-/dataflöde.

**Undvik**
- "spaghetti diagrams",
- blandade symbolsystem,
- onödigt dekorativa ikoner,
- att försöka visa hela modellen på samma slide,
- för små etiketter.
