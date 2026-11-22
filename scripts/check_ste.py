#!/usr/bin/env python3
"""
ASD-STE100 Issue 9 (2025-01-15) Automated Compliance Checker (`check_ste.py`)

Zero-dependency Python 3 validator for technical and software documentation.
Enforces ASD-STE100 Issue 9 writing rules (Sections 1-9 and GR-1..GR-8) and
validates vocabulary against the bundled Issue 9 dictionary and software glossary.
"""

import argparse
import csv
import json
import os
import re
import sys
from typing import Any, Dict, List, Optional, Set, Tuple

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
RES_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, "..", "resources"))

DICT_JSON_PATH = os.path.join(RES_DIR, "ste-issue9-dictionary.json")
UNAPPROVED_JSON_PATH = os.path.join(RES_DIR, "unapproved-words.json")
DEFAULT_GLOSSARY_PATH = os.path.join(RES_DIR, "default-software-glossary.json")

# Rule 8.6 #2: Common abbreviated and spelled-out units of measurement and time
UNITS_OF_MEASUREMENT = {
    "a", "amp", "amps", "ampere", "amperes", "ma", "ua",
    "v", "volt", "volts", "mv", "kv",
    "w", "watt", "watts", "mw", "kw", "kwh",
    "ohm", "ohms", "kohm", "mohm",
    "hz", "khz", "mhz", "ghz", "hertz",
    "b", "bit", "bits", "byte", "bytes", "kb", "mb", "gb", "tb", "pb",
    "kib", "mib", "gib", "tib", "kbps", "mbps", "gbps", "mb/s", "gb/s", "kb/s",
    "s", "sec", "secs", "second", "seconds", "ms", "us", "ns",
    "min", "mins", "minute", "minutes", "h", "hr", "hrs", "hour", "hours",
    "d", "day", "days", "week", "weeks", "month", "months", "year", "years",
    "a.m.", "p.m.", "am", "pm",
    "m", "mm", "cm", "km", "meter", "meters", "millimeter", "millimeters",
    "centimeter", "centimeters", "kilometer", "kilometers",
    "in", "inch", "inches", "ft", "foot", "feet", "yd", "yard", "yards", "mi", "mile", "miles",
    "g", "mg", "kg", "gram", "grams", "milligram", "milligrams", "kilogram", "kilograms",
    "lb", "lbs", "pound", "pounds", "oz", "ounce", "ounces", "ton", "tons", "tonne", "tonnes",
    "l", "ml", "liter", "liters", "milliliter", "milliliters", "gal", "gallon", "gallons",
    "pa", "kpa", "mpa", "bar", "mbar", "psi", "atm",
    "c", "f", "k", "°c", "°f", "°k", "deg", "degree", "degrees",
    "celsius", "fahrenheit", "kelvin",
    "n", "kn", "nm", "n-m", "db", "dbm", "rpm", "rps", "knot", "knots", "%", "percent",
}

CONTRACTIONS = {
    "aren't": "are not",
    "can't": "cannot",
    "couldn't": "could not",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hasn't": "has not",
    "haven't": "have not",
    "he's": "he is (also replace gendered pronoun 'he' per GR-7)",
    "i'd": "I would (avoid first-person pronoun per GR-3)",
    "i'll": "I will (avoid first-person pronoun per GR-3)",
    "i'm": "I am (avoid first-person pronoun per GR-3)",
    "i've": "I have (avoid first-person pronoun per GR-3)",
    "isn't": "is not",
    "it's": "it is",
    "let's": "let us (use imperative verb)",
    "mustn't": "must not",
    "shan't": "shall not (use 'must not')",
    "she's": "she is (also replace gendered pronoun 'she' per GR-7)",
    "shouldn't": "should not (use 'must not' or 'do not')",
    "that's": "that is",
    "there's": "there is",
    "they'd": "they would",
    "they'll": "they will",
    "they're": "they are",
    "they've": "they have",
    "wasn't": "was not",
    "we'd": "we would (avoid 'we' per GR-3)",
    "we'll": "we will (avoid 'we' per GR-3)",
    "we're": "we are (avoid 'we' per GR-3)",
    "we've": "we have (avoid 'we' per GR-3)",
    "weren't": "were not",
    "what's": "what is",
    "where's": "where is",
    "who's": "who is",
    "won't": "will not",
    "wouldn't": "would not",
    "you'd": "you would",
    "you'll": "you will",
    "you're": "you are",
    "you've": "you have",
}

UNAPPROVED_PRONOUNS_AND_GENDERED = {
    "we": ("GR-3", "Use active subject ('the system', 'the operator') or imperative ('you')."),
    "our": ("GR-3", "Use 'the' or a specific technical noun instead of 'our'."),
    "ours": ("GR-3", "Do not use first-person plural pronouns."),
    "ourselves": ("GR-3", "Do not use reflexive first-person pronouns."),
    "us": ("GR-3", "Do not use first-person plural pronouns."),
    "myself": ("GR-3", "Do not use first-person reflexive pronouns."),
    "he": ("GR-7", "Use gender-neutral terms ('the operator', 'the user', 'the technician', 'they')."),
    "him": ("GR-7", "Use gender-neutral terms ('the operator', 'the user', 'them')."),
    "his": ("GR-7", "Use gender-neutral terms ('the', 'their')."),
    "himself": ("GR-7", "Use gender-neutral terms."),
    "she": ("GR-7", "Use gender-neutral terms ('the operator', 'the user', 'the technician', 'they')."),
    "her": ("GR-7", "Use gender-neutral terms ('the operator', 'the user', 'their', 'them')."),
    "hers": ("GR-7", "Use gender-neutral terms."),
    "herself": ("GR-7", "Use gender-neutral terms."),
    "man": ("GR-7", "Use 'PERSON (n)', 'PERSONNEL (n)', 'OPERATOR (TN)', or 'TECHNICIAN (TN)'."),
    "men": ("GR-7", "Use 'PERSONNEL (n)', 'PERSONS (n)', 'OPERATORS (TN)', or 'TECHNICIANS (TN)'."),
    "woman": ("GR-7", "Use 'PERSON (n)', 'PERSONNEL (n)', 'OPERATOR (TN)', or 'TECHNICIAN (TN)'."),
    "women": ("GR-7", "Use 'PERSONNEL (n)', 'PERSONS (n)', 'OPERATORS (TN)', or 'TECHNICIANS (TN)'."),
    "workman": ("GR-7", "Use 'TECHNICIAN (TN)', 'OPERATOR (TN)', or 'PERSONNEL (n)'."),
    "workmen": ("GR-7", "Use 'TECHNICIANS (TN)', 'OPERATORS (TN)', or 'PERSONNEL (n)'."),
    "manpower": ("GR-7", "Use 'PERSONNEL (n)' or 'WORKERS (TN)'."),
    "man-hour": ("GR-7", "Use 'WORK HOUR (TN)'."),
    "man-hours": ("GR-7", "Use 'WORK HOURS (TN)'."),
}

