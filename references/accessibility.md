# Accessibility review for WCAG 2.1 and 2.2 AA

Use this workflow in full website reviews and new builds, and for the affected content and interactions in scoped updates. An accessibility-only request uses this workflow without requiring a marketing redesign. For a visual concept or screenshot-only review, report observable issues and implementation requirements; do not claim functional checks were performed.

## Scope, versions, and evidence

Default to **WCAG 2.1 Level AA and WCAG 2.2 Level AA**, including each version's Level A requirements. Honor an explicitly different target. Report results separately by version rather than combining them into a compliance percentage. AAA requirements and other usability recommendations may be useful, but label them separately from A/AA failures.

Record the target versions, inspection date, site/environment, pages, complete journeys, states, browser/operating system, viewport/zoom settings, assistive technologies actually used, and available tools. Check navigation and representative page types, plus relevant menus, dialogs, forms, error/success states, media, cookie controls, and embedded services. Include public login or signup steps when they belong to the requested journey; this does not authorize an unrelated authenticated-app redesign. Identify exclusions and linked documents requiring a separate review. Do not silently exclude third-party content that affects the page or process.

Use the index below to account for all A/AA criteria within the declared scope. The short prompts are an original review aid, not replacements for the normative requirements, definitions, exceptions, or conformance rules. Consult the linked W3C standards and their criterion-specific Understanding pages when deciding applicability or an exception. If those sources cannot be accessed and the decision is uncertain, record the uncertainty rather than guessing.

Current source baseline: WCAG 2.1 Recommendation dated 2025-05-06 and WCAG 2.2 Recommendation dated 2024-12-12; checked 2026-11-24. Later standards guidance may clarify interpretation; record the version used in an actual review.

## Run the checks the environment supports

1. **Inspect the rendered journey.** Establish what people must perceive and operate. Examine the actual DOM and accessibility information when available; repository source alone does not prove deployed behavior. Inspect relevant responsive layouts and interaction states, not just the homepage's initial screen.
2. **Use available automated checks.** Run an existing accessibility scanner when the environment provides one. Include the applicable A/AA rules for 2.1 and 2.2, including their shared 2.0 requirements. Record the engine/version, supported rules or tags, pages/states, and exclusions. Verify findings, preserve items needing review, and identify coverage gaps. Do not assume all tools support the same versions or that enabling only 2.2-specific rules tests the earlier requirements. No scanner, dependency, browser, paid service, or screen reader is bundled with this skill.
3. **Perform interaction and human checks.** Follow the practical checks below using available capabilities. Reading markup, an accessibility tree, or an automated browser trace is not equivalent to operating a real screen reader. If a required capability is unavailable, provide the steps for a person to complete and mark that portion **Not tested**. In Claude or ChatGPT sessions with only text/images, deliver a limited review and manual test plan rather than invented scan results.
4. **Fix and retest only within the requested scope.** Review-only requests produce findings. When edits are authorized, reproduce the issue, make a targeted fix, and rerun the relevant automatic and manual checks. Distinguish recommended, applied, and retested fixes. Use authorized test data and environments for form submissions or transactions; a review does not authorize sending a live message or placing an order.

## Practical checks and common interpretation errors

