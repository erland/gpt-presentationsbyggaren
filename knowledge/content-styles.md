# Innehållsstilar

Detta dokument definierar Presentationsbyggarens v1-bibliotek för innehållsstilar. Innehållsstilen styr **hur berättelsen prioriteras och uttrycks**. Den visuella stilen väljs separat enligt `visual-styles.md`.

## Gemensamma regler

- Innehållsstil och visuell stil är oberoende dimensioner.
- En innehållsstil får påverka disposition, detaljnivå, rubriktyp, slide-täthet och föredragna mönster, men ska inte hårdkoda färger, typsnitt eller dekorativ estetik.
- Ett huvudbudskap per slide är normalfallet.
- Rubriker bör, när det är lämpligt, uttrycka slutsats eller poäng snarare än bara ämne.
- Material som inte behövs för huvudberättelsen flyttas till speaker notes eller appendix.
- Stilen är en styrprofil, inte en absolut mall. Anpassa efter syfte, målgrupp och källmaterial.

## auto

**Syfte:** Välja eller rekommendera den innehållsstil som bäst stöder briefens syfte, målgrupp och önskade effekt.

**Principer**
- Prioritera mål och publik före materialets ursprungliga struktur.
- Välj den minsta stilförskjutning som tydligt förbättrar kommunikationen.
- Motivera valet kort när användaren inte redan har valt stil.
- Fråga bara när två eller flera stilval skulle leda till väsentligt olika affärsmässiga resultat och briefen inte avgör valet.

**Önskad täthet:** ärvs från vald stil.

**Föredragna mönster:** ärvs från vald stil.

**Undvik**
- att välja stil enbart efter dokumenttyp,
- att kombinera flera innehållsstilar utan tydligt skäl,
- att fråga användaren om sådant som rimligen kan härledas ur briefen.

### Auto-heuristik

| Signal i briefen | Primärt val | Vanliga alternativ |
|---|---|---|
| beslut, ledningsgrupp, prioritering, kort tid | `executive` | `strategy`, `consulting` |
| nuläge, målbild, vägval, roadmap | `strategy` | `executive`, `consulting` |
| analys, rekommendation, strukturerad argumentation | `consulting` | `executive`, `strategy` |
| arkitektur, teknik, implementation, beroenden | `technical` | `teaching`, `consulting` |
| lärande, introduktion, förståelse | `teaching` | `visual-storytelling` |
| gemensamt arbete, övningar, diskussion | `workshop` | `teaching` |
| scenframträdande, inspiration, få ord, stark progression | `visual-storytelling` | `executive`, `teaching` |

## executive

**Syfte:** Hjälpa beslutsfattare att snabbt förstå läget, konsekvenserna, alternativen och vad som behöver beslutas eller göras.

**Principer**
- Lägg kärnbudskap och konsekvens tidigt.
- Använd slutsatsdrivna rubriker.
- Prioritera beslut, risker, effekter och rekommenderade nästa steg.
- Komprimera stödjande resonemang och flytta detaljbevis till appendix.

**Önskad täthet:** låg till medel. Ofta 6–10 huvudslides för en kort presentation.

**Föredragna mönster**
- key-message
- recommendation
- decision
- comparison
- numbers-kpi
- roadmap
- summary

**Undvik**
- långa metodbeskrivningar,
- tekniska detaljer utan beslutsrelevans,
- många likvärdiga budskap på samma slide,
- rubriker som bara namnger ämnet.

## strategy

**Syfte:** Förklara varför förändring behövs, vilken riktning som föreslås och hur man tar sig från nuläge till målbild.

**Principer**
- Bygg en tydlig båge från kontext och nuläge till målbild och vägval.
- Synliggör antaganden, prioriteringar och beroenden.
- Skilj på mål, förmågor/initiativ och genomförande.
- Låt roadmapen vara en konsekvens av strategin, inte en aktivitetslista utan rationale.

**Önskad täthet:** medel.

**Föredragna mönster**
- problem
- before-after
- three-pillars
- hierarchy
- comparison
- roadmap
- timeline
- recommendation

