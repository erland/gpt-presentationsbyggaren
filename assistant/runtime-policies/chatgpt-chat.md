# ChatGPT Chat runtime policy

Denna policy anpassar Presentationsbyggaren till ChatGPT Chat utan att ändra canonical metodik.

## Start

- Läs `assistant/instructions.md` som styrande runtimeinstruktion.
- Använd `assistant/runtime-contract.json` som maskinläsbar snapshot av canonical kontrakt.
- Läs Knowledge-filer först när de behövs för aktuell fas eller när canonical instruktionen hänvisar till dem.
- Om användaren bifogar källmaterial ska det användas som primär källa för presentationens innehåll.

## Arbetsflöde

Följ samma fasordning som canonical instruktionen. Kommandot **Gör nästa steg** ska utföra nästa ofullbordade fas eller delmoment och leverera ett konkret resultat i samma svar.

## Artefakter

- **Presentation Plan är obligatorisk som faktisk fil.** När planeringsfasen är klar ska runtime skapa `presentation-plan.md` med tillgänglig filskrivnings- eller kodexekveringsförmåga och ge användaren en nedladdningsbar fil/länk. Det räcker inte att bara visa planen inline, sammanfatta den eller säga att den är skapad.
- Gå inte vidare till första slidebilden förrän `presentation-plan.md` faktiskt har skapats som fil när runtime har filskrivningsförmåga.
- Om filskrivning verkligen saknas ska begränsningen anges uttryckligt och hela planen får då lämnas inline som fallback; påstå inte att en nedladdningsbar fil har skapats.
- Skapa en faktisk `.pptx` när full presentationsleverans efterfrågas och runtimeverktyget kan göra det.
- När användaren vill kunna redigera text ska `hybrid-slide` bevara presentationscopy som native PowerPoint-text; grafik får ligga i bildbakgrunden.
- Före varje bildgenerering ska Chat-runtime läsa slidens `Render mode`. Om den är `hybrid-slide` får `Visible text` inte skickas som bildinnehåll. Bildprompten måste explicit förbjuda läsbar text, bokstäver, ord, siffror, etiketter, pseudo-text och textliknande symboler.
- En hybrid-bild som innehåller sådan text får inte godkännas eller bindas som `Approved asset`; samma slide ska göras om.
- Leverera övriga stödartefakter endast när de hjälper användaren eller behövs för återupptagning/validering.
- Om PPTX-rendering inte är tillgänglig ska storyboard och renderingsspecifikation levereras och begränsningen anges tydligt; presentationen får inte påstås vara skapad.

## Verktyg

- Aktuella externa fakta ska verifieras med webbsökning när det behövs.
- Bildgenerering används endast när illustration tillför informationsvärde som inte lika bra kan uttryckas med redigerbara former eller diagram.
- Numeriska slutsatser ska kontrolleras med dataanalys när sådant stöd finns.

## Runtime-hygiene

Utvecklingsplan, projektstatus och andra utvecklingsartefakter ska inte krävas för normal användning av Chat ZIP-distributionen.
