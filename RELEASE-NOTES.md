# Release notes – 0.3.2-rc.1

## Explicit slide interaction och nedladdningsbar Presentation Plan

0.3.2 justerar visual-first-flödet efter praktisk testning. Explicit godkännande och val av nästa slide fungerade bättre än `Gör nästa steg` mellan separata bildgenerationer.

### Ändringar

- informationssteg före första bildgenereringen,
- rekommenderad dialog: `Det ser bra ut. Skapa slide X enligt planen.`,
- separata exempel för ändring och omgenerering,
- `Gör nästa steg` rekommenderas inte längre mellan bildgenerationer,
- `Next slide: none` är giltigt medan en genererad/redo slide väntar på användarens bedömning,
- validatorn har regressionstest för vänteläget,
- `presentation-plan.md` ska levereras som nedladdningsbar Markdown-fil när runtime stöder filskrivning,
- hela planen visas inline endast på uttrycklig begäran,
- version bump till 0.3.2-rc.1.

## Kvalificering

CI ska passera projektvalidering, lint, deterministiska tester, hygiene och runtime-distributioner. Praktiskt slide-för-slide-test återstår.

---

# Release notes – 0.3.1-rc.1

## En slide per bildgenerering

0.3.1 skärper visual-first-flödet efter praktisk testning där flera slide-assets i samma generation blev ett montage med många små bilder.

### Ändringar

- exakt en slutlig 16:9-slidebild per bildgenerering,
- `max_batch_size = 1` i generation-kontraktet,
- explicit anti-collage-regel,
- collage, kontaktkartor, moodboards, storyboardark och thumbnail-grids är blockerande,
- persistent `## Rendering status` i `presentation-plan.md`,
- högst en slide får vara `next`,
- validatorn kontrollerar att `Next slide` matchar statusen,
- före varje bildgenerering instrueras användaren att skriva **Gör nästa steg** när bilden är klar,
- efter sista slide går flödet till PPTX/PDF-paketering,
- Copilot-handoff är nu kompletterande/experimentellt medan visual-first är huvudspår.

## Kvalificering

CI ska validera schema, planstatus, regressionstester, lint, hygiene och runtime-distributioner. Praktiskt visual-first-test återstår före release.

---

# Release notes – 0.3.0-rc.1

## Presentation Plan, visual-first och Copilot-handoff

0.3 separerar presentationsplanering från rendering. `presentation-plan.md` är nu den kanoniska sparbara artefakten som kan återanvändas senare utan att brief, storyline eller storyboard behöver göras om.

### Nytt

- Visual-first är huvudspår när visuell kvalitet prioriteras framför objektredigerbarhet.
- Bildbaserad PPTX och PDF kan skapas från samma plan.
- 1–2 anchor slides etablerar formspråket före övrig bildgenerering.
- Hero-/komplexa slides genereras normalt en i taget.
- Enklare närbesläktade assets får genereras i batcher om högst 2–4.
- Hela decket får inte genereras i en enda bildprompt som standard.
- Exakt presentationscopy hålls normalt utanför bildgenereringen.
- Copilot-handoff ger DOCX/PDF + kort startprompt för redigerbar presentation.
- Presentation-planen har deterministisk strukturvalidator.
- Generation-kontraktet använder presentation-planen som primär indata.

## Kvalificering

CI ska validera planformat, generation-schema, lint, tester, hygiene och båda runtime-distributionerna. Praktiskt A/B-test med samma presentation återstår före stabil 0.3.

---

# Release notes – 0.2.0-rc.1

## Rendering och visuell kvalitet

0.2 adresserar fynd från praktisk testning av 0.1 RC1: en PPTX kunde innehålla ogiltiga Open XML-referenser och den visuella designen blev för ofta wireframe-lik.

### Viktiga ändringar

- Kommunikationskvalitet går före automatisk native-redigerbarhet.
- Fyra renderingsstrategier: native, designed composition, generated visual och hybrid.
- Ny rendering/visual-quality guide med explicit ambitionsnivå.
- Deterministisk PPTX-validator för ZIP/Open XML, Content Types och relationship-targets.
- Trasig PPTX och genomgående wireframe-lik design är blockerande kvalitetsproblem.
- Preview-baserad visuell kvalitetsgate när runtime kan rendera slides.
- PDF är rekommenderad visuellt stabil följeslagare.
- HTML kan användas när webbpresentation och visuell frihet väger tyngre än PowerPoint-redigerbarhet.
- Presentation-generation-kontraktet bär teknisk valideringsstatus och visuell ambitionskontroll.
- Regressionstester täcker den felklass som observerades i 0.1-testet.

## Kvalificering

GitHub Actions CI passerar för PR #2 med projektvalidering, lint, deterministiska tester, hygiene, distributionsbuild och distributionsvalidering.

Kvar före slutlig 0.2 releasekandidat är praktiskt end-to-end-test: skapa en verklig presentation, öppna PPTX i Microsoft PowerPoint och jämför mot PDF/preview.

## Kända begränsningar

- Projektet innehåller en deterministisk paketvalidator men ingen egen generell presentationsrenderer. Runtime ska använda en etablerad presentationsrenderer och får inte handbygga rå Open XML.
- Oberoende Office-rendering och preview kräver att aktuell runtime har motsvarande verktyg.
- Live cross-model-kvalificering kvarstår från 0.1-planen.

---

# Release notes – 0.1.0-rc.1

## Första releasekandidat

Presentationsbyggaren 0.1.0-rc.1 är den första kompletta releasekandidaten. Den hjälper användaren från presentationsbehov och källmaterial till storyline, storyboard, stilval, visuell design, redigerbar PowerPoint och kvalitetsgranskning.

## Viktig funktionalitet

- Styrt flöde: Brief → Storyline → Storyboard → Design → Presentation → Kvalitetsgranskning.
- 8 innehållsstilar och 6 visuella stilar som kan kombineras oberoende.
- 20 slide patterns och 7 storytelling patterns.
- Runtime-neutral storyboard- och genereringsmodell.
- Transformationsflöden för att korta, byta målgrupp/stil och göra presentationer mer visuella.
- Separata distributioner för ChatGPT Chat och ChatGPT Custom, byggda från samma canonical källa.
- CI, release-build, checksummor, hygiene och runtime-paritetskontroll.

## Kända begränsningar

- Live cross-model-kvalificering mot separat enklare och starkare modell har inte kunnat köras i den aktuella byggmiljön.
- Faktisk PPTX-kvalitet beror på presentationsförmågan i den runtime där GPT:n körs.
