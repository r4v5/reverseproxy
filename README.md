reverseproxy
============

Hopefully, this'll be a reverse proxy that can sit between Github's push notifications and private Jenkins servers.

TODO:
- Handle CSRF crumbs for places that have that enabled (and really, you should have that enabled)
- Turn off debug mode, because exposing a shell running with the privileges of the user running the app to the Entire Internet is kinda bad
- Return jenkins's response to github's server