# Rule 3.3 permitted state adjectives after to be / to become / to stay
STATE_PAST_PARTICIPLES = {
    "activated", "aligned", "allowed", "applicable", "approved", "assembled",
    "attached", "authorized", "balanced", "blocked", "broken", "calibrated",
    "charged", "cleaned", "cleared", "closed", "clogged", "coated", "completed",
    "compressed", "configured", "connected", "contaminated", "cooled",
    "corroded", "corrupted", "cracked", "cured", "damaged", "deactivated",
    "de-energized", "deflated", "deformed", "degreased", "deleted", "dented",
    "deployed", "depressurized", "disabled", "disassembled", "discharged",
    "disconnected", "disengaged", "dissolved", "drained", "dried", "empty",
    "enabled", "encrypted", "energized", "engaged", "erased", "expired",
    "extended", "extinguished", "fastened", "filled", "finished", "fitted",
    "fixed", "flushed", "folded", "formatted", "frayed", "frozen", "full",
    "grounded", "heated", "ignited", "illuminated", "inflated", "inhibited",
    "initialized", "installed", "isolated", "jammed", "known", "leveled",
    "limited", "loaded", "located", "locked", "loosened", "lost", "lowered",
    "lubricated", "magnetized", "marked", "matched", "melted", "mixed",
    "moistened", "mounted", "needed", "neutralized", "obstructed", "open",
    "opened", "operated", "overheated", "painted", "parked", "permitted",
    "plugged", "polished", "powered", "pressurized", "primed", "protected",
    "purged", "ready", "recommended", "recorded", "reduced", "removed",
    "repaired", "replaced", "required", "reset", "restricted", "retracted",
    "reversed", "rinsed", "riveted", "rotated", "ruptured", "safetied",
    "saturated", "saved", "scheduled", "scratched", "sealed", "secured",
    "selected", "separated", "serialized", "serviceable", "set", "settled",
    "sharpened", "shown", "shut", "signed", "soaked", "soldered", "specified",
    "spilled", "spliced", "started", "sterilized", "stopped", "stored",
    "straightened", "strengthened", "stripped", "submerged", "supplied",
    "supported", "synchronized", "tagged", "taped", "tensioned", "terminated",
    "tested", "thinned", "threaded", "tightened", "tilted", "torqued",
    "transferred", "trimmed", "tuned", "turned", "twisted", "unfastened",
    "unlocked", "unloaded", "unscrewed", "unsoldered", "untied", "updated",
    "upgraded", "used", "validated", "verified", "warmed", "washed", "worn",
    "wrapped", "written",
}

COMMON_IMPERATIVE_STARTERS = {
    "abort", "accept", "activate", "add", "adjust", "align", "allow", "apply",
    "assemble", "attach", "authenticate", "authorize", "avoid", "balance",
    "begin", "bend", "bind", "bleed", "blow", "boot", "break", "brush", "build",
    "burn", "bypass", "calculate", "calibrate", "call", "cancel", "change",
    "charge", "check", "chock", "clean", "clear", "click", "clone", "close",
    "coat", "collect", "compare", "compile", "complete", "compress",
    "configure", "confirm", "connect", "consult", "contact", "continue",
    "control", "convert", "cool", "copy", "correct", "count", "cover", "create",
    "crimp", "cut", "deactivate", "debug", "decompress", "decrease", "decrypt",
    "de-energize", "deflate", "degrease", "delete", "deploy", "depressurize",
    "deselect", "determine", "disable", "disassemble", "discard", "discharge",
    "disconnect", "disengage", "display", "dissolve", "distill", "do",
    "download", "drain", "drag", "drill", "drop", "dry", "edit", "eliminate",
    "empty", "enable", "encode", "encrypt", "energize", "engage", "ensure",
    "enter", "erase", "examine", "execute", "expand", "export", "extend",
    "extinguish", "extract", "fasten", "fetch", "fill", "filter", "find",
    "finish", "fit", "fix", "flush", "fold", "follow", "format", "free",
    "fumigate", "generate", "get", "give", "go", "grind", "ground", "halt",
    "hang", "heat", "help", "hide", "highlight", "hit", "hold", "identify",
    "ignite", "illuminate", "import", "include", "increase", "index",
    "indicate", "inflate", "inhibit", "initialize", "initiate", "inject",
    "insert", "inspect", "install", "interchange", "invalidate", "invoke",
    "isolate", "jack", "keep", "kill", "launch", "let", "lift", "light",
    "limit", "link", "lint", "list", "listen", "load", "locate", "lock", "log",
    "look", "loosen", "lower", "lubricate", "magnetize", "maintain", "make",
    "manage", "map", "mark", "match", "maximize", "measure", "melt", "merge",
    "migrate", "minimize", "mix", "modify", "moisten", "monitor", "mount",
    "move", "navigate", "neutralize", "notify", "obey", "obtain", "open",
    "operate", "override", "paint", "park", "parse", "pass", "paste", "patch",
    "perform", "pickle", "ping", "place", "point", "polish", "poll", "pour",
    "prepare", "press", "pressurize", "prevent", "prime", "print", "proceed",
    "process", "protect", "provide", "provision", "publish", "pull", "pump",
    "purge", "push", "put", "query", "queue", "read", "ream", "reboot",
    "receive", "recommend", "record", "redirect", "reduce", "refer", "refresh",
    "refuel", "register", "reject", "release", "reload", "remove", "render",
    "repair", "repeat", "replace", "replicate", "report", "request", "reset",
    "resolve", "restart", "restore", "retain", "retract", "retrieve", "retry",
    "return", "reverse", "revoke", "rinse", "rivet", "roll", "rotate", "route",
    "rub", "run", "safety", "sand", "saturate", "save", "saw", "scale", "scan",
    "schedule", "scrape", "screw", "scrub", "scroll", "seal", "search",
    "secure", "see", "select", "send", "separate", "serialize", "serve", "set",
    "settle", "shake", "sharpen", "shear", "show", "shut", "sign", "signal",
    "simulate", "slide", "soak", "solder", "sort", "spawn", "specify", "splice",
    "spray", "start", "stay", "steer", "sterilize", "stop", "store",
    "straighten", "strengthen", "strip", "submerge", "submit", "subscribe",
    "suck", "supply", "support", "swage", "sweep", "swipe", "switch", "sync",
    "synchronize", "tag", "take", "tap", "tape", "tell", "tension", "terminate",
    "test", "thin", "thread", "throttle", "tighten", "tilt", "tokenize",
    "torque", "touch", "tow", "trace", "transfer", "transmit", "trigger",
    "trim", "truncate", "try", "turn", "twist", "type", "unfasten", "unlock",
    "unload", "unmount", "unpack", "unscrew", "unsolder", "unsubscribe",
    "untie", "update", "upgrade", "upload", "use", "utilize", "vacuum",
    "validate", "verify", "vibrate", "wait", "walk", "warm", "wash", "watch",
    "wear", "weigh", "weld", "wipe", "wire", "wrap", "write", "zoom",
}


