# Presentationsmetod – Brief och storyline

Detta dokument fördjupar den canonical operativa kärnan utan att ersätta den. Vid konflikt gäller `assistant/instructions.md`.

## 1. Brief: minsta nödvändiga förståelse

En Presentation Brief ska göra tre saker tydliga innan storyline skapas:

1. **Vem** mottagaren är och vilken förkunskap/beslutsroll målgruppen har.
2. **Varför** presentationen görs och vilken effekt den ska få.
3. **Vad** som är känt, antaget, begränsat eller fortfarande öppet.

Briefen ska normalt kunna byggas utan en frågerunda om syfte, målgrupp och material redan framgår av användarens uppdrag eller bifogade källor.

### Fråga endast när svaret påverkar ett väsentligt val

Ställ en fråga om minst ett av följande gäller:

- två rimliga tolkningar leder till tydligt olika presentationer,
- ett krav från användaren inte kan uppfyllas utan ett saknat beslut,
- en lågkonfidens-uppgift riskerar att ändra kärnbudskap eller målgruppsanpassning,
- användaren uttryckligen vill välja mellan alternativ.

Fråga **inte** när uppgiften kan lösas genom ett reversibelt designval eller ett tydligt deklarerat antagande.

### Antaganden

När något härleds i stället för att frågas:

- skriv antagandet konkret,
- ange `confidence` som low/medium/high,
- sätt `needs_confirmation=true` endast om nästa fas inte bör låsas utan bekräftelse.

## 2. Auto-val av presentationsstil

Auto ska alltid resonera i två oberoende dimensioner: **innehållsstil** och **visuell stil**.

### Auto – innehållsstil

Använd följande heuristik som startpunkt:

| Signal i uppdraget | Rekommenderad innehållsstil |
|---|---|
| Ledning, beslut, prioritering, kort möte | `executive` |
| Nuläge, målbild, vägval, initiativ, roadmap | `strategy` |
| Analys, hypoteser, tydlig argumentation, jämförelse | `consulting` |
| Arkitektur, implementation, komponenter, beroenden | `technical` |
| Förklara/lära ut, progression från enkelt till avancerat | `teaching` |
| Aktivt deltagande, övningar, frågor, samskapande | `workshop` |
| Stark berättelse och få ord, visuell förflyttning | `visual-storytelling` |

Om flera signaler finns: välj den stil som bäst stödjer **önskad effekt**, inte den som bäst beskriver källmaterialet.

### Auto – visuell stil

| Signal i uppdraget | Rekommenderad visuell stil |
|---|---|
| Neutral, professionell, mycket luft | `minimal-light` |
| Mörk scen/skärm, hög kontrast, modern känsla | `minimal-dark` |
| Formell organisation/företagskontext | `corporate` |
| Rapport-/magasinkänsla, narrativ typografi | `editorial` |
| Stora budskap/illustrationer och hög visuell energi | `bold-visual` |
| Processer, arkitektur, modeller och relationer dominerar | `diagram-heavy` |

Om användaren har en mall eller designprofil ska den väga tyngre än Auto-heuristiken.

### Rekommendation kontra inferens

- `user_selected`: användaren har uttryckligen valt stil.
- `assistant_recommended`: flera val är rimliga och GPT:n presenterar en rekommendation.
- `assistant_inferred`: valet är tydligt från uppdraget och behöver inte belasta användaren med ett extra val.

Auto får aldrig bli en ursäkt för att ställa en onödig fråga.

## 3. Storyline: berättelse före innehållsförteckning

Storyline utgår från briefens `desired_outcome`, inte från källmaterialets kapitelordning.

### Core message

`core_message` ska kunna uttryckas i en eller ett fåtal meningar. Det ska vara den tes, slutsats eller förståelse som presentationen som helhet bygger mot.

### Narrative points

Varje punkt ska:

- ha en tydlig funktion (`role`),
- stödja kärnbudskapet eller vara nödvändig för mottagarens förståelse,
- komma i en ordning som är lätt att följa,
- kunna översättas till en eller flera slides senare utan att redan nu låsa layouten.

### Vanliga storyline-mönster

- **Problem → konsekvens → lösning**: när ett behov först måste etableras.
- **Nuläge → målbild → gap → åtgärder**: för transformation och strategi.
- **Varför → vad → hur**: för införande, förankring och utbildning.
- **Före → förändring → efter**: när skillnaden mellan två arbetssätt är central.
- **Strategi → förmågor → initiativ → roadmap**: när strategisk riktning ska omsättas till handling.

Mönstret är ett stöd, inte en tvångströja. Välj eller kombinera endast när det förbättrar logiken.

## 4. Gate mellan brief och storyline

Briefen är tillräcklig när följande kan besvaras utan spekulation som riskerar att förändra presentationen:

- vem är presentationen till för,
- varför görs den,
- vad ska mottagaren förstå, känna eller göra,
- vilka centrala krav eller begränsningar gäller.

Storylinen är tillräcklig när:

- core message är tydligt,
- varje narrative point har en funktion,
- ordningen är logisk,
- huvudpoängerna stödjer core message,
- sidospår är borttagna eller markerade som appendix.

## 5. Två typiska startlägen

### Kort idé

När användaren bara ger ett ämne eller en idé:

1. härled en preliminär brief från formuleringen,
2. deklarera nödvändiga antaganden,
3. fråga endast om ett väsentligt vägval saknas,
4. rekommendera eller inferera stil,
5. skapa storyline när brief-gaten är passerad.

### Större källmaterial

När användaren ger rapport, dokument eller flera filer:

1. identifiera materialets huvudbudskap, fakta och struktur,
2. skilj källans disposition från presentationens kommunikationsmål,
3. bygg brief utifrån användarens uppdrag + källan,
4. notera luckor eller motsägelser i `source_material.gaps`,
5. skapa storyline som prioriterar målgruppens behov framför dokumentets kapitelordning.
