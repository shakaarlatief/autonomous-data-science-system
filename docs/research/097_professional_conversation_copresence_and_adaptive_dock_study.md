# Research 097: Professional Conversation Co-Presence and Adaptive Dock Study

**Date:** 2026-08-29  
**Status:** IMPLEMENTED / DETERMINISTICALLY VERIFIED / AWAITING HUMAN VISUAL REVIEW  
**Scope:** Whole-product study of how the held Quiet Graphite Conversation Workspace should coexist with the Project Cockpit without reading as two complete applications forced side by side.  
**Interaction environment:** ChatGPT  
**Interaction session:** `chatgpt-10`  
**Branch:** `v1-cockpit-design-exploration`

## 1. Human review transition

The project owner accepted the Checkpoint 256 / 257 corrected Cockpit as good enough to continue:

```text
Conversation Boxes spacing
    accepted for continuation

current flat Project Grid rail control set
    accepted for continuation

canonical no-query route
    accepted as the normal current Cockpit route
```

The next issue was then identified from the complete Cockpit rather than a detached fixture.

The project owner reported that the current Conversation/Cockpit co-present composition was not good or professional. The supplied screenshot showed the project world on the left while the right side simultaneously contained both the permanent Conversation thread rail and the long-form Conversation transcript.

The resulting hierarchy read as:

```text
full Cockpit application
    beside
full Conversation application with its own permanent navigation
```

rather than one coherent professional workbench.

This research therefore reopens only the **co-present composition geometry and navigation presentation**. It does not reopen the accepted Conversation semantics or Quiet Graphite visual baseline.

## 2. Existing repository evidence

The earlier Conversation design sequence already contains the relevant ingredients.

### Research 079

Research 079 explicitly explored Conversation as a first-class workspace and preserved multiple presentation architectures, including:

```text
CV0 Focus Workspace
CV1 Right Dock
CV2 Split Workbench
CV3 Canvas Lens
CV4 Bottom Workbench
CV5 Focus + Context Rail
CV6 Conversation + Inspector
CV7 Progressive Recent-to-Full
CV8 Tabbed Stage
```

The important unresolved point was never whether Conversation should exist as a serious workspace. The unresolved point was how that workspace should compose with the project surface.

### Research 081 through 085

The held Conversation language converged on:

```text
Quiet Graphite
transcript-first / document-like reading
compact user turns
long-form ADS responses
project references separate from prose
project-aware composer
project-general + WorkUnit-scoped conversation
Boxes / Text thread navigation
A6 Adaptive Anchor
no redundant floating A6 source card
```

These are not candidates to redraw during the current integration study.

### Research 086

Research 086 is the most important architectural constraint. It separates:

```text
WORK CONTEXT
    Grid neutral / selected / X5 / Deep Dive

CONVERSATION PRESENTATION
    compact composer / full-focus / co-present

CONVERSATION SCOPE
    project-general / WorkUnit
```

It also explicitly left the exact co-present split proportions, resizing behavior, responsive behavior and pane-collapse policy unresolved.

Therefore the current problem is a legitimate open composition question beneath an already-held semantic architecture.

## 3. External professional-workbench references

The external review focused on products where conversational assistance must coexist with a primary professional work surface.

### Visual Studio Code

Official VS Code documentation currently places Chat in the **Secondary Side Bar**, beside the editor rather than replacing the editor. The Chat view can also move into an editor tab when it needs more room. VS Code describes the Secondary Side Bar as a separately showable/hideable workbench region and specifically moved Chat there so chat could remain available while other views remained accessible.

Sources:

```text
https://code.visualstudio.com/docs/agents/run/chat-view
https://code.visualstudio.com/docs/configure/custom-layout
https://code.visualstudio.com/updates/v1_95
```

Useful principle for ADS:

```text
a persistent assistant surface may coexist with primary work
without becoming a second full application shell
```

### Notion

Notion Agent exposes more than one chat presentation. Its official documentation allows users to switch between a right-side **Sidebar** and a **Floating** chat mode.

Source:

```text
https://www.notion.com/help/notion-agent
```

Useful principle for ADS:

```text
conversation presentation can adapt to the amount of attention it currently deserves
```

These products are references for workbench composition only. ADS retains its own project semantics, Conversation scope model and interaction architecture.

