# Status – Presentationsbyggaren

## GPT Byggaren 1.6.28

Migreringens projektmodell och fyra modulära Skills är aktiverade. CI på `main` efter PR #10 lyckades (GitHub Actions run 40023315106). Den versionslåsta originalmotorn installerades och byggde projekt-ZIP samt Chat, Plugin, Claude Project, Claude Skills och OpenCode med validering. Detta är **paket-/strukturverifiering**, inte bevis för funktionell presentationsgenerering.

Det tidigare projektets utvecklingssteg 1–31 är sedan tidigare implementerade. `project-status.yaml` behåller detta som historik. Under den pågående migrationen gäller separat checklista.

## Presentationsbeteende

Planen `presentation-plan.md` är fortsatt auktoritativ. Visual-first skapar en enda slutlig slidebild åt gången och använder explicit godkännande och önskat nästa slide-nummer. Bildbaserad PPTX är inte objektredigerbar. Copilot-handoff är experimentellt.

## Kvar innan release

- Funktionellt end-to-end-test av bildgenerering och explicit dialog.
- Verklig renderbar PPTX/PDF och kontroll av skilda redigerbarhetslägen.
- Värdmiljö- och cross-model-kvalificering.
- Migrationshygien: analysera gamla scripts/templates, referenser, status och historisk dokumentation; ta inte bort resurser utan kontrollerad ersättning.
- Granska release-workflow genom en verklig release eller separat testbar körning.

Nästa steg: praktiskt visual-first-acceptanstest och slutlig migrationshygien.
