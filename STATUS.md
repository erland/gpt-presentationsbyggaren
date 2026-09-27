# Status – Presentationsbyggaren

Grundplanens steg 1–13, 0.2-stegen 14–18 och 0.3-stegen 19–24 är implementerade.

## 0.3-arkitektur

`presentation-plan.md` är nu kanonisk presentationsartefakt efter planeringen.

Från planen finns två primära leveransspår:

### Visual-first

- 1–2 anchor slides först.
- Viktiga/komplexa bilder genereras normalt en i taget.
- Enklare assets kan genereras i små batcher om högst 2–4.
- Hela decket genereras inte i en enda bildprompt.
- Slutlig PowerPoint får vara bildbaserad och behöver inte vara objektredigerbar.
- PDF levereras som motsvarande visuellt stabil representation när runtime stöder det.

### Copilot-handoff

- DOCX är primärt strukturerat underlag för redigerbar presentation.
- PDF är valfri stabil referens.
- En kort Markdown-prompt används tillsammans med dokumentet.
- Handoff projiceras från samma presentation-plan och ska inte ändra kärnbudskapet.

## Kvar före 0.3 releasekandidat

- CI ska passera på förbättringsbranchen.
- Praktiskt A/B-test med samma case: visual-first vs Copilot-handoff.
- Live cross-model-kvalificering kvarstår från tidigare plan.
