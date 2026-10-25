# Hero Top Spacing Design

## Goal

Noticeably reduce the visual gap between the site header and the
`~/portfolio · profile` eyebrow on the homepage.

## Approach

Adjust only the hero section's top padding at the existing desktop and mobile
breakpoints: use `clamp(2.5rem, 6vw, 4.5rem)` on desktop and `2.5rem` on mobile.
This is a more noticeable reduction from the current values. Keep the hero's
bottom padding, content, portrait, and layout unchanged. This is narrower than
changing the entire hero padding or reducing header spacing.

## Verification

Preview the homepage at desktop and mobile widths and confirm the eyebrow sits
closer to the header without changing the spacing below the hero content.
