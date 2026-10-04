title: Privacy policy — Triage: Boxes for Gmail
description: The Chrome extension collects, transmits, sells and shares nothing. There is no server, no analytics and no third party.
updated: 2026-10-04

# Privacy policy — Triage: Boxes for Gmail

<p class="lead">Triage is a Chrome extension by OtterMade that puts a row of boxes above your Gmail inbox and files mail into Gmail labels when you drag or click. This page is its privacy policy.</p>

**Last updated: 4 October 2026.** The substance is unchanged since 30 July 2026; this date marks the move of the policy to this public page.

## The short version

This extension does not collect, transmit, sell, or share anything. There is no server, no analytics, no tracking, no advertising, and no third party of any kind. Your mail never leaves your browser except through Google's own interfaces, which it already does.

If that is all you needed, you can stop here.

## What the extension does

It adds a strip of boxes above your Gmail inbox and files mail into Gmail labels when you drag or click. Everything it does is something you could do by hand in Gmail: apply a label, remove a label, take a mail out of the inbox.

**It never deletes mail.** There is no code path in it that deletes a message, a thread, or a Gmail label.

## What is stored, and where

Two things, both locally:

1. **Your box and tab configuration** — names, the one-line rules, colours, and any templates you saved.
2. **Your Google account address**, but only in the optional build that uses the Gmail API, and only after you have signed in to it. It is kept so the hourly token renewal can name the account and stay silent; without it Google asks which account to use every time. The published build never has it.

Both use Chrome's extension storage. If you are signed into Chrome, Chrome may sync the configuration between your own devices, the same way it syncs bookmarks. That is between you and Chrome; the extension has no server for any of it to go to.

**No message content is ever stored.** Not subjects, not senders, not bodies. The extension reads a thread's identifier so it can tell Gmail which mail you dragged, and that identifier is used for the length of that one action and then discarded.

## Network requests

The extension makes no network requests of its own.

In the published build there is no network access at all: filing is done by operating Gmail's own menus, exactly as if you had clicked them.

If you have configured your own Google API credentials — an optional, self-built setup — the extension additionally talks to `https://gmail.googleapis.com` to apply labels directly, because it is faster. Those requests go to Google, using credentials you created, under your own Google Cloud project. They go nowhere else.

## Google user data

Where the Gmail API is used, the extension requests one scope:

- `https://www.googleapis.com/auth/gmail.modify` — to add and remove labels, and to read the label names and counts shown on the boxes.

This is used **only** to provide the features you can see: filing mail into boxes and showing counts on them. It is not used for any other purpose. It is not transferred to anyone. It is not used for advertising, for training any model, or for determining creditworthiness or lending. No human reads it.

Access tokens are held in memory and in Chrome's session storage, are never written to disk, and are discarded when the browser closes.

This use complies with the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy), including the Limited Use requirements.

## Permissions, and why each exists

| Permission | Why |
|---|---|
| `storage` | To remember your boxes and tabs between sessions. |
| Host access to `mail.google.com` | To show the strip inside Gmail and read the list you are dragging from. |
| `identity` *(optional build only)* | To let you sign in to your own Google Cloud project, if you configured one. |
| Host access to `gmail.googleapis.com` *(optional build only)* | To apply labels through the Gmail API rather than by driving menus. |

The published build ships without the last two.

## Children

The extension is not directed at children and collects nothing from anyone.

## Changes

Any change to this policy changes the date at the top. Every earlier version stays readable in the public history of this site: <https://github.com/ottermade/ottermade.github.io>.

## Contact

Questions or concerns: use the support link on the extension's Chrome Web Store page.
