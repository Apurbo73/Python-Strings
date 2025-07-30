# Python Strings

 
Here is a comprehensive list of **Python string functions** and **string methods**, categorized for easier understanding:

---

### 🔤 **Basic String Methods**

| Method             | Description                                     |
| ------------------ | ----------------------------------------------- |
| `str.capitalize()` | Capitalizes first character.                    |
| `str.lower()`      | Converts all characters to lowercase.           |
| `str.upper()`      | Converts all characters to uppercase.           |
| `str.title()`      | Capitalizes the first letter of each word.      |
| `str.swapcase()`   | Swaps case of all characters.                   |
| `str.casefold()`   | Aggressive lowercasing (for caseless matching). |

---

### 🔍 **Search and Check Methods**

| Method                   | Description                                         |
| ------------------------ | --------------------------------------------------- |
| `str.find(sub)`          | Returns index of first occurrence or `-1`.          |
| `str.rfind(sub)`         | Returns highest index of occurrence or `-1`.        |
| `str.index(sub)`         | Like `find()` but raises `ValueError` if not found. |
| `str.rindex(sub)`        | Like `rfind()` but raises `ValueError`.             |
| `str.startswith(prefix)` | Returns `True` if string starts with prefix.        |
| `str.endswith(suffix)`   | Returns `True` if string ends with suffix.          |

---

### 🔠 **Format and Alignment**

| Method                        | Description                         |
| ----------------------------- | ----------------------------------- |
| `str.center(width)`           | Centers string with padding.        |
| `str.ljust(width)`            | Left-justifies string.              |
| `str.rjust(width)`            | Right-justifies string.             |
| `str.zfill(width)`            | Pads string on the left with zeros. |
| `str.format(*args, **kwargs)` | Performs string formatting.         |
| `str.format_map(mapping)`     | Uses a dict for formatting.         |

---

### 🔡 **Check Character Types**

| Method               | Description                               |
| -------------------- | ----------------------------------------- |
| `str.isalnum()`      | Alphanumeric check.                       |
| `str.isalpha()`      | Alphabetic check.                         |
| `str.isascii()`      | ASCII check.                              |
| `str.isdecimal()`    | Decimal characters check.                 |
| `str.isdigit()`      | Digit check.                              |
| `str.isnumeric()`    | Numeric check (includes unicode numeric). |
| `str.isidentifier()` | Valid Python identifier check.            |
| `str.islower()`      | All lowercase check.                      |
| `str.isupper()`      | All uppercase check.                      |
| `str.isspace()`      | Whitespace check.                         |
| `str.istitle()`      | Title case check.                         |

---

### 🧵 **Modify Strings**

| Method                     | Description                          |
| -------------------------- | ------------------------------------ |
| `str.replace(old, new)`    | Replaces substrings.                 |
| `str.translate(table)`     | Translates characters using a table. |
| `str.strip()`              | Removes leading/trailing whitespace. |
| `str.lstrip()`             | Removes leading whitespace.          |
| `str.rstrip()`             | Removes trailing whitespace.         |
| `str.removeprefix(prefix)` | Removes a prefix (Python 3.9+).      |
| `str.removesuffix(suffix)` | Removes a suffix (Python 3.9+).      |

---

### 📐 **Split and Join**

| Method                 | Description                               |
| ---------------------- | ----------------------------------------- |
| `str.split(sep=None)`  | Splits string into list.                  |
| `str.rsplit(sep=None)` | Splits from the right.                    |
| `str.splitlines()`     | Splits at line boundaries.                |
| `str.partition(sep)`   | Splits at first occurrence into 3 parts.  |
| `str.rpartition(sep)`  | Splits at last occurrence into 3 parts.   |
| `str.join(iterable)`   | Joins elements using string as separator. |

---

### 🔄 **Encoding and Expanding**

| Method                      | Description                |
| --------------------------- | -------------------------- |
| `str.encode(encoding)`      | Encodes string to bytes.   |
| `str.expandtabs(tabsize=8)` | Replaces tabs with spaces. |

---




### 🧙‍♂️ Python Escape Characters (Escape Operators)

Escape characters in Python are used to insert **special characters** into strings that are otherwise hard or impossible to type directly.

Here’s a list of **commonly used escape sequences**:

| Escape Sequence | Meaning                         | Example                | Result              |
| --------------- | ------------------------------- | ---------------------- | ------------------- |
| `\\`            | Backslash                       | `"A\\B"`               | `A\B`               |
| `\'`            | Single quote                    | `'It\'s OK'`           | `It's OK`           |
| `\"`            | Double quote                    | `"He said \"Hi\""`     | `He said "Hi"`      |
| `\n`            | Newline                         | `"Hello\nWorld"`       | Prints on 2 lines   |
| `\t`            | Tab                             | `"A\tB"`               | `A    B`            |
| `\r`            | Carriage return                 | `"123\rABC"`           | `ABC` (overwrites)  |
| `\b`            | Backspace                       | `"ABC\bD"`             | `ABD`               |
| `\f`            | Form feed                       | `"Hello\fWorld"`       | Platform-dependent  |
| `\v`            | Vertical tab                    | `"Hello\vWorld"`       | Platform-dependent  |
| `\a`            | Bell (Alert)                    | `"\a"`                 | Beep (if supported) |
| `\ooo`          | Octal value (e.g. `\141` = 'a') | `"\141"`               | `a`                 |
| `\xhh`          | Hex value (e.g. `\x61` = 'a')   | `"\x61"`               | `a`                 |
| `\N{name}`      | Unicode character by name       | `"\N{COPYRIGHT SIGN}"` | `©`                 |
| `\uXXXX`        | 16-bit Unicode                  | `"\u00A9"`             | `©`                 |
| `\UXXXXXXXX`    | 32-bit Unicode                  | `"\U0001F600"`         | 😀                  |

---

### ✅ Example Usage:

```python
print("Line1\nLine2")        # Newline
print("She said, \"Hi!\"")  # Quotes
print("C:\\Users\\Name")    # Backslashes
```

---



