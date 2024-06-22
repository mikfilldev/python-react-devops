#!/bin/sh

sleep 1

if [ ! -d /app/build ]; then npm run build; fi

serve -s build -l 3000
