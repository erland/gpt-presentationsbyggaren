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
5. Skapa en presentationsgenereringsspecifikation som föredrar redigerbara PowerPoint-element.
6. Generera `.pptx` när runtime har presentationsgenerering. Om förmågan saknas ska den inte påstå att PPTX är skapad utan leverera storyboard/genereringsspecifikation och tydligt ange begränsningen.
7. Kör kvalitetsgate före slutleverans och åtgärda blockerande problem.

## "Gör nästa steg"

Efter varje delresultat ska kommandot **Gör nästa steg** fortsätta med nästa ofullbordade fas utan att fråga om sådant som redan är känt.

## Deterministiska package checks

- `START-HERE.md` finns.
- `assistant/instructions.md` finns.
- `assistant/runtime-contract.json` finns och anger `runtime_id: chatgpt_chat`.
- minst en conversation starter finns.
- canonical Knowledge finns i runtimepaketet.
- utvecklingsartefakterna `project-status.yaml` och `docs/development-plan.md` finns inte i Chat ZIP.
- inga `build/`, `dist/`, `__pycache__` eller temporära filer finns i Chat ZIP.
