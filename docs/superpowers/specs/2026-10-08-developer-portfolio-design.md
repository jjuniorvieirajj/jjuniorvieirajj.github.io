# Developer Portfolio Design

## Goal

Create a polished personal portfolio for J. Junior, a full-stack developer with
20 years of experience. The site should make the developer's social profiles,
experience, about information, and selected GitHub projects easy to find.

## Audience and success criteria

The primary audience is recruiters, collaborators, and developers who arrive
from GitHub. In one visit, they should be able to identify the developer, scan
the featured work, and follow a profile link. The site must work on desktop and
mobile, and be deployable directly as a GitHub Pages site.

## Page structure and content

Build a single-page portfolio with these sections:

1. **Top navigation:** LinkedIn, GitHub, and Instagram profile links, followed
   by in-page Experience and About links.
2. **Hero:** Introduce “J. Junior” as a full-stack developer with 20 years of
   experience. Include a clear in-page call to explore featured work.
3. **Featured projects:** Curate three repositories from the public GitHub
   profile, linking each card to its repository:
   - `angular-rxjs-signals-fundamentals-begin`
   - `playwright-docker-repo`
   - `spring-boot-restcontrolleradvice`
4. **Experience:** Summarize the stated 20-year full-stack background without
   inventing employers, job dates, or achievements.
5. **About:** A concise profile summary, followed by social links in the footer.

Use these profile URLs:

- LinkedIn: <https://www.linkedin.com/in/jjuni0rvieira/>
- GitHub: <https://github.com/jjuniorvieirajj>
- Instagram: <https://www.instagram.com/jjuniorvieirajj/>

Do not fetch GitHub data at runtime. Keep the project selection and page copy
static so the portfolio is fast, reliable, and independent of API availability
or rate limits.

## Visual direction

Use the approved developer-terminal aesthetic: a near-black background,
monospace typography, restrained mint-green accents, fine dividers, and subtle
terminal details. Keep the interface polished and readable rather than
imitating a full command-line application. The palette and accent styling must
maintain readable contrast.

Use a responsive single-column flow on narrow screens and a more spacious
layout on wider screens. Keep motion subtle, and honor reduced-motion
preferences.

## Implementation boundaries

- Implement as a dependency-free static page with semantic HTML, CSS, and only
  the JavaScript needed for small presentation details.
- GitHub Pages must be able to serve the page directly without a build step,
  backend, or secrets.
- Use real anchor links for navigation. External profile and project links must
  point to the supplied profiles and selected repositories.
- Keep project descriptions factual and limited to the repository names,
  available language metadata, and verified project contents.
- Do not add fabricated testimonials, metrics, employment history, or claims.

## Accessibility and behavior

- Use a logical heading hierarchy and semantic navigation, main, section, and
  footer landmarks.
- Ensure all links are keyboard accessible with a visible focus treatment.
- Use descriptive link text and ensure the Experience and About navigation
  targets exist.
- Do not rely on color alone to communicate meaning.
- Respect `prefers-reduced-motion`.

## Validation

- Open the page locally and check layout and readability at desktop and mobile
  viewport sizes.
- Verify the nav anchors resolve and each external link points to the intended
  profile or repository.
- Check keyboard focus visibility and reduced-motion behavior.
- Run any available repository checks; since the site is static and has no
  existing test harness, manually verify the served page and links.
