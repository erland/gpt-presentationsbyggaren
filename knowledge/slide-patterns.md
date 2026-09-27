# Slide patterns

Detta dokument definierar Presentationsbyggarens v1-bibliotek för slide patterns. Ett pattern beskriver **vilket kommunikationsjobb en slide ska göra**. Det är inte en färdig PowerPoint-layout.

## Urvalsregler

1. Börja med slidens huvudbudskap och syfte i storylinen.
2. Välj det enklaste pattern som gör budskapet tydligt.
3. Använd normalt ett primärt pattern per slide. Ett sekundärt element får stödja men inte konkurrera.
4. Välj inte pattern för variationens skull. Samma pattern får återkomma när samma kommunikationsjobb återkommer.
5. Om två patterns verkar likvärdiga, välj det som kräver minst text och minst visuell komplexitet.
6. Pattern styr informationsarkitektur; vald visuell stil styr uttryck och komposition.

## Pattern-bibliotek

### `title`
**Kommunikationssyfte:** öppna presentationen och etablera ämne, avsändare eller central fråga.

**Använd när:** publiken behöver orienteras innan argumentationen börjar.

**Undvik när:** sliden egentligen behöver bära ett sakbudskap; då är `key-message` bättre.

### `section-divider`
**Kommunikationssyfte:** markera ett tydligt skifte i berättelsen.

**Använd när:** en längre presentation byter fas, perspektiv eller frågeställning.

**Undvik när:** presentationen är kort eller skiftet redan är självklart.

### `key-message`
**Kommunikationssyfte:** göra en slutsats eller central idé omedelbart tydlig.

**Använd när:** en enda poäng är viktigare än stödjande detalj.

**Undvik när:** mottagaren behöver förstå relationer, jämförelser eller sekvens; välj då ett mer specifikt pattern.

### `problem`
**Kommunikationssyfte:** beskriva ett problem, dess omfattning och varför det spelar roll.

**Använd när:** berättelsen behöver skapa en tydlig anledning till förändring.

**Undvik när:** problemet redan är etablerat och nästa fråga är konsekvens, val eller lösning.

### `before-after`
**Kommunikationssyfte:** visa en meningsfull förändring mellan nuläge och framtida läge.

**Använd när:** skillnaden mellan två tillstånd är själva budskapet.

**Undvik när:** förändringen har flera steg eller tidsberoenden; välj `process`, `timeline` eller `roadmap`.

### `comparison`
**Kommunikationssyfte:** synliggöra skillnader och trade-offs mellan två eller flera alternativ.

**Använd när:** samma dimensioner kan jämföras konsekvent.

**Undvik när:** alternativen inte är jämförbara på samma kriterier eller när beslutet kräver en tvådimensionell positionering; överväg `2x2-matrix`.

### `2x2-matrix`
**Kommunikationssyfte:** positionera objekt längs två betydelsefulla dimensioner för att synliggöra grupper, prioriteringar eller trade-offs.

**Använd när:** båda axlarna har tydlig betydelse och placeringen ger en faktisk insikt.

**Undvik när:** axlarna är godtyckliga, skalorna oklara eller en vanlig jämförelse räcker.

### `three-pillars`
**Kommunikationssyfte:** visa ett litet antal parallella, samverkande delar som tillsammans bär en helhet.

**Använd när:** 3–5 jämbördiga områden eller principer behöver förstås samtidigt.

**Undvik när:** delarna egentligen har sekvens, hierarki eller beroenden.

### `hierarchy`
**Kommunikationssyfte:** visa nivåer, gruppering eller över-/underordning.

**Använd när:** struktur och abstraktionsnivå är viktigare än flöde.

**Undvik när:** relationerna främst är tidsmässiga eller processuella.

### `process`
**Kommunikationssyfte:** visa en ordnad följd av aktiviteter, ansvar eller transformationer.

**Använd när:** mottagaren behöver förstå hur något går till och i vilken ordning.

**Undvik när:** tidpunkter och milstolpar är viktigare än logisk sekvens; välj `timeline` eller `roadmap`.

### `timeline`
**Kommunikationssyfte:** visa händelser, utveckling eller milstolpar längs faktisk eller relativ tid.

