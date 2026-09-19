# The Unofficial Guide

Stephany L. - 🏙️ City Guides 🗺️



---

# Week 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

This Unofficial guide focuses on answering questions based on the `city_guide` corpus. This system provides informational or facutal answers to city travel related questions such as sites to see, weather, population size, acessibility, foods to eat, and payment expectation. 

## Chunking Strategy

**Chunk size: 750**

The longest char count of a section is 712 so to encompass this, I lowered the original chunk size from 800 to 750 for a closer fit.

**Overlap: 100**

Since I already have the doc title and section headers associated with each chunk, I don't need to rely on too much overlap to get context that may blend different city information together. 

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: `` — produced by: chunker.py::split_documents``

```
Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance
```

**Chunk 2** — source: `` — produced by:chunker.py::split_documents ``

```
Corry Vale — Where to stay

Perhaps thirty beds in the entire valley, spread across two pubs and a handful of farmhouse rooms. In summer these are booked months ahead. Camping is permitted on two marked fields and nowhere else.
```

**Chunk 3** — source: `` — produced by:chunker.py::split_documents ``

```
Givens Mill — Eat and drink

A tearoom attached to the mill, open 10 to 4 daily except Tuesdays, which sells bread made from the flour ground twenty metres away and is the reason most people come. One pub, food served lunchtimes and Thursday to Saturday evenings.
```

**Chunk 4** — source: `` — produced by: chunker.py::split_documents``

```
Kestrelford — When to go

Late spring and early autumn. The Saturday market runs year-round but is much reduced from November to February. August is busy with walkers. The single-track approach road is genuinely difficult in snow and the town can be cut off for a day or two most winters.
```

**Chunk 5** — source: `` — produced by: chunker.py::split_documents``

```
Getting around the region — Buses

Three operators run in the region and they do not accept each other's tickets,
which is the single most common source of confusion for visitors. Services
concentrate on weekday daytimes. Sunday service is minimal to non-existent
outside the Brightwater town routes.

The Kestrelford service is hourly on weekdays, two-hourly on Saturdays, and
does not run on Sundays. The Halden Bay coast service runs four times daily
year-round.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:** "Which town has the flattest area that makes it easy to explore with someone in a wheelchair?"

**Answer:**

```
Based on the provided documents, **Thornby Wells** is described as the region's most accessible town on foot, with flat, formal gardens and level streets (from `guide_walking.md`). It is also noted as the easiest town in the region for limited mobility, being flat, compact, with level pump rooms and gardens (from `guide_accessibility.md`).
```

**My relevance cutoff: .75**

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
|  "Which town has the flattest area that makes it easy to explore with someone in a wheelchair?" | yes | 0.533 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.**
To help come up with a chunking strategy for the city guides, I had Claude help analyze the stats of the city guide documents such as finding the min, average, and max section length. This helped me figure out the best chunking size to ensure it was able to accomodate the largest section without being too large. 

**2.**
Claude assisted in implenting the chunking function based on my discussion with it in determining the best approach to splitting the sections for the city guides. I had to configure the chunk size and overlap to ensure the chunks were more fitted for precise answers.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Week 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     week 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 3/5 | 2/5 | 3/5 | MISSED |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5  | 5/5  | 5/5 | MET  |
| 4. Chunks should be ~700 characters with ~100 overlap. | 1/5| 1/5 | 1/5 | 1/5 |MISSED |
| 5. For 4 of 5 questions, the answer can be found in the source document listed. | 4/5 | 4/5 | 4/5 | 4/5 | MET |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

**Criterion 1**- scored by scorer.py::retrieval_hit, which checks whether the expects phrase appears in any retrieved chunk. From the before log:


| Which town have the flattest paths that would be suitable to explore with someone in a wheelchair? | pass | pass | pass 

| Should I expect to pay using card or cash when visiting these cities? | fail | fail | fail 

| Which cities have the best buildings that are free and open to the public like museums or churches? | fail | fail | fail 

| When's the best month to visit Brightwater when's the weather is good and is not too busy? | pass | pass | pass 

| Which is the largest country that can fit the total population of Marchwood and Corry? | pass | fail | pass 

**Criterion 2** — read off the answers in the before log, produced by generate.py::answer_from_chunks. Every one of the fifteen names a file:

```
Based on the provided documents, **Thornby Wells** has flat, formal gardens and level streets, making it the region's most accessible town on foot. 

