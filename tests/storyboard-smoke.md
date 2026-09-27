# Storyboard smoke tests

## Test 1 – Storyline till komplett storyboard

**Givet** en validerad storyline med kärnbudskapet att ett nytt arbetssätt kortar ledtiden och en `problem-consequence-solution`-båge.

**När** storyboard skapas.

**Då ska** varje slide ha `title`, `message`, `purpose`, `pattern`, `visual_intent`, `layout`, `content`, `speaker_notes` och `quality_checks`, och hela artefakten ska validera mot `schemas/storyboard.schema.json`.

## Test 2 – Ett huvudbudskap per slide

**Givet** en storyline-punkt som innehåller två självständiga slutsatser: lägre ledtid och högre kvalitet.

**När** båda kräver olika evidens eller visualisering.

**Då ska** de bli separata slides eller den sekundära slutsatsen flyttas från huvudbudskapet. `message` får inte vara en lista med flera parallella huvudbudskap.

## Test 3 – Text flyttas till speaker notes

**Givet** en slide med en tydlig processvisualisering och sex långa förklarande textpunkter.

**När** storyboardet kvalitetsgranskas.

**Då ska** endast nödvändiga etiketter eller korta punkter ligga kvar i `content.on_slide`; förklaringar flyttas till `speaker_notes`, och `text_density_ok` ska först sättas till true efter korrigering.

## Test 4 – Appendix för fördjupning

**Givet** en executive-presentation där en detaljerad jämförelsetabell stödjer men inte bär huvudbudskapet.

**När** storyboardet skapas.

**Då ska** huvudsliden sammanfatta slutsatsen och den detaljerade tabellen markeras som appendixkandidat eller appendixreferens.
