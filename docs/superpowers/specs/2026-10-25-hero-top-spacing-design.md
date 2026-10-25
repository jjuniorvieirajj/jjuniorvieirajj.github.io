# Hero Top Spacing Design

## Goal

Noticeably reduce the visual gap between the site header and the
`~/portfolio · profile` eyebrow on the homepage.

## Approach

Adjust the hero section's top padding at the existing desktop and mobile
breakpoints: use `clamp(2.5rem, 6vw, 4.5rem)` on desktop and `2.5rem` on mobile.
At desktop widths, top-align the text column while keeping the portrait
vertically centered; this removes the extra gap caused by centering the shorter
text column beside the portrait. Keep the hero's bottom padding, content, and
mobile layout unchanged.

## Verification

Preview the homepage at desktop and mobile widths. Confirm the desktop eyebrow
starts at the reduced top padding, the portrait remains centered, the mobile
layout is unchanged, and the spacing below the hero remains unchanged.
