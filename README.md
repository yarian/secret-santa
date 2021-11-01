# Secret Santa

## Overview

This lets you generate secret santa pairs and then sends out an email to everyone with their assignment so you don't know who everybody's pair is.

I did not write this for other people to use. Heck, I don't even claim it's good code. If you for some bizzare reason find it helpful, enjoy. 

## Running

Should only have to change two files.

### Secrets.py

Copy `.secrets.py` into `secrets.py`.

Fill out the name, email, and password of the SMTP account you're going to log into.

For Gmail accounts, use an app password.
https://myaccount.google.com/apppasswords

### people.py

Copy `.people.py` into `people.py`.

Add your people and include them in the `PEOPLE` variable.

### Install dependencies

```bash
poetry install
```

### Run

```bash
python3 main.py
```

## Testing

If you want to check how random the pairings are you can look at `checks.py`. Run the file to get a report with some insight.