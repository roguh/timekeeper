#!/bin/sh
exec uvicorn src.timekeeper_server.main:app $@