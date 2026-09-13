"""
Stage 2 of the pipeline: splitting documents into chunks.

⚠️ THIS IS THE FILE YOU CHANGE IN MILESTONE 3.

`split_documents` below is deliberately plain. It cuts every document into
fixed-size pieces with a fixed overlap and pays no attention to where sentences
or paragraphs end. It works, and it is not good.

On a corpus of short posts it may not cut anything at all: `campus_life` comes
out as 88 documents and 88 chunks, because almost nothing in it reaches 800
characters. That is the baseline, not a bug — Milestone 3 is where you decide
whether one post should stay one chunk.

Your job in Milestone 3 is to replace the *body* of `split_documents` with a
strategy that fits the documents you actually read in Milestone 1. Keep the
name and the shape of what it returns — the rest of the pipeline calls it, and
your README has to name the function that produced your chunks.

If you get stuck for 30 minutes, `fallback_split` is the original. Switch back
to it, write down what you saw, and move on. That's a real observation about
your pipeline, not giving up.
"""

import re
from dataclasses import dataclass

import config
from ingest import Document


@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in week 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        start = 0
        index = 0
        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()
            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1
            start += chunk_size - overlap

    return chunks


# A title is "# Brightwater"; a section is "## Getting there". The `\s+` after
# the hashes is what keeps the two apart — a second `#` is not whitespace, so
# the title pattern can't match a section heading.
_TITLE_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
_HEADING_RE = re.compile(r"^##\s+(.+)$", re.MULTILINE)


def _parse_sections(text: str) -> tuple[str, list[tuple[str, str]]]:
    """
    Break one guide into its title and its `##` sections.

    Returns the document title and a list of (heading, body) pairs. Anything
    sitting between the title and the first heading comes back with an empty
    heading, so the intro paragraph in guide_accessibility.md isn't dropped.
    """
    title_match = _TITLE_RE.search(text)
    title = title_match.group(1).strip() if title_match else ""
    start = title_match.end() if title_match else 0

    headings = list(_HEADING_RE.finditer(text, start))
    sections: list[tuple[str, str]] = []

    intro = text[start : headings[0].start() if headings else len(text)].strip()
    if intro:
        sections.append(("", intro))

    for i, match in enumerate(headings):
        end = headings[i + 1].start() if i + 1 < len(headings) else len(text)
        body = text[match.end() : end].strip()
        if body:
            sections.append((match.group(1).strip(), body))

    # Catch sections w/ neither headings nor a body under
    # its title by indexing it whole and with no prefix.
    if not sections:
        return "", [("", text.strip())]

    return title, sections


def split_documents(documents: list[Document]) -> list[Chunk]:
    """
    Split each guide on its `##` headings — one section per chunk.

    Written for the city_guides corpus, whose documents are markdown guides
    with a `# Town` title and topical `## ` sections running 24 to 712
    characters.
    """
    chunks: list[Chunk] = []

    for doc in documents:
        title, sections = _parse_sections(doc.text)
        index = 0

        for heading, body in sections:
            prefix = " — ".join(part for part in (title, heading) if part)
            header = f"{prefix}\n\n" if prefix else ""

            if len(header) + len(body) <= config.CHUNK_SIZE:
                bodies = [body]
            else:
                # Every piece carries the prefix, so the window has to leave
                # room for it.
                window = max(
                    config.CHUNK_SIZE - len(header), config.CHUNK_OVERLAP + 1
                )
                bodies = [
                    piece.text
                    for piece in fallback_split(
                        [Document(source=doc.source, text=body)],
                        chunk_size=window,
                    )
                ]

            for piece in bodies:
                chunks.append(
                    Chunk(
                        text=f"{header}{piece}",
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::split_documents",
                    )
                )
                index += 1

    return chunks


def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""
    if not chunks:
        return "0 chunks"
    lengths = [len(c.text) for c in chunks]
    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))
