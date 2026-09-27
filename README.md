# Presentationsbyggaren

Presentationsbyggaren hjälper användaren från idé eller källmaterial till en återupptagningsbar presentationsplan och därefter till en visuellt driven presentation.

Kärnflödet är:

**brief → storyline → storyboard → presentation-plan → visual-first → kvalitetsgranskning → PPTX/PDF**

## 0.3.1

Visual-first är huvudspåret när visuell kvalitet prioriteras framför objektredigerbarhet.

Produktionsregler:

- `presentation-plan.md` är kanonisk sparbar masterartefakt,
- 1–2 anchor slides etablerar formspråket,
- **exakt en slide genereras per bildgenerering**,
- collage, kontaktkartor, moodboards, storyboardark och thumbnail-grids är blockerande fel,
- flera delar inom samma slide ska vara få, stora och sammanhängande,
- före varje bildgenerering får användaren veta vilken slide som skapas och att skriva **Gör nästa steg** när bilden är klar,
- `presentation-plan.md` håller persistent renderingstatus och pekar ut exakt en `next` slide,
- efter sista godkända slide är nästa steg paketering till bildbaserad PPTX och PDF.

Copilot-handoff finns kvar som ett **kompletterande/experimentellt** spår för den som vill prova att skapa en redigerbar presentation från samma plan.

## Aktiverade runtimes

- ChatGPT Chat
- ChatGPT Custom

## Fortsättning

Läs `project-status.yaml` och `docs/development-plan.md`. Nästa rekommenderade aktivitet är ett praktiskt visual-first-test där presentationen skapas en slide i taget och `Gör nästa steg` används mellan bildgenerationerna.
