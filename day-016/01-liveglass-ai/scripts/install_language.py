#!/usr/bin/env python3
"""Download and install an Argos Translate pair, such as de -> en."""
import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--from-lang", required=True)
    parser.add_argument("--to-lang", default="en")
    args = parser.parse_args()
    try:
        import argostranslate.package
        packages = argostranslate.package.get_available_packages()
        match = next((p for p in packages if p.from_code == args.from_lang and p.to_code == args.to_lang), None)
        if match is None:
            print(f"No package available for {args.from_lang} -> {args.to_lang}", file=sys.stderr)
            return 2
        filename = match.download()
        argostranslate.package.install_from_path(filename)
        print(f"Installed Argos model {args.from_lang} -> {args.to_lang}")
        return 0
    except ImportError:
        print("Install Argos Translate first: python -m pip install argostranslate", file=sys.stderr)
        return 2
    except Exception as exc:
        print(f"Installation failed: {exc}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
