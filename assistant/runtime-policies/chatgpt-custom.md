# ChatGPT Custom runtimepolicy

Denna policy gäller endast Custom GPT-distributionen och ändrar inte canonical presentationsmetodik.

- Använd `builder/instructions.md` som GPT Builder-instruktion.
- Lägg alla filer i `builder/knowledge-package/` som Knowledge.
- Aktivera capabilities enligt `builder/capabilities.md`.
- Bevara flödet brief → storyline → storyboard → design → presentation → kvalitetsgranskning.
- Om en Builder-capability saknas ska relevant fallback i runtime-kontraktet följas och begränsningen beskrivas öppet.
- Kritiska beteenderegler får inte flyttas från instruktionen till Knowledge för att kringgå instruktionsgränsen.
- Custom GPT ska inte låtsas ha lokala scripts eller annan verktygsåtkomst som Buildern inte faktiskt ger.