- **Keyboard and focus:** Traverse the journey using Tab, Shift+Tab, and each control's expected keys. Verify activation, meaningful order, visible focus, escape from widgets, dialog focus handling, and return to the invoking control. Check fixed headers, cookie banners, and open overlays. Under 2.4.11, an author-created overlay must not entirely hide the focused component; stricter full visibility belongs to AAA 2.4.12. Do not mistake a source-code focus style for a verified rendered focus indicator.
- **Screen-reader operation:** When available, record the actual screen reader and browser. Check reading order, headings/landmarks, image meaning, names/roles/states, form instructions/errors, and announcements after updates. A successful scan cannot establish understandable announcements or complete task operation. Missing access to a screen reader means this testing is not completed.
- **Contrast:** Measure the actual rendered foreground/background combinations, including transparency and relevant states. Under 1.4.3, normal text needs 4.5:1; large text needs 3:1. Large means at least 18 pt (24 CSS px) regular or 14 pt (about 18.67 CSS px) bold. Do not round a failing ratio upward. Under 1.4.11, required visual information for controls, states, and graphics generally needs 3:1 against adjacent colors. Check the criterion's exceptions, including inactive controls and logo text; a logo exception does not exempt nearby navigation or a whole brand palette. Measure rather than estimating from a screenshot.
- **Resize, reflow, and text spacing:** Check text enlargement to 200% without lost content/function (1.4.4). For vertically scrolling content, verify reflow at 320 CSS px; for horizontally scrolling content, use 256 CSS px height (1.4.10). Browser zoom to 400% from a 1280 CSS px starting width is a useful reflow test. Record actual browser zoom and layout dimensions; viewport resizing alone is not proof of browser-zoom behavior. Apply the criterion's two-dimensional-layout exceptions carefully. Test user overrides for line height 1.5 times font size, paragraph spacing 2 times, letter spacing 0.12 times, and word spacing 0.16 times (1.4.12), with applicable language/script exceptions. These are override tests, not mandatory default styling values.
- **Pointer and touch:** Check simple alternatives to multipoint/path gestures, cancellation of unintended activation, and a non-dragging single-pointer way to perform drag actions. For 2.5.8, test a 24 by 24 CSS px target or a qualifying exception, such as sufficient separation using the specified 24 CSS px circles around undersized targets. Inline links and other exceptions need a reason. The 44 by 44 CSS px target in 2.5.5 is AAA, not a universal AA requirement. A keyboard alternative alone does not satisfy 2.5.7's single-pointer requirement.
- **Forms and authentication:** Check persistent labels/instructions, input purpose, clear errors and corrections, accessible status updates, and appropriate review/correction/reversal for consequential submissions. Check reused information within the same process under 3.3.7. For in-scope authentication, examine password-manager support, paste, and accessible alternatives/assistance for cognitive tests under 3.3.8, including its exceptions. Do not report every CAPTCHA on every form as a 3.3.8 failure; determine whether authentication is involved and also check the relevant non-text, keyboard, and other criteria.
- **Media, timing, and motion:** Assess accurate captions, required audio description/alternatives, player operation, timing controls, flashing, and pause/stop/hide behavior. A transcript alone does not replace all required captions or audio description. Reduced-motion support is useful, but it neither satisfies every media requirement nor makes AAA 2.3.3 an AA requirement. Assess 2.2.2 separately: the over-five-second condition concerns qualifying moving/blinking/scrolling content; qualifying auto-updating content has no such duration threshold. Avoid exposing a person to suspected hazardous flashing to prove a failure; use suitable analysis or report that test as pending.
- **Semantics and consistency:** Check structure, reading order, language, link purpose, help placement, and predictable controls. Prefer native HTML where suitable. Do not invent failures solely from a heading-level preference, the absence of ARIA on an already semantic control, or a decorative image's intentionally empty alternative.

## Criterion coverage index

Every row below needs an applicability decision and evidence/status for the declared scope. Group repeated instances in findings, but retain a criterion-level coverage record. A criterion absent from a scanner's output is not automatically passed or not applicable.

### Shared requirements in 2.1 AA and 2.2 AA

