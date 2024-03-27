!!! danger "Review status: IN PROGRESS"

# functions.mk

This makefile exposes utility makefile functions used by the build system, which can also be used by your project.

## Basic usage

By including this makefile it will expose several utility functions which can be invoked via GNU Make [`$(call)`](https://www.gnu.org/software/make/manual/html_node/Call-Function.html) function.

```Makefile
include $(CPB_DIR)/functions.mk
```

!!! note
    This makefile is automatically included by `builder.mk`

## Make targets

_This makefile does not expose any target._

## Variables

_This makefile does not expect nor expose any variables (except [functions](#functions))._

## Functions

Following are listed exposed functions:

### Text functions

#### FN_SPLIT

#### FN_TOKEN

#### FN_UNIQUE

#### FN_EQ

#### FN_REVERSE

#### FN_HOST_FACTORIZE

#### FN_NUMBER_CMP

### Semantic versioning

#### FN_SEMVER_CHECK

#### FN_SEMVER_MAJOR

#### FN_SEMVER_MINOR

#### FN_SEMVER_PATCH

#### FN_SEMVER_CMP

### File system functions

#### FN_FIND_FILES

#### FN_REL_DIR

#### FN_IS_INSIDE_DIR

### Makefile utilities

#### FN_SHELL

#### FN_CHECK_ORIGIN

#### FN_CHECK_OPTIONS

#### FN_CHECK_NON_EMPTY

#### FN_CHECK_NO_WHITESPACE

#### FN_CHECK_RESERVED

Checks if a reserved variable is defined elsewhere

**Syntax:**

```Makefile
$(call FN_CHECK_RESERVED,varName,errorMessage=?)
```

**Parameters:**

| Parameter | Details |
|-----------|---------|
| varName | Variable name |


### Colored output

#### FN_COLORED_TEXT

#### FN_LOG

#### FN_LOG_INFO




* **`$(call FN_SPLIT,baseString,delimiter,cutIndex)`**

  Returns a token on delimited string.

  **Parameters:**

  * `baseString`

    String containing tokens.

  * `delimiter`

    Single char used to delimit tokens.

  * `cutIndex`

    Token index (starts at 1) according to [cut(1)](https://man7.org/linux/man-pages/man1/cut.1.html) syntax (see `-f` option).

* **`$(call FN_UNIQUE,list)`**

  Removes duplicate entries in a list without sorting.

  **Parameters:**

  * `list`

    Whitespace-delimited list of values.


* **`$(call FN_EQ,val1,val2)`**

  Checks if given two values are equal each other. On success, returns the value, otherwise, returns an empty value.

  **Parameters:**

  * `val1`

    First value.

  * `val2`

    Second value.

### Semantic version functions

* **`$(call FN_SEMVER_CHECK,semanticVersion)`**

  Checks if a given value contains a valid semantic version. On success, returns the value. Otherwise returns an empty value.

  **Parameters:**

  * `semanticVersion`

    Tested value.

* **`$(call FN_SEMVER_MAJOR,semanticVersion)`**

  Returns the major component for given semantic version (if it is invalid, returns an empty value).

  **Parameters:**

  * `semanticVersion`

    Tested value.

* **`$(call FN_SEMVER_MINOR,semanticVersion)`**

  Returns the minor component for given semantic version (if it is invalid, returns an empty value).

  **Parameters:**

  * `semanticVersion`

    Tested value.

* **`$(call FN_SEMVER_PATCH,semanticVersion)`**

  Returns the patch component for given semantic version (if it is invalid, returns an empty value).

  **Parameters:**

  * `semanticVersion`

    Tested value.

### Filesystem functions

* **`$(call FN_FIND_FILES,directory,findFlags)`**

  Lists files in a directory.

  **Parameters:**

  * `directory`

    Inspected directory path.

  * `findFlags`

    Flags to be passed to [find(1)](https://linux.die.net/man/1/find).

* **`$(call FN_IS_INSIDE_DIR,dir,path)`**

  Checks if a path is inside a directory (on success, returns the path, otherwise returns an empty value).

  **Parameters:**

  * `dir`

    Directory where given path must be contained.

  * `path`

    Tested path.

* **`$(call FN_REL_DIR,srcDir,destDir)`**

  Returns the relative path between source and destination directories.

  This function is useful when defining the output directory of a library being build as a dependency for another project.

  **Parameters:**

  * `srcDir`

    Source directory.

  * `destDir`

    Destination directory.