def generate_regular_inflections(word: str, pos: str) -> Set[str]:
    """Generate common English inflected surface forms for an unapproved root word."""
    w = word.lower().strip()
    forms = {w}
    if " " in w or len(w) < 3:
        return forms

    if pos in ("v", "v/n", "n/v"):
        # 3rd person singular
        if w.endswith(("s", "sh", "ch", "x", "z", "o")):
            forms.add(w + "es")
        elif w.endswith("y") and len(w) > 2 and w[-2] not in "aeiou":
            forms.add(w[:-1] + "ies")
        else:
            forms.add(w + "s")
        # past / past participle & -ing
        if w.endswith("e"):
            forms.add(w + "d")
            if not w.endswith(("ee", "ye", "oe")):
                forms.add(w[:-1] + "ing")
            else:
                forms.add(w + "ing")
        elif w.endswith("y") and len(w) > 2 and w[-2] not in "aeiou":
            forms.add(w[:-1] + "ied")
            forms.add(w + "ing")
        else:
            forms.add(w + "ed")
            forms.add(w + "ing")
            # consonant doubling for common stressed endings (e.g. permit -> permitted, occur -> occurred, omit -> omitted,fit -> fitted)
            if (
                len(w) >= 3
                and w[-1] in "bdgmnprt"
                and w[-2] in "aeiou"
                and w[-3] not in "aeiou"
            ):
                forms.add(w + w[-1] + "ed")
                forms.add(w + w[-1] + "ing")
    elif pos == "n":
        if w.endswith(("s", "sh", "ch", "x", "z")):
            forms.add(w + "es")
        elif w.endswith("y") and len(w) > 2 and w[-2] not in "aeiou":
            forms.add(w[:-1] + "ies")
        else:
            forms.add(w + "s")
    return forms


class STEResources:
    def __init__(
        self,
        use_default_glossary: bool = True,
        extra_glossaries: Optional[List[str]] = None,
        extra_dictionaries: Optional[List[str]] = None,
    ):
        with open(DICT_JSON_PATH, "r", encoding="utf-8") as f:
            self.full_dict = json.load(f)
        with open(UNAPPROVED_JSON_PATH, "r", encoding="utf-8") as f:
            self.unapproved_db = json.load(f)

        self.approved_forms: Dict[str, List[Dict[str, str]]] = {}
        for entry in self.full_dict.get("entries", []):
            if entry.get("approved"):
                for form in entry.get("forms", []):
                    clean_f = re.sub(r"\([^)]*\)", "", form).strip().lower()
                    if clean_f:
                        self.approved_forms.setdefault(clean_f, []).append(
                            {"headword": entry["headword"], "pos": entry["pos"]}
                        )

        self.approved_ing_words: Set[str] = set()
        for cat_words in self.full_dict.get("approved_ing_words", {}).values():
            for w in cat_words:
                self.approved_ing_words.add(w.lower())

        # Technical Nouns & Technical Verbs
        self.technical_nouns: Set[str] = set()
        self.technical_verbs: Set[str] = set()

        # Always load official Issue 9 Rule 1.5 Cat 19 and Rule 1.12 Cat 2
        for tn in self.full_dict.get("rule_1_5_cat_19_ict_technical_nouns", []):
            self.technical_nouns.add(tn.lower())
        for tv_list in self.full_dict.get("rule_1_12_cat_2_computer_technical_verbs", {}).values():
            for tv in tv_list:
                self.technical_verbs.add(tv.lower())

        if use_default_glossary and os.path.exists(DEFAULT_GLOSSARY_PATH):
            self._load_glossary_file(DEFAULT_GLOSSARY_PATH)

        if extra_glossaries:
            for gpath in extra_glossaries:
                self._load_glossary_file(gpath)

        # Build expanded surface-form lookup for strictly unapproved words
        self.unapproved_words: Dict[str, Dict[str, Any]] = {}
        raw_unapproved = self.unapproved_db.get("unapproved_words", {})

        # Precompute all valid TV inflections and TN plurals so we don't flag approved TVs/TNs
        self.allowed_domain_forms: Set[str] = set()
        for tn in self.technical_nouns:
            for piece in generate_regular_inflections(tn, "n"):
                self.allowed_domain_forms.add(piece)
            for token in tn.split():
                if token.endswith("ing"):
                    self.approved_ing_words.add(token.lower())
        for tv in self.technical_verbs:
            for piece in generate_regular_inflections(tv, "v"):
                self.allowed_domain_forms.add(piece)

        for hw_lower, rec in raw_unapproved.items():
            for inflected in generate_regular_inflections(hw_lower, rec.get("unapproved_pos", "")):
                if inflected in self.approved_forms or inflected in self.allowed_domain_forms:
                    continue
                if inflected not in self.unapproved_words:
                    self.unapproved_words[inflected] = rec

        self.unapproved_phrases: Dict[str, Dict[str, Any]] = dict(
            self.unapproved_db.get("unapproved_phrases", {})
        )
        # Also add multi-word strictly unapproved entries from the dictionary
        for hw_lower, rec in raw_unapproved.items():
            if " " in hw_lower and hw_lower not in self.unapproved_phrases:
                self.unapproved_phrases[hw_lower] = {
                    "alternatives": rec.get("alternatives", []),
                    "rule": "1.1",
                    "note": f"Unapproved phrase '{rec.get('headword', hw_lower)}' in ASD-STE100 Issue 9.",
                }

        if extra_dictionaries:
            for dpath in extra_dictionaries:
                self._load_extra_dictionary(dpath)

        # Multi-word Technical Nouns sorted longest-first for phrase collapsing
        self.multiword_tns: List[str] = sorted(
            [tn for tn in self.technical_nouns if " " in tn],
            key=lambda s: (-len(s.split()), -len(s)),
        )

    def _load_glossary_file(self, path: str) -> None:
        if path.endswith(".json"):
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            for tn in data.get("technical_nouns", []):
                self.technical_nouns.add(tn.lower().strip())
            for tv in data.get("technical_verbs", []):
                self.technical_verbs.add(tv.lower().strip())
        elif path.endswith(".csv"):
            with open(path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    term = (row.get("term") or row.get("word") or "").strip().lower()
                    kind = (row.get("type") or row.get("category") or row.get("pos") or "tn").strip().lower()
                    if not term:
                        continue
                    if kind in ("tv", "verb", "technical_verb"):
                        self.technical_verbs.add(term)
                    else:
                        self.technical_nouns.add(term)

    def _load_extra_dictionary(self, path: str) -> None:
        if path.endswith(".json"):
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            for w, rec in data.get("unapproved_words", {}).items():
                self.unapproved_words[w.lower()] = rec
            for w in data.get("approved_words", []):
                w_low = w.lower() if isinstance(w, str) else w.get("headword", "").lower()
                if w_low:
                    self.approved_forms.setdefault(w_low, []).append({"headword": w_low.upper(), "pos": ""})
                    self.unapproved_words.pop(w_low, None)
        elif path.endswith(".csv"):
            with open(path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    word = (row.get("word") or row.get("headword") or "").strip().lower()
                    status = (row.get("status") or row.get("approved") or "").strip().lower()
                    alt = (row.get("alternatives") or row.get("replacement") or "").strip()
                    if not word:
                        continue
                    if status in ("true", "1", "yes", "approved", "ste"):
                        self.approved_forms.setdefault(word, []).append({"headword": word.upper(), "pos": ""})
                        self.unapproved_words.pop(word, None)
                    else:
                        self.unapproved_words[word] = {
                            "headword": word,
                            "unapproved_pos": row.get("pos", ""),
                            "alternatives": [a.strip() for a in alt.split(",") if a.strip()],
                            "ste_example": row.get("ste_example", ""),
                            "non_ste_example": "",
                            "notes": [],
                        }


class Diagnostic:
    def __init__(
        self,
        severity: str,
        rule: str,
        line: int,
        message: str,
        sentence: str = "",
        suggestion: str = "",
    ):
        self.severity = severity  # "ERROR" or "WARN"
        self.rule = rule
        self.line = line
        self.message = message
        self.sentence = sentence.strip()
        self.suggestion = suggestion.strip()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "severity": self.severity,
            "rule": self.rule,
            "line": self.line,
            "message": self.message,
            "sentence": self.sentence,
            "suggestion": self.suggestion,
        }


def count_ste_words(sentence: str) -> Tuple[int, List[str], List[Tuple[str, int]]]:
    """
    Count words in a sentence according to ASD-STE100 Issue 9 Section 8 (Rules 8.4-8.7):
      - Rule 8.5: Text in parentheses (...) counts as 1 word in the enclosing sentence,
                  and the inner text is also returned with its own STE word count.
      - Rule 8.6:
          1. Numbers -> 1 word
          2. Numbers together with units of measurement (10 °C, 10 degrees Celsius, 20 kg) -> 1 word
          3. Abbreviations -> 1 word
          4. Alphanumeric identifiers (36L7, No. 1, v2.4.1) -> 1 word
          5. Quoted text ("...") and inline code (`...`) -> 1 word
          6. Titles, headings, and text on placards/labels -> 1 word
          7. Proper nouns -> 1 word
      - Rule 8.7: Hyphenated words -> 1 word
    """
    s = sentence.strip()
    if not s:
        return 0, [], []

    # Strip Markdown link URLs: [link text](https://...) -> link text
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)

    # 1. Replace inline code spans `...` with single token
    s = re.sub(r"`[^`]+`", " __CODE_TOKEN__ ", s)

    # 2. Replace double-quoted strings "..." with single token (Rule 8.6 #5)
    s = re.sub(r'"[^"]+"', " __QUOTE_TOKEN__ ", s)
    s = re.sub(r"“[^”]+”", " __QUOTE_TOKEN__ ", s)

    # 3. Extract parenthetical expressions (...) (Rule 8.5)
    parentheticals: List[Tuple[str, int]] = []

    def _replace_paren(match: re.Match) -> str:
        inner = match.group(1).strip()
        if not inner:
            return ""
        # Count words inside the parenthetical
        inner_tokens = [
            tok for tok in re.findall(r"[A-Za-z0-9_°%./+-]+(?:-[A-Za-z0-9_°%./+-]+)*", inner)
        ]
        parentheticals.append((inner, len(inner_tokens)))
        return " __PAREN_TOKEN__ "

    s_no_parens = re.sub(r"\(([^()]*)\)", _replace_paren, s)

    # 4. Collapse "No. 12", "Fig. 3" (Rule 8.6 #4)
    s_no_parens = re.sub(r"\b(?:No|Fig|Ref)\.\s*\d+[A-Za-z0-9.-]*", "__ALNUM_ID__", s_no_parens)

    # 5. Extract raw word/hyphenated/number tokens
    raw_tokens = re.findall(
        r"__[A-Z_]+__|[A-Za-z0-9°%]+(?:[-'’./][A-Za-z0-9°%]+)*|[°%]",
        s_no_parens,
    )

    # 6. Merge Rule 8.6 #2 (Number + Unit of measurement, e.g., "10", "°C" or "10", "degrees", "Celsius" or "20", "kg")
    merged_tokens: List[str] = []
    i = 0
    n = len(raw_tokens)
    while i < n:
        tok = raw_tokens[i]
        is_num = bool(re.match(r"^\d+(?:[.,/]\d+)*$", tok))
        if is_num and i + 1 < n:
            next1 = raw_tokens[i + 1].lower().rstrip(".")
            if (
                next1 in ("degree", "degrees", "deg", "°")
                and i + 2 < n
                and raw_tokens[i + 2].lower().rstrip(".") in ("c", "f", "k", "celsius", "fahrenheit", "kelvin")
            ):
                merged_tokens.append(f"{tok}_{raw_tokens[i+1]}_{raw_tokens[i+2]}")
                i += 3
                continue
            if (
                next1 in ("cubic", "square")
                and i + 2 < n
                and raw_tokens[i + 2].lower().rstrip(".") in UNITS_OF_MEASUREMENT
            ):
                merged_tokens.append(f"{tok}_{raw_tokens[i+1]}_{raw_tokens[i+2]}")
                i += 3
                continue
            if next1 in UNITS_OF_MEASUREMENT or raw_tokens[i + 1].lower() in ("a.m.", "p.m."):
                merged_tokens.append(f"{tok}_{raw_tokens[i+1]}")
                i += 2
                continue
        merged_tokens.append(tok)
        i += 1

    return len(merged_tokens), merged_tokens, parentheticals


