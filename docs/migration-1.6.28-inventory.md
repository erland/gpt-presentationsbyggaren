# Migreringsinventering – GPT Byggaren 1.6.28

Datum: 2026-10-23. Källa: `main` i `erland/gpt-presentationsbyggaren`.
Status: **inventerad, inte migrerad**.

## Utgångsläge
- Projektversion: `0.3.2-rc.1`.
- `assistant/instructions.md` innehåller monolitiskt canonical beteende.
- `gpt-project.yaml` har en Skill, tre aktiva runtimes (Chat, Custom GPT, Plugin) och egna distributionsskript.
- `presentation-plan.md` är kanonisk presentationsartefakt; brief → storyline → storyboard → plan → visual-first → granskning → PPTX/PDF.
- Visual-first: exakt en slutlig slidebild per generering; mellan bilderna krävs explicit godkännande/slidekommando, inte generell ”Gör nästa steg”.
- `Copilot-handoff` är experimentellt kompletteringsspår.
- Projektstatus redovisar 31 implementerade steg samt två återstående praktiska kvalificeringar.

## Målbild
Fem jämbördiga, kontraktsdrivna runtime-mål: `chat`, `plugin`, `claude_project`, `claude_skills`, `opencode`. Historisk Custom GPT-projektion avvecklas när ersättningen har verifierats. Ingen runtime får påstå stöd för verklig PPTX-/PDF-leverans utan verifierad host-förmåga.

## Förslag till Skill-arkitektur (beslutas före uppdelning)
Gemensam `canonical/core.md` med kärnmetod, faktakrav, state-regler och gemensam kvalitet.

| Skill | Aktiveringsvillkor | Exklusivt ansvar | Resurser att inventera |
| --- | --- | --- | --- |
| `presentationsplanering` | Ny/förändrad presentation | brief, storyline, storyboard, plan | presentation-method, storytelling-patterns, plan-format; brief/storyboard/storyline-scheman |
| `bildproduktion` | Visual-first vald | anchor slides, exakt en bild, explicit godkännande och renderingsstate | visual-first-workflow, visual-generation-guide, visual-styles |
| `presentationsexport` | Plan/slides ska paketeras/överlämnas | PPTX/PDF och Copilot-handoff med host-gates | copilot-handoff-guide, rendering-quality-guide, validate_pptx.py |
| `kvalitetsgranskning` | Revidering/slutgranskning | innehåll, bildrendering och teknisk kontroll | quality-guide, slide-design-guide, presentation-review-schema |

**Gates före modularisering:** analysera om kvalitetsgranskning är ett eget fristående arbetsflöde eller gemensam gate; fastställ exklusiv resursfördelning samt `skills.resource_policy: explicit` med `references`, `assets` och `scripts` för varje Skill. Behåll originalinstruktion som spårbar källa men inte parallell auktoritativ instruktion.

## Spårbarhet för beteende (får inte tappas)
| Källa i gamla instruktionen | Mål | Acceptans |
| --- | --- | --- |
| Operativ kärna, brief/storyline/storyboard-gates | core + presentationsplanering | originalflödet och informationsgates bevarade |
| Presentation Plan | planering + core | `presentation-plan.md` nedladdningsbar, återupptagningsbar; inte automatiskt utskriven i chatten |
| Visual-first | bildproduktion | en enda slutlig slidebild per generering; explicita slidekommandon; approval/state |
| Copilot-handoff | presentationsexport | experimentellt, från samma plan |
| Rendering och kvalitet | granskning + export | visuell preview och PPTX-integritet verifieras |
| Befintliga presentationer | planering + granskning | transformation och helhetsanalys bevaras |
| Gör nästa steg | core | fasövergångar, men inte som mellanbilds-godkännande |
| Källor och runtime-neutralitet | core | externa fakta styrks, hostbegränsningar deklareras |

## Risker
1. `PROJECT.md` anger redigerbar PPTX som huvudartefakt, medan senare instruktion/README prioriterar visual-first. Dokumentera två skilda utfall; gör inte bildbaserad PPTX till ”redigerbar”.
2. `contracts/tools.yaml` listar generiska API-actions (`presentation.generate`, `file.write`, m.fl.) som inte får antas finnas i respektive runtime. Härled faktisk host-mappning och fallback.
3. Runtimeparitet: kräver funktionstester, inte enbart paketering av gemensamma resurser.
4. Egna `scripts/build_distributions.py`, `lint_gpt_project.py`, `validate_distributions.py` etc får inte raderas innan kanonisk ersättning och anrop i CI/release verifierats.
5. Format- och schemaändringar måste inte förstöra återupptagning av befintliga `presentation-plan.md`.

## Verifiering hittills
Bifogad original-Engine ZIP `gpt-byggaren-engine-1.6.28(2).zip` lästes lokalt. Originalets `scripts/selftest_distribution_engine.py --source .` rapporterade PASS för source, materialize, integrity (SHA-256 för 62 filer), installer och smoke-build (sex arkiv). **Detta verifierar bara motorn, inte en migration eller funktionstest av Presentationsbyggaren.**
