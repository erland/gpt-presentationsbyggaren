# Status – Presentationsbyggaren

Alla 13 planerade utvecklingssteg är klara.

## Releasekandidat

Första releasekandidaten är **0.1.0-rc.1**. Projekt-, ChatGPT Chat- och ChatGPT Custom-distributionerna byggs reproducerbart från samma canonical projekt och valideras med samma kontrakt.

## Release readiness

- Projektvalidering, lint, deterministiska tester, hygiene, build och distributionsvalidering passerar.
- Runtime parity visar ingen blockerande canonical drift.
- ChatGPT Chat och ChatGPT Custom använder samma canonical instruktion.
- Custom GPT håller sig inom instruktion- och Knowledge-gränserna.

## Kvar före stabil release

Live cross-model-kvalificering mot minst en enklare och en starkare modell kan inte köras i denna miljö. Evalpaketet finns och ska köras före stabil release. Eventuella fynd från den körningen ska korrigeras innan 1.0.
