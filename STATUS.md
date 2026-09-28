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


## 0.4 candidate – redigerbar text i visual-first

Steg 31–35 är implementerade på förbättringsbranchen.

- `hybrid-slide` använder bildbaserad grafik med native redigerbar PowerPoint-text.
- `presentation-plan.md` bär `Text layout`, text-safe area och explicit `Approved asset`.
- Godkännande uppdateras deterministiskt med `scripts/approve_slide_asset.py`.
- Mixed-mode PPTX kan innehålla både `image-slide` och `hybrid-slide`.
- Slutpaketering blockeras tills alla visuella slides är godkända och bundna till exakt asset-version.
- End-to-end-regression verifierar approval → plan → assetbindning → PPTX → native text.
- Senaste push-CI och PR-CI är gröna.

## Nästa steg

Merge PR #6. Därefter är nästa produktvalidering ett praktiskt live-test med verkligt bildgenererade hybrid-slides i ChatGPT-flödet.
