# Implementation architecture

Use vanilla HTML/CSS/JavaScript. Keep editable source files if convenient and build one self-contained `dist/workshop.html`. Runtime assets, slide data, styling and notes must be embedded so opening via file:// works without a server. Do not fetch slides.json/config.json at presentation time. A build-time script may read these files and generate the HTML; document it. No framework/backend/CDN dependency is needed.

## Existing reference
The six-slide prototype has a shared shell, scoped panels, hash navigation, decision feedback, notes dialog, fullscreen and touch. It is a starting implementation. Current assumptions to fix when expanding:
- `go()` and keyboard End clamp to six slides.
- Counter says `/ 06`, hash validation accepts only 1–6.
- Dot navigation will crowd if used for 61 screens. Replace the long dot row with a compact module menu/slide index consistent with existing controls.
- Notes are a six-entry array.
- Global element IDs and handler references assume one email/chat/decision instance.

## Extension strategy
Use unique slide IDs from slides.json. Scope interactions to their slide root, via component classes/data attributes and event delegation or safe per-slide closures. Keep state per slide. Navigation changes one active slide and one counter. Build notes/reference lists from the same content data. Generate references from source IDs, and avoid duplicated text/code arrays that drift.

Escape navigation text safely when injecting content. Use textContent for strings and deliberately created DOM nodes. Never treat arbitrary customer JSON as executable HTML. Validate source URL schemes as https/http, and reserved mock destinations stay text-only. All links to external sources use explicit user clicks with noopener/noreferrer.

## Accessibility
Semantic headings, native controls, expanded/pressed states, visible focus, polite status regions, and modal focus/Escape behaviour. Hide inactive slides from interaction/accessibility. Do not intercept typing or native controls unnecessarily with global shortcuts. Provide clear fallback when browser fullscreen is unavailable. Respect reduced motion. Caption any audio and provide a text-only alternative; default voice scenes use read-aloud scripts.

## Presentation shell (redesign, 8 October 2026)
The slide canvas is authored at 1600×900 canvas pixels and scaled to the viewport by `deck.js` (`--s` on `#stage`); below 900px wide the CSS switches to an unscaled reading layout. The only persistent controls are the header (identity, module label, menu button) and a bottom-right slide counter generated from the slide sequence. A native modal `<dialog>` drawer holds the slide index (built from the embedded slide data and grouped by module), presenter notes, sources, fullscreen, keyboard help, workshop information and a reset for slides with a vote or reveal. Notes, sources, help and about are side panels with a fixed header and a scrolling body. All navigation (keys, menu, swipe, hash) goes through `go()`. Design tokens live in `src/css/base.css`; components in `src/css/deck.css` use only tokens.

## Visual assets (8 October 2026)
Slide IDs are `SLnn`, with an optional continuation letter (`SL09B`) for a slide inserted directly after its parent by the readability rework of 8 October 2026; order comes from `04-content/slides.json`, not from the ID, and the counter and index numbers are positions. The build’s fragment regex, the runtime hash parser (`#SL09B`), the tests and the package validator accept the suffix; the legacy `#slide-N` link stays position-based. The slide header is rendered by `render_slide()` as a kicker-and-pill row above a full-width title (a reveal button is pinned at the right and the title keeps a right padding). Generated layouts are `agenda`, `opener`, `glossary` (SL41B: the module terms on their own slide), `takeaway` and `recap`.

Diagrams live in `src/img/assets/*.svg` and are inlined by `build/assets.py` through the `{{asset:name|wide}}` token: the root width/height are dropped (the stylesheet sizes the drawing by width, the viewBox keeps proportions), the embedded `<style>` is removed, and every id and `url(#…)`/`href="#…"`/`aria-labelledby` reference is prefixed with the slide ID and asset name, so the build’s id rule and the document-wide uniqueness check hold even if an asset is repeated. The icon sprite is inlined once in the shell (`<!--SPRITE-->`, symbol ids `icon-*`) and referenced with `{{icon:name|lg}}`; icons are `aria-hidden` companions to written labels. Scene photographs are JPEG data URIs via `{{image:name|alt|short}}` (CSP `img-src data:`); backdrops are data URIs injected into the stylesheet with `{{asset-uri:file}}` (`|band=26` clips the opener pattern for SL41; `|transparent` drops its navy base so it can overlay a photograph). The office photograph is painted on `.viewport::before`, behind the scaled canvas, so it fills the window on any aspect ratio; `go()` writes the active slide’s layout to `<body data-layout>` and the stylesheet turns the backdrop on only for the cover and module openers. Below 900px wide a diagram keeps a minimum width inside a horizontally scrolling wrapper; swipe navigation ignores touches that start on it.

## Presenter notes
Menu › Presenter notes opens same-screen notes. They are visible on the projected display. User guide must say so. A separate presenter-window system is optional future work, not a claimed feature. The facilitator guide provides a printable alternative.

## State and privacy
Keep learner choices in memory for the current tab. No personal names, credentials, OTPs, telemetry, cookies or score backend. Reload resets interaction state. Local anonymous feedback only. No report gets sent from a demonstration.
