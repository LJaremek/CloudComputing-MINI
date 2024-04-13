#!/bin/bash

# Assigning input arguments to variables
HOST=$1
USER=$2
PASSWORD=$3
DBNAME=$4

echo "$HOST"
echo "$USER"
echo "$PASSWORD"
echo "$DBNAME"

# Using variables in the psql command
PGPASSWORD=$PASSWORD psql -h "$HOST" -U "$USER" -d "$DBNAME" -c "
CREATE TABLE IF NOT EXISTS users (
  id_user SERIAL PRIMARY KEY,
  username TEXT NOT NULL,
  email TEXT NOT NULL,
  pass_hash TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS notes (
  id_note SERIAL PRIMARY KEY,
  id_user INT NOT NULL REFERENCES users(id_user),
  content TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT now(),
  shared_at TIMESTAMP NOT NULL DEFAULT now()
);
CREATE TABLE IF NOT EXISTS shared_notes (
  id_shared SERIAL PRIMARY KEY,
  id_user INT NOT NULL REFERENCES users(id_user),
  id_note INT NOT NULL REFERENCES notes(id_note),
  shared_at TIMESTAMP NOT NULL DEFAULT now(),
  permission_type TEXT NOT NULL
);
"
