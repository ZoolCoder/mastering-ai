# Mastering AI

A free, open course that takes you from zero knowledge of AI to building
agents and the harnesses that make them reliable.

**Read it:** https://zoolcoder.github.io/mastering-ai

Eleven parts, from foundations to the frontier:

1. Foundations: what AI is, how machines learn, neural networks
2. How LLMs work
3. Prompt engineering
4. Building with model APIs
5. Context engineering and RAG
6. Agents
7. Coding agents
8. Harness engineering
9. Production and safety
10. The frontier
11. Capstone

Each part ends with a lab in [`labs/`](labs/). Pick a route on the
[learning paths](https://zoolcoder.github.io/mastering-ai/mastering-ai/paths.html) page.

**Status:** part 1 is complete. Parts 2 to 11 are outlined, with the planned
lessons on each part's page, and are being written.

## Contribute

Found a mistake, or a sentence that lost you?
[Open an issue](../../issues/new/choose). Want to write a lesson or a lab? Read
[CONTRIBUTING.md](CONTRIBUTING.md): it has the lesson template, the style guide
and the build steps. Everyone is welcome; see the
[code of conduct](CODE_OF_CONDUCT.md).

## Build the site locally

```sh
npm ci
npm run docs:site      # HTML only
npm run docs           # HTML and the PDF coursebook (needs Ruby: bundle install)
npm run docs:serve     # http://localhost:8080
```

The site is built with [Antora](https://antora.org) and the
[zc-supplemental-ui](https://github.com/zoolcoder/zc-supplemental-ui) theme.
Lessons are AsciiDoc files in `docs/modules/<part>/pages/`.

## Licence

Course text: [CC BY 4.0](LICENSE-CONTENT). Code: [MIT](LICENSE).