def split_sentences(text: str) -> List[str]:
    """
    Split a block of prose into sentences while respecting:
      - Inline code `...`
      - Quoted strings "..."
      - Abbreviations like e.g., i.e., etc., No., Fig., v1.2.3, a.m., p.m.
      - Rule 8.4: A colon (:) at the end of a block or lead-in clause terminates the sentence.
    """
    protected = text.strip()
    if not protected:
        return []

    placeholders: Dict[str, str] = {}
    counter = [0]

    def _stash(match: re.Match) -> str:
        key = f"__STASH_{counter[0]}__"
        counter[0] += 1
        placeholders[key] = match.group(0)
        return key

    # Stash inline code, markdown link URLs, and quoted strings
    protected = re.sub(r"`[^`]+`", _stash, protected)
    protected = re.sub(r"\]\([^)]+\)", _stash, protected)
    protected = re.sub(r'"[^"]+"', _stash, protected)

    # Protect dots in common abbreviations and decimal numbers
    for abbr in ("e.g.", "i.e.", "etc.", "viz.", "cf.", "et al.", "a.m.", "p.m.", "No.", "Fig.", "vs."):
        protected = re.sub(
            re.escape(abbr),
            lambda m: m.group(0).replace(".", "__DOT__"),
            protected,
            flags=re.IGNORECASE,
        )
    protected = re.sub(r"(\d)\.(\d)", r"\1__DOT__\2", protected)

    # Split on sentence-ending punctuation (. ! ?) followed by whitespace + uppercase/quote/end, or colon at end of line
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'`(>]|__STASH_)|(?<=:)\s*$", protected)

    sentences: List[str] = []
    for part in parts:
        p = part.strip()
        if not p:
            continue
        p = p.replace("__DOT__", ".")
        for k, v in placeholders.items():
            p = p.replace(k, v)
        if p:
            sentences.append(p)
    return sentences


def strip_code_and_quotes(sentence: str) -> str:
    """Remove inline code spans, link URLs, and double-quoted literals before lexical checks."""
    s = re.sub(r"`[^`]+`", " __CODE__ ", sentence)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = re.sub(r'"[^"]+"', " __QUOTE__ ", s)
    s = re.sub(r"“[^”]+”", " __QUOTE__ ", s)
    return s


