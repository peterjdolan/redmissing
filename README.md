# Red Missing

A simple utility to search for items on with [Redacted](https://redacted.ch/), identifying those search terms that return no results.

Useful for finding albums that aren't on Redacted yet.

## Examples

```
$ echo "The Beatles - Revolver" | redmissing
```

```
$ redmissing -i artist_albums.txt -o missing.txt
```

```
$ cat artist_albums.txt | redmissing -o missing.txt
```

```
$ beet ls -a | redmissing > missing.txt
```

## Installation

```
$ pip install git+https://github.com/peterjdolan/redmissing.git
```