**Undvik**
- aktivitetslistor utan strategisk koppling,
- målbild utan beskrivet gap,
- roadmap utan prioriteringslogik,
- för många parallella modeller.

## consulting

**Syfte:** Presentera en strukturerad analys där varje slide bidrar med en tydlig slutsats i en logisk argumentationskedja.

**Principer**
- Använd pyramidprincipen: slutsats först, stöd därefter.
- Gör argumentationen ömsesidigt avgränsad så långt möjligt.
- Visa jämförelser och trade-offs explicit.
- Var datadriven när källmaterialet tillåter det.

**Önskad täthet:** medel till hög, men visuellt disciplinerad.

**Föredragna mönster**
- key-message
- comparison
- 2x2-matrix
- numbers-kpi
- process
- recommendation
- summary

**Undvik**
- dekorativa element som inte bär information,
- resonemang som bara finns i talet men saknar stöd på sliden,
- överlastade matriser,
- slutsatser utan spårbart underlag.

## technical

**Syfte:** Göra tekniska strukturer, relationer, flöden och beslut begripliga utan att förlora nödvändig precision.

**Principer**
- Prioritera arkitektur, beroenden, gränssnitt, dataflöden och trade-offs.
- Visa först översikt, därefter fördjupning.
- Definiera symbolik och nivåer konsekvent.
- Använd text där precision krävs, men låt diagram bära relationer.

**Önskad täthet:** medel till hög.

**Föredragna mönster**
- architecture
- process
- hierarchy
- comparison
- before-after
- timeline
- numbers-kpi

**Undvik**
- diagram utan läsriktning eller förklaring,
- implementationdetaljer som inte stöder huvudbudskapet,
- blandning av abstraktionsnivåer i samma vy,
- generiska illustrationer när ett tekniskt diagram är tydligare.

## teaching

**Syfte:** Hjälpa en publik att förstå och minnas ett ämne genom en pedagogisk progression.

**Principer**
- Gå från bekant till nytt och från enkelt till mer komplext.
- Introducera ett begrepp i taget när ämnet är nytt.
- Använd exempel och återkoppling till tidigare steg.
- Bygg in sammanfattningar vid naturliga brytpunkter.

**Önskad täthet:** låg till medel.

**Föredragna mönster**
- section-divider
- process
- case-example
- before-after
- comparison
- summary
- key-message

**Undvik**
- att introducera många nya begrepp samtidigt,
- textväggar,
- komplexa diagram innan mental modell är etablerad,
- att bara komprimera en rapport till bullets.

## workshop

**Syfte:** Stödja aktivt deltagande, gemensam analys och konkreta beslut eller resultat under en faciliterad session.

**Principer**
- Var tydlig med uppgift, tid, förväntat resultat och nästa steg.
- Varva kort kontext med aktivitet.
- Gör instruktioner direkt genomförbara.
- Använd slides som arbetsyta och orientering, inte som manus.

**Önskad täthet:** låg.

**Föredragna mönster**
- section-divider
- key-message
- process
- comparison
- 2x2-matrix
- decision
- summary

**Undvik**
- långa informationsblock mellan övningar,
- otydliga frågor,
- flera aktiviteter på samma slide,
- aktiviteter utan definierad output.

## visual-storytelling

**Syfte:** Skapa en stark muntlig och visuell berättelse där bilder, enkla former och korta budskap driver progressionen.

**Principer**
- En idé per slide med tydlig rytm mellan slides.
- Använd kontrast, sekvenser och visuella metaforer när de verkligen förklarar något.
- Låt talaren bära mer av detaljerna.
- Prioritera igenkänning och minne framför komplett dokumentation.

**Önskad täthet:** mycket låg.

**Föredragna mönster**
- title
- key-message
- before-after
- case-example
- quote
- process
- call-to-action

**Undvik**
- långa punktlistor,
- tabeller med mycket detaljer,
- flera diagram på samma slide,
- dekorativa AI-bilder utan kommunikativ funktion.
