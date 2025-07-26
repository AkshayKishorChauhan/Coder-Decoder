import argparse
import string

ALPHABET = string.ascii_lowercase


def word_to_numbers(word: str) -> list[int]:
    """Convert a word to a list of 1-indexed alphabet positions."""
    return [ALPHABET.index(c.lower()) + 1 for c in word]


def numbers_to_word(numbers: list[int]) -> str:
    """Convert list of alphabet positions back to a word."""
    return ''.join(ALPHABET[(n - 1) % 26] for n in numbers)


def build_pattern(code_word: str, decoded_word: str) -> list[int]:
    """Return difference pattern between two words."""
    n1 = word_to_numbers(code_word)
    n2 = word_to_numbers(decoded_word)
    if len(n1) != len(n2):
        raise ValueError("Words used to build pattern must be the same length")
    return [a - b for a, b in zip(n1, n2)]


def apply_pattern(word: str, pattern: list[int], mode: str = "decode") -> str:
    """Apply a difference pattern to a word."""
    numbers = word_to_numbers(word)
    if len(numbers) != len(pattern):
        raise ValueError("Word length must match the pattern length")
    if mode == "decode":
        result = [((n - p - 1) % 26) + 1 for n, p in zip(numbers, pattern)]
    elif mode == "encode":
        result = [((n + p - 1) % 26) + 1 for n, p in zip(numbers, pattern)]
    else:
        raise ValueError("mode must be 'encode' or 'decode'")
    return numbers_to_word(result)


def main() -> None:
    parser = argparse.ArgumentParser(description="Decode or encode words using a difference pattern.")
    parser.add_argument("code_word", help="First word in the pattern pair")
    parser.add_argument("decoded_word", help="Second word in the pattern pair")
    parser.add_argument("target_word", help="Word to transform")
    parser.add_argument("--mode", choices=["encode", "decode"], default="decode", help="Transformation mode")
    parser.add_argument("--show-pattern", action="store_true", help="Print numerical pattern")
    args = parser.parse_args()

    pattern = build_pattern(args.code_word, args.decoded_word)
    if args.show_pattern:
        print("Pattern:", pattern)
    result = apply_pattern(args.target_word, pattern, mode=args.mode)
    print(result)


if __name__ == "__main__":
    main()
