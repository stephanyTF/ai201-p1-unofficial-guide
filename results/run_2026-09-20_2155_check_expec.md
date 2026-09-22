# Run log — check_expec

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `city_guides` (index variant `default`)
- top-k: 8 · relevance cutoff: 0.75
- Runs per question: 3, caching off
- When: 2026-09-20 21:55

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Which town have the flattest paths that would be suitable to explore with someone in a wheelchair? | pass | pass | pass |
| Should I expect to pay using card or cash when visiting these cities? | pass | pass | pass |
| Which cities have the best buildings that are free and open to the public like museums or churches? | fail | fail | fail |
| When's the best month to visit Brightwater when's the weather is good and is not too busy? | pass | pass | pass |
| Which is the largest country that can fit the total population of Marchwood and Corry? | fail | fail | fail |

---

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.75. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.808 | refused |
| How do I change the oil in a diesel engine? | 0.881 | refused |
| Who won the 1994 World Cup? | 0.982 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.835 | refused |
| How do I write a for loop in Rust? | 0.859 | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### Which town have the flattest paths that would be suitable to explore with someone in a wheelchair? — run 1

- Best distance: 0.5426 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_corry_vale.md, guide_elder_ness.md, guide_regional_transport.md, guide_walking.md

```
Thornby Wells has flat, formal gardens and level streets, making it the region's most accessible town on foot (from guide_walking.md).
```

### Which town have the flattest paths that would be suitable to explore with someone in a wheelchair? — run 2

- Best distance: 0.5426 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_corry_vale.md, guide_elder_ness.md, guide_regional_transport.md, guide_walking.md

```
Based on the documents, Thornby Wells has flat, formal gardens and level streets, making it the region's most accessible town on foot (guide_walking.md).
```

### Which town have the flattest paths that would be suitable to explore with someone in a wheelchair? — run 3

- Best distance: 0.5426 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_corry_vale.md, guide_elder_ness.md, guide_regional_transport.md, guide_walking.md

```
Thornby Wells has flat, formal gardens and level streets, making it the region's most accessible town on foot (guide_walking.md).
```

### Should I expect to pay using card or cash when visiting these cities? — run 1

- Best distance: 0.5689 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_corry_vale.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md

```
You should expect that cash is still useful at the market and in smaller places, although cards are accepted almost everywhere now. This information comes from `guide_kestrelford.md`, `guide_corry_vale.md`, `guide_halden_bay.md`, `guide_marchwood.md`, `guide_brightwater.md`, `guide_pellew_sands.md`, `guide_givens_mill.md`, and `guide_elder_ness.md`.
```

### Should I expect to pay using card or cash when visiting these cities? — run 2

- Best distance: 0.5689 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_corry_vale.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md

```
You can expect cards to be accepted almost everywhere, though cash is still useful at the market and in smaller places. 
Sources: `guide_kestrelford.md`, `guide_corry_vale.md`, `guide_halden_bay.md`, `guide_marchwood.md`, `guide_brightwater.md`, `guide_pellew_sands.md`, `guide_givens_mill.md`, and `guide_elder_ness.md`.
```

### Should I expect to pay using card or cash when visiting these cities? — run 3

- Best distance: 0.5689 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_corry_vale.md, guide_elder_ness.md, guide_givens_mill.md, guide_halden_bay.md, guide_kestrelford.md, guide_marchwood.md, guide_pellew_sands.md

```
You can expect cards to be accepted almost everywhere, though cash is still useful at the market and in smaller places. 

This is mentioned across the documents, including `guide_kestrelford.md`, `guide_corry_vale.md`, `guide_halden_bay.md`, `guide_marchwood.md`, `guide_brightwater.md`, `guide_pellew_sands.md`, `guide_givens_mill.md`, and `guide_elder_ness.md`.
```

### Which cities have the best buildings that are free and open to the public like museums or churches? — run 1

- Best distance: 0.5719 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_elder_ness.md, guide_givens_mill.md, guide_kestrelford.md, guide_marchwood.md

```
I can't say what's best since I don't have access to ratings or reviews, but based on the knowledge I have, here's what I can provide ... Marchwood features a city museum that is free and genuinely excellent (guide_marchwood.md).
```

### Which cities have the best buildings that are free and open to the public like museums or churches? — run 2

- Best distance: 0.5719 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_elder_ness.md, guide_givens_mill.md, guide_kestrelford.md, guide_marchwood.md

```
I can't say what's best since I don't have access to ratings or reviews, but based on the knowledge I have, here's what I can provide ... Marchwood has a city museum that is free and genuinely excellent, as stated in `guide_marchwood.md`.
```

### Which cities have the best buildings that are free and open to the public like museums or churches? — run 3

- Best distance: 0.5719 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_elder_ness.md, guide_givens_mill.md, guide_kestrelford.md, guide_marchwood.md

```
I can't say what's best since I don't have access to ratings or reviews, but based on the knowledge I have, here's what I can provide ... Marchwood features a city museum that is free and genuinely excellent, particularly the industrial floor (guide_marchwood.md).
```

### When's the best month to visit Brightwater when's the weather is good and is not too busy? — run 1

- Best distance: 0.2124 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_halden_bay.md, guide_regional_transport.md, guide_seasons.md

```
I can't say what's best since I don't have access to ratings or reviews, but based on the knowledge I have, here's what I can provide: May and June are the best months, featuring long days, everything open, and students largely gone (guide_brightwater.md). Additionally, September is described as a sweet spot that is warm and quiet with everything still open (guide_seasons.md).
```

### When's the best month to visit Brightwater when's the weather is good and is not too busy? — run 2

- Best distance: 0.2124 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_halden_bay.md, guide_regional_transport.md, guide_seasons.md

```
I can't say what's best since I don't have access to ratings or reviews, but based on the knowledge I have, here's what I can provide: May and June are the best months for Brightwater because they feature long days, everything open, and the students largely gone (guide_brightwater.md and guide_seasons.md). September is also noted as a sweet spot where it is warm, quiet, and everything is still open before it gets busy in late September (guide_seasons.md).
```

### When's the best month to visit Brightwater when's the weather is good and is not too busy? — run 3

- Best distance: 0.2124 (passed the gate)
- Sources retrieved: guide_brightwater.md, guide_halden_bay.md, guide_regional_transport.md, guide_seasons.md

```
I can't say what's best since I don't have access to ratings or reviews, but based on the knowledge I have, here's what I can provide: May and June are the best months to visit Brightwater, as they feature long days, reliable weather, everything open, and the students largely gone (guide_brightwater.md and guide_seasons.md). September is also noted as a warm and quiet "sweet spot" before the town gets busy in late September (guide_seasons.md).
```

### Which is the largest country that can fit the total population of Marchwood and Corry? — run 1

- Best distance: 0.4936 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_corry_vale.md, guide_marchwood.md, guide_walking.md

```
I don't have enough information to answer your question.
```

### Which is the largest country that can fit the total population of Marchwood and Corry? — run 2

- Best distance: 0.4936 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_corry_vale.md, guide_marchwood.md, guide_walking.md

```
I don't have enough information to answer this question.
```

### Which is the largest country that can fit the total population of Marchwood and Corry? — run 3

- Best distance: 0.4936 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_corry_vale.md, guide_marchwood.md, guide_walking.md

```
I don't have enough information to answer this question.
```
