title: Privacy policy — Triage: Boxes for Gmail
description: The Chrome extension collects, sells and shares nothing. It talks only to Google, from your browser. There is no server, no analytics and no third party.
updated: 2026-10-06

# Privacy policy — Triage: Boxes for Gmail

<p class="lead">Triage is a Chrome extension by OtterMade that puts a row of boxes above your Gmail inbox and files mail into Gmail labels when you drag or click. This page is its privacy policy.</p>

**Last updated: 6 October 2026.** What changed since 4 October: the extension published on the Chrome Web Store now lets you sign in with Google and files mail through the Gmail API. It used to work only by operating Gmail's menus. It can also delete a Gmail *label*, never mail, when you ask it to and confirm. Nothing is collected, sold or shared, as before.

## The short version

This extension does not collect, transmit, sell, or share anything. There is no server, no analytics, no tracking, no advertising, and no third party of any kind. When you sign in with Google, it talks to Gmail's own API from your browser, and to nothing else.

If that is all you needed, you can stop here.

## What the extension does

It adds a strip of boxes above your Gmail inbox and files mail into Gmail labels when you drag or click. Everything it does is something you could do by hand in Gmail: apply a label, remove a label, take a mail out of the inbox.

**It never deletes mail.** There is no code path in it that deletes a message or a thread. It deletes a Gmail *label* only when you ask it to, with "Tidy labels" or "delete this tab's labels", and only after you confirm. The mail under a deleted label stays in your mailbox.

## What is stored, and where

Two things, both locally:

1. **Your box and tab configuration** — names, the one-line rules, colours, and any templates you saved.
2. **Your Google account address**, once you have signed in. It is kept so the hourly token renewal can name the account and stay silent; without it Google asks which account to use every time.

Both use Chrome's extension storage. If you are signed into Chrome, Chrome may sync the configuration between your own devices, the same way it syncs bookmarks. That is between you and Chrome; the extension has no server for any of it to go to.

**No message content is ever stored.** Not subjects, not senders, not bodies. The extension reads a thread's identifier so it can tell Gmail which mail you dragged, and that identifier is used for the length of that one action and then discarded.

## Network requests

Every request the extension makes goes to Google, from your browser. There is no server of ours for anything to go to.

- **The Gmail API** (`https://gmail.googleapis.com`), once you have signed in with Google: to apply and remove the labels your boxes stand for, create and rename those labels, and read how many conversations each holds.
- **Sign-in** (`https://accounts.google.com`): Google's own sign-in page, which hands the extension a short-lived access token.
- **Gmail's unread feed** (`https://mail.google.com/mail/u/…/feed/atom/<label>`), only if you have not signed in: to show each box's unread count without the API. That request goes to Gmail, on the page you already have open, signed in as you already are. The feed also lists the subjects and snippets of a few unread mails; the extension reads only the label's name and the count, and keeps neither the rest nor the count beyond the next refresh.

If you decline to sign in, the extension still works by operating Gmail's own menus, exactly as if you had clicked them.

## Google user data

When you sign in, the extension requests one scope:

- `https://www.googleapis.com/auth/gmail.modify` — to add and remove labels, and to read the label names and counts shown on the boxes.

This is used **only** to provide the features you can see: filing mail into boxes and showing counts on them. It is not used for any other purpose. It is not transferred to anyone. It is not used for advertising, for training any model, or for determining creditworthiness or lending. No human reads it.

Access tokens are held in memory and in Chrome's session storage, are never written to disk, and are discarded when the browser closes.

This use complies with the [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy), including the Limited Use requirements.

## Permissions, and why each exists

| Permission | Why |
|---|---|
| `storage` | To remember your boxes and tabs between sessions. |
| Host access to `mail.google.com` | To show the strip inside Gmail, read the list you are dragging from, and read each box's unread count from Gmail's unread feed. |
| `identity` | To let you sign in with your Google account, so filing goes through the Gmail API. |
| Host access to `gmail.googleapis.com` | To apply and remove labels, create and rename them, and read their counts through the Gmail API. |

## Children

The extension is not directed at children and collects nothing from anyone.

## Changes

Any change to this policy changes the date at the top. Every earlier version stays readable in the public history of this site: <https://github.com/ottermade/ottermade.github.io>.

## Contact

Questions or concerns: use the support link on the extension's Chrome Web Store page.
