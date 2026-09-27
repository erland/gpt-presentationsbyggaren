# Compatibility – {{GPT_NAME}}

## Runtime-rekommendation

ChatGPT Chat och ChatGPT Custom är jämbördiga distributionsmål från samma canonical presentationsmetodik. Valet avgörs av hur assistenten ska användas: Chat ZIP för portabel konversationskontext, Custom GPT för en installerad återanvändbar assistent.

## Paritet

| Område | ChatGPT Chat | ChatGPT Custom |
|---|---|---|
| Brief → storyline → storyboard → design → presentation → review | Equivalent | Equivalent |
| Ett huvudbudskap per slide | Equivalent | Equivalent |
| Slutsatsdrivna rubriker | Equivalent | Equivalent |
| Stil- och patternbibliotek | Equivalent | Equivalent via Knowledge-paket |
| "Gör nästa steg" | Equivalent | Equivalent |
| Runtime-kontrakt | Inbäddad snapshot | Inbäddad Builder-snapshot |

## Reducerade funktioner

Custom GPT-paketet bäddar inte in lokala scripts eller lokala kommandon. Faktisk åtkomst till webbsökning, dataanalys, bildgenerering, filhantering och presentationsgenerering beror på vilka Builder-capabilities som är tillgängliga och aktiverade i den aktuella ChatGPT-miljön.

Om en rekommenderad capability saknas ska GPT:n följa canonical fallback-regel och beskriva reduceringen; den får inte låtsas att capabilityn finns.

## Saknade funktioner

Ingen känd skillnad i canonical presentationsmetodik. Full funktionell paritet för själva PPTX-renderingen förutsätter att Custom GPT-miljön erbjuder fil-/presentationsgenerering som kan leverera redigerbar PowerPoint.

## Installation

Följ `README.md`, klistra in `builder/instructions.md`, aktivera rekommenderade capabilities och ladda upp filerna i `builder/knowledge-package/`.
