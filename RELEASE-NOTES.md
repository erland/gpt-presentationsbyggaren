# Release notes – 0.1.0-rc.1

## Första releasekandidat

Presentationsbyggaren 0.1.0-rc.1 är den första kompletta releasekandidaten. Den hjälper användaren från presentationsbehov och källmaterial till storyline, storyboard, stilval, visuell design, redigerbar PowerPoint och kvalitetsgranskning.

## Viktig funktionalitet

- Styrt flöde: Brief → Storyline → Storyboard → Design → Presentation → Kvalitetsgranskning.
- 8 innehållsstilar och 6 visuella stilar som kan kombineras oberoende.
- 20 slide patterns och 7 storytelling patterns.
- Runtime-neutral storyboard- och genereringsmodell.
- Redigerbarhet först: text, former, tabeller och diagram prioriteras före rasteriserade slides.
- Transformationsflöden för att korta, byta målgrupp/stil och göra presentationer mer visuella.
- Separata distributioner för ChatGPT Chat och ChatGPT Custom, byggda från samma canonical källa.
- CI, release-build, checksummor, hygiene och runtime-paritetskontroll.

## Kända begränsningar

- Live cross-model-kvalificering mot separat enklare och starkare modell har inte kunnat köras i den aktuella byggmiljön. Evalfallen är definierade och schema-validerade och ska köras före stabil release.
- Faktisk PPTX-kvalitet beror på presentationsförmågan i den runtime där GPT:n körs. Canonical projektet definierar metod, kontrakt och fallback men innehåller ingen egen generell PowerPoint-renderingsmotor.
- Aktuella fakta kräver tillgång till webbresearch eller användarens källmaterial.

## Distributionsmål

- ChatGPT Chat: releasekandidat.
- ChatGPT Custom: releasekandidat med dokumenterade capability-beroenden.
