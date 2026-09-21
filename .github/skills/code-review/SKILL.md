---
name: code-review
description: "Use when reviewing a pull request, patch, or code change for correctness, security, maintainability, design quality, and test coverage. Produce a prioritized review with evidence, severity, and actionable fixes."
---

# Code Review

## Purpose

Review a change for correctness, risk, and maintainability before merge. Focus on evidence and user impact, not style alone.

## When to use

- Before approving or merging a pull request
- When validating a fix or regression patch
- When assessing a change in logic, API behavior, or data flow
- When checking whether tests and docs match real behavior

## Workflow

### 1. Understand the scope and intent

- Read the summary, diff, and relevant changed files
- Identify the intended behavior, user-facing impact, and boundaries of the change
- Note which APIs, inputs, outputs, and contracts are affected

### 2. Check correctness first

- Trace the main execution path and data flow
- Evaluate edge cases: nulls, empty values, invalid inputs, retries, concurrency, timeouts, boundaries, and error states
- Compare the implementation against the expected contract or requirement
- Look for logic that is correct in the happy path but fails under realistic conditions

### 3. Review the evidence

- Check whether the patch includes or needs regression tests
- Verify that tests cover the changed behavior and the failure mode being fixed
- Run the smallest relevant validation command or test slice when possible
- Prefer evidence from actual execution over assumptions

### 4. Evaluate risk areas

- Security: auth, validation, sanitization, secrets, injection, unsafe deserialization, access control
- Reliability: retry logic, cleanup, rollback, ordering, race conditions, partial failures, idempotence
- Performance: loops, repeated queries, memory growth, serialization cost, blocking I/O, unbounded work
- Maintainability: duplication, hidden coupling, unclear naming, fragile abstractions, poor error handling

### 5. Prioritize findings

Classify each issue before writing the review:

- Critical: correctness, security, data integrity, or release blocker
- Major: likely bug, degraded behavior, or significant risk
- Minor: clarity, maintainability, naming, or cleanup

### 6. Write the review

Provide concise, actionable findings:

- Affected file or function
- What is wrong or risky
- Why it matters
- Evidence from code, tests, or runtime behavior
- Recommended fix or next step

Keep the review professional and specific. Separate must-fix items from optional suggestions.

### 7. Verify the follow-up

After the author addresses comments, re-check the revised behavior and confirm the change still satisfies the original requirement and the relevant tests.

## Decision points

- If the issue affects correctness or user data, review it before style or polish.
- If there is no test coverage, request it unless the behavior is trivial and obvious.
- If the change modifies public behavior, inspect compatibility, docs, and backward-compatibility assumptions.
- If the patch introduces I/O, mutation, or state changes, validate error-handling and retry semantics.
- If a comment is only stylistic, keep it as a low-priority note rather than a blocker.

## Completion checklist

A review is complete when all of the following are true:

- The change’s intent and scope are understood
- The core logic has been traced for edge cases and failure modes
- Risk areas have been checked: security, reliability, performance, and maintainability
- Test coverage and validation evidence were reviewed
- Findings are prioritized and actionable
- The final recommendation is clear: approve, request changes, or discuss further

## Output format

Return the review in this structure:

1. Summary: short assessment of the patch and overall risk
2. Findings: numbered list with severity, evidence, and suggested fix
3. Questions: missing context or assumptions that need clarification
4. Recommendation: approve, request changes, or needs discussion

## Examples of good review comments

- “This path throws when input is empty, but the API contract allows empty input; the current implementation will crash in production. A guard clause or validation check is needed before the loop.”
- “The function retries on every exception without limiting backoff, which can amplify load under a transient dependency outage.”
- “No regression test covers this failure mode; please add one to lock in the expected behavior.”

## Anti-patterns to avoid

- Reviewing only style while ignoring correctness or security
- Making vague statements without code references or evidence
- Blocking on minor issues before addressing critical defects
- Recommending a fix without explaining the root cause or impact
