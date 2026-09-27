# Status – Presentationsbyggaren

Steg 1–30 är implementerade.

## 0.3.2

Praktiska tester visade att explicit dialog fungerar bättre än `Gör nästa steg` mellan bildgenerationer.

### Ny interaktion

Före första bilden informeras användaren om att fortsätta exempelvis med:

- `Det ser bra ut. Skapa slide 2 enligt planen.`
- `Ändra slide 1: ...`
- `Gör om slide 1 enligt planen, men ...`

Efter en genererad bild kan `presentation-plan.md` stå i vänteläge med `Next slide: none` tills användaren har bedömt resultatet.

### Presentation Plan

Den kanoniska planen ska när runtime stöder filskrivning levereras som `presentation-plan.md` för nedladdning. Chatten visar bara en kort sammanfattning om användaren inte ber att få se hela Markdown-innehållet.

## Kvar

- CI på förbättringsbranchen.
- Praktiskt test av explicit slide-för-slide-dialog.
- Live cross-model-kvalificering kvarstår.