| Criterion | Level | Review prompt |
| --- | --- | --- |
| 1.1.1 | A | Do images and other non-text content have appropriate equivalents or a justified exception? |
| 1.2.1 | A | Are suitable alternatives available for prerecorded audio-only or video-only content? |
| 1.2.2 | A | Are prerecorded synchronized-media captions present and accurate where required? |
| 1.2.3 | A | Is the required description or media alternative available for prerecorded synchronized media? |
| 1.2.4 | AA | Does live synchronized media have the required captions? |
| 1.2.5 | AA | Does prerecorded synchronized video include the required audio description? |
| 1.3.1 | A | Are visually conveyed relationships and structure also available programmatically or in text? |
| 1.3.2 | A | Does the programmatically available sequence preserve the meaning? |
| 1.3.3 | A | Can instructions be understood without relying only on sensory characteristics? |
| 1.3.4 | AA | Does content work in both orientations unless one is essential? |
| 1.3.5 | AA | Can software identify applicable inputs collecting information about the user? |
| 1.4.1 | A | Is information conveyed through something in addition to color? |
| 1.4.2 | A | Can users stop/pause qualifying automatic audio or control it separately? |
| 1.4.3 | AA | Do applicable text/background pairs meet the required contrast? |
| 1.4.4 | AA | Does enlarging text to 200% preserve content and operation? |
| 1.4.5 | AA | Is real text used instead of text rendered as imagery unless an exception applies? |
| 1.4.10 | AA | Does content reflow at the specified dimensions with only justified two-dimensional exceptions? |
| 1.4.11 | AA | Do required control/state indicators and meaningful graphics have sufficient contrast? |
| 1.4.12 | AA | Do the specified user text-spacing overrides preserve content and function? |
| 1.4.13 | AA | Can additional hover/focus content be dismissed, hovered, and kept visible as required? |
| 2.1.1 | A | Can the functionality be operated through a keyboard interface, subject to the exception? |
| 2.1.2 | A | Can a keyboard user leave each component without becoming trapped? |
| 2.1.4 | A | Can character-only shortcuts be disabled/remapped or limited to the focused component? |
| 2.2.1 | A | Can users manage time limits as required, or does a documented exception apply? |
| 2.2.2 | A | Can users control qualifying movement, blinking, scrolling, and auto-updating content? |
| 2.3.1 | A | Is flashing within the permitted frequency or flash thresholds? |
| 2.4.1 | A | Can users bypass repeated blocks of content? |
| 2.4.2 | A | Does each page have a useful title reflecting its purpose? |
| 2.4.3 | A | Does focus order preserve meaning and operation? |
| 2.4.4 | A | Can users understand a link's purpose from its permitted context? |
| 2.4.5 | AA | Are multiple ways to locate pages provided where required? |
| 2.4.6 | AA | Do headings and labels describe their subject or purpose? |
| 2.4.7 | AA | Is keyboard focus visibly identifiable? |
| 2.5.1 | A | Is a simple single-pointer alternative available for qualifying complex gestures? |
| 2.5.2 | A | Can unintended pointer actions be avoided, aborted, or undone as required? |
| 2.5.3 | A | Does a control's accessible name include its visible textual label? |
| 2.5.4 | A | Is motion-triggered functionality also available through controls, with motion disablement where required? |
| 3.1.1 | A | Can software determine the page's default language? |
| 3.1.2 | AA | Are relevant changes of language identified, subject to the exceptions? |
| 3.2.1 | A | Does receiving focus avoid an unexpected change of context? |
| 3.2.2 | A | Do input changes avoid unexpected context changes unless users are informed first? |
| 3.2.3 | AA | Is repeated navigation ordered consistently across the page set? |
| 3.2.4 | AA | Are components with the same functionality identified consistently? |
| 3.3.1 | A | Are automatically detected input errors identified and described in text? |
| 3.3.2 | A | Are necessary labels and instructions supplied for user input? |
| 3.3.3 | AA | Are known corrections suggested unless doing so compromises security or purpose? |
| 3.3.4 | AA | Can consequential legal/financial/data/test submissions be reversed, checked, or confirmed as required? |
| 4.1.2 | A | Are control names, roles, values, and changes exposed correctly to assistive technology? |
| 4.1.3 | AA | Can assistive technology announce appropriate status messages without moving focus to them? |

### Additional requirements in 2.2 AA

These six criteria are not requirements of 2.1 AA. Report them under 2.2 even when the same component also has a shared-criterion issue.

