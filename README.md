# Presentationsbyggaren

Presentationsbyggaren hjälper användaren från idé eller källmaterial till en återupptagningsbar presentationsplan och därefter till visuella eller redigerbara presentationsspår.

Kärnflödet är:

**brief → storyline → storyboard → presentation-plan → visual-first och/eller Copilot-handoff → kvalitetsgranskning**

## 0.3

Version 0.3 ändrar huvudarkitekturen:

- `presentation-plan.md` är kanonisk sparbar masterartefakt,
- visual-first är huvudspår när visuell kvalitet prioriteras framför objektredigerbarhet,
- 1–2 anchor slides etablerar formspråket innan resten genereras,
- viktiga slides genereras normalt en i taget; små batcher får vara högst 2–4,
- hela presentationen genereras inte i en enda bildprompt,
- bildbaserad PPTX + PDF är visual-first-leveransen,
- `copilot-handoff.docx`/PDF + `copilot-prompt.md` är spåret för redigerbar presentation via Copilot.

## Aktiverade runtimes

- ChatGPT Chat
- ChatGPT Custom

## Fortsättning

Läs `project-status.yaml` och `docs/development-plan.md`. Nästa rekommenderade aktivitet är ett praktiskt A/B-test med samma presentationsplan: visual-first-resultat jämfört med presentation skapad från Copilot-handoff.
