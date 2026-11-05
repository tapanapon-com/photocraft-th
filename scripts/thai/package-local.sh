#!/usr/bin/env bash
# Package the native host build for local testing. No notarization or Developer ID claim.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
DIST="$ROOT/dist/thai"
APP="$DIST/PhotoCraft.app"
STAGE="$DIST/dmg-stage"
VERSION=0.20.1-th.1
ARCH="$(uname -m)"
BINARY="$ROOT/target/release/photocraft"
[[ -x "$ROOT/target/release/photocraft-cli" ]] || { echo 'Build photocraft-cli --release --features heif first.' >&2; exit 1; }
[[ -x "$BINARY" ]] || { echo 'Build photocraft --release --features heif first.' >&2; exit 1; }
CRAFT_FONTS_DIR="${CRAFT_FONTS_DIR:-$ROOT/../craft-fonts}"
mkdir -p "$APP/Contents/Resources/Licenses"
for license in "$CRAFT_FONTS_DIR"/fonts/*/OFL.txt; do
  [[ -f "$license" ]] || continue
  family="$(basename "$(dirname "$license")")"
  cp "$license" "$APP/Contents/Resources/Licenses/OFL-$family.txt"
done
mkdir -p "$APP/Contents/MacOS" "$APP/Contents/Resources" "$STAGE"
cp "$BINARY" "$APP/Contents/MacOS/PhotoCraft"
cp "$ROOT/target/release/photocraft-cli" "$APP/Contents/MacOS/photocraft-cli"
cp "$ROOT/assets/app-icon/photocraft.icns" "$APP/Contents/Resources/PhotoCraft.icns"
cp "$ROOT/NOTICE" "$ROOT/ATTRIBUTION.md" "$ROOT/LICENSE-MIT" "$ROOT/LICENSE-APACHE" "$APP/Contents/Resources/"
cp "$ROOT/docs/localization-th.md" "$APP/Contents/Resources/"
sed -e "s/@VERSION@/$VERSION/g" -e 's/@SHORT_VERSION@/0.20.1/g' \
  -e "s/@BUILD_SHA@/$(git -C "$ROOT" rev-parse --short HEAD)-thai/g" \
  "$ROOT/packaging/macos/Info.plist.in" > "$APP/Contents/Info.plist"
printf 'APPL????' > "$APP/Contents/PkgInfo"
plutil -lint "$APP/Contents/Info.plist"
codesign --force --sign - --timestamp=none --identifier ai.storyteller.photocraft-cli "$APP/Contents/MacOS/photocraft-cli"
codesign --force --sign - --timestamp=none "$APP/Contents/MacOS/PhotoCraft"
codesign --force --sign - --timestamp=none "$APP"
codesign --verify --deep --strict "$APP"
ditto "$APP" "$STAGE/PhotoCraft.app"
[[ -L "$STAGE/Applications" ]] || ln -s /Applications "$STAGE/Applications"
DMG="$DIST/PhotoCraft-TH-$VERSION-macOS-$ARCH.dmg"
# A filesystem image preserves executable metadata when mounted.
hdiutil create -ov -fs HFS+ -format UDZO -srcfolder "$STAGE" -volname 'PhotoCraft Thai' "$DMG"
hdiutil verify "$DMG"
(cd "$DIST" && shasum -a 256 "$(basename "$DMG")" > "$(basename "$DMG").sha256")
echo "Local ad-hoc build (not notarized): $DMG"
