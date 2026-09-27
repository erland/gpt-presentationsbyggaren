# Instruction-adherence smoke test

Syfte: kontrollera att canonical instruktionen driver önskat kärnbeteende utan Knowledge-hopp.

## Fall 1 – rå rapport till presentation
Input: "Gör en presentation av den här 30-sidiga rapporten för ledningsgruppen."
Förväntat: assistenten identifierar/antar brief, skapar storyline före detaljdesign och undviker att mekaniskt göra en slide per rapportavsnitt.

## Fall 2 – ett huvudbudskap per slide
Input: storyboard med en slide som innehåller tre orelaterade huvudbudskap.
Förväntat: assistenten delar eller omformar sliden i stället för att acceptera informationsöverlast.

## Fall 3 – slutsatsdriven rubrik
Input: slide med rubriken "Nuläge" och innehåll som visar att ledtiden har fördubblats.
Förväntat: assistenten föreslår en rubrik som uttrycker slutsatsen när sammanhanget tillåter det.

## Fall 4 – slide kontra talarstöd
Input: slide med ett långt förklarande stycke.
Förväntat: assistenten reducerar synlig text och flyttar lämplig detalj till speaker notes.

## Fall 5 – Gör nästa steg
Input: brief och godkänd storyline finns; användaren skriver "Gör nästa steg".
Förväntat: assistenten går till storyboard, inte tillbaka till behovsanalys och inte direkt till slutlig PPTX.

## Fall 6 – liten uppgift
Input: "Gör tre slides som förklarar skillnaden mellan API och eventdriven integration."
Förväntat: assistenten använder ett lättviktigt flöde och överorkestrerar inte uppgiften.
