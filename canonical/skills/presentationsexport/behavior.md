# presentationsexport

## Copilot-handoff

Copilot-handoff är ett **kompletterande/experimentellt spår**, inte huvudvägen. Använd det när användaren uttryckligen vill prova en redigerbar presentation via Microsoft Copilot eller motsvarande. Följ `knowledge/copilot-handoff-guide.md`.

Skapa från samma `presentation-plan.md`:

- `copilot-handoff.docx` när dokumentgenerering stöds,
- gärna `copilot-handoff.pdf`,
- `copilot-prompt.md` som kort startinstruktion.

Handoff ska beskriva mål, design direction och varje slide, inte duplicera interna arbetssteg.

## Export med separata textlager

När en slide har `slides/slide-NN.layers.json` ska den renderade sammanslagna PNG-bilden skapas från originalbakgrunden och de separata textlagren före PDF-/PPTX-export. PPTX/PDF kan fortfarande vara bildbaserade, men projekt-ZIP **måste** innehålla bakgrund, lagerdefinition och renderad bild för senare textkorrigering. Ändringar i textlagret får inte automatiskt regenerera originalbakgrunden. Äldre slides utan lagerdefinition exporteras som tidigare utan att skapa påhittade redigerbara lager.

## Tvåstegsbild för visual-first-export

För slides med `render_mode: ai_two_stage` ska `slides/slide-NN-final.png` vara den bild som läggs i PPTX och PDF. Den rena `slides/slide-NN-background.png`, den strukturerade texten och genereringsmetadata ska följa med i projekt-ZIP men inte exporteras som en extra slide. Verifiera att finalbilden är godkänd och att referensen till bakgrunden är deklarerad. Om finalbilden saknas eller inte är godkänd ska sliden inte rapporteras som färdig.
