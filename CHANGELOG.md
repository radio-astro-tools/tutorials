# Changelog

All notable changes to this tutorial collection are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning uses **CalVer** (`YYYY.MM.DD`), matching this repo's existing
`2021_07_06` tag: a version marks a snapshot of the tutorial set (e.g. before
a workshop, or for a citable Binder link), not an API contract. Tag the
corresponding commit with the same date when a section is finalized.

## [Unreleased]

### Added
- Site header on rendered notebook pages and an issue-tracker link (#51).
- `nbstripout` pre-commit hook + CI check to keep notebooks output-free on `master` (#52).
- Breathing room below the injected nav bar on notebook pages (#53).

### Fixed
- `simple_norm` call updated to use `vmin`/`vmax` (#50).

<!--
Add new entries above this line, under Unreleased, grouped as:
  ### Added / ### Changed / ### Fixed / ### Removed

When cutting a snapshot:
1. Rename "Unreleased" to "[YYYY.MM.DD] - YYYY-MM-DD" (today's date).
2. Add a fresh empty "## [Unreleased]" section above it.
3. Tag the commit: git tag YYYY.MM.DD && git push origin YYYY.MM.DD
-->
