# CI verification report

## Local clean-source verification

Steg 12 verifierades med samma ordning som GitHub Actions-workflowen använder:

1. Generate runtime parity report — PASS
2. Validate project contracts and eval definitions — PASS
3. Lint — PASS, 0 errors, 0 warnings
4. Deterministic pytest suite — PASS, 3 tests
5. Project hygiene (final, fix safe caches) — PASS
6. Build `project`, `chat_zip`, `custom_gpt` with CI version `0.0.0-ci` — PASS
7. Validate generated Chat and Custom distributions — PASS
8. Required artifacts and checksums — PASS

## Eval status

Nine eval definitions are schema-valid and are included in the project. The deterministic CI suite checks their structure and core invariants. Live cross-model execution remains a release-readiness requirement because this environment has no independent model runner.

## Release build behavior

`.github/workflows/release.yml` derives the artifact version from a published GitHub Release tag matching `vMAJOR.MINOR.PATCH` with optional suffix, then rebuilds and validates all artifacts before upload.
