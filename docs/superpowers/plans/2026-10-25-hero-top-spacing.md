# Hero Top Spacing Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Noticeably reduce the gap above the homepage's `~/portfolio · profile` eyebrow.

**Architecture:** Keep the existing hero structure, reduce the top padding values at desktop and mobile breakpoints, and top-align only the desktop text column while leaving the portrait vertically centered. Leave bottom padding, content, and mobile layout unchanged.

**Tech Stack:** Static HTML with embedded CSS; browser preview for visual verification.

## Global Constraints

- On desktop, use `clamp(2.5rem, 6vw, 4.5rem)` for hero top padding.
- On mobile, use `2.5rem` for hero top padding.
- On desktop, top-align the text column and keep the portrait vertically centered.
- Keep the hero's bottom padding, content, and mobile layout unchanged.

---

### Task 1: Reduce hero top padding

**Files:**
- Modify: `index.html` (the `.hero` and mobile `.hero` CSS rules)

**Interfaces:**
- Consumes: Existing `.hero` rules in the page's embedded stylesheet.
- Produces: A smaller responsive gap above the eyebrow; no HTML or asset changes.

- [x] **Step 1: Update the desktop top padding**

In the base `.hero` rule, replace:

```css
padding-block: clamp(4.5rem, 12vw, 9rem) clamp(4rem, 9vw, 7rem);
```

with:

```css
padding-block: clamp(2.5rem, 6vw, 4.5rem) clamp(4rem, 9vw, 7rem);
```

- [x] **Step 2: Update the mobile top padding**

In the `@media (max-width: 38rem)` `.hero` rule, replace:

```css
padding-block: 4rem 3.5rem;
```

with:

```css
padding-block: 2.5rem 3.5rem;
```

- [x] **Step 3: Top-align desktop hero copy**

In `.hero-copy`, add:

```css
align-self: flex-start;
```

The desktop flex row then starts the text at the top of the hero content area while `.hero-inner` continues to center the portrait. The mobile column already aligns its children at the start, so this does not change its layout.

- [x] **Step 4: Verify the homepage at desktop and mobile widths**

Open the local homepage and confirm the desktop eyebrow starts 72px below the header and the portrait stays vertically centered. At mobile width, confirm the eyebrow remains 40px below the header. Confirm the hero's bottom padding is unchanged at both widths.
