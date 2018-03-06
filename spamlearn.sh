#!/bin/bash

# Learn spam from spam folder
sa-learn --no-sync --spam /var/vmail/[domain]/[username]/.Junk/cur/

# Learn ham (non-spam messages) from inbox
sa-learn --no-sync --ham /var/vmail/[domain]/[username]/cur/