def check_sentence(
    sentence: str,
    line_num: int,
    block_mode: str,
    is_note: bool,
    is_safety: bool,
    is_heading: bool,
    resources: STEResources,
) -> List[Diagnostic]:
    diags: List[Diagnostic] = []
    word_count, _, parentheticals = count_ste_words(sentence)

    # 1. Word count limits (Rule 5.1, Rule 5.5, Rule 6.3, Rule 7.1, Rule 8.5, Rule 8.6)
    if not is_heading:
        if is_note:
            limit = 25
            rule_id = "STE-5.5/6.3"
            mode_label = "Note (descriptive limit)"
        elif is_safety:
            limit = 20
            rule_id = "STE-5.1/7.1"
            mode_label = "Safety instruction (procedural limit)"
        elif block_mode == "procedural":
            limit = 20
            rule_id = "STE-5.1"
            mode_label = "Procedural sentence"
        else:
            limit = 25
            rule_id = "STE-6.3"
            mode_label = "Descriptive sentence"

        if word_count > limit:
            diags.append(
                Diagnostic(
                    severity="ERROR",
                    rule=rule_id,
                    line=line_num,
                    message=f"{mode_label} has {word_count} STE words (maximum allowed is {limit} words).",
                    sentence=sentence,
                    suggestion=f"Split this {word_count}-word sentence into two shorter sentences or use a vertical list introduced by a colon (:).",
                )
            )

        # Rule 8.3 & 8.5: Parenthetical nesting and inner word count
        prose_only = strip_code_and_quotes(sentence)
        if re.search(r"\([^()]*\([^()]*\)[^()]*\)", prose_only):
            diags.append(
                Diagnostic(
                    severity="ERROR",
                    rule="STE-8.3",
                    line=line_num,
                    message="Nested parentheses '((...))' are not permitted in ASD-STE100.",
                    sentence=sentence,
                    suggestion="Flatten or remove the nested parentheses.",
                )
            )
        for inner_text, inner_count in parentheticals:
            if inner_count > limit:
                diags.append(
                    Diagnostic(
                        severity="ERROR",
                        rule="STE-8.5",
                        line=line_num,
                        message=f"Parenthetical text has {inner_count} words (evaluated as a separate sentence under Rule 8.5; max {limit} words).",
                        sentence=f"({inner_text})",
                        suggestion="Move the parenthetical explanation into its own standalone sentence.",
                    )
                )

    prose = strip_code_and_quotes(sentence)

    # 2. Rule 8.1: Semicolons (;)
    if ";" in prose:
        diags.append(
            Diagnostic(
                severity="ERROR",
                rule="STE-8.1",
                line=line_num,
                message="Semicolon (';') is forbidden by Rule 8.1.",
                sentence=sentence,
                suggestion="Replace the semicolon with a period ('.') or a coordinating conjunction ('and', 'but').",
            )
        )

    # 3. Rule 4.2: Contractions
    for word_match in re.finditer(r"\b[A-Za-z]+['’][A-Za-z]+\b", prose):
        raw_w = word_match.group(0)
        norm_w = raw_w.lower().replace("’", "'")
        if norm_w in CONTRACTIONS:
            diags.append(
                Diagnostic(
                    severity="ERROR",
                    rule="STE-4.2",
                    line=line_num,
                    message=f"Contraction '{raw_w}' is forbidden by Rule 4.2.",
                    sentence=sentence,
                    suggestion=f"Write '{CONTRACTIONS[norm_w]}' in full.",
                )
            )

    # 4. Slashes (and/or, word/word)
    for slash_match in re.finditer(r"\b([A-Za-z]+)/([A-Za-z]+)\b", prose):
        full_slash = slash_match.group(0)
        low_slash = full_slash.lower()
        if low_slash in UNITS_OF_MEASUREMENT or low_slash in ("ci/cd", "i/o", "tcp/ip", "http/2", "http/3", "read/write"):
            continue
        if low_slash == "and/or":
            diags.append(
                Diagnostic(
                    severity="ERROR",
                    rule="STE-1.1",
                    line=line_num,
                    message="Construction 'and/or' is unapproved in ASD-STE100 Issue 9.",
                    sentence=sentence,
                    suggestion="Write 'A, B, or the two' or 'A or B, or all of them'.",
                )
            )
        else:
            diags.append(
                Diagnostic(
                    severity="ERROR",
                    rule="STE-8.0",
                    line=line_num,
                    message=f"Slash construction '{full_slash}' is ambiguous.",
                    sentence=sentence,
                    suggestion=f"Replace '{full_slash}' with 'or', 'and', or a hyphenated compound.",
                )
            )

    # 5. Unapproved phrases & Latin abbreviations (GR-6, Rule 9.3, Rule 1.1)
    prose_lower = prose.lower()
    for phrase, pinfo in resources.unapproved_phrases.items():
        # Match phrase with word boundaries (handling trailing period in e.g., i.e., etc.)
        if phrase.endswith("."):
            pat = r"(?<![A-Za-z0-9])" + re.escape(phrase)
        else:
            pat = r"\b" + re.escape(phrase) + r"\b"
        if re.search(pat, prose_lower):
            alts = ", ".join(pinfo.get("alternatives", []))
            rule_tag = f"STE-{pinfo.get('rule', '1.1')}"
            diags.append(
                Diagnostic(
                    severity="ERROR",
                    rule=rule_tag,
                    line=line_num,
                    message=f"Unapproved phrase or abbreviation '{phrase}'. {pinfo.get('note', '')}".strip(),
                    sentence=sentence,
                    suggestion=f"Use approved STE replacement: {alts}.",
                )
            )

    # 6. Mask contractions and multi-word Technical Nouns so their constituent words are not false-flagged
    masked_prose = re.sub(r"\b[A-Za-z]+['’][A-Za-z]+\b", " __CONTRACTION__ ", prose)
    for mw_tn in resources.multiword_tns:
        pat = r"\b" + re.escape(mw_tn) + r"s?\b"
        masked_prose = re.sub(pat, " __TN_PHRASE__ ", masked_prose, flags=re.IGNORECASE)

    # 7. Word-level checks: GR-3/GR-7 pronouns, Rule 1.1 strictly unapproved words, Rule 3.5 -ing forms
    word_tokens = list(re.finditer(r"\b[A-Za-z]+(?:-[A-Za-z]+)*\b", masked_prose))
    for idx, wm in enumerate(word_tokens):
        raw_tok = wm.group(0)
        low_tok = raw_tok.lower()
        if low_tok.startswith("__") or low_tok in ("warning", "caution", "note"):
            continue

        # GR-3 / GR-7 Pronouns and gendered nouns
        if low_tok in UNAPPROVED_PRONOUNS_AND_GENDERED:
            gr_id, gr_msg = UNAPPROVED_PRONOUNS_AND_GENDERED[low_tok]
            diags.append(
                Diagnostic(
                    severity="ERROR",
                    rule=f"STE-{gr_id}",
                    line=line_num,
                    message=f"Unapproved pronoun or gender-specific word '{raw_tok}' ({gr_id}).",
                    sentence=sentence,
                    suggestion=gr_msg,
                )
            )
            continue

        # Skip if part of hyphenated compound modifier (Rule 8.2 / 8.7)
        if "-" in low_tok:
            continue

        # Rule 1.1: Strictly unapproved words from Issue 9 dictionary
        if low_tok in resources.unapproved_words:
            rec = resources.unapproved_words[low_tok]
            alts = ", ".join(rec.get("alternatives", [])[:4])
            ste_ex = rec.get("ste_example", "")
            sug = f"Use: {alts}."
            if ste_ex:
                sug += f" (STE example: '{ste_ex}')"
            diags.append(
                Diagnostic(
                    severity="ERROR",
                    rule="STE-1.1",
                    line=line_num,
                    message=f"Unapproved word '{raw_tok}' (dictionary entry: '{rec.get('headword')} ({rec.get('unapproved_pos')})').",
                    sentence=sentence,
                    suggestion=sug,
                )
            )
            continue

        # Rule 3.5: -ing forms
        if (
            low_tok.endswith("ing")
            and len(low_tok) > 4
            and low_tok not in resources.approved_ing_words
            and low_tok not in resources.technical_nouns
        ):
            # Allow if immediately followed by a Technical Noun as part of a compound TN modifier (e.g., 'cooling fan', 'connecting rod')
            next_tok = word_tokens[idx + 1].group(0).lower() if idx + 1 < len(word_tokens) else ""
            if next_tok and next_tok in resources.technical_nouns:
                pass
            else:
                diags.append(
                    Diagnostic(
                        severity="ERROR",
                        rule="STE-3.5",
                        line=line_num,
                        message=f"Unapproved '-ing' form '{raw_tok}' (Rule 3.5 permits '-ing' words only in the 9 approved dictionary entries or as part of a Technical Noun).",
                        sentence=sentence,
                        suggestion="Rewrite with a simple verb tense (Infinitive, Imperative, Simple Present, Simple Past, or Simple Future) or an explicit clause ('Before you start...', 'When the service runs...').",
                    )
                )

    # 8. Rule 3.2 / 3.4: Complex verb tenses (perfect tenses: have/has/had + past participle; progressive: is/are/was/were + -ing)
    m_perf = re.search(
        r"\b(have|has|had)\s+(?:not\s+|never\s+|already\s+)?([a-z]+ed|been|gone|done|made|taken|given|shown|written|run|seen|known|come|become|broken|chosen|fallen|forgotten|frozen|grown|hidden|spoken|stolen|torn|worn)\b",
        prose_lower,
    )
    if m_perf:
        diags.append(
            Diagnostic(
                severity="ERROR",
                rule="STE-3.2/3.4",
                line=line_num,
                message=f"Complex perfect verb construction '{m_perf.group(0)}' is forbidden by Rules 3.2 and 3.4.",
                sentence=sentence,
                suggestion="Use the Simple Past ('started', 'failed') or Simple Present ('starts', 'is') instead of perfect tenses.",
            )
        )

    m_prog = re.search(
        r"\b(is|are|was|were|be|been)\s+(?:not\s+|currently\s+|still\s+)?([a-z]{4,}ing)\b",
        prose_lower,
    )
    if m_prog and m_prog.group(2) not in ("missing", "remaining", "mating"):
        diags.append(
            Diagnostic(
                severity="ERROR",
                rule="STE-3.2/3.4",
                line=line_num,
                message=f"Progressive/continuous verb construction '{m_prog.group(0)}' is forbidden by Rules 3.2 and 3.4.",
                sentence=sentence,
                suggestion="Use the Simple Present ('the service runs') or Simple Past ('the service ran').",
            )
        )

    # 9. Rule 5.5: No imperative commands inside a NOTE
    if is_note and not is_heading:
        stripped_note = re.sub(r"^(?:>\s*)?(?:\[!NOTE\]\s*)?(?:NOTE:\s*)?", "", prose).strip()
        first_word_m = re.match(r"^([A-Za-z]+)\b", stripped_note)
        if first_word_m:
            fw = first_word_m.group(1).lower()
            if fw in ("do", "make", "never", "always") or fw in COMMON_IMPERATIVE_STARTERS:
                # Check if 'do not' or imperative verb at sentence start
                if fw not in ("the", "a", "an", "this", "these", "if", "when", "it", "there", "all", "only", "each", "two", "three"):
                    diags.append(
                        Diagnostic(
                            severity="ERROR",
                            rule="STE-5.5",
                            line=line_num,
                            message=f"A NOTE must only give information, never instructions (starts with imperative '{first_word_m.group(1)}').",
                            sentence=sentence,
                            suggestion="Rewrite the NOTE as a declarative statement in descriptive style, or convert it into a numbered procedural step.",
                        )
                    )

    # 10. Rule 1.2 / 1.3 & GR-1 Contextual POS/Meaning Checks
    # 10a. GR-1: 'make sure' not followed by 'that'
    if re.search(r"\bmake\s+sure\s+(?!that\b)[a-z]", prose_lower):
        diags.append(
            Diagnostic(
                severity="ERROR",
                rule="STE-GR-1",
                line=line_num,
                message="'make sure' must be followed by the conjunction 'that' (General Recommendation GR-1).",
                sentence=sentence,
                suggestion="Write 'Make sure that ...'.",
            )
        )

    # 10b. 'check' or 'test' used as a verb (Rule 1.2 Recurring Error)
    for noun_only in ("check", "test"):
        # Inflected verb forms checked/tested/checks/tests or imperative at start / after 'to' / after modal
        verb_pat = (
            rf"(?:^\s*{noun_only}\b|\b(?:to|can|must|will|you|not|do\s+not|please|and|then)\s+{noun_only}\b|\b{noun_only}ed\b)"
        )
        # Strip leading step numbers or condition clause before comma for imperative check
        clauses = [prose_lower]
        if "," in prose_lower:
            clauses.append(prose_lower.split(",", 1)[1].strip())
        clean_start = re.sub(r"^(?:\d+[.)]\s*|\*\s*|-\s*)", "", clauses[-1]).strip()
        if re.search(verb_pat, prose_lower) or re.match(rf"^{noun_only}\s+(?:the|a|an|this|these|that|if|whether|for)\b", clean_start):
            repl = (
                "'DO A CHECK OF', 'MAKE SURE THAT', 'EXAMINE (v)', or 'MEASURE (v)'"
                if noun_only == "check"
                else "'DO A TEST OF (n)'"
            )
            diags.append(
                Diagnostic(
                    severity="ERROR",
                    rule="STE-1.2",
                    line=line_num,
                    message=f"Recurring error: '{noun_only}' is used as a verb, but '{noun_only.upper()} (n)' is approved ONLY as a noun in ASD-STE100 Issue 9.",
                    sentence=sentence,
                    suggestion=f"Use {repl}.",
                )
            )

    # 10c. 'complete' used as an adjective (Rule 1.2 Recurring Error: COMPLETE is an approved verb, COMPLETED is the approved adjective)
    if re.search(r"\b(?:a|an|the|is|are|was|were)\s+complete\b", prose_lower):
        diags.append(
            Diagnostic(
                severity="WARN",
                rule="STE-1.2",
                line=line_num,
                message="'complete' appears to be used as an adjective. In Issue 9, 'COMPLETE (v)' is a verb; 'complete (adj)' is unapproved.",
                sentence=sentence,
                suggestion="Use 'COMPLETED (adj)', 'FULL (adj)', or 'ALL (adj)'.",
            )
        )

    # 10d. 'about' or 'above' before a quantity/number (Rule 1.3 Meaning Trap)
    if re.search(r"\babout\s+\d", prose_lower):
        diags.append(
            Diagnostic(
                severity="ERROR",
                rule="STE-1.3",
                line=line_num,
                message="'about' is used before a number. 'ABOUT (prep)' is approved only for 'concerned with'.",
                sentence=sentence,
                suggestion="Use 'APPROXIMATELY (adv)' before quantities.",
            )
        )
    if re.search(r"\babove\s+\d", prose_lower):
        diags.append(
            Diagnostic(
                severity="WARN",
                rule="STE-1.3",
                line=line_num,
                message="'above' is used before a number. 'ABOVE (prep)' is approved only for physical position.",
                sentence=sentence,
                suggestion="Use 'MORE THAN' for numerical values.",
            )
        )

    # 10e. 'see' used for document cross-references (Rule 1.3 Meaning Trap)
    if re.search(r"\bsee\s+(?:the\s+)?(?:section|table|figure|chapter|appendix|page|step|guide|manual|document|specification)\b", prose_lower):
        diags.append(
            Diagnostic(
                severity="ERROR",
                rule="STE-1.3",
                line=line_num,
                message="'see' is used for a document cross-reference. 'SEE (v)' is approved only for physical sight with the eyes.",
                sentence=sentence,
                suggestion="Use 'REFER TO' (e.g., 'Refer to Section 2.').",
            )
        )

    # 11. Rule 3.6: Passive voice check (distinguishing Rule 3.3 state adjectives)
    for pm in re.finditer(
        r"\b(is|are|was|were|be)\s+(?:not\s+)?([a-z]+ed|done|made|taken|given|shown|written|sent|run|seen|known|found|kept|held|left|put|read|set|told)\b(\s+by\b)?",
        prose_lower,
    ):
        aux, pp, by_agent = pm.group(1), pm.group(2), pm.group(3)
        if by_agent:
            diags.append(
                Diagnostic(
                    severity="ERROR",
                    rule="STE-3.6",
                    line=line_num,
                    message=f"Passive voice construction '{pm.group(0)}' violates Rule 3.6.",
                    sentence=sentence,
                    suggestion="Rewrite in the active voice with the actor as the subject.",
                )
            )
        elif pp not in STATE_PAST_PARTICIPLES:
            diags.append(
                Diagnostic(
                    severity="WARN",
                    rule="STE-3.6",
                    line=line_num,
                    message=f"Possible passive voice '{pm.group(0)}'. Rule 3.3 permits past participles after 'to be' only as state adjectives.",
                    sentence=sentence,
                    suggestion="If this describes an action rather than a state, rewrite in the active voice.",
                )
            )

    # 12. Rule 2.1: Multi-word noun clusters exceeding 3 consecutive unhyphenated nouns
    if not is_heading:
        noun_run: List[str] = []
        raw_words_and_punct = re.findall(r"[A-Za-z]+(?:-[A-Za-z]+)*|[.,!?:;()]", prose)
        for token in raw_words_and_punct:
            t_low = token.lower()
            if token in ".,!?:;()" or t_low.startswith("__") or "-" in t_low:
                if len(noun_run) > 3:
                    cluster_str = " ".join(noun_run)
                    diags.append(
                        Diagnostic(
                            severity="WARN",
                            rule="STE-2.1",
                            line=line_num,
                            message=f"Multi-word noun cluster '{cluster_str}' has {len(noun_run)} consecutive nouns (Rule 2.1 limit is 3 words).",
                            sentence=sentence,
                            suggestion="Insert prepositions ('of', 'for', 'in', 'on') or hyphenate related modifiers (up to 3 words) per Rule 2.2.",
                        )
                    )
                noun_run = []
                continue
            app_entries = resources.approved_forms.get(t_low, [])
            is_strict_noun = (
                t_low in resources.technical_nouns
                or (t_low.endswith("s") and t_low[:-1] in resources.technical_nouns)
                or (bool(app_entries) and all(e["pos"] in ("n", "TN") for e in app_entries))
            ) and t_low not in ("a", "an", "the", "this", "these", "all", "no", "not", "and", "or", "but", "for", "of", "in", "on", "to", "with", "from", "by", "at", "as", "if", "when")
            if is_strict_noun:
                noun_run.append(token)
            else:
                if len(noun_run) > 3:
                    cluster_str = " ".join(noun_run)
                    diags.append(
                        Diagnostic(
                            severity="WARN",
                            rule="STE-2.1",
                            line=line_num,
                            message=f"Multi-word noun cluster '{cluster_str}' has {len(noun_run)} consecutive nouns (Rule 2.1 limit is 3 words).",
                            sentence=sentence,
                            suggestion="Insert prepositions ('of', 'for', 'in', 'on') or hyphenate related modifiers (up to 3 words) per Rule 2.2.",
                        )
                    )
                noun_run = []
        if len(noun_run) > 3:
            cluster_str = " ".join(noun_run)
            diags.append(
                Diagnostic(
                    severity="WARN",
                    rule="STE-2.1",
                    line=line_num,
                    message=f"Multi-word noun cluster '{cluster_str}' has {len(noun_run)} consecutive nouns (Rule 2.1 limit is 3 words).",
                    sentence=sentence,
                    suggestion="Insert prepositions ('of', 'for', 'in', 'on') or hyphenate related modifiers (up to 3 words) per Rule 2.2.",
                )
            )

    return diags


