# Projekt – Presentationsbyggaren

## Produktidé

Specialiserad presentationsassistent som skapar, förbättrar och transformerar professionella presentationer. Kommunikationsmål och visuell kvalitet går före teknikval.

## Målgrupp

Ledning, strategi, IT-arkitektur, teknik, utbildning och workshop.

## Funktionella mål

- Separata innehålls- och visuella stilar och rekommendationer.
- Brief, storyline, storyboard och kanonisk `presentation-plan.md`.
- Visual-first med exakt en slidebild per generering och explicita godkännanden.
- Bildbaserad PPTX/PDF som standard när redigerbarhet inte krävs.
- Redigerbar PPTX endast om faktisk hostförmåga finns; annan teknisk och funktionell kvalitetsgate.
- Experimentell Copilot-handoff från samma plan.
- Systematisk innehållslig, visuell och teknisk granskning.

## Arkitektur

Gemensam `canonical/core.md` och fyra modulära Skills enligt `gpt-project.yaml`. Originalmotorn GPT Byggaren 1.6.28 bygger fem peer-distributioner: Chat, Plugin, Claude Project, Claude Skills, OpenCode. Äldre Custom GPT-distribution är historisk.

Renderings- och filförmågor kommer från värden. Paketet får inte påstå att den faktiskt har skapat en PPTX om värden inte har genererat filen. Projektet är ingen generell PowerPoint-renderingsmotor.

## Kvalitet och verifiering

CI har verifierat deklarerade fem runtimepaket, originalmotorns självtest och deterministiska tester. Funktionsprov av renderad presentation, användarens slide-godkännande och cross-model-beteende återstår. Se `STATUS.md` och `docs/migration-1.6.28-checklist.md`.
