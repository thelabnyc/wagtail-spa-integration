# 3.0.0

- Add Wagtail 4.1.x compatibility. Drop all previous wagtail versions.

# 2.1.3

- Add Wagtail 2.13 compatibility (no breaking changes)

# 2.1.2

- Fix bug when editing pages with wagtail 2.10

# 2.1.1

- Fix Wagtail 2.9 compatibility issue with getting site

# 2.1.0

- Base preview on wagtail-headless-preview to simplify our code base. Migration is optional in this release but may be required in the future.

To migrate:

- Remove `wagtail_spa_integration` from settings.py
- Follow README.md instructions for to configure wagtail-headless-preview

# 2.0.0

- Minimum Wagtail version is now 2.8 - making this a major version bump
- Compatibility with Wagtail 2.9 and fixes deprecation warnings for 2.9+

# 1.1.0

- Added support for drafts when a user edits a slug field by searching revision data for slugs