Source: `guide_walking.md`
```

Criterion 3 — run_eval.py::check_out_of_scope, straight from the before log:
| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.808 | refused |
| How do I change the oil in a diesel engine? | 0.881 | refused |
| Who won the 1994 World Cup? | 0.982 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.835 | refused |
| How do I write a for loop in Rust? | 0.859 | refused |


Criterion 4 — The 14th Chunk out of the 15th chunks from chunker.py::split_documents has the most chars (479) while most other sections are around 300 chars
```
Getting around the region — Walking and cycling

The river path from Brightwater runs four miles upstream on a good surface. The
old railway trackbed from Kestrelford runs six miles on an easy gradient and is
the best walking in the region for the effort involved. The coastal path from
Halden Bay is more serious — exposed, and closed in high wind.

Cycling is pleasant on the river path and the trackbed, and unpleasant on Mill
Road and the coast road, neither of which has a shoulder.
```

**Criterion 5 —** Read manually against the sources the log says were retrieved. 2 of five answers stay inside their documents. 2 others have answers in the listed sources but 1 question about cash/card was marked failed when it should have been pass while the other question about building sight sees in each town have answers in the listed docs but the llm is not confident. The fifth shouldn't have answers because it's an out of scope question. :

```
Question: ### Which cities have the best buildings that are free and open to the public like museums or churches? — run 2

I do not have enough information to answer which cities have the best buildings that are free and open to the public, as the documents do not compare the quality of the buildings across cities or state which ones are free, other than mentioning that the city museum in Marchwood is free (guide_marchwood.md).

```



## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     week — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunks contain the answer | MISSED | 3/5 on 2 runs and 2/5 for 1 run |
| 2 | Every answer names a source | MET | All fifteen answers name at least one file.|
| 3 |The relevance gate stops out-of-corpus questions  | MET  | 5 of 5 refused, worst distance 0.982 against a 0.75 cutoff. Target was 4 of 5. |
| 4 | Chunks should be ~700 characters with ~100 overlap. | MISSED | Most of the chunks from the 15 sample was around 200-300 and only stopped at sections. |
| 5 | For 4 of 5 questions, the answer can be found in the source document listed. | MET  | 4/5 against target of 4/5. There's only one question that failed only 1/3 runs, "best building" question, which may be more of a system error or question framing.|

Original: Chunks should be ~700 characters with ~100 overlap. 

Revised: Chunks should have file and section titles (if applicable) with concise and contained topics (no cut off sentences.)

Why: The original should have said max 750ish chars since the largest section was a low 700. Yet there's no way of testing that since the chunks that were used to answer a question are not visible. Overlap was not useful since the chunker was already dividing by sections which would keep the information more concise and not mixed. 


Original: For 4 of 5 questions, the answer can be found in the source document listed.

Revised: For 4 of 5 questions, the way the question is answered should reflect accurately on what's found in the source document listed.

Why: Gemini model seems to be a little too strict on  matching the question with answers and can't reason if it's close enough. For instance for opinionated questions that may include "whats the best place", Gemini will avoid ranking the place if it's not mentioned in the docs which is fair but then misleads in its answer by saying it doesn't know eventhough it does contain answers that would be useful to the user. 


## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

*False misses- Missed criteria that doesn't accurately reflect the chunking strategy robustness

Criterian 1- Retrieved chunks contain the answer
- No change in chunk strategy, the issue may be the "expectation" in the questions doc. 

Criterian 4- Retrieved chunks contain the answer
 - Nothing wrong with the chunk strategy for the revised critieria. The only fault was poor wording and thought process of the previous criteria that was not significant and not able to test. 

*What Criteria I would ACTUALLY revisit:
Criterian 5- 
- Original: For 4 of 5 questions, the answer can be found in the source document listed.

- Revised: For 4 of 5 questions, the way the question is answered should reflect accurately on what's found in the source document listed.





## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
