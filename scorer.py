def judge(question: str, expects: str, answer: str, results) -> bool:
    """
    True when the answer contains the phrase a correct answer has to contain.

    `results` — the retrieved chunks — is in the signature and unused here on
    purpose. It is what you reach for if you want to separate the two questions
    every RAG eval has to answer: was the right thing retrieved, and did the
    model use it? `retrieval_hit` below is that second scorer, and criterion 1
    in criteria.md is scored with it rather than with this function.
    """
    if not expects:
        return False
    return expects.strip().lower() in (answer or "").lower()


def retrieval_hit(expects: str, results) -> bool:
    """
    True when the expected phrase is in at least one RETRIEVED CHUNK.

    This is the criterion-1 scorer, and it is a different measurement from
    `judge`. A question where this is True and `judge` is False is a generation
    failure; one where both are False is a retrieval failure. Splitting them is
    what makes the week 2 diagnosis a lookup rather than a guess.
    """
    if not expects:
        return False
    needle = expects.strip().lower()
    return any(needle in (r.text or "").lower() for r in results)