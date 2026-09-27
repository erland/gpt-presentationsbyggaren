# Status – Presentationsbyggaren

Grundplanens steg 1–13 och förbättringscykelns steg 14–18 är implementerade.

## 0.2-förbättring

Praktisk testning av 0.1 RC1 visade att presentationsmetodiken var bättre än den faktiska renderingens kvalitet. Två problem styr 0.2:

1. PPTX måste vara tekniskt giltig, inte bara skrivbar.
2. presentationen ska se designad ut, inte som ett wireframe byggt av små boxar och linjer.

Projektet prioriterar nu kommunikationskvalitet före teknisk bekvämlighet, använder en explicit rendering/preview-gate och har en deterministisk Open XML-validator.

## Leveransformat

- PPTX när PowerPoint och fortsatt redigering krävs.
- PDF som rekommenderad visuellt stabil följeslagare.
- HTML som alternativ när hög visuell frihet är viktigare än PowerPoint-redigering.

## Kvar före 0.2 releasekandidat

- Kör CI på ändringsbranchen.
- Praktiskt end-to-end-test med en verklig presentation.
- Öppna PPTX i PowerPoint och jämför med PDF/preview.
- Live cross-model-kvalificering kvarstår från 0.1-planen.