| Criterion | Level | Review prompt |
| --- | --- | --- |
| 2.4.11 | AA | Is the focused component never entirely covered by author-created content? |
| 2.5.7 | AA | Can drag-based operations be performed with a single pointer without dragging, unless exempt? |
| 2.5.8 | AA | Do pointer targets meet the 24 CSS px sizing/spacing rule or a specific exception? |
| 3.2.6 | A | Are repeated help mechanisms in a consistent relative order, subject to the exception? |
| 3.3.7 | A | Can previously supplied information be reused within the same process unless exempt? |
| 3.3.8 | AA | Does each authentication step avoid an unassisted cognitive test or provide a qualifying alternative/exception? |

### The 2.1 parsing entry

| Criterion | Level | Version handling |
| --- | --- | --- |
| 4.1.1 | A | Retained in 2.1 with updated W3C notes; removed from 2.2. For HTML/XML, record it as satisfied under the current 2.1 note, with that basis explicitly stated. For other markup, check the applicable normative requirement. In 2.2, record it as not applicable because it was removed. |

Do not resurrect a 4.1.1 failure from an older scanner's duplicate-ID or parsing warning. Investigate the actual effect and map any confirmed name, role, relationship, or other problem to the criterion it violates. This does not make malformed markup harmless. The index has 49 shared entries, six additions for 2.2, and this separate 2.1 entry: 50 entries to account for in 2.1 and 55 in 2.2.

## Report findings and coverage

For each criterion, use **Passed**, **Failed**, **Not applicable**, or **Not tested**, qualified by the tested scope:

- **Passed:** the applicable requirement was actually evaluated with sufficient evidence across the declared in-scope instances/states. List the method and evidence. A scan rule pass is evidence only for what that rule tested.
- **Failed:** a confirmed counterexample exists. Describe the reproduction and user impact even if other instances still need testing.
- **Not applicable:** the condition is absent or a valid exception applies, with a reason based on inspection. Inaccessible material and missing tools are not evidence of non-applicability.
- **Not tested:** evidence is missing or incomplete. State the remaining method, page/state, or human check needed. When only some instances passed, retain that evidence while marking the criterion's overall coverage incomplete.

Supply a compact coverage table with criterion ID, level, version(s), status, tested pages/states, method/evidence, and outstanding checks. A focused change may list relevant criteria and explicitly identify the rest as outside this limited review; do not imply full-site coverage. A full accessibility review accounts for every indexed criterion, including those not tested.

For actionable findings, include URL/component/state, reproduction steps, expected versus observed behavior, applicable criterion(s) and version, user impact, priority, recommended fix, and retest result. Group a repeated component problem without losing affected pages. Prioritize blocked tasks before other barriers; WCAG levels do not set defect severity. Preserve failures until an actual retest supports closing them.

Do not turn a scanner score, a selected-page sample, a screenshot review, or an incomplete matrix into a claim that the whole site conforms. WCAG conformance has requirements for full pages, complete processes, accessibility-supported technology use, and non-interference in addition to success criteria. State the exact tested scope and remaining limitations. This skill supports accessibility review and remediation; it does not issue ADA certification, a legal opinion, or a guarantee of accessibility. Do not add a compliance badge or publish a conformance claim on the user's behalf merely because checks ran.

## Authoritative references

- [WCAG 2.1 requirements and conformance rules](https://www.w3.org/TR/WCAG21/)
- [WCAG 2.2 requirements and conformance rules](https://www.w3.org/TR/WCAG22/)
- [W3C explanation of the parsing change](https://www.w3.org/WAI/standards-guidelines/wcag/faq/#parsing411)
- [W3C evaluation guidance and the role of human testing](https://www.w3.org/WAI/test-evaluate/)
- [W3C explanation of target sizing and its exceptions](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- [W3C explanation of accessible authentication](https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html)
- [W3C explanation of obscured focus](https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html)

Keep this reference generic to the site under review. It does not prescribe a particular brand, framework, jurisdiction, scanner, or paid service.
