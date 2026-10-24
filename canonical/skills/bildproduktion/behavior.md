# bildproduktion

## Visual-first

När redigerbarhet inte krävs är visual-first normal huvudväg. Följ `knowledge/visual-first-workflow.md`.

- Skapa först 1–2 anchor slides som etablerar formspråket.
- **Varje bildgenerering ska skapa exakt en bild av en slide.** Standardflödet består av en bildgenerering (ren bakgrund), följd av en **bildredigering i en senare användartur** (final med integrerad text).
- Generera aldrig flera slides, varianter, thumbnails, collage, kontaktkartor eller moodboards på samma canvas.
- Även enkla slides genereras en i taget; flera delar inom samma slide ska vara få, stora och sammanhängande.
- **Innan första bildgenereringen**, informera användaren om arbetsformen:
  - om bilden är bra: skriv t.ex. `Det ser bra ut. Skapa slide 2 enligt planen.`
  - om bilden behöver ändras: skriv t.ex. `Ändra slide 1: ...`
  - om bilden ska göras om: skriv t.ex. `Gör om slide 1 enligt planen, men ...`
- Mellan bildgenerationer ska du inte rekommendera `Gör nästa steg`; användaren ska explicit ange om den föregående sliden är godkänd och vilken slide som ska skapas härnäst.
- När användaren skriver `Det ser bra ut. Skapa slide X enligt planen.`, markera föregående **finalbild** som `approved` och börja med ren bakgrund för slide X. Efter bakgrundsgenereringen ska assistenten **stanna** i `background_ready`. Finalbilden skapas först efter nästa uttryckliga användarmeddelande; gå aldrig vidare till nästa slide dessförinnan.
- Uppdatera renderingsstatusen i `presentation-plan.md` så att framsteg kan återupptas.
- Bakgrundsgenereringen får inte innehålla text, textrutor, textplatshållare, tonplattor eller textrelaterade dekorativa ramar. Ge modellen frihet att skapa en fullvärdig ren komposition.
- Slutbilden skapas genom **explicit redigering av den faktiskt sparade originalbakgrunden**, inte genom ny fristående eller referensstyrd generering; den exakta texten och textnära effekter (typografi, kontrast, skuggor, toningar, plattor om motiverat) integreras **först i detta steg**. Granska att texten är korrekt; reparera samma slide vid behov.
- Bevara båda bildfilerna och strukturerad text i projekt-ZIP. För enbart textändring: återanvänd samma rena bakgrund och generera ny finalbild, utan att ändra godkänd originalbakgrund. Bildgeneratorn kan trots referens ge stil- och layoutvariationer; lova inte identisk pixelkomposition.
- `scripts/render_slide_layers.py` är ett valfritt deterministiskt specialläge, **inte standardflödet**. Äldre godkända slides utan ren bakgrund bevaras oförändrade.
- Slutlig PPTX får bestå av färdigrenderade helslidebilder och behöver inte vara objektredigerbar.
- Skapa även PDF när runtime stöder det.


## Kontrollpunkt före finalbild

Gör **ett bildgenereringsanrop och, i nästa användartur, ett bildredigeringsanrop** per slide, aldrig en bild som visar båda stegen. Det första anropet ska efterfråga enbart den färdiga bakgrundsscenen i 16:9, inte ett diagram eller en illustration av presentationsarbetsflödet. Bakgrundsprompten får inte innehålla citat av rubrik- eller stödtext, eller beskrivningar av projektfiler, testresultat eller processteg. Inga textbehållare, rutor, särskilda tonplattor eller platshållare får förberedas.

Granska den **faktiskt returnerade bilden** innan nästa anrop. Kontrollera att den är en enda textfri scen utan färdiga textbehållare, att den inte är en jämförelse-/processinfografik och att kompositionen är användbar. Om kontrollen fallerar: gör om **endast bakgrundssteget**, återanvänd inte den felaktiga bilden. Bakgrunden ska materialiseras till en faktisk fil, inte enbart visas i chatten. Beräkna SHA-256 och spara `background_gate` med `checked: true`, `text_free: true`, `no_text_containers: true`, `single_scene: true`, `sha256` från den sparade filen.

Först därefter får assistenten skicka den sparade bakgrunden som **direkt redigeringsunderlag** i ett separat bildredigeringsanrop med exakt text och eventuell textnära grafisk utformning. Om värdmiljön inte kan skicka med referensbilden ska assistenten rapportera begränsningen och inte påstå att referensbaserad generering ägt rum. Ingen automatiskt påhittad PASS-rapport i den genererade bilden. Användaren godkänner slutbilden; bakgrundsgranskningen är en intern kvalitetsgrind.