## 4. Candidate families considered

### A. Keep the current wide side-by-side Workspace

```text
Cockpit
+
56vw Conversation surface
+
permanent 228px Conversation thread rail
```

Rejected as the current co-present direction. The user screenshot demonstrates the failure mode directly: the Conversation Workspace brings too much of its full-focus shell into co-presence and visually competes with the Cockpit.

### B. Symmetric 50/50 split

This would make the geometry more regular but would preserve the deeper problem. Two equally dominant applications are not the desired hierarchy when Conversation is supposed to coexist with active project work.

### C. Floating conversational window

This remains plausible for a future lightweight or temporary conversational mode. It is weaker as the sole answer for long-form persistent Conversation because it can occlude project work and becomes harder to use for sustained reading.

### D. Full-focus Conversation with only a project context rail

This remains appropriate when Conversation is the primary task and is already represented by the held full-focus mode. It does not solve co-presence.

### E. Adaptive secondary Conversation dock

Selected as the **current review candidate**, not as a promoted product decision.

It treats co-present Conversation as a secondary workbench surface while preserving the complete source-faithful Workspace for full focus.

## 5. Adaptive Conversation Dock candidate

The candidate has two intentionally different presentation states.

### Full focus

Full-focus Conversation remains source-faithful:

```text
Quiet Graphite Workspace owns the stage
persistent Boxes / Text thread rail remains visible
long-form transcript retains full reading width
existing A6 behavior remains available
```

No new visual system is introduced.

### Co-present

Co-present becomes a compact right-side workbench dock:

```text
default width      clamp(520px, 38vw, 650px)
right anchored     yes
resizable          yes, from left edge
Cockpit remains    majority visible / primary
thread rail        hidden by default
Threads control    invokes the existing rail as a drawer
Boxes / Text       preserved inside that same drawer
transcript         remains the main dock surface
composer           remains project-aware
A6                 available as an invoked inspector sheet
```

The design therefore changes **hierarchy and space ownership**, not Conversation meaning.

## 6. Why the thread rail becomes invoked in co-presence

The accepted Boxes / Text rail remains valuable for:

```text
conversation discovery
project-general versus WorkUnit scope recognition
canonical WorkUnit identity in Boxes mode
fast thread switching
```

But keeping it permanently visible inside a compact co-present surface creates a nested-sidebar problem.

The candidate therefore uses:

```text
full focus
    permanent thread rail

co-present
    Threads button -> temporary drawer containing the same rail
```

This preserves the accepted navigation model while adapting its **presentation persistence** to the available width.

## 7. Resize behavior

A narrow secondary dock should not freeze one arbitrary width for every professional monitor/window arrangement.

The candidate therefore supports direct width adjustment from its left edge, including keyboard adjustment on the separator.

The resize changes presentation only. It must not mutate:

```text
Grid selection
X5 expansion
Deep Dive source state
conversation ownership
thread scope
project semantics
```

The width is deliberately not promoted as a final persistence decision. No account/project-level dock-width storage is selected here.

## 8. Isolation from the accepted current Cockpit

