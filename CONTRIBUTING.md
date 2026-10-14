# Contributing

Thank you for helping. This course is for people who know nothing about AI
yet, so every contribution is judged by one question: **will a beginner
understand it?**

## Ways to help

| You want to | Do this |
| --- | --- |
| Report a mistake, a broken link or a confusing sentence | [Open an issue](../../issues/new/choose) |
| Fix a typo or a small error | Edit the page on GitHub (the pencil on every site page links there) and open a pull request |
| Write a lesson from a part's outline | Comment on that part's issue or open one, so two people do not write the same lesson, then follow [Write a lesson](#write-a-lesson) |
| Add or improve a lab | Follow [Write a lab](#write-a-lab) |
| Translate the course | Open an issue first: each language is its own Antora component |

New here? Look for issues labelled
[`good first issue`](../../issues?q=is%3Aopen+label%3A%22good+first+issue%22).

## Where things live

```
docs/
  antora.yml                   the course: title and nav order
  modules/
    ROOT/pages/                start here, learning paths, resources
    <part>/nav.adoc            the part's menu
    <part>/pages/index.adoc    the part's overview and outline
    <part>/pages/<lesson>.adoc one file per lesson
    <part>/examples/           symlinks to lab code, for include::
labs/
  NN-<part>/                   runnable lab code, one folder per part
```

The parts, in order: `foundations`, `llms`, `prompting`, `apis`, `context`,
`agents`, `coding-agents`, `harness`, `production`, `frontier`, `capstone`.

## Write a lesson

1. Pick a lesson from the outline on the part's `index.adoc`.
2. Create `docs/modules/<part>/pages/<short-name>.adoc` from the template below.
3. Add it to `docs/modules/<part>/nav.adoc`.
4. On the part's `index.adoc`, turn the outline line into a link:
   `xref:<short-name>.adoc[2.1 Tokens]`.
5. Point the previous lesson's `Next:` line at your lesson.
6. Build the site and read your page there (see [Build and check](#build-and-check)).

`docs/modules/foundations/` is the reference: copy its shape.

### Lesson template

```asciidoc
= 2.1 Tokens
:description: One sentence on what the lesson covers. It shows in search and link previews.

.What you will learn
* Two to four concrete goals.

== First idea

Short sections. One idea each.

.Key ideas
****
* The lesson in about five lines.
****

== Check yourself

. A question.

[%collapsible]
.Answers
====
. The answer, with the reason.
====

Next: xref:embeddings.adoc[].
```

### Style

- **Plain English.** Short sentences, active voice, everyday words. Explain every
  term the first time it appears, in **bold**.
- **One idea per section.** If a section needs two examples to make sense, it is
  two sections.
- **Concrete before abstract.** Start with an example (the spam filter, the
  umbrella neuron), then name the idea.
- **No hype, no fear.** Say what a technique does and where it breaks.
- **Teach the idea, then name the product.** Concepts outlive product names.
  Mention a product only as an example, and never as the only option.
- **Credit sources.** Quote or adapt from another course only within its
  licence, and link to it. Link to an existing explanation rather than copying it.
- **Check facts.** Every number, date and claim must be checkable. Link the
  source for anything recent.

## Write a lab

- Put the code in `labs/NN-<part>/`, runnable with one command.
- Parts 1–3 use plain Python 3.11+ with no libraries. Parts 4–8 use Python or
  TypeScript (Node 22+). Keep dependencies to the minimum.
- Never commit an API key. Read keys from environment variables, and say which
  ones in the lab page.
- Symlink the file into `docs/modules/<part>/examples/` and pull it into the
  page with `include::example$<file>[]`, so the page and the code never drift.
- **Run it.** Any output shown on the lab page must come from a real run.

## Build and check

You need Node 22+.

```sh
npm ci
npm run docs:site    # build the HTML site into build/site
npm run docs:serve   # open http://localhost:8080
```

`npm run docs` also builds the PDF coursebook; it needs Ruby and
`bundle install`. CI builds both, and **fails on any Antora warning**, such as a
broken `xref:`. Fix warnings before opening a pull request.

## Pull requests

- One lesson, lab or fix per pull request.
- Commit messages follow [Conventional Commits](https://www.conventionalcommits.org):
  `type(scope): description`, for example `docs(llms): add lesson on tokens` or
  `fix(foundations): correct sigmoid example`.
- By contributing you agree that your text is licensed under CC BY 4.0 and your
  code under MIT, the same as the rest of the course.

## Code of conduct

Be kind and assume good faith. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
