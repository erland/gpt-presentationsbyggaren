# bildproduktion

## Visual-first

När redigerbarhet inte krävs är visual-first normal huvudväg. Följ `knowledge/visual-first-workflow.md`.

- Skapa först 1–2 anchor slides som etablerar formspråket.
- **Varje bildgenerering ska skapa exakt en bild av en slide.** Standardflödet består av två separata bildgenereringar per slide: först en ren bakgrund, sedan en finalbild med text där den rena bakgrunden används som bildreferens.
- Generera aldrig flera slides, varianter, thumbnails, collage, kontaktkartor eller moodboards på samma canvas.
- Även enkla slides genereras en i taget; flera delar inom samma slide ska vara få, stora och sammanhängande.
- **Innan första bildgenereringen**, informera användaren om arbetsformen:
  - om bilden är bra: skriv t.ex. `Det ser bra ut. Skapa slide 2 enligt planen.`
  - om bilden behöver ändras: skriv t.ex. `Ändra slide 1: ...`
  - om bilden ska göras om: skriv t.ex. `Gör om slide 1 enligt planen, men ...`
- Mellan bildgenerationer ska du inte rekommendera `Gör nästa steg`; användaren ska explicit ange om den föregående sliden är godkänd och vilken slide som ska skapas härnäst.
- När användaren skriver `Det ser bra ut. Skapa slide X enligt planen.`, markera föregående **finalbild** som `approved` och börja med ren bakgrund för slide X. Efter enbart bakgrundsgenereringen ska samma slide fortsätta med finalbilden, inte gå vidare till nästa slide.
- Uppdatera renderingsstatusen i `presentation-plan.md` så att framsteg kan återupptas.
- Bakgrundsgenereringen får inte innehålla text, textrutor, textplatshållare, tonplattor eller textrelaterade dekorativa ramar. Ge modellen frihet att skapa en fullvärdig ren komposition.\n- Slutbilden skapas genom bildredigering eller referensstyrd generering av **den sparade bakgrunden**; den exakta texten och textnära effekter (typografi, kontrast, skuggor, toningar, plattor om motiverat) integreras **först i detta steg**. Granska att texten är korrekt; reparera samma slide vid behov.\n- Bevara båda bildfilerna och strukturerad text i projekt-ZIP. För enbart textändring: återanvänd samma rena bakgrund och generera ny finalbild, utan att ändra godkänd originalbakgrund. Bildgeneratorn kan trots referens ge stil- och layoutvariationer; lova inte identisk pixelkomposition.\n- `scripts/render_slide_layers.py` är ett valfritt deterministiskt specialläge, **inte standardflödet**. Äldre godkända slides utan ren bakgrund bevaras oförändrade.
- Slutlig PPTX får bestå av färdigrenderade helslidebilder och behöver inte vara objektredigerbar.
- Skapa även PDF när runtime stöder det.


## Kontrollpunkt före finalbild

Gör två **separata** bildgenereringsanrop per slide, aldrig en bild som visar båda stegen. Det första anropet ska efterfråga enbart den färdiga bakgrundsscenen i 16:9, inte ett diagram eller en illustration av presentationsarbetsflödet. Bakgrundsprompten får inte innehålla citat av rubrik- eller stödtext, eller beskrivningar av projektfiler, testresultat eller processteg. Inga textbehållare, rutor, särskilda tonplattor eller platshållare får förberedas.

Granska den **faktiskt returnerade bilden** innan nästa anrop. Kontrollera att den är en enda textfri scen utan färdiga textbehållare, att den inte är en jämförelse-/processinfografik och att kompositionen är användbar. Om kontrollen fallerar: gör om **endast bakgrundssteget**, återanvänd inte den felaktiga bilden. Bakgrunden ska materialiseras till en faktisk fil, inte enbart visas i chatten. Beräkna SHA-256 och spara `background_gate` med `checked: true`, `text_free: true`, `no_text_containers: true`, `single_scene: true`, `sha256` från den sparade filen.

Först därefter får assistenten använda den sparade bakgrunden som **faktisk bildreferens** i ett separat slutbildsanrop med exakt text och eventuell textnära grafisk utformning. Om värdmiljön inte kan skicka med referensbilden ska assistenten rapportera begränsningen och inte påstå att referensbaserad generering ägt rum. Ingen automatiskt påhittad PASS-rapport i den genererade bilden. Användaren godkänner slutbilden; bakgrundsgranskningen är en intern kvalitetsgrind.
