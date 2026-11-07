# Photocraft Thai upgrade 7 November 2026

Upstream release: https://github.com/storytold/photocraft/releases/tag/v0.21.0

Thai distribution being prepared: 0.21.0-th.1. Based on the complete upstream release tag, preserving its engine and format crate versions. Existing Thai translations remain, with new source strings translated. Current Thai catalog: 4,726 entries.

Catalog validation passed. Native build, platform packaging and integration checks are in progress. This record does not claim that installers have been released or that all upstream functionality has been tested. Previous 0.20.1 validation reports remain historical.

Mac builds are ad-hoc signed and are not Apple-notarized. Windows builds are unsigned. Build one job at a time.

## Font selection compatibility fix

Retyping the currently applied font name must remain an explicit query, and the first Down key must retain its exact match before stepping to substring matches. This addresses the previously observed Inter versus SignPainter selection failure on this Mac. A focused picker regression test and the existing selected-range font tests verify the behavior. The complete UI and integration suites passed after the fix (5,513 tests, 23 ignored). Clippy, dependency layering and both wasm checks passed. Source scanning identified 29 additional strings beyond the reference-catalog union; those are now translated and are being revalidated.

Final source validation: 4,726 Thai entries, 2,361/2,361 source keys, 63 localization checks after the last catalog update. Clippy and both wasm checks passed again for that final catalog. Full UI and integration tests passed (5,513 tests, 23 ignored); updater checks passed (4). The previous three font-selection failures are resolved. Platform packages are the next step.
