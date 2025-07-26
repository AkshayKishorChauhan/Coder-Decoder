# Coder-Decoder

A small utility for decoding or encoding words based on the difference between two example words.

## Usage

```
python decoder.py CODE_WORD DECODED_WORD TARGET_WORD [--mode encode|decode] [--show-pattern]
```

- `CODE_WORD` and `DECODED_WORD` establish the pattern. They must be the same length.
- `TARGET_WORD` is transformed using that pattern. By default the tool decodes the word.
- `--mode encode` applies the pattern in reverse.
- `--show-pattern` prints the numerical differences used in the transformation.

Example:

```
$ python decoder.py abc xyz abc --show-pattern
Pattern: [-23, -23, -23]
xyz
```

This repository also contains `coder.py`, an early implementation kept for reference.
