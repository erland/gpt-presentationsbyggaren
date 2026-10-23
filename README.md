# Presentationsbyggaren

Presentationsbyggaren hjälper användaren att gå från idé eller källmaterial till en återupptagningsbar presentationsplan och en professionell presentation.

**Arbetsflöde:** brief → storyline → storyboard → `presentation-plan.md` → produktion → kvalitetsgranskning → export.

## Leveranslägen

- **Visual-first (standard när objektredigerbarhet inte krävs):** en separat slutlig slidebild per generering, explicit användargodkännande mellan slides och bildbaserad PPTX/PDF. En sådan PPTX är inte objektredigerbar.
- **Redigerbar PPTX:** kräver en värdmiljö med faktisk kapacitet att producera och verifiera redigerbara PowerPoint-objekt; får inte likställas med visual-first.
- **Copilot-handoff (experimentellt):** exporterad instruktion/underlag från samma presentationsplan, inte en garanti för färdig redigerbar PPTX.

`presentation-plan.md` är kanonisk presentationsstate och levereras som nedladdningsbar Markdown-fil när filskrivning stöds. Hela filen ska normalt inte skrivas ut i chatten.

Innan första visual-first-genereringen förklaras arbetsformen. En bildgenerering ger **exakt en slidebild**, aldrig collage eller flera slides. Fortsätt via exempelvis `Det ser bra ut. Skapa slide 2 enligt planen.`, `Ändra slide 1: ...` eller `Gör om slide 1 enligt planen ...`. Använd inte `Gör nästa steg` som rekommenderat godkännandekommando mellan bilder. När sista sliden godkänts paketeras leveransen.

## Arkitektur och distributioner

Migrerad till GPT Byggaren Engine **1.6.28**. Gemensam `canonical/core.md` och fyra modulära Skills: `presentationsplanering`, `bildproduktion`, `presentationsexport` och `kvalitetsgranskning`.

Fem aktiva distributioner byggs från samma kanoniska källor:
- ChatGPT Chat
- OpenAI Plugin
- Claude Project
- Claude Skills
- OpenCode

Hostförmågor varierar: filskrivning, bildgenerering, renderad förhandsvisning och PPTX/PDF måste prövas innan faktiskt resultat utlovas. Historisk ChatGPT Custom-distribution är inte ett aktivt byggmål.

CI installerar versionslåst originalmotor och verifierar källor, motor, tester, fem distributioner och projektpaket. Att distributionsbygget passerar är inte liktydigt med ett funktionellt test av bild-/presentationsgenerering.

## Status och nästa steg

Se `STATUS.md`, `project-status.yaml` och `docs/migration-1.6.28-checklist.md`. Praktiskt visual-first-flöde, faktisk PPTX/PDF-rendering och cross-model-kvalificering återstår inför release.
