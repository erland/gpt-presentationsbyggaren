# Inventering av historiska bygg- och distributionsfiler

Datum: 2026-10-23. Bas: GPT Byggaren Engine 1.6.28; senaste gröna main-CI 40023732693.

## Identifierat

| Resurs | Bedömning | Beslut |
|---|---|---|
| `scripts/build_distributions.py`, `scripts/lint_gpt_project.py`, `scripts/validate_distributions.py` | Tidigare generella byggskript; kanonisk motor installerar motsvarande vid CI | Behåll tills anrop, funktionsersättning och slutlig hygiene verifierats |
| `scripts/lib/project_model.py`, `scripts/project_hygiene.py` | Äldre gemensamma hjälpfunktioner | Behåll tills beroenden kartlagts |
| `scripts/generate_runtime_parity.py` | Felaktigt låst till tre gamla runtimes | Ersatt med konservativ femruntime-inventering och regressionstest |
| `scripts/validate_project.py` | Projektspecifika scheman, evals, manifest | Behåll |
| `scripts/validate_presentation_plan.py`, `scripts/validate_pptx.py` | Domänspecifik validering | Behåll |
| `templates/README.custom-gpt.md.tpl`, `tests/custom-runtime-e2e.md`, `assistant/runtime-policies/chatgpt-custom.md` | Historiska Custom GPT-referenser | Behåll tills referenser och historiskt värde bedömts, exkludera från aktiva mål |
| `templates/presentation-plan.md.tpl`, `templates/copilot-prompt.md.tpl` | Domänartefakter | Behåll |

## Risk och testgräns

Det tidigare parityskriptet rapporterade Custom GPT som publikationskandidat och saknade Claude Project, Claude Skills och OpenCode. Grön CI bevisade därmed **inte** korrekt deklarativ runtime-inventering. Den nya rapporten är medvetet försiktig: alla fem runtime-mål märks som värdberoende och kräver verkliga acceptanstester. Inga praktiska presentationer eller PDF/PPTX-exporter har verifierats av denna ändring.

## Återstående hygien

- Kartlägg import/anrop till gamla scripts och visa att deras ansvar täcks innan radering.
- Granska release-workflow, utvecklingsplan och historiska Custom GPT-mallar.
- Lägg till visuella end-to-end-tester, exportkontroll och cross-model-verifiering.
- Ta ett nytt slutligt beslut om release-readiness efter dessa kontroller.
