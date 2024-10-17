# Red Missing

A simple utility to search for items on with [Redacted](https://redacted.ch/), identifying those search terms that return no results.

Useful for finding albums that aren't on Redacted yet.

## Examples

```
$ echo "The Beatles - Revolver" | REDACTED_API_KEY=... redmissing
```

```
$ export REDACTED_API_KEY=...
$ redmissing -i artist_albums.txt -o missing.txt
```

```
$ cat artist_albums.txt | REDACTED_API_KEY=... redmissing -o missing.txt
```

```
$ beet ls -a | REDACTED_API_KEY=... redmissing > missing.txt
```

## Installation

```
$ pip install git+https://github.com/peterjdolan/redmissing.git
```

