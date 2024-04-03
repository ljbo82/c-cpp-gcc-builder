!!! hint "Review status: OK"

# functions.mk

This makefile exposes utility makefile functions used by the build system, which can also be used by your project.

--------------------------------------------------------------------------------

## Basic usage

By including this makefile it will expose several utility functions which can be invoked via GNU Make [`$(call)`](https://www.gnu.org/software/make/manual/html_node/Call-Function.html) function.

```Makefile
include $(CPB_DIR)/functions.mk
```

!!! note
    This makefile is automatically included by `builder.mk`

--------------------------------------------------------------------------------

## Make targets

_This makefile does not expose any target._

--------------------------------------------------------------------------------

## Variables

_This makefile does not expect nor expose any variables (except [functions](#functions))._

--------------------------------------------------------------------------------

## Functions

Following are listed exposed functions:

### Text functions

#### FN_EQ

Checks if two strings are equal each other.

If strings are equal, returns the string. Otherwise, returns an empty value.

**Syntax:**

```Makefile
$(call FN_EQ,srt1,str2)
```

**Parameters:**

| Parameter | Details         |
|-----------|-----------------|
| `srt1`    | First string.   |
| `str2`    | Second string.  |

#### FN_REVERSE

Reverses a list of words.

**Syntax:**

```Makefile
$(call FN_REVERSE,word1 word2 ...)
```

**Parameters:**

| Parameter         | Details        |
|--------------  ---|----------------|
| `word1 word2 ...` | List of words. |

#### FN_SPLIT

Explodes a delimited word into a list of words.

**Syntax:**

```Makefile
$(call FN_SPLIT,delimitedWord,delimiter,[tokenPrefix])
```

**Parameters:**

| Parameter       | Details                                                                                                                                                                                            |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `delimitedWord` | Delimited word which will be exploded into a list of words.                                                                                                                                        |
| `delimiter`     | Delimiter used to explode the string into a list of words.                                                                                                                                         |
| `tokenPrefix`   | Optional token prefix to be added for each word.<br/> Since GNU Make ignores empty words, a token prefix can be used to force<br/>split of empty tokens (afterwards token prefix shall be removed).|

#### FN_TOKEN

Returns a token on delimited word (i.e. explodes the word into a list of words and returns a word of generated list).

**Syntax:**

```Makefile
$(call FN_TOKEN,delimitedWord,delimiter,index)
```

**Parameters:**

| Parameter       | Details                                                          |
|-----------------|------------------------------------------------------------------|
| `delimitedWord` | Delimited word which will be exploded into a list of words.      |
| `delimiter`     | Delimiter used to explode the word into a list of words.         |
| `index`         | Index of word to get from generated list (first element is `1`). |

#### FN_UNIQUE

Returns a string removing duplicate words without sorting.

This function differs from GNU Make [`$(sort)`](https://www.gnu.org/software/make/manual/make.html#Text-Functions) in terms of sorting. `$(sort)` removes duplicate words sorting resulting string. This function only remove duplicate words preserving original ordering or words.

**Syntax:**

```Makefile
$(call FN_UNIQUE,word1 word2 ...)
```

**Parameters:**

| Parameter         | Details        |
|--------------  ---|----------------|
| `word1 word2 ...` | List of words. |

--------------------------------------------------------------------------------

### Semantic versioning

#### FN_SEMVER_CHECK

Checks if a semantic version string is valid.

If given value is valid, returns it. Otherwise, raises an error. Only numbers are accepted for major.minor.patch.

**Syntax:**

```Makefile
$(call FN_SEMVER_CHECK,semanticVersion)
```

**Parameters:**

| Parameter         | Details                  |
|-------------------|--------------------------|
| `semanticVersion` | Semantic version string. |

#### FN_SEMVER_CMP

Compares two semantic versions. If tested version is compatible with a minimum one, returns tested version. Otherwise returns an empty value.

!!! Note
    The components of inspected semantic version values (major, minor, and patch) must be numeric values.

**Syntax:**

```Makefile
$(call FN_SEMVER_CMP,testVer,MinVer)
```

**Parameters:**

| Parameter | Details                   |
|-----------|---------------------------|
| `testVer` | Tested version.           |
| `MinVer`  | Minimal accepted version. |

#### FN_SEMVER_MAJOR

Returns the major component for given version.

**Syntax:**

```Makefile
$(call FN_SEMVER_MAJOR,semanticVersion)
```

**Parameters:**

| Parameter         | Details                  |
|-------------------|--------------------------|
| `semanticVersion` | Semantic version string. |

#### FN_SEMVER_MINOR

Returns the minor component for given version.

**Syntax:**

```Makefile
$(call FN_SEMVER_MINOR,semanticVersion)
```

**Parameters:**

| Parameter         | Details                  |
|-------------------|--------------------------|
| `semanticVersion` | Semantic version string. |


#### FN_SEMVER_MIN_CHECK

Checks if a version is compatible with a minimum one.  If version is not compatible, it raises an error.

**Syntax:**

```Makefile
$(call FN_SEMVER_MIN_CHECK,minVersion,version,[errorMessage])
```

**Parameters:**

| Parameter      | Details                            |
|----------------|------------------------------------|
| `minVersion`   | Minimum accepted version.          |
| `version`      | Tested version.                    |
| `errorMessage` | Optional customized error message. |

#### FN_SEMVER_PATCH

Returns the patch component for given version.

**Syntax:**

```Makefile
$(call FN_SEMVER_PATCH,semanticVersion)
```

**Parameters:**

| Parameter         | Details                  |
|-------------------|--------------------------|
| `semanticVersion` | Semantic version string. |

--------------------------------------------------------------------------------

### File system functions

#### FN_FIND_FILES

Lists files in a directory.

This function returns the list of files in given directory (by default recursively) through a call to the [`find`](https://man7.org/linux/man-pages/man1/find.1.html) command.

**Syntax:**

```Makefile
$(call FN_FIND_FILES,directory,[findFlags])
```

**Parameters:**

| Parameter   | Details                                            |
|-------------|----------------------------------------------------|
| `directory` | Path to the directory which will be inspected.     |
| `findFlags` | Optional flags to be passed to the `find` command. |

#### FN_IS_INSIDE_DIR

Checks if a path is inside a directory.

If given path correspond to a path inside given directory, return the path. Otherwise, returns an empty value.

**Syntax:**

```Makefile
$(call FN_IS_INSIDE_DIR,parentDir,path)
```

**Parameters:**

| Parameter   | Details                                           |
|-------------|---------------------------------------------------|
| `parentDir` | Directory which should be parent of given `path`. |
| `path`      | Tested path.                                      |

#### FN_REL_DIR

Returns the relative path for going from `fromDir` to `toDir`.

**Syntax:**

```Makefile
$(call FN_REL_DIR,fromDir,toDir)
```

**Parameters:**

| Parameter | Details                     |
|-----------|-----------------------------|
| `fromDir` | Departure directory path.   |
| `toDir`   | Destination directory path. |

--------------------------------------------------------------------------------

### General utilities

#### FN_CHECK_NO_WHITESPACE

Ensures a variable value has no whitespaces.

If a variable value has whitespaces, an error will be raised.

**Syntax:**

```Makefile
$(call FN_CHECK_NO_WHITESPACE,varName,[errorMessage])
```

**Parameters:**

| Parameter      | Details                                                                                                                     |
|----------------|-----------------------------------------------------------------------------------------------------------------------------|
| `varName`      | Variable name                                                                                                               |
| `errorMessage` | Optional error message. If value is suppressed or an empty value is given,<br/>a standardized message will be used instead. |

#### FN_CHECK_NON_EMPTY

Checks if a variable, which should NOT be empty, has an empty value.

If variable has an empty value, an error will be raised.

**Syntax:**

```Makefile
$(call FN_CHECK_NON_EMPTY,varName,[errorMessage])
```

**Parameters:**

| Parameter      | Description                                                                                                                 |
|----------------|-----------------------------------------------------------------------------------------------------------------------------|
| `varName`      | Variable name                                                                                                               |
| `errorMessage` | Optional error message. If value is suppressed or an empty value is given,<br/>a standardized message will be used instead. |

#### FN_CHECK_OPTIONS

Ensures the contents of a variable is one among a list of accepted values.

If variable contents has an unexpected value, an error will be raised.

**Syntax:**

```Makefile
$(call FN_CHECK_OPTIONS,varName,acceptedOptions,[errorMessage])
```

**Parameters:**

| Parameter         | Description                                                                                                                 |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `varName`         | Variable name                                                                                                               |
| `acceptedOptions` | List of accepted words for variable contents.                                                                               |
| `errorMessage`    | Optional error message. If value is suppressed or an empty value is given,<br/>a standardized message will be used instead. |

#### FN_CHECK_ORIGIN

Ensures the [origin](https://www.gnu.org/software/make/manual/make.html#Origin-Function) of an variable.

If a variable has an unexpected origin, an error will be raised.

**Syntax:**

```Makefile
$(call FN_CHECK_ORIGIN,varName,expectedOrigin,[errorMessage])
```

**Parameters:**

| Parameter        | Description                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `varName`        | Variable name                                                                                                               |
| `expectedOrigin` | Accepted origin for the variable.                                                                                           |
| `errorMessage`   | Optional error message. If value is suppressed or an empty value is given,<br/>a standardized message will be used instead. |

#### FN_CHECK_RESERVED

Ensures a variable is not defined until the call the function.

If variable is defined in the moment of calling this function, it will raise an error.

**Syntax:**

```Makefile
$(call FN_CHECK_RESERVED,varName,[errorMessage])
```

**Parameters:**

| Parameter      | Details                                                                                                                     |
|----------------|-----------------------------------------------------------------------------------------------------------------------------|
| `varName`      | Variable name                                                                                                               |
| `errorMessage` | Optional error message. If value is suppressed or an empty value is given,<br/>a standardized message will be used instead. |

#### FN_HOST_FACTORIZE

Factorizes a host string (used to decompose host string into a list of compatible layers).

For example, the value `linux-arm-v7` can be decomposed into `linux`, `linux/arm`, `linux/arm/v7` layers.

**Syntax:**

```Makefile
$(call FN_HOST_FACTORIZE,hostString,[delimiter],[replacement])
```

**Parameters:**

| Parameter     | Details                                                                               |
|---------------|---------------------------------------------------------------------------------------|
| `hostString`  | A host string value (e.g. `linux-arm-v7`).                                            |
| `delimiter`   | Optional token delimiter for `hostString` (defaults to `-`).                          |
| `replacement` | Optional replacement for delimiters while factorizing `hostString` (defaults to `/`). |

#### FN_NUMBER_CMP

Numeric comparison of two numbers. Returns the following values:

| Returned value | If                        |
|----------------|---------------------------|
| `0`            | first == second           |
| `1`            | first > second            |
| `-1`           | first < second            |
| `?`            | Invalid values were given |

**Syntax:**

```Makefile
$(call FN_NUMBER_CMP,[first],[second])
```

**Parameters:**

| Parameter | Details                                              |
|-----------|------------------------------------------------------|
| `first`   | First number. If empty, `0` (zero) will be assumed.  |
| `second`  | Second number. If empty, `0` (zero) will be assumed. |

#### FN_SHELL

Executes a shell command and returns execution output.

This function differs from [`$(shell)`](https://www.gnu.org/software/make/manual/make.html#Shell-Function) in terms of error handling. With this function, if an error happens in the execution, an error will be raised.

**Syntax:**

```Makefile
$(call FN_SHELL,cmd,[errorMessage])
```

**Parameters:**

| Parameter        | Description                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `cmd`            | Shell command to execute                                                                                                    |
| `errorMessage`   | Optional error message. If value is suppressed or an empty value is given,<br/>a standardized message will be used instead. |

--------------------------------------------------------------------------------

### Colored output

#### FN_COLORED_TEXT

Generate a colored string.

!!! Note
    Real color support relies on terminal support. If there is no support colors are ignored.

**Syntax:**

```Makefile
$(call FN_COLORED_TEXT,[ansiColor],msg)
```

**Parameters:**

| Parameter   | Description                                                            |
|-------------|------------------------------------------------------------------------|
| `ansiColor` | Optional ANSI color code (e.g. for bold bright green would be `92;1`). |
| `msg`       | Message to be printed to stdout.                                       |

#### FN_LOG

Generates an echo command for a log message.

!!! Notes
    * Real color support relies on terminal support. If there is no support colors are ignored.
    * This function returns the command string to be used by recipees. It does not execute any actual printing command.

 **Syntax:**

```Makefile
$(call FN_LOG,[color],msg)
```

**Parameters:**

| Parameter   | Description                                                            |
|-------------|------------------------------------------------------------------------|
| `ansiColor` | Optional ANSI color code (e.g. for bold bright green would be `92;1`). |
| `msg`       | Message to be printed to stdout.                                       |

#### FN_LOG_INFO

Generates an echo command for INFO log message.

!!! Notes
    * Real color support relies on terminal support. If there is no support colors are ignored.
    * This function returns the command string to be used by recipees. It does not execute any actual printing command.

 **Syntax:**

```Makefile
$(call FN_LOG_INFO,[useColor],msg)
```

**Parameters:**

| Parameter  | Description                                                                                                                                                |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `useColor` | Defines if generated command should use colored text. Defaults to `0` (no color output).<br/>Any other non-empty value will cause the use of colored text. |
| `msg`      | Message to be printed to stdout.                                                                                                                           |
