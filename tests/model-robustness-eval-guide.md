# Modellrobusthet och evals

Dessa evals verifierar att samma canonical instruktion fungerar över modellnivåer utan separata modellunika instruktioner.

## Körprincip
Kör varje YAML-fall mot den runtime/modellkombination som ska kvalificeras. Bedöm svaret mot `expected.required` och `expected.forbidden`. `critical`-fall blockerar release. Ett förbjudet beteende i ett `critical`-fall ska behandlas som blockerande.

## Nivåer att kvalificera
Minst en enklare och en starkare modellkonfiguration bör köras före stabil release. `assistant/instructions.md` ska vara identisk; runtime-adaptern får inte lägga till modellspecifika presentationsregler.

## Fokus
- enkla uppgifter ska inte överorkestreras,
- komplexa uppgifter ska behålla brief → storyline → storyboard-gates,
- multi-turn retention via **Gör nästa steg**,
- felåterhämtning utan omstart,
- terminalt beteende när slutgaten är godkänd,
- stilbyte utan ändrat kärnbudskap,
- redigerbarhet först vid PowerPoint-rendering.

## Rapport
Dokumentera modell/runtime, datum, passerade/misslyckade fall, brustet kriterium och om felet beror på instruction-adherence, runtime-capability eller modellbegränsning.
