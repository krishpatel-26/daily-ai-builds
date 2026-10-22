#!/usr/bin/env python3
"""JSON stdin/stdout bridge to Argos Translate."""
import json
import sys

def main():
    try:
        request = json.load(sys.stdin)
        texts = request.get("texts", [])
        source = request.get("source", "de")
        target = request.get("target", "en")
        import argostranslate.translate
        installed = argostranslate.translate.get_installed_languages()
        src = next((lang for lang in installed if lang.code == source), None)
        dst = next((lang for lang in installed if lang.code == target), None)
        if src is None or dst is None:
            print(json.dumps({"ok": False, "reason": f"No installed Argos language pair for {source} -> {target}"}))
            return 0
        translation = src.get_translation(dst)
        if translation is None:
            print(json.dumps({"ok": False, "reason": f"No installed Argos translation for {source} -> {target}"}))
            return 0
        result = [translation.translate(str(text)) for text in texts]
        print(json.dumps({"ok": True, "translations": result}, ensure_ascii=False))
        return 0
    except Exception as exc:
        print(json.dumps({"ok": False, "reason": str(exc)}, ensure_ascii=False))
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