**Använd när:** kronologi är central för förståelsen.

**Undvik när:** sliden främst ska visa prioriterade initiativ och framtida genomförande; välj `roadmap`.

### `roadmap`
**Kommunikationssyfte:** visa hur prioriterade initiativ eller förmågor utvecklas över tid mot en målbild.

**Använd när:** publiken behöver förstå riktning, etapper och ordningsföljd för genomförandet.

**Undvik när:** sliden bara återger historik eller datum utan strategisk progression.

### `architecture`
**Kommunikationssyfte:** visa komponenter, ansvar, gränser och viktiga relationer i en teknisk eller verksamhetsmässig struktur.

**Använd när:** relationerna mellan delar är huvudbudskapet.

**Undvik när:** hela modellen inte behövs för budskapet. Reducera hellre vy än att visa allt.

### `numbers-kpi`
**Kommunikationssyfte:** låta ett fåtal siffror eller nyckeltal bära slutsatsen.

**Använd när:** data är centrala och kan sammanfattas utan att dölja relevant kontext.

**Undvik när:** många datapunkter behöver jämföras över tid eller kategorier; använd lämpligt diagram i stället för KPI-kort.

### `case-example`
**Kommunikationssyfte:** konkretisera ett abstrakt resonemang med ett representativt exempel eller scenario.

**Använd när:** publiken behöver se hur en princip fungerar i praktiken.

**Undvik när:** exemplet är anekdotiskt och riskerar att framstå som generellt bevis.

### `quote`
**Kommunikationssyfte:** ge röst, perspektiv eller auktoritativ formulering som stödjer berättelsen.

**Använd när:** källan och formuleringen tillför något som en parafras inte gör.

**Undvik när:** citatet bara används som dekor eller saknar tydlig källa.

### `recommendation`
**Kommunikationssyfte:** presentera en rekommenderad riktning och den viktigaste rationalen.

**Använd när:** analysen ska mynna ut i ett tydligt handlingsförslag.

**Undvik när:** beslutskriterier eller alternativ fortfarande behöver etableras; använd först `comparison` eller `decision`.

### `decision`
**Kommunikationssyfte:** tydliggöra vilket beslut som behövs, vilka alternativ som finns och vad beslutet påverkar.

**Använd när:** mottagaren förväntas välja, godkänna eller prioritera.

**Undvik när:** sliden bara innehåller en rekommendation utan verkligt beslutstillfälle.

### `summary`
**Kommunikationssyfte:** knyta ihop flera tidigare budskap till en liten mängd slutsatser.

**Använd när:** publiken behöver återankring före beslut, diskussion eller avslutning.

**Undvik när:** den bara upprepar rubriker ordagrant utan syntes.

### `call-to-action`
**Kommunikationssyfte:** avsluta med en konkret handling, nästa aktivitet eller önskad respons.

**Använd när:** presentationen ska leda till ett tydligt nästa steg.

**Undvik när:** mottagaren inte förväntas agera eller när beslutet redan fångas bättre av `decision`.

## Konfliktlösning mellan närliggande patterns

- `before-after` vs `comparison`: välj `before-after` när det är **samma objekt över förändring**; `comparison` när det är **olika alternativ samtidigt**.
- `timeline` vs `roadmap`: välj `timeline` för **kronologi**; `roadmap` för **avsiktlig framtida progression**.
- `process` vs `architecture`: välj `process` när **ordning/överföring** är kärnan; `architecture` när **struktur/relationer** är kärnan.
- `recommendation` vs `decision`: välj `recommendation` när assistenten **föreslår riktning**; `decision` när mottagaren **behöver fatta ett explicit val**.
- `key-message` vs `summary`: välj `key-message` för **en central poäng**; `summary` för **syntes av flera redan etablerade poänger**.

## Kvalitetskontroll

Ett valt pattern är lämpligt om:
- det går att förklara varför just detta kommunikationsjobb behövs i storylinen,
- det kan uttrycka slidens huvudbudskap utan onödig text,
- det inte duplicerar föregående slide,
- det går att gestalta konsekvent inom vald visuell stil.
