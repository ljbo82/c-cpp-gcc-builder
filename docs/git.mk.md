# git.mk

This file inspects project's directory tree and exposes git repository information (current commit, tag, status, etc) through output variables.

## Variables

Following are described all variables used/exported by this makefile:

!!! note "Variable details"
    For each detailed variable, the following fields refer to:

    * **Description:** Contains descriptive information about the variable.

    * **Required:** Defines if a variable must be defined (and it must be non-empty) during build.

    * **Default value:** Contains the value which will be assumed if variable is optional and it is not defined.

    * **Mutable:** Some variables defined in makefiles can be updated by the build system. This field explain details about how such variables can be modified by the build system.

    * **Origins:** Contains the list of allowed origins for variable definition.

    * **Restrictions:** Contains information about restrictions on which kind of values that can be stored in the variable.

### Input variables

The following variables are used to customize the repository inspection:

#### GIT_REPO_DIR

* **Description:** Defines directory containing the repository to be inspected.
* **Required:** No
* **Default value:** `.` _(current directory)_
* **Origins:** Makefile
* **Restrictions:** Value shall not contain whitespaces nor can be result into an empty string.

### Output variables

The following variables are generated automatically by this makefile in order to expose repository information:

#### GIT_COMMIT

* **Description:** Contains current commit hash for inspected repository. If directory is not versioned by git, variable will be undefined.
* **Required:** _(Not applicable)_
* **Default value:** _(Not applicable)_
* **Origins:** _(Not applicable)_
* **Restrictions:** This is a read-only reserved variable.

#### GIT_COMMIT_SHORT

* **Description:** Contains current short commit for inspected repository. If directory is not versioned by git, variable will be undefined.
* **Required:** _(Not applicable)_
* **Default value:** _(Not applicable)_
* **Origins:** _(Not applicable)_
* **Restrictions:** This is a read-only reserved variable.

#### GIT_STATUS

* **Description:** Contains repository status. Possible values are:

    * `clean` : Repository does not contain uncommited changes
    * `dirty` : Repository contains uncommited changes.

  If directory is not versioned by git, variable will be undefined.

* **Required:** _(Not applicable)_
* **Default value:** _(Not applicable)_
* **Origins:** _(Not applicable)_
* **Restrictions:** This is a read-only reserved variable.

#### GIT_TAG

* **Description:** Contains current tag for inspected repository. If directory is not versioned by git, variable will be undefined.
* **Required:** _(Not applicable)_
* **Default value:** _(Not applicable)_
* **Origins:** _(Not applicable)_
* **Restrictions:** This is a read-only reserved variable.

#### GIT_VERSION

* **Description:** Contains a candidate version for the project using current repository commit/tag. If directory is not versioned by git, variable value undefined.
* **Required:** _(Not applicable)_
* **Default value:** _(Not applicable)_
* **Origins:** _(Not applicable)_
* **Restrictions:** This is a read-only reserved variable.