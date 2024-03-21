# functions.mk

This file provides utility functions that can be used by other makefiles (using [`$(call)`](https://www.gnu.org/software/make/manual/html_node/Call-Function.html)).

## Exposed functions

Following are listed exposed functions:

### Text functions

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
