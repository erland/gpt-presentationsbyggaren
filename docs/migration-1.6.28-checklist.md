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
- [x] Installera/pinna exakt 1.6.28 i projektets CI och kör originalmotorns självtest
- [ ] Jämför ersättning med gamla generella skript före eventuell städning

## 4. Fem distributioner
- [x] Bygg projektpaket och Chat, Plugin, Claude Project, Claude Skills, OpenCode med originalmotor (CI main 40023315106)
- [x] Kör kanonisk distributionsvalidering i CI (verifierar struktur; hostfunktioner återstår)
- [x] Ta bort Custom GPT från aktiv build (historiskt material kvar tills städning är säker)

## 5. Dokumentation och filhygien
- [ ] Synkronisera README, PROJECT, STATUS, utvecklingsplan, CI och migrationschecklista (README/PROJECT/STATUS uppdaterade i PR #11; övrigt återstår)
- [ ] Gå igenom gamla scripts, genererade filer och brutna hänvisningar
- [ ] Bevara historik och fastställ projektets versions-/releasepolicy

## 6. Slutverifiering
- [ ] Kör projektspecifika validators och deterministiska tester
- [ ] Testa återupptagen plan, explicit godkännande, en bild per slide
- [ ] Testa PPTX/PDF renderbarhet och skilj visuella helslidebilder från redigerbara objekt
- [ ] Kvalificera host-skillnader och enklare/starkare modell
- [ ] Verifiera CI och release-readiness innan merge/release

## Verifierad status och nästa steg

CI på main efter PR #10: GitHub Actions run 40023315106 PASS. Sex ZIP-arkiv byggda från GPT Byggaren 1.6.28 och distributionsvalidering genomförd. Detta verifierar inte verklig PPTX/PDF-produktion eller beteende i alla värdar.

Nästa steg: färdigställ migrationshygien (gamla scripts/templates, dokumentation och referenser) samt praktiskt visual-first-test. Behåll projektspecifika validatorer tills ekvivalens och anrop är bevisade.
