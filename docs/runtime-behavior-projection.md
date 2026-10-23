# Modulära Skills och runtimernas projektioner

I projektmodellen används fyra modulära Skills, men distributionerna är **inte** strukturellt identiska.

- Chat, Plugin och Claude Skills har separata SKILL.md-resurser.
- Claude Project och OpenCode får de fyra specialiserade beteendena sammanfogade i `project/instructions.md` respektive `AGENTS.md`. Detta är avsiktligt för deras runtime-format, och är **inte** frånvaro av skillbeteende.
- Delat innehåll kan dupliceras i Skill-källorna; vi optimerar inte bort det utan att först verifiera motorns kontrakt om fristående Skills.

`scripts/verify_runtime_behavior_projection.py` läser projektets fyra canonical behavior-filer och kräver alla avsnitt i respektive runtime-ZIP. Kontrollen körs både vid CI och release. Den skyddar **textuell och strukturell paritet**, inte att en modell följer instruktionerna.

Kvar att testa: riktig installation, filskrivning, bildgenerering per slide, explicit användargodkännande, rendering samt verifierad PPTX/PDF i respektive runtime.

Historisk ChatGPT Custom-policy i Chat ZIP bör hanteras separat i motorn eller distributionskonfigurationen, inte genom att modifiera genererade ZIP manuellt.
