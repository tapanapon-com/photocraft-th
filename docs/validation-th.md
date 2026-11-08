# Thai localization validation — 2026-11-05

Historical report for 0.20.1-th.1. The font-selection failures below were resolved in 0.21.0-th.1; see [current validation](validation-0.21.0-th.1.json) and the [upgrade log](thai-upgrade-20261107.md).

Environment: macOS 26.3.1, Apple Silicon (arm64). Upstream source: `8e9277e20e8d5185ed4259908022a719a647237e`, PhotoCraft 0.20.1.

## Passed

- Catalog: 4,627 entries; all 4,571 keys in reference catalogs plus 56 newly discovered source keys. No duplicate keys, missing placeholders, changed numeric values, escaped-newline/tab mismatches, shortcut-symbol mismatches or incorrect Thai plural forms.
- `xtask i18n-coverage`: Thai 2,272/2,272 source-derived keys (100%).
- Localization unit/live tests: 61 passed, including regional Thai preferences, packed-catalog consistency and switching languages without replacing the document.
- Integration tests: 187 passed, 1 ignored.
- Clippy (`--all-targets -- -D warnings`), rustfmt, dependency layering and wasm checks passed. Wasm check includes HEIF.
- Desktop smoke: created a document with Thai text and multiple layers; saved/reopened `.pcraft`; switched Thai → English → Thai; exported PNG. The UI screenshot and exported PNG were visually inspected for Thai shaping.
- GPU viewport-page test passed when rerun alone (0.82 s); it timed out in the full run while builds and other tests were active.

## Remaining test failures

The full library run reported **4,842 passed, 4 failed, 21 ignored**. The GPU test above subsequently passed. Three font-selection tests still fail when run alone on this Mac:

- `selected_fonts_commit_pattern_0`
- `selected_fonts_commit_pattern_2`
- `selected_fonts_commit_pattern_3`

The assertion expected `Inter` but observed the installed `SignPainter` face after an arrow/Enter/checkmark sequence. The font-selection implementation is unchanged by this localization. This report does **not** claim the entire upstream test suite is green; the remaining failures are recorded rather than hidden or disabled.

Tests use upstream craft-fonts at `b076417b5880bd4154bd22f00695b1d28c6bea83`. `TMPDIR` was placed on the T7 drive because the system temporary disk was below PhotoCraft's free-space threshold, which otherwise overwrote expected status messages with scratch-disk warnings.

## Distribution limitations

This is an independently modified local build. It is ad-hoc signed, not Developer ID signed or Apple-notarized. The DMG supports Apple Silicon only. Technical names, document/layer names and some engine diagnostics and OS/third-party error messages may remain in their original language. Catalog coverage is not a claim of universal translation of every external message.

## Packaged artifact and installation

- Artifact: `dist/thai/PhotoCraft-TH-0.20.1-th.1-macOS-arm64.dmg`.
- SHA-256: `75d1378113bf476f5864ba64e581418f01bf17b4ed8d27395809be7508b0dfcf`.
- HFS+ filesystem image created with `hdiutil create -srcfolder`; checksum verification passed.
- Mounted read-only: app/CLI signatures passed `codesign --verify --deep --strict`; both executables matched the tested app; Applications symlink points to `/Applications`. Volume detached after verification.
- Avoided the hybrid-image route: it introduced an empty FinderInfo attribute on the mounted CLI and failed strict signature verification on this Mac.
- Packaged app smoke passed again, including native document round-trip, PNG export and Thai dialogs.
- Installed at `/Applications/PhotoCraft.app`, signature and executable comparison passed, saved `interface.language = th`, and confirmed the installed process started.
- Previous app and preferences retained under `dist/backups/`. Screenshots and the synthetic demo are under `dist/thai/`.