def validate_markdown_document(
    content: str,
    mode: str,
    resources: STEResources,
) -> Tuple[List[Diagnostic], Dict[str, int]]:
    diags: List[Diagnostic] = []
    lines = content.splitlines()

    in_fenced_code = False
    in_frontmatter = False
    current_section_mode = "procedural" if mode == "procedural" else "descriptive"

    # Group contiguous prose lines into paragraphs / list items / callouts
    blocks: List[Dict[str, Any]] = []
    current_para: List[Tuple[int, str]] = []
    current_alert_type: Optional[str] = None

    def flush_para():
        nonlocal current_para, current_alert_type
        if current_para:
            blocks.append({
                "type": "alert" if current_alert_type else "paragraph",
                "alert_type": current_alert_type,
                "section_mode": current_section_mode,
                "start_line": current_para[0][0],
                "lines": list(current_para),
            })
            current_para = []
            current_alert_type = None

    for idx, raw_line in enumerate(lines, start=1):
        stripped = raw_line.strip()

        # Frontmatter at line 1
        if idx == 1 and stripped == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
            continue

        # Fenced code block
        if stripped.startswith("```") or stripped.startswith("~~~"):
            flush_para()
            in_fenced_code = not in_fenced_code
            continue
        if in_fenced_code:
            continue

        # Blank line or horizontal rule
        if not stripped or re.match(r"^[-*_]{3,}$", stripped):
            flush_para()
            continue

        # HTML comments
        if stripped.startswith("<!--") and stripped.endswith("-->"):
            continue

        # Markdown Heading
        if stripped.startswith("#"):
            flush_para()
            heading_text = re.sub(r"^#+\s*", "", stripped).strip()
            if mode == "auto":
                h_low = heading_text.lower()
                if any(
                    kw in h_low
                    for kw in ("procedure", "step", "runbook", "how to", "install", "deploy", "configure", "restore", "recover", "troubleshoot", "quick start", "usage")
                ):
                    current_section_mode = "procedural"
                elif any(
                    kw in h_low
                    for kw in ("overview", "architecture", "description", "concept", "about", "design", "reference", "specification", "parameter", "schema", "summary")
                ):
                    current_section_mode = "descriptive"
            blocks.append({
                "type": "heading",
                "alert_type": None,
                "section_mode": current_section_mode,
                "start_line": idx,
                "lines": [(idx, heading_text)],
            })
            continue

        # Markdown Table Row
        if stripped.startswith("|") and stripped.endswith("|"):
            flush_para()
            # Skip separator row | :--- | :--- |
            if re.match(r"^\|\s*[:\-| ]+\|\s*$", stripped):
                continue
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            for cell in cells:
                # Only evaluate table cells that contain multi-word prose sentences (>4 words or ending with period)
                if len(cell.split()) >= 5 or cell.endswith("."):
                    blocks.append({
                        "type": "table_cell",
                        "alert_type": None,
                        "section_mode": current_section_mode,
                        "start_line": idx,
                        "lines": [(idx, cell)],
                    })
            continue

        # GitHub Alert / Blockquote (> [!WARNING], > [!CAUTION], > [!NOTE])
        if stripped.startswith(">"):
            b_content = re.sub(r"^>\s*", "", stripped).strip()
            if not b_content:
                flush_para()
                continue
            m_alert = re.match(r"^(?:\[!(WARNING|CAUTION|NOTE|IMPORTANT|TIP)\]|\*{0,2}(WARNING|CAUTION|NOTE):?\*{0,2}:?)\s*(.*)$", b_content, re.IGNORECASE)
            if m_alert:
                flush_para()
                atype = (m_alert.group(1) or m_alert.group(2)).upper()
                if atype in ("IMPORTANT", "TIP"):
                    atype = "NOTE"
                current_alert_type = atype
                rem = m_alert.group(3).strip()
                if rem:
                    current_para.append((idx, rem))
                continue
            else:
                if current_alert_type is None:
                    current_alert_type = "QUOTE"
                current_para.append((idx, b_content))
                continue
        elif current_alert_type is not None:
            flush_para()

        # Numbered or bulleted list item
        m_list = re.match(r"^(\d+[.)]|\*|-|\+)\s+(.*)$", stripped)
        if m_list:
            flush_para()
            marker, item_text = m_list.group(1), m_list.group(2).strip()
            is_numbered = marker[0].isdigit()
            item_mode = mode if mode != "auto" else ("procedural" if is_numbered else current_section_mode)
            blocks.append({
                "type": "list_item",
                "alert_type": None,
                "section_mode": item_mode,
                "start_line": idx,
                "lines": [(idx, item_text)],
            })
            continue

        # Inline WARNING: / CAUTION: / NOTE: prefix (with optional **bold** markdown)
        m_prefix = re.match(r"^\*{0,2}(WARNING|CAUTION|NOTE):?\*{0,2}:?\s+(.*)$", stripped)
        if m_prefix:
            flush_para()
            blocks.append({
                "type": "alert",
                "alert_type": m_prefix.group(1).upper(),
                "section_mode": current_section_mode,
                "start_line": idx,
                "lines": [(idx, m_prefix.group(2).strip())],
            })
            continue

        current_para.append((idx, stripped))

    flush_para()

    total_sentences = 0
    total_paragraphs = 0

    for blk in blocks:
        btype = blk["type"]
        atype = blk["alert_type"]
        bmode = mode if mode != "auto" else blk["section_mode"]
        is_note = atype == "NOTE"
        is_safety = atype in ("WARNING", "CAUTION")
        is_heading = btype == "heading"

        full_text = " ".join(line_txt for _, line_txt in blk["lines"])
        start_line = blk["start_line"]

        if is_heading:
            diags.extend(
                check_sentence(
                    sentence=full_text,
                    line_num=start_line,
                    block_mode=bmode,
                    is_note=False,
                    is_safety=False,
                    is_heading=True,
                    resources=resources,
                )
            )
            continue

        sents = split_sentences(full_text)
        if btype == "paragraph":
            total_paragraphs += 1
            # Rule 6.6: Maximum 6 sentences per paragraph in descriptive text
            if len(sents) > 6:
                diags.append(
                    Diagnostic(
                        severity="ERROR",
                        rule="STE-6.6",
                        line=start_line,
                        message=f"Paragraph contains {len(sents)} sentences (Rule 6.6 allows a maximum of 6 sentences per paragraph).",
                        sentence=sents[0] + " ...",
                        suggestion="Split this paragraph into two focused paragraphs, each starting with a clear topic sentence (Rule 6.4).",
                    )
                )

        # Rule 7.2 / 7.3 check on safety notices
        if is_safety and len(sents) == 0:
            diags.append(
                Diagnostic(
                    severity="ERROR",
                    rule="STE-7.2",
                    line=start_line,
                    message=f"{atype} notice is empty.",
                    sentence=full_text,
                    suggestion=f"Start the {atype} with a clear command or condition and explain the risk (Rules 7.2-7.3).",
                )
            )

        for s in sents:
            total_sentences += 1
            diags.extend(
                check_sentence(
                    sentence=s,
                    line_num=start_line,
                    block_mode="procedural" if is_safety else ("descriptive" if is_note else bmode),
                    is_note=is_note,
                    is_safety=is_safety,
                    is_heading=False,
                    resources=resources,
                )
            )

    stats = {
        "total_blocks": len(blocks),
        "total_paragraphs": total_paragraphs,
        "total_sentences": total_sentences,
        "errors": sum(1 for d in diags if d.severity == "ERROR"),
        "warnings": sum(1 for d in diags if d.severity == "WARN"),
    }
    return diags, stats


