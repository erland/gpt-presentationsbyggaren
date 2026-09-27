# Presentationsbyggaren

Presentationsbyggaren hjälper användaren från idé eller källmaterial till en återupptagningsbar presentationsplan och därefter till en visuellt driven presentation.

Kärnflödet är:

**brief → storyline → storyboard → presentation-plan.md → visual-first → kvalitetsgranskning → PPTX/PDF**

## 0.3.2

Visual-first är huvudspåret när visuell kvalitet prioriteras framför objektredigerbarhet.

### Planering

- `presentation-plan.md` är kanonisk masterartefakt.
- När runtime kan skapa filer levereras planen som **nedladdningsbar Markdown-fil**.
- Hela planen visas inte direkt i chatten om användaren inte uttryckligen ber om det.

### Bildproduktion

Innan första bilden förklarar Presentationsbyggaren hur flödet fungerar.

Efter varje bild används ett explicit kommando, exempelvis:

`Det ser bra ut. Skapa slide 3 enligt planen.`

Alternativt:

- `Ändra slide 2: gör huvudillustrationen större.`
- `Gör om slide 2 enligt planen, men utan ikoner.`

`Gör nästa steg` används inte som rekommenderad kontrollsignal mellan bildgenerationer.

Övriga regler:

- exakt en slutlig slidebild per bildgenerering,
- collage, kontaktkartor, moodboards, storyboardark och thumbnail-grids underkänns,
- planen kan stå i vänteläge efter en genererad slide tills användaren godkänner eller begär ändring,
- efter sista godkända slide paketeras presentationen till bildbaserad PPTX och PDF.

Copilot-handoff finns kvar som kompletterande/experimentellt spår.

## Aktiverade runtimes

- ChatGPT Chat
- ChatGPT Custom

## Fortsättning

Nästa rekommenderade aktivitet är ett praktiskt visual-first-test med den explicita dialogen mellan varje slide.
