# functions.mk

This makefile exposes utility makefile functions used by the build system, which can also be used by your project.

--------------------------------------------------------------------------------

## Basic usage

By including this makefile it will expose several utility functions which can be invoked via GNU Make [`$(call)`](https://www.gnu.org/software/make/manual/html_node/Call-Function.html) function (in the following example is assumed the existence of the variable `CPB_DIR` pointing the directory where the build system is located):

```Makefile
include $(CPB_DIR)/functions.mk
```

!!! note
    This makefile is automatically included by [builder.mk](../builder.mk), [git.mk](../git.mk), [doxygen.mk](../doxygen.mk), and [native.mk](../native.mk).

--------------------------------------------------------------------------------

## Make targets

_This makefile does not expose any target._

--------------------------------------------------------------------------------

## Variables

!!! note "Variable details"
    For each detailed variable, the following fields refer to:

    * **Description:** Contains descriptive information about the variable.

    * **Required:** Defines if a variable must be defined (and it must be non-empty) during build.

    * **Default value:** Contains the value which will be assumed if variable is optional and it is not defined.

    * **Origins:** Contains the list of allowed origins for variable definition.

    * **Restrictions:** Contains information about restrictions on which kind of values that can be stored in the variable.

!!! Warning
    The build system declare internal private variables and functions that are not intended to be used by projects. All of those private variables and functions, have their names prefixed with `cpb_` prefix. Please avoid using/defining variables or functions with names beginning with such prefix.

    The build system checks for attempts to define variables and functions with the same name of reserved ones. Any attempt to define such items will result in errors being raised by the build system.

### Input variables

_This makefile does not expect any variables._

--------------------------------------------------------------------------------

### Output variables

#### comma

* **Description:** Escape variable to represent a comma char (see limitations of [`$(call)`](https://www.gnu.org/software/make/manual/html_node/Syntax-of-Functions.html)).
* **Required:** Not applicable (variable is set by the build system).
* **Default value:** Variable expands to a `,` (comma) character.
* **Origins:** Not applicable (variable is set by the build system).
* **Restrictions:** This is a read-only reserved variable.
--------------------------------------------------------------------------------

#### empty

* **Description:** Escape variable to represent an empty value (see limitations of [`$(call)`](https://www.gnu.org/software/make/manual/html_node/Syntax-of-Functions.html)).
* **Required:** Not applicable (variable is set by the build system).
* **Default value:** The variable expands to an empty value.
* **Origins:** Not applicable (variable is set by the build system).
* **Restrictions:** This is a read-only reserved variable.
--------------------------------------------------------------------------------

#### space

* **Description:** Escape variable to represent a whitespace value (see limitations of [`$(call)`](https://www.gnu.org/software/make/manual/html_node/Syntax-of-Functions.html)).
* **Required:** Not applicable (variable is set by the build system).
* **Default value:** The variable expands to a single whitespace.
* **Origins:** Not applicable (variable is set by the build system).
* **Restrictions:** This is a read-only reserved variable.
--------------------------------------------------------------------------------

## Functions

Following are listed exposed functions:

### Validations

#### fn_check_no_whitespace

Ensures a variable value has no whitespaces.

If a variable value has whitespaces, an error will be raised.

**Syntax:**

```Makefile
$(call fn_check_no_whitespace,varName,[errorMessage=<predefined_message>])
```

**Parameters:**

| Parameter      | Details                                                                                                                     |
|----------------|-----------------------------------------------------------------------------------------------------------------------------|
| `varName`      | Variable name                                                                                                               |
| `errorMessage` | Optional error message. If value is suppressed or an empty value is given,<br/>a standardized message will be used instead. |

**Return value:**

_This function does not return any value._

--------------------------------------------------------------------------------

#### fn_check_not_empty

Checks if a variable, which should NOT be empty, has an empty value.

If variable has an empty value, an error will be raised.

**Syntax:**

```Makefile
$(call fn_check_not_empty,varName,[errorMessage=<predefined_message>])
```

**Parameters:**

| Parameter      | Description                                                                                                                 |
|----------------|-----------------------------------------------------------------------------------------------------------------------------|
| `varName`      | Variable name                                                                                                               |
| `errorMessage` | Optional error message. If value is suppressed or an empty value is given,<br/>a standardized message will be used instead. |

**Return value:**

_This function does not return any value._

--------------------------------------------------------------------------------

#### fn_check_not_origin

Ensures the [origin](https://www.gnu.org/software/make/manual/make.html#Origin-Function) of an variable differs from a forbidden one.

If a variable has the same origin as a forbidden one, an error will be raised.

**Syntax:**

```Makefile
$(call fn_check_not_origin,varName,forbiddenOrigin,[errorMessage=<predefined_message>])
```

**Parameters:**

| Parameter         | Description                                                                                                                 |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `varName`         | Variable name                                                                                                               |
| `forbiddenOrigin` | Forbidden origin.                                                                                                           |
| `errorMessage`    | Optional error message. If value is suppressed or an empty value is given,<br/>a standardized message will be used instead. |

**Return value:**

_This function does not return any value._

--------------------------------------------------------------------------------





#### fn_check_options

Ensures the contents of a variable is one among a list of accepted values.

If variable contents has an unexpected value, an error will be raised.

**Syntax:**

```Makefile
$(call fn_check_options,varName,acceptedOptions,[errorMessage=<predefined_message>])
```

**Parameters:**

| Parameter         | Description                                                                                                                 |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `varName`         | Variable name                                                                                                               |
| `acceptedOptions` | List of accepted words for variable contents.                                                                               |
| `errorMessage`    | Optional error message. If value is suppressed or an empty value is given,<br/>a standardized message will be used instead. |

**Return value:**

_This function does not return any value._

--------------------------------------------------------------------------------

#### fn_check_origin

Ensures the [origin](https://www.gnu.org/software/make/manual/make.html#Origin-Function) of an variable.

If a variable has an unexpected origin, an error will be raised.

**Syntax:**

```Makefile
$(call fn_check_origin,varName,expectedOrigin,[errorMessage=<predefined_message>])
```

**Parameters:**

| Parameter        | Description                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `varName`        | Variable name                                                                                                               |
| `expectedOrigin` | Accepted origin for the variable.                                                                                           |
| `errorMessage`   | Optional error message. If value is suppressed or an empty value is given,<br/>a standardized message will be used instead. |

**Return value:**

_This function does not return any value._

--------------------------------------------------------------------------------

#### fn_check_reserved

Ensures a variable is not defined until the call the function.

If variable is defined in the moment of calling this function, it will raise an error.

**Syntax:**

```Makefile
$(call fn_check_reserved,varName,[errorMessage=<predefined_message>])
```

**Parameters:**

| Parameter      | Details                                                                                                                     |
|----------------|-----------------------------------------------------------------------------------------------------------------------------|
| `varName`      | Variable name                                                                                                               |
| `errorMessage` | Optional error message. If value is suppressed or an empty value is given,<br/>a standardized message will be used instead. |

**Return value:**

_This function does not return any value._

--------------------------------------------------------------------------------

### Text functions

#### fn_eq

Checks if two strings are equal each other.

**Syntax:**

```Makefile
$(call fn_eq,srt1,str2)
```

**Parameters:**

| Parameter | Details        |
|-----------|----------------|
| `srt1`    | First string.  |
| `str2`    | Second string. |

**Return value:**

If strings are equal, returns the string. Otherwise, returns an empty value.

--------------------------------------------------------------------------------

#### fn_host_factorize

Factorizes a host string (used to decompose host string into a list of compatible layers).

For example, the value `linux-arm-v7` can be decomposed into `linux`, `linux/arm`, `linux/arm/v7` layers.

**Syntax:**

```Makefile
$(call fn_host_factorize,hostString,[delimiter=-],[replacement=/])
```

**Parameters:**

| Parameter     | Details                                                                               |
|---------------|---------------------------------------------------------------------------------------|
| `hostString`  | A host string value (e.g. `linux-arm-v7`).                                            |
| `delimiter`   | Optional token delimiter for `hostString` (defaults to `-`).                          |
| `replacement` | Optional replacement for delimiters while factorizing `hostString` (defaults to `/`). |

**Return value:**

A list of decomposed compatible layers for given `hostString`.

--------------------------------------------------------------------------------

#### fn_reverse

Reverses a list of words.

**Syntax:**

```Makefile
$(call fn_reverse,word1 word2 ...)
```

**Parameters:**

| Parameter         | Details        |
|--------------  ---|----------------|
| `word1 word2 ...` | List of words. |

**Return value:**

A reversed list of words.

--------------------------------------------------------------------------------

#### fn_split

Explodes a delimited word into a list of words.

**Syntax:**

```Makefile
$(call fn_split,delimitedWord,delimiter,[tokenPrefix=__?__])
```

**Parameters:**

| Parameter       | Details                                                                                                                                                                                            |
|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `delimitedWord` | Delimited word which will be exploded into a list of words.                                                                                                                                        |
| `delimiter`     | Delimiter used to explode the string into a list of words.                                                                                                                                         |
| `tokenPrefix`   | Optional token prefix to be added for each word.<br/> Since GNU Make ignores empty words, a token prefix can be used to force<br/>split of empty tokens (afterwards token prefix shall be removed).|

**Return value:**

A list of words as a result of exploding given string using given delimiter.

--------------------------------------------------------------------------------

#### fn_text

Generate a colored string.

!!! Note
    Real color support relies on terminal support. If there is no support, colors are ignored.

**Syntax:**

```Makefile
$(call fn_text,msg,[ansiColor=])
```

**Parameters:**

| Parameter   | Description                                                            |
|-------------|------------------------------------------------------------------------|
| `msg`       | Message to be printed to stdout.                                       |
| `ansiColor` | Optional ANSI color code (e.g. for bold bright green would be `92;1`). |

**Return value:**

If terminal support color output, return colored `msg`. If either `ansiColor` is not provided, or terminal does not support color output, returns `msg`.

--------------------------------------------------------------------------------

#### fn_token

Returns a token on delimited word (i.e. explodes the word into a list of words and returns a word of generated list).

**Syntax:**

```Makefile
$(call fn_token,delimitedWord,delimiter,index)
```

**Parameters:**

| Parameter       | Details                                                          |
|-----------------|------------------------------------------------------------------|
| `delimitedWord` | Delimited word which will be exploded into a list of words.      |
| `delimiter`     | Delimiter used to explode the word into a list of words.         |
| `index`         | Index of word to get from generated list (first element is `1`). |

**Return value:**

The corresponding word of exploded string.

--------------------------------------------------------------------------------

#### fn_unique

Returns a string removing duplicate words without sorting.

This function differs from GNU Make [`$(sort)`](https://www.gnu.org/software/make/manual/make.html#Text-Functions) in terms of sorting. `$(sort)` removes duplicate words sorting resulting string. This function only remove duplicate words preserving original ordering or words.

**Syntax:**

```Makefile
$(call fn_unique,word1 word2 ...)
```

**Parameters:**

| Parameter         | Details        |
|--------------  ---|----------------|
| `word1 word2 ...` | List of words. |

**Return value:**

The string without duplicate words

--------------------------------------------------------------------------------

### Semantic versioning

#### fn_semver

Checks if a semantic version string is valid.

A valid semantic version matches with the following regex:

```text
<major>[.<minor>[.<patch>]][-<metadata>]
```

* `major` must be a numeric value.
* `minor` must be a numeric value. If omitted, it is assumed `0` for comparisons.
* `patch` must be a numeric value. If omitted, it is assumed `0` for comparisons.
* `metadata` must match with the regex `[A-Za-z0-9_\.\-]+`

**Syntax:**

```Makefile
$(call fn_semver,semanticVersion,[errorMessage=<predefined_message>])
```

**Parameters:**

| Parameter         | Details                            |
|-------------------|------------------------------------|
| `semanticVersion` | Semantic version string.           |
| `errorMessage`    | Optional customized error message. |

**Return value:**

If given value is valid, returns it. Otherwise, raises an error.

--------------------------------------------------------------------------------

#### fn_semver_check_compat

Checks if a version is compatible with a minimum one. If version is not compatible, it raises an error.

See [fn_semver](#fn_semver).

**Syntax:**

```Makefile
$(call fn_semver_check_compat,minVersion,version,[errorMessage=<predefined_message>])
```

**Parameters:**

| Parameter      | Details                            |
|----------------|------------------------------------|
| `minVersion`   | Minimum accepted version.          |
| `version`      | Tested version.                    |
| `errorMessage` | Optional customized error message. |

**Return value:**

_This function does not return any value._

--------------------------------------------------------------------------------

#### fn_semver_cmp

Compares two semantic versions.

See [fn_semver](#fn_semver).

**Syntax:**

```Makefile
$(call fn_semver_cmp,v1,v2)
```

**Parameters:**

| Parameter      | Details         |
|----------------|-----------------|
| `v1`           | First version.  |
| `v2`           | Second version. |

**Return value:**

| Return value | If                                                                                       |
|--------------|------------------------------------------------------------------------------------------|
| `-3`         | `v1.major < v2.major`.                                                                   |
| `3`          | `v1.major > v2.major`.                                                                   |
| `-2`         | `v1.major == v2.major and v1.minor < v2.minor`.                                          |
| `2`          | `v1.major == v2.major and v1.minor > v2.minor`.                                          |
| `-1`         | `v1.major == v2.major, v1.minor == v2.minor and v1.patch < v2.patch`.                    |
| `1`          | `v1.major == v2.major, v1.minor == v2.minor and v1.patch > v2.patch`.                    |
| `0`          | Versions are equal (NOTE: any [metadata](#fn_semver_metadata) is ignored in comparison). |

If any of provided versions is invalid, an error will be raised.

--------------------------------------------------------------------------------

#### fn_semver_major

Returns the major component for given version.

See [fn_semver](#fn_semver).

**Syntax:**

```Makefile
$(call fn_semver_major,semanticVersion)
```

**Parameters:**

| Parameter         | Details                  |
|-------------------|--------------------------|
| `semanticVersion` | Semantic version string. |

**Return value:**

The major component of given version.

--------------------------------------------------------------------------------

#### fn_semver_metadata

Returns the metadata component for given version.

See [fn_semver](#fn_semver).

**Syntax:**

```Makefile
$(call fn_semver_metadata,semanticVersion)
```

**Parameters:**

| Parameter         | Details                  |
|-------------------|--------------------------|
| `semanticVersion` | Semantic version string. |

**Return value:**

The metadata component of given version. If there is no metadata component in `semanticVersion`, returns an empty string.

--------------------------------------------------------------------------------

#### fn_semver_minor

Returns the minor component for given version.

See [fn_semver](#fn_semver).

**Syntax:**

```Makefile
$(call fn_semver_minor,semanticVersion)
```

**Parameters:**

| Parameter         | Details                  |
|-------------------|--------------------------|
| `semanticVersion` | Semantic version string. |

**Return value:**

The minor component of given version. If there is no minor component in `semanticVersion`, returns an empty string.

--------------------------------------------------------------------------------

#### fn_semver_patch

Returns the patch component for given version.

See [fn_semver](#fn_semver).

**Syntax:**

```Makefile
$(call fn_semver_patch,semanticVersion)
```

**Parameters:**

| Parameter         | Details                  |
|-------------------|--------------------------|
| `semanticVersion` | Semantic version string. |

**Return value:**

The patch component of given version. If there is no patch component in `semanticVersion`, returns an empty string.

--------------------------------------------------------------------------------

### File system functions

#### fn_find_files

Lists files in a directory.

**Syntax:**

```Makefile
$(call fn_find_files,directory,[findFlags=])
```

**Parameters:**

| Parameter   | Details                                            |
|-------------|----------------------------------------------------|
| `directory` | Path to the directory which will be inspected.     |
| `findFlags` | Optional flags to be passed to the `find` command. |

**Return value:**

This function returns the list of files in given directory (by default recursively) through a call to the [`find`](https://man7.org/linux/man-pages/man1/find.1.html) command.

--------------------------------------------------------------------------------

#### fn_is_inside_dir

Checks if a path is inside a directory.

**Syntax:**

```Makefile
$(call fn_is_inside_dir,parentDir,path)
```

**Parameters:**

| Parameter   | Details                                           |
|-------------|---------------------------------------------------|
| `parentDir` | Directory which should be parent of given `path`. |
| `path`      | Tested path.                                      |

**Return value:**

If given path correspond to a path inside given directory, return the path. Otherwise, returns an empty value.

--------------------------------------------------------------------------------

#### fn_rel_dir

Returns the relative path for going from `fromDir` to `toDir`.

**Syntax:**

```Makefile
$(call fn_rel_dir,fromDir,toDir)
```

**Parameters:**

| Parameter | Details                     |
|-----------|-----------------------------|
| `fromDir` | Departure directory path.   |
| `toDir`   | Destination directory path. |

**Return value:**

Returns the relative path for going from `fromDir` to `toDir`.

--------------------------------------------------------------------------------

### Miscellaneous

#### fn_error

Raises an error and output a colored message.

!!! Notes
    * Real color support relies on terminal support. If there is no support colors are ignored.

 **Syntax:**

```Makefile
$(call fn_error,msg,[skipColor=0])
```

**Parameters:**

| Parameter   | Description                                                                                                                        |
|-------------|------------------------------------------------------------------------------------------------------------------------------------|
| `msg`       | Message to be printed.                                                                                                             |
| `skipColor` | Optional parameter which instructs the call to not use colors. Defaults to `0` (by default text is colored when there is support). |


**Return value:**

_This function does not return any value._

--------------------------------------------------------------------------------

#### fn_info

Prints a colored info message into console.

!!! Notes
    * Real color support relies on terminal support. If there is no support colors are ignored.

 **Syntax:**

```Makefile
$(call fn_info,msg,[skipColor=0])
```

**Parameters:**

| Parameter   | Description                                                                                                                        |
|-------------|------------------------------------------------------------------------------------------------------------------------------------|
| `msg`       | Message to be printed.                                                                                                             |
| `skipColor` | Optional parameter which instructs the call to not use colors. Defaults to `0` (by default text is colored when there is support). |

**Return value:**

_This function does not return any value._

--------------------------------------------------------------------------------

#### fn_log

Prints an log message in standardized way. If verbose mode is informed, messages are colored.

!!! Notes
    * Real color support relies on terminal support. If there is no support colors are ignored.

 **Syntax:**

```Makefile
$(call fn_log,msg,[verbose=0])
```

**Parameters:**

| Parameter  | Description                                                                        |
|------------|------------------------------------------------------------------------------------|
| `msg`      | Message to be printed to stdout.                                                   |
| `verbose`  | Defines if generated command for verbose mode. Defaults to `0` (non-verbose mode). |

**Return value:**

_This function does not return any value._

--------------------------------------------------------------------------------

#### fn_number_cmp

Numeric comparison of two numbers.

**Syntax:**

```Makefile
$(call fn_number_cmp,[first=0],[second=0])
```

**Parameters:**

| Parameter | Details                                              |
|-----------|------------------------------------------------------|
| `first`   | First number. If empty, `0` (zero) will be assumed.  |
| `second`  | Second number. If empty, `0` (zero) will be assumed. |

**Return value:**

| Returned value | If                        |
|----------------|---------------------------|
| `0`            | first == second           |
| `1`            | first > second            |
| `-1`           | first < second            |
| `?`            | Invalid values were given |

--------------------------------------------------------------------------------

#### fn_shell

Executes a shell command and returns execution output.

This function differs from [`$(shell)`](https://www.gnu.org/software/make/manual/make.html#Shell-Function) in terms of error handling. With this function, if an error happens in the execution, an error will be raised.

**Syntax:**

```Makefile
$(call fn_shell,cmd,[errorMessage=<predefined_message>])
```

**Parameters:**

| Parameter        | Description                                                                                                                 |
|------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `cmd`            | Shell command to execute                                                                                                    |
| `errorMessage`   | Optional error message. If value is suppressed or an empty value is given,<br/>a standardized message will be used instead. |

**Return value:**

Output of given `cmd` execution.

--------------------------------------------------------------------------------

#### fn_warning

Prints a colored warning message into console.

!!! Notes
    * Real color support relies on terminal support. If there is no support colors are ignored.

 **Syntax:**

```Makefile
$(call fn_warning,msg,[skipColor=0])
```

**Parameters:**

| Parameter   | Description                                                                                                                        |
|-------------|------------------------------------------------------------------------------------------------------------------------------------|
| `msg`       | Message to be printed.                                                                                                             |
| `skipColor` | Optional parameter which instructs the call to not use colors. Defaults to `0` (by default text is colored when there is support). |

**Return value:**

_This function does not return any value._

--------------------------------------------------------------------------------
