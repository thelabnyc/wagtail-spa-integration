Project status - experiment. May change at any time without notice.

# Wagtail Single Page Application Integration

This project provides some tools for using Wagtail as an API only CMS that a JS application will consume.

It was designed to work with angular-wagtail - but works without Angular if you provide the client integration.

## Features

- Wagtail Redirect API
- Preview button support (requires saving draft, unlike typical Wagtail)
- Supports multiple wagtail sites

# Usage

- Install from pypi (coming soon)
- Ensure API is registered

## Multiple wagtail sites

Wagtail itself can support having one API "default" site and multiple sites branched from it. For example:

- api.example.com is where wagtail runs
- burkesoftware.com is one site served by wagtail
- passit.io is another site served by the same wagtail instance

This set up would require multiple Wagtail Sites and each Site needs it's own page.

- api.example.com should be the default wagtail site and a child of the root page.
- burkesoftware.com's Homepage should be a child of the api.example.com page. And should have a Site.
- passit.io's Homepage should be a child of the api.example.com page. And should have a Site.

The api.example.com page actually wouldn't be used in a API only use case. You may simply make it the Page Type "wagtailcore.Page".

## Usage without angular-wagtail

Review the angular-wagtail project and reimplement it's logic. Essentially you'll need to make a page router that loads pages from the api and connects wagtail pages to your view layer. For example a wagtail page HomePage would need to be connected to a JS HomePageComponent.

It's not likely that I'll be developing any of this, but if you make an integration for your favorite JS framework I'd be happy to note it here. Angular happens to be a good fit because we can expect certain resources to be available (Router Module, transfer state, etc).
