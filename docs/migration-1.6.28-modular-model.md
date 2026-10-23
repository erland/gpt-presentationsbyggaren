# Modulär målmodell – steg 2 (staging)

**OBS:** Källorna i `canonical/` är förberedda men ännu inte aktiverade som byggkälla. Befintlig `assistant/instructions.md`, `gpt-project.yaml` och CI är oförändrade för att inte riskera den fungerande 0.3.2-distributionen före ett verifierat motorbyte.

## Skills och resurser (förslag att verifiera)

Resurserna delas upp per ansvar. Alla sökvägar finns i `main`. `skills.resource_policy: explicit` införs vid faktisk aktivering när motorns schema och distributionsvalidering går igenom.

| Skill | references | assets | scripts |
|---|---|---|---|
| presentationsplanering | `knowledge/presentation-method.md`, `knowledge/presentation-plan-format.md`, `knowledge/storytelling-patterns.md`, `knowledge/content-styles.md`, `knowledge/slide-design-guide.md`, `knowledge/slide-patterns.md`, `schemas/presentation-brief.schema.json`, `schemas/storyline.schema.json`, `schemas/storyboard.schema.json` | `templates/presentation-plan.md.tpl` | `scripts/validate_presentation_plan.py` |
| bildproduktion | `knowledge/visual-first-workflow.md`, `knowledge/visual-generation-guide.md`, `knowledge/visual-styles.md`, `knowledge/rendering-quality-guide.md` | [] | [] |
| presentationsexport | `knowledge/copilot-handoff-guide.md`, `schemas/presentation-generation.schema.json` | `templates/copilot-prompt.md.tpl` | `scripts/validate_pptx.py` |
| kvalitetsgranskning | `knowledge/quality-guide.md`, `knowledge/rendering-quality-guide.md`, `schemas/presentation-review.schema.json` | [] | [] |

Gemensamma källor: `knowledge/source-and-tool-guide.md` samt kontrakten under `contracts/`. De behöver placeras antingen i kärnan eller uttryckligen i respektive Skill beroende på motorns policy för resursisolering. Dela inte en resurs implicit bara för att den finns i projektträdet.

## Aktiveringsplan

1. Granska resursfördelning och skill-beteende med deterministisk avsnittstäckning.
2. Ställ om `gpt-project.yaml` till `instructions.mode: modular_skills`, `instructions.core: canonical/core.md`, `instructions.canonical: canonical/core.md`, `skills.resource_policy: explicit` och fyra definitioner med `source`.
3. Sätt fem runtime-mål till `chat`, `plugin`, `claude_project`, `claude_skills`, `opencode`. Ta bort Custom GPT **endast ur den nya buildkedjan** efter verifiering.
4. Installera originalmotorn 1.6.28 i CI via versionslåst release, kör lint, build, parity, distribution-validation samt originalprojektets Python-tester.
5. Stäm av README, PROJECT, STATUS och utvecklingsplan först när faktisk migration är verifierad.

## Gränser för presentationsexport

Visual-first innebär bildbaserade helslides i PPTX/PDF och säger inget om enskilda objekts redigerbarhet. Copilot-handoff är experimentellt och kan inte utlovas som färdig redigerbar PPTX. Objektredigerbar presentation kräver eget host-stöd och eget test.
