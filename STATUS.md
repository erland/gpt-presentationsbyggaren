# Status – Presentationsbyggaren

Grundplanens steg 1–13 och förbättringsstegen 14–27 är implementerade.

## 0.3.1

Praktisk visual-first-testning visade att flera slide-assets i samma bildgeneration kunde bli ett montage med många små bilder. 0.3.1 gör därför produktionsflödet strikt sekventiellt.

### Visual-first

- Exakt en slutlig slidebild per bildgenerering.
- Ingen batchgenerering av flera slides.
- Collage, kontaktkartor, moodboards, storyboardark och thumbnail-grids underkänns.
- 1–2 anchor slides etablerar formspråket.
- Presentation Plan innehåller persistent status för varje slide.
- Högst en slide får vara `next`.
- Före bildgenereringen informeras användaren att skriva `Gör nästa steg` när bilden är klar.
- Efter sista godkända slide går flödet vidare till PPTX/PDF-paketering.

### Copilot

Copilot-handoff finns kvar men är ett kompletterande/experimentellt spår. Visual-first är standardvägen.

## Kvar före releasekandidat

- CI ska passera på förbättringsbranchen.
- Praktiskt test av en riktig presentation slide för slide.
- Live cross-model-kvalificering kvarstår från tidigare plan.
