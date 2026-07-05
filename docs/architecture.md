# Email Response Agent Architecture

Email support agent that classifies inbound support emails, generates contextual draft responses, prioritizes by urgency, routes to specialists, and tracks resolution metrics.

## Domain Tools

- **classify_email**: Classify inbound support email by category, urgency, and sentiment
- **draft_response**: Draft a contextual response to a support email
- **route_email**: Route email to the appropriate specialist queue
- **detect_duplicate**: Detect if this email is a duplicate or follow-up
- **track_sla**: Track email response SLA compliance