# Build a new site or implement updates

## Match the requested outcome

Distinguish a visual concept, a working local site, a shareable preview, and a production deployment. Build to the requested level. If tools or access prevent implementation, deliver the most useful complete design or code artifact available and identify the specific remaining dependency.

Inspect the existing project and its instructions before choosing tools. Reuse its framework, design tokens, components, and established conventions where appropriate. For an empty project, choose a simple approach suited to the requested content and behavior. Do not add a CMS, account system, database, payment service, or large dependency solely because such sites sometimes use one.

## Shape the content before decoration

Create a concise page map and visitor path based on the brief. Use the smallest set of pages and sections that answers the audience's real questions. Not every site needs pricing, testimonials, a product tour, or a sales funnel. An informational site may primarily help people find and understand material.

Draft the actual headline, supporting text, main actions, and essential sections early. Carry supported facts into the design. Use clearly marked placeholders only for genuinely missing information; identify consequential gaps before treating the site as ready to publish.

For updates, retain working content and structure unless the task or evidence justifies a change. Account for existing URLs, incoming links, metadata, and redirects when moving content.

## Establish a coherent visual system

Use [shared checks](design-and-content.md) to define color roles, type hierarchy, spacing, content widths, image treatment, and controls. Reuse approved assets. When no identity is supplied, choose a coherent provisional direction and state the assumptions; do not let an absent brand manual block a first working version.

Let the audience and content determine the composition. Avoid repeating one fashionable layout across unrelated projects. Make opening text and actions available immediately, and use product or subject imagery to clarify rather than decorate.

Design for both wide and narrow viewports. Plan how columns, navigation, headings, imagery, and tables adapt. Check the actual exported or hosted artifact: an embedded preview's fixed width or oversized media can produce a poor standalone desktop page.

## Implement useful behavior

Use working destinations for navigation and actions. Implement needed menu, disclosure, tab, and demo states with semantic controls, keyboard access, visible focus, and appropriate labels. Make loading, empty, success, and error states meaningful for the behaviors in scope.

Connect forms and other integrations only when the relevant functionality and destination are authorized. Verify real success before showing a success message. When a backend is outside scope, label the interaction as a demonstration or provide an honest alternative; do not imply that a message, booking, or payment was processed.

Keep sample data fictional. Do not embed secrets or private data in frontend assets. Preserve required asset and font licenses. Use proper image sizing and responsive assets, and avoid unnecessary script or media weight.

## Verify the result

Choose checks proportional to the work and run the project's relevant build, lint, or test commands where available. Do not create a large test suite for a simple copy or spacing change. For a new site or meaningful layout change, inspect:

- Desktop and phone rendering, with extra widths for observed breakpoint issues.
- Navigation, primary and secondary actions, anchor destinations, and direct page loads.
- Essential interaction states, keyboard operation, focus visibility, labels, and reduced motion where applicable.
- Text readability, actual color contrast, image crops, logo backgrounds, long content, and horizontal overflow.
- Forms and integrations in authorized test conditions; otherwise explicitly mark delivery or backend behavior as unverified.
- Page titles, descriptions, missing assets, index settings, and redirects relevant to the work.

Fix failures within scope and recheck the affected behavior. Use screenshots of the actual result to support visual claims. Source inspection and a successful build alone do not prove the rendered experience.

## Preview, publish, and hand off

When a preview is requested, use the project's normal preview mechanism or another destination the user has authorized. An unlinked page is publicly accessible if its URL is known; no-index directives do not provide access control. Use actual access restrictions when privacy is required.

Publish when it is in the authorized scope and the result is ready. If a necessary approval is still missing, finish the reviewable implementation first and request only that final decision. After publication, verify the deployed page and primary journey rather than treating an upload or push as proof of success.

Deliver the usable preview or output files, concise setup notes where needed, what changed, and the checks actually performed. Record any remaining content decisions or integration limits. Never describe a local-only site as live or an illustrative experience as connected product functionality.