The study is opt-in only:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html?conversation=adaptive-dock
```

The normal route remains:

```text
http://localhost:4173/design-lab/cockpit-reintegration.html
```

The plain route intentionally receives none of the adaptive-dock classes, controls or geometry. Human review can therefore compare the candidate against the accepted current substrate without contaminating that substrate first.

## 9. Implementation artifacts

```text
frontend/design-lab/cockpit-conversation-integration-study.css
frontend/design-lab/cockpit-conversation-integration-study.js
frontend/design-lab/cockpit-spatial-rail-study-gen2-anchor.js
frontend/e2e/cockpit-reintegration-conversation-integration-study.spec.ts
```

Implementation target:

```text
00957b684cbc57dad11561f7ed262faf1bba4383
```

## 10. Deterministic evidence

Complete Cockpit fidelity workflow:

```text
workflow run  33238181528
job           99062775945
result        SUCCESS
browser tests 71 / 71 passing
```

The three new tests establish that:

```text
canonical no-query Cockpit is unchanged by the opt-in study
adaptive co-present uses a compact right-side dock rather than the prior 56vw page-like composition
thread navigation is hidden by default in co-presence
Threads reveals the same Boxes / Text rail as a drawer
dock width is adjustable
full-focus restores the persistent rail
selected project state survives dock open/resize/presentation-switch/close
all previous 68 source-faithful Cockpit tests remain green
```

Two earlier study runs exposed timing assumptions in the newly added resize assertion while all prior source-faithful tests remained green. The final assertion waits for the existing Conversation width transition to settle before measuring. No accepted mechanism was weakened to obtain the final pass.

## 11. Preserved semantic boundary

This study does **not** alter:

```text
Quiet Graphite baseline
project-general + WorkUnit-scoped conversation
Boxes / Text semantics
A6 Adaptive Anchor semantics
Conversation ownership versus SEL2 selection
Grid / X5 / Deep Dive access
full-focus + co-present capability
source work-state preservation
current-process Focus
Project Grid rail composition
Deep Dive topology compass
```

It also does not promote a final Conversation co-presence geometry. The human product-design gate remains open.

## 12. Human-review questions

Review the candidate as a whole-product composition, especially:

```text
Does the Cockpit now remain visually primary while Conversation is co-present?
Does the dock feel like one native ADS workbench surface rather than a second page?
Is the default width appropriate?
Is invoked Threads navigation better than a permanently nested thread rail?
Does resizing feel useful and restrained?
Does switching back to full focus recover the correct long-form Conversation hierarchy?
Does the A6 inspector remain understandable when used from the compact dock?
```

If the overall direction is good, later tuning should refine this exact candidate. If the composition still feels wrong, the next experiment should challenge the adaptive-dock family itself rather than cosmetically tuning the old 56vw two-page layout.

## 13. Practical keyboard contract refinement

Human review later exposed an interaction flaw in the first practical keyboard refinement.

The intended contract had become:

```text
Escape
    application Back

F
    enter or exit browser fullscreen

Shift+C
    switch Conversation between full-focus and co-present presentation
```

The first implementation correctly gave `F` an explicit fullscreen shortcut, but it did not actually remove the browser's native single-press `Escape` fullscreen exit. The code deliberately avoided `preventDefault()` while `document.fullscreenElement` was active, and the new Playwright regression mocked `document.fullscreenElement` and fullscreen methods without reproducing the browser-owned Escape behavior. Therefore an 81/81 deterministic pass did not contradict the human observation. The test was incomplete for the browser-level behavior being judged.

The corrected Adaptive Dock contract is now:

```text
normal Escape press
    application Back only
    closes Conversation when Conversation is the active layer
    otherwise continues to the existing Deep Dive / overlay Back recovery
    does not exit fullscreen

F
    exclusive normal fullscreen toggle
```

The adaptive route now requests fullscreen with browser keyboard locking and also uses the Keyboard Lock API to capture `Escape` while fullscreen is active. The top-layer keyboard router always cancels the normal Escape default action in fullscreen, while still allowing the Cockpit's Back routing to execute. The lock is released when fullscreen ends.

The implementation deliberately uses both mechanisms:

```text
requestFullscreen({ keyboardLock: 'browser', navigationUI: 'hide' })

