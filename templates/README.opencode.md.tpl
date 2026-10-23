# {{GPT_NAME}} – OpenCode

Version: {{VERSION}}

Detta är **Presentationsbyggarens** OpenCode-distribution. Den hjälper dig att planera, skapa och kvalitetssäkra presentationer från en kanonisk `presentation-plan.md`. Den är **inte** GPT Byggarens motor och förutsätter inget separat GPT-projekt.

## Installation

1. Packa upp arkivet i ett eget workspace och öppna katalogen i OpenCode.
2. Läs `AGENTS.md` för assistentens instruktioner och `knowledge/` för presentationsmetodiken.
3. Öppna eller skapa `presentation-plan.md` i workspace-katalogen. Använd `projectRoot` om presentationens projektfiler ligger i en underkatalog.
4. Generera en slide åt gången och invänta ditt uttryckliga godkännande. Visual-first ger bildbaserad PPTX, inte redigerbara PowerPoint-objekt.
5. Använd de verktyg som **faktiskt** ingår under `.opencode/tools/`. Verktygsnamn och argument finns där, inte i en generell GPT Byggaren-manual.

## Presentationens valideringsverktyg

- `gpt_presentation_plan_validate` kontrollerar en `presentation-plan.md`. Verktyget kräver filsökvägen `file`.
- `gpt_pptx_validate` kontrollerar att en PPTX har en giltig Open XML-struktur. Verktyget kräver filsökvägen `file`.

Dessa verktygs `file`-argument stöds först av GPT Byggarens uppdaterade motor efter rättningen av wrappergeneratorn. **Äldre OpenCode-arkiv, inklusive 1.4.2, har defekta wrappers; byt inte bara ut README och anta att de fungerar.**

## Runtime-begränsningar

Bildgenerering och produktion av PPTX/PDF kräver verklig värdförmåga eller kompatibelt verktyg. Python-validatorerna producerar inte presentationer. `.opencode/runtime-contract.json` beskriver deklarerade förmågor; det är inte ett bevis på praktisk leverans. Skills nämns bara om de faktiskt har paketerats; `AGENTS.md` är primär ingång.

## Filer

- `AGENTS.md`: Presentationsbyggarens instruktioner
- `knowledge/`: presentationsmetodik
- `.opencode/tools/`: tillgängliga specialverktyg
- `scripts/`: medföljande deterministiska skript
- `opencode.json`: behörigheter
- `.opencode/runtime-contract.json`: adapterkontrakt
- `MANIFEST.json`: distributionens manifest
