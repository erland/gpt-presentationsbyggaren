# Migreringschecklista – Presentationsbyggaren

Migrering till GPT Byggaren **1.6.28**. Checka bara av efter faktisk kontroll. Dessa sex steg är migrationens enda övergripande steg.

## 1. Inventering
- [x] Inventera repo, instruktioner, status, kontrakt och befintliga runtime-mål
- [x] Dokumentera preliminär beteendespårbarhet och risker
- [ ] Granska alla kunskapsresurser, scheman, templates, scripts och GitHub Actions mot referenser och beroenden
- [ ] Fastställ Skill-indelning och resursisolering

## 2. Projektmodell
- [x] Förbered `gpt-project.yaml` för 1.6.28 med fem runtime-mål (deklarerat; ännu ej distributionsverifierat)
- [ ] Definiera skilda artefaktlägen: visual-first, redigerbar PPTX, Copilot-handoff
- [ ] Inventera verkliga host-förmågor och deklarera fallback för alla tools
- [x] Koppla in fyra kanoniska Skill-källor med explicita resurslistor (kräver byggverifiering)

## 3. Motor
- [x] Kontrollera bifogad Engine ZIP och kör originalmotorns självtest
- [ ] Installera/pinna exakt 1.6.28 i projektets CI, dokumentera integritetskontroller
- [ ] Jämför ersättning med gamla generella skript före eventuell städning

## 4. Fem distributioner
- [ ] Bygg projektpaket och Chat, Plugin, Claude Project, Claude Skills, OpenCode med originalmotor
- [ ] Kontrollera samtliga skillresurser, parity och distributionernas interna struktur
- [ ] Ta bort Custom GPT från aktiv build först efter beslutad migration

## 5. Dokumentation och filhygien
- [ ] Synkronisera README, PROJECT, STATUS, utvecklingsplan, CI och migrationschecklista
- [ ] Gå igenom gamla scripts, genererade filer och brutna hänvisningar
- [ ] Bevara historik och fastställ projektets versions-/releasepolicy

## 6. Slutverifiering
- [ ] Kör projektspecifika validators och deterministiska tester
- [ ] Testa återupptagen plan, explicit godkännande, en bild per slide
- [ ] Testa PPTX/PDF renderbarhet och skilj visuella helslidebilder från redigerbara objekt
- [ ] Kvalificera host-skillnader och enklare/starkare modell
- [ ] Verifiera CI och release-readiness innan merge/release

## Nästa rekommenderade PR
**Projektmodell + moduleringsbeslut:** inventera samtliga resurser och fastställ exakt Skill-ansvar, därefter uppdatera `gpt-project.yaml` och inför canonical-källor. Behåll gamla builds tills faktisk ersättningsparitet uppmätts.

## PR för aktivering – verifieringsgräns

Modulära källor har aktiverats deklarativt i `gpt-project.yaml`, men befintlig CI och gamla byggskript har inte bytts ut. Motorns tidigare självtest är **inte** bevis för att den omställda projektmodellen går att bygga. Denna PR hålls därför som draft och får inte mergas innan 1.6.28 canonical lint, source-validation, fem byggda distributioner, samtliga distributionsvalidators, gamla projektets deterministiska tester samt CI passerar. Vid kompatibilitetsfel: korrigera projektmodell/schema/byggkedja på samma PR; gör inte ändringen på `main`.