navigator.keyboard.lock(['Escape'])
```

The first is the current Fullscreen API keyboard-lock mode. The second is the established Chromium progressive-enhancement mechanism and provides a compatibility path when the newer fullscreen option is unsupported. Unsupported option errors fall back to ordinary `requestFullscreen()` before the explicit Keyboard Lock attempt.

Reference behavior:

```text
https://developer.mozilla.org/en-US/docs/Web/API/Element/requestFullscreen
https://developer.chrome.com/blog/better-full-screen-mode
```

Browser security still retains an emergency escape mechanism. In Chromium, a long hold of `Escape` can leave keyboard lock/fullscreen. That safety path is intentionally not treated as an ADS shortcut. The normal press contract is the product interaction being controlled here.

Corrected implementation target:

```text
6a1386a1dd5045655d38d306a3ecc1fdb4a7ffd2
```

Complete Cockpit V3 verification:

```text
workflow run  33266585890
job           99137601843
result        SUCCESS
browser       Chrome for Testing 151.0.7922.34
browser tests 81 / 81 passing
```

The strengthened fullscreen test now verifies all of the following explicitly:

```text
F requests browser fullscreen with keyboardLock=browser
Escape is captured through the keyboard-lock seam
Escape closes full-focus Conversation while fullscreen remains active
another Escape in the plain Cockpit still leaves fullscreen active
Escape can perform Deep Dive Back while fullscreen remains active
F exits fullscreen and releases the Escape keyboard lock
```

Human browser review remains authoritative for the actual reserved-key behavior because the regression necessarily mocks fullscreen state for deterministic headless execution. The human recheck should therefore specifically confirm that a normal Escape press no longer leaves fullscreen in the user's real browser.

## 14. Co-present Project tools edge-utility-strip refinement

After the practical keyboard behavior was accepted for continuation, human review moved to the visual relationship between Conversation and the retained Project Grid tool rail.

The supplied whole-product screenshot exposed a different hierarchy problem from the original nested Conversation rail problem. Conversation itself now behaved as a useful dock, but the Project tool rail still appeared as a rounded, inset floating card with its own top mark, internal stack and surrounding Grid margin. When placed immediately beside the already substantial Conversation dock, the composition read as:

```text
Project Grid
+
Conversation dock
+
third floating mini-application / tool card
```

That is unnecessarily panel-heavy for a professional workbench. The tools are persistent project utilities, not a third workspace.

### Current adaptive candidate

Only while Conversation is co-present on the opt-in Adaptive Dock route, the existing real Project tool rail is re-presented as a **flush application-edge utility strip**.

```text
compact width        56px
expanded clarity     196px
vertical ownership   full viewport height
right edge           flush at x = viewport right
outer card radius    none
outer floating gap   none
Conversation seam    direct adjoining boundary
control semantics    unchanged
control ordering     unchanged
canonical rail       unchanged outside co-present Adaptive Dock
```

The same controls remain mounted and operational. This is therefore a presentation refinement, not a new project-tool system.

The compact state uses restrained icon targets and hover labels. The existing clarity control still widens the same strip and reveals labels when explicit readability is needed. Search, Appearance and Focus surfaces remain invoked panels and stay attached immediately to the left of the utility strip.

The important hierarchy is now:

```text
primary Project work surface
secondary resizable Conversation dock
thin application-level Project utility edge
```

rather than three visually independent cards.

### Isolation and preserved behavior

The canonical no-query Project Grid rail is deliberately untouched. It retains the current accepted flat compact floating composition from Research 095/096 when Conversation is not co-present.

The edge-strip refinement is restricted to:

```text
conversation=adaptive-dock
Conversation open
presentation=copresent
Deep Dive not owning the work surface
```

Deep Dive + Conversation continues to use its dedicated split-workspace composition, where the project rail is not a competing third surface.

### Implementation and targeted verification

Implementation artifacts:

```text
frontend/design-lab/cockpit-practical-workspace-study.css
frontend/e2e/cockpit-reintegration-conversation-integration-study.spec.ts
frontend/e2e/cockpit-reintegration-adaptive-edge-rail.spec.ts
```

Current implementation/test head:

```text
b044dfb97039e178b7f5802e35c44a449bcca232
```

Existing Adaptive Conversation subsystem regression:

```text
workflow run  33267782088
job           99140848962
verification  V1 targeted
result        SUCCESS
browser tests 6 / 6 passing
```

Dedicated edge-utility-strip regression:

```text
workflow run  33267858446
job           99141018564
verification  V1 targeted
result        SUCCESS
browser tests 3 / 3 passing
```

The dedicated checks establish:

```text
compact rail is flush with the viewport top/right/bottom
compact width is approximately 56px
Conversation touches the tool strip at one direct seam
floating-card border radius is removed in co-presence
controls retain usable target height
clarity expansion widens the strip to approximately 196px
Conversation tracks the widened strip rather than overlapping it
labels remain available in clarity mode
standalone canonical Project Grid rail remains unchanged
```

A new full V3 gate is intentionally deferred at this visual-iteration stage. The relevant Conversation and edge-rail regressions are green, and the repository's risk-scaled verification method calls for targeted evidence during iteration, followed by a wider/full gate at a meaningful acceptance or promotion boundary. Human visual review remains the next authority for whether this new rail composition is actually better.