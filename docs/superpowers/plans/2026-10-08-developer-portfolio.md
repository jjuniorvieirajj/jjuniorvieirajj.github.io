# Developer Portfolio Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a polished, responsive, terminal-inspired portfolio for J. Junior that presents the developer's profiles, experience, about information, and selected GitHub projects.

**Architecture:** Implement one self-contained static `index.html` with semantic markup and inline CSS, without a framework, runtime API, backend, or build step. Update the README with the site purpose and local preview command; GitHub Pages can serve the page directly from the repository root.

**Tech Stack:** HTML5, CSS3, GitHub Pages, Python 3 standard-library HTTP server for local browser verification.

## Global Constraints

- “Use the approved developer-terminal aesthetic: a near-black background, monospace typography, restrained mint-green accents, fine dividers, and subtle terminal details.”
- “Use a responsive single-column flow on narrow screens and a more spacious layout on wider screens.”
- “The palette and accent styling must maintain readable contrast.”
- “Keep motion subtle, and honor reduced-motion preferences.”
- “Implement as a dependency-free static page with semantic HTML, CSS, and only the JavaScript needed for small presentation details.”
- “GitHub Pages must be able to serve the page directly without a build step, backend, or secrets.”
- “Do not fetch GitHub data at runtime. Keep the project selection and page copy static so the portfolio is fast, reliable, and independent of API availability or rate limits.”
- “Keep project descriptions factual and limited to the repository names, available language metadata, and verified project contents.”
- “Do not add fabricated testimonials, metrics, employment history, or claims.”
- “Use real anchor links for navigation. External profile and project links must point to the supplied profiles and selected repositories.”
- “Use a logical heading hierarchy and semantic navigation, main, section, and footer landmarks.”
- “Ensure all links are keyboard accessible with a visible focus treatment.”
- “Use descriptive link text and ensure the Experience and About navigation targets exist.”
- “Do not rely on color alone to communicate meaning.”
- “Respect `prefers-reduced-motion`.”

---

### Task 1: Build the Static Portfolio Page

**Files:**
- Create: `index.html`
- Modify: `README.md`

**Interfaces:**
- Consumes: Public profile URLs and repository links listed below.
- Produces: A complete root-level `index.html` that GitHub Pages can serve without a build step.

- [ ] **Step 1: Confirm the project content and static-page baseline**

Inspect the root directory and the current README. Confirm there is no existing app framework, package manifest, or test runner to extend. Verify the three selected repositories are public and inspect their README files before writing project summaries:

```bash
for repo in angular-rxjs-signals-fundamentals-begin playwright-docker-repo spring-boot-restcontrolleradvice; do
  gh api "repos/jjuniorvieirajj/$repo/readme" --jq '.download_url'
done
```

Open the returned public README URLs and use only details they support. The project cards must link to:

```text
https://github.com/jjuniorvieirajj/angular-rxjs-signals-fundamentals-begin
https://github.com/jjuniorvieirajj/playwright-docker-repo
https://github.com/jjuniorvieirajj/spring-boot-restcontrolleradvice
```

The profiles in the header and footer must link to:

```text
https://www.linkedin.com/in/jjuni0rvieira/
https://github.com/jjuniorvieirajj
https://www.instagram.com/jjuniorvieirajj/
```

- [ ] **Step 2: Create a semantic page skeleton and verify its required links**

Create `index.html` with the required metadata, a skip link, header/navigation, `main`, and footer. Give Experience and About stable in-page IDs and add the three external profile links. Use text labels rather than decorative icons so the navigation remains understandable without icon fonts.

Use the title `J. Junior — Full-Stack Developer` and a concise description mentioning full-stack development and 20 years of experience. Open the page through a local server and verify the document title and navigation are present:

```bash
python3 -m http.server 4173
```

Expected: the server serves the repository root at `http://localhost:4173/`; opening that URL shows the page title and the LinkedIn, GitHub, Instagram, Experience, and About links.

- [ ] **Step 3: Add the terminal-inspired visual system and responsive layout**

In the page's inline `<style>`, define reusable CSS custom properties for a near-black background, dark-green surfaces, high-contrast text, muted secondary text, and mint accent. Use a readable monospace stack, restrained borders, small terminal prompts, and clear section spacing. Do not add external fonts, images, icon libraries, or dependencies.

Set a centered content width for desktop, and use a single-column flow for mobile. Allow navigation links to wrap on narrow screens. Give links visible `:focus-visible` styles and use `@media (prefers-reduced-motion: reduce)` to disable nonessential transitions.

Verify at a desktop viewport and a narrow mobile viewport. Expected: no horizontal page overflow, readable text, and navigation that remains visible and wraps cleanly on narrow screens.

- [ ] **Step 4: Add hero, featured projects, Experience, and About copy**

Add a hero headed `J. Junior` with the role `Full-stack developer` and the stated `20 years of experience`. Include an anchor CTA to the projects section.

Add three project cards using the exact repository names from Step 1, links to those repositories, GitHub-reported primary languages when available, and short summaries grounded in each repository's README. If a README does not substantiate a proposed summary, use the repository name and language only.

Add an Experience section that states the 20-year full-stack background without naming employers, dates, accomplishments, or technologies not verified by the user. Add a concise About section using only the known role and experience. Verify the page contains no invented employment claims or unsupported project details.

- [ ] **Step 5: Check navigation, external destinations, keyboard access, and responsive behavior**

Run the local server from Step 2 and inspect the page in a browser. Follow each in-page anchor and confirm it reaches an existing section. Confirm profile links and repository cards open the exact URLs from Steps 1–2. Tab through the entire page and confirm every interactive link has a visible focus indicator. Check desktop and mobile widths and emulate reduced motion.

Expected: all links work, no section anchor is missing, every focus state is visible, the layout fits the viewport, and reduced-motion preferences suppress nonessential motion.

- [ ] **Step 6: Document the static site in the README**

Replace the one-line README with a short site description and local preview instructions:

```markdown
# J. Junior — Developer Portfolio

A responsive, static portfolio for GitHub Pages.

## Local preview

Run `python3 -m http.server 4173` from the repository root, then open
http://localhost:4173/.
```

Verify the command is accurate from the repository root. Stop the local server after browser verification.

- [ ] **Step 7: Review the final changes**

Run:

```bash
git diff --check
git status --short
```

Review the complete `index.html` and README diff. Expected: only the root portfolio page and README are changed, there are no whitespace errors, no dependencies or build configuration were added, and the page meets every validation item in Step 5.
