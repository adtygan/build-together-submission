# build-together-submission

- In this hackathon we build Keynote AI, which can write slide deck content given a problem statement by the user.
- We use Relevance AI to solve this challenge by developing an agent called Joe.
- Joe can interact with the user using Slack making for a convenient interface.
- Once the user's problem has been gathered, Joe starts working and generates content for the slide-deck.
- The content is then rendered to Slack for the user.

### Relevance AI links
- **Link to clone**: https://app.relevanceai.com/agents/d7b62b/63b6147ef98c-4f11-9e00-f9a5214dcecd/0e2c069a-ef9f-46ba-96be-5f70f30eba0d/clone
- **Link to share and embed**: https://app.relevanceai.com/agents/d7b62b/63b6147ef98c-4f11-9e00-f9a5214dcecd/0e2c069a-ef9f-46ba-96be-5f70f30eba0d/share

## sli.dev
- After content for slide-deck is generated, [sli.dev](https://sli.dev) is used to render the content as slides.
- This is a Javascript framework which takes markdown input and renders it as slides using layouts.
- Before we can use `sli.dev`, we need to do some preprocessing, which is handled by `markdown_parser.py`.
- At the end of this pre-processing, we end up with `slides.md` file.
- This file can then be used in `sli.dev`.
- We clone the repo at [https://github.com/slidevjs/slidev](https://github.com/slidevjs/slidev?tab=readme-ov-file) and follow setup instructions to get a locally running version.
- After, this, move the `slides.md` file to the root directory and the slide deck should render.

