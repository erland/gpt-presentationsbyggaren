# Presentationsbyggaren

Presentationsbyggaren är ett GPT-projekt för att skapa och förbättra professionella presentationer från idé eller källmaterial till färdig presentationsleverans.

Kärnflödet är **brief → storyline → storyboard → stil/design → rendering → teknisk och visuell kvalitetsgranskning**.

## Status

Den ursprungliga 0.1-releasekandidaten är genomförd. En 0.2-förbättringscykel har lagts till efter praktisk testning som visade två problem: för primitiv/wireframe-lik design och en PPTX med ogiltiga Open XML-referenser.

0.2 inför bland annat:

- kommunikationskvalitet före automatisk native-redigerbarhet,
- renderingsstrategierna native, designed composition, generated visual och hybrid,
- deterministisk PPTX/Open XML-validering,
- preview-baserad visuell kvalitetsgate,
- PDF som rekommenderad visuell följeslagare,
- HTML som valfritt format när visuell frihet är viktigare än PowerPoint-redigering.

## Aktiverade runtimes

- ChatGPT Chat
- ChatGPT Custom

Övriga registrerade runtimes är bedömda men inte aktiverade som standard.

## Fortsättning

Läs `project-status.yaml` och `docs/development-plan.md`. Nästa rekommenderade aktivitet är ett praktiskt end-to-end-test av 0.2-renderingen i PowerPoint och visuell granskning av preview/PDF.
