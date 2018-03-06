#!/bin/bash
sudo rndc dumpdb -cache
sudo less /var/cache/bind/named_dump.db