## Steg 2 – explicit bildredigering

Använd **bildredigeringsoperationen** i bildverktyget; skapa inte ett nytt motiv från en textprompt med bakgrunden endast som inspirationsreferens. Peka ut den faktiska ursprungliga, rena bakgrunden från steg 1 som redigeringsunderlag och instruera kort: ”Redigera denna befintliga bild. Lägg till exakt text: [text]. Behåll motiv, komposition och färger så oförändrade som möjligt. Integrera typografi och eventuella texteffekter naturligt. Skapa inte en ny miljö.” Verifiera med faktiskt verktygsresultat att originalbilden var redigeringsunderlaget. Att en bild är lik originalet räcker inte.

Vid textändring: utgå från **samma textfria originalbakgrund**, aldrig från den tidigare textförsedda finalbilden. Bevara tidigare finalversion och gör om slutbildens godkännande. Om bildverktyget bara gör text-till-bild eller inte kan välja avsett original som redigeringsunderlag: stoppa och redovisa PARTIAL, inte PASS.

Spara för nya slides `workflow_version: 2`, `final_from_background` (samma sökväg som `background`), och under `generation`: `final_operation: edit_original_background`, `edit_source`, `edit_source_sha256`, samt `edit_confirmed` som true **bara om utförd redigering med just originalet är verifierad**. Vid textrevision kan `revision_of_text` peka på föregående textversion. Validatorn kontrollerar deklarationer och checksummor, men kan inte tekniskt bevisa modellens interna redigeringsbeteende.

## Två promptar och två separata användarmeddelanden (obligatorisk standard)

### Moment A – bakgrundsgenerering

Bygg en **fristående** prompt från `templates/background-generation.md.tpl`. Parametrar: `visual_concept` och `visual_style`. Rubrik, `exact_text`, textplacering och senare redigeringsinstruktioner får **inte** ingå i Prompt A. Anropa bildgenereringsverktyget en gång för endast denna bakgrund; kombinera aldrig Moment A och Moment B i ett uppdrag eller genererat bildmontage.

Efter faktiskt utförd granskning och sparad fil med SHA-256: sätt `status: background_ready` (inte `final_ready`). **Avsluta detta användarsvar**. Säg kort: ”Bakgrunden är skapad. Skriv **Lägg på texten enligt planen** för att redigera just den här originalbilden.” Kör INTE textredigeringen i samma assistenttur, även om assistenten redan känner rubriken. Ingen automatisk fortsättning eller implicit godkännande. Ett nytt användarmeddelande krävs.

### Moment B – explicit textredigering

När ett **nytt användarmeddelande** begär `Lägg på texten enligt planen`, använd `templates/text-overlay-edit.md.tpl` och ersätt endast `exact_text` med slideplanens exakta text. Prompt B får inte upprepa motiv, färger, rum, personer eller bakgrundsgenereringsprompten: sådant finns i den sparade bilden.

Välj `slides/slide-NN-background.png` som **faktisk bildindata** till bildverktygets redigeringsfunktion. Kontrollera innan anropet att originalets hash stämmer och att rätt bild verkligen bifogas/valts i verktygsoperationen; en sökväg i prompttext är **inte** i sig en bifogad bild. Kontrollera resultatet och tillgänglig verktygsproveniens efteråt. `generation.edit_confirmed` sätts till true endast om verklig redigering med just originalbilden kan verifieras. Avsaknad av metadata är inte i sig bevis för utebliven redigering, men får inte tolkas som PASS. Om värden inte kan bifoga/välja originalbilden: stoppa med **PARTIAL**, skapa inte en ny liknande bild och erbjud det redan tillgängliga deterministiska textlagerläget som uttryckligt alternativ.

Vid senare textändring: kör ett nytt Moment B med `slides/slide-NN-background.png` som bildindata, **aldrig** föregående `final`; bevara tidigare final som separat version och nollställ dess godkännandestatus. Användaren godkänner slutbilden efter redigering.

Ett separat indata-/utdatakontrakt per moment gäller: A tar motiv/stil och ger kontrollerat `background.png` + SHA-256; B tar den verifierade originalbildens bytes och exakt text och ger en ny `final-vN.png`. Tester får aldrig kallas PASS enbart för att resultatbilder ser lika ut.
