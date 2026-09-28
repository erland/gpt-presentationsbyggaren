# ChatGPT Chat runtime – end-to-end smoke test

## Syfte

Verifiera att Chat ZIP-distributionen bär hela kärnflödet från en enkel idé till en presentationsartefakt utan att kräva utvecklingsplan eller projektstatus vid normal körning.

## Scenario

**Input:**

> Skapa en kort presentation för en IT-ledningsgrupp om varför ett team bör gå från ad hoc-användning av AI till återanvändbara AI-assistenter. Rekommendera stil och gör nästa steg tills presentationen kan genereras.

## Förväntat flöde

1. Skapa eller härled en Presentation Brief med syfte, målgrupp, önskad effekt och antaganden.
2. Rekommendera innehållsstil och visuell stil med kort motivering.
3. Skapa en storyline med ett tydligt kärnbudskap.
4. Skapa ett storyboard där varje slide har ett huvudbudskap, pattern, visual intent och speaker notes när det behövs.
5. Skapa en fullständig `presentation-plan.md` och leverera den som faktisk nedladdningsbar fil; att bara visa eller sammanfatta planen i chatten är inte godkänt när runtime har filskrivningsförmåga.
6. Gå först därefter vidare till visual-first-rendering enligt planen.
7. Skapa en presentationsgenereringsspecifikation när den behövs för rendering/validering.
8. Generera `.pptx` när runtime har presentationsgenerering. Om användaren kräver redigerbar text ska hybrid-slides använda native PowerPoint-text ovanpå bildbaserad grafik.
9. Kör kvalitetsgate före slutleverans och åtgärda blockerande problem.

## "Gör nästa steg"

Efter varje delresultat ska kommandot **Gör nästa steg** fortsätta med nästa ofullbordade fas utan att fråga om sådant som redan är känt.

## Deterministiska package checks

- `START-HERE.md` finns.
- `assistant/instructions.md` finns.
- `assistant/runtime-contract.json` finns och anger `runtime_id: chatgpt_chat`.
- minst en conversation starter finns.
- canonical Knowledge finns i runtimepaketet.
- Chat-runtime-policyn kräver faktisk nedladdningsbar `presentation-plan.md` före första slidebilden.
- utvecklingsartefakterna `project-status.yaml` och `docs/development-plan.md` finns inte i Chat ZIP.
- inga `build/`, `dist/`, `__pycache__` eller temporära filer finns i Chat ZIP.