def main() -> int:
    parser = argparse.ArgumentParser(
        description="ASD-STE100 Issue 9 (2025-01-15) Automated Compliance Checker"
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="File path(s) to check, or '-' to read from stdin.",
    )
    parser.add_argument(
        "--mode",
        choices=["auto", "procedural", "descriptive"],
        default="auto",
        help="Enforcement mode (default: auto).",
    )
    parser.add_argument(
        "--glossary",
        action="append",
        default=[],
        help="Path to additional project glossary (.json or .csv). Can be passed multiple times.",
    )
    parser.add_argument(
        "--dictionary",
        action="append",
        default=[],
        help="Path to additional custom dictionary override (.json or .csv).",
    )
    parser.add_argument(
        "--no-default-glossary",
        action="store_true",
        help="Disable the bundled default-software-glossary.json (keeps only official Issue 9 Rule 1.5 Cat 19 and Rule 1.12 Cat 2 computer terms).",
    )
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text).",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Return non-zero exit code on warnings as well as errors.",
    )

    args = parser.parse_args()
    resources = STEResources(
        use_default_glossary=not args.no_default_glossary,
        extra_glossaries=args.glossary,
        extra_dictionaries=args.dictionary,
    )

    all_results: List[Dict[str, Any]] = []
    total_errors = 0
    total_warnings = 0

    for path in args.paths:
        if path == "-":
            content = sys.stdin.read()
            display_path = "<stdin>"
        else:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            display_path = path

        diags, stats = validate_markdown_document(content, args.mode, resources)
        total_errors += stats["errors"]
        total_warnings += stats["warnings"]
        all_results.append({
            "file": display_path,
            "stats": stats,
            "diagnostics": [d.to_dict() for d in diags],
        })

    if args.format == "json":
        print(
            json.dumps(
                {
                    "standard": "ASD-STE100 Issue 9 (2025-01-15)",
                    "total_errors": total_errors,
                    "total_warnings": total_warnings,
                    "results": all_results,
                },
                indent=2,
                ensure_ascii=False,
            )
        )
    else:
        for res in all_results:
            st = res["stats"]
            status_str = "PASS" if st["errors"] == 0 and (not args.strict or st["warnings"] == 0) else "FAIL"
            print(
                f"=== ASD-STE100 Issue 9 Check: {res['file']} [{status_str}] "
                f"(Sentences: {st['total_sentences']}, Errors: {st['errors']}, Warnings: {st['warnings']}) ==="
            )
            for d in res["diagnostics"]:
                print(f"  [{d['severity']}] Line {d['line']} ({d['rule']}): {d['message']}")
                if d["sentence"]:
                    print(f"    Sentence  : {d['sentence']}")
                if d["suggestion"]:
                    print(f"    Suggestion: {d['suggestion']}")
            if not res["diagnostics"]:
                print("  No ASD-STE100 Issue 9 violations detected.")
            print()

    if total_errors > 0 or (args.strict and total_warnings > 0):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
