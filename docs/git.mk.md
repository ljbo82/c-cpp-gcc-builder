# git.mk

This file inspects `<PROJ_ROOT>` directory and exposes git repository information (current commit, tag, status, etc) through certain variables.

--------------------------------------------------------------------------------

## Basic usage

When this makefile is included, it will expose git repository (if applicable) information through output variables (in the following example is assumed the existence of the variable `CPB_DIR` pointing the directory where the build system is located):

```Makefile
include $(CPB_DIR)/git.mk
```

--------------------------------------------------------------------------------

## Make targets

_This makefile does not expose any target._

--------------------------------------------------------------------------------

## Variables

Following are described all variables used/exported by this makefile:

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

The following variables are used to customize the repository inspection:

#### GIT_REPO_DIR

* **Description:** Defines directory containing the repository to be inspected.
* **Required:** No.
* **Default value:** `.` (current directory).
* **Origins:** Makefile.
* **Restrictions:** Value shall not contain whitespaces nor can be result into an empty string.

--------------------------------------------------------------------------------

### Output variables

The following variables are generated automatically by this makefile in order to expose repository information:

#### GIT_COMMIT

* **Description:** Contains current commit hash for inspected repository.
* **Required:** Not applicable (variable is set by the build system).
* **Default value:** Current commit hash for inspected repository. If directory is not versioned by git, variable will be undefined.
* **Origins:** Not applicable (variable is set by the build system).
* **Restrictions:** This is a read-only reserved variable.

--------------------------------------------------------------------------------

#### GIT_COMMIT_SHORT

* **Description:** Contains current short commit for inspected repository.
* **Required:** Not applicable (variable is set by the build system).
* **Default value:** Current short commit for inspected repository. If directory is not versioned by git, variable will be undefined.
* **Origins:** Not applicable (variable is set by the build system).
* **Restrictions:** This is a read-only reserved variable.

--------------------------------------------------------------------------------

#### GIT_STATUS

* **Description:** Contains repository status.
* **Required:** Not applicable (variable is set by the build system).
* **Default value:** Repository status. Possible values are:
    * `clean` : Repository does not contain uncommited changes
    * `dirty` : Repository contains uncommited changes.

    If directory is not versioned by git, variable will be undefined.

* **Origins:** Not applicable (variable is set by the build system).
* **Restrictions:** This is a read-only reserved variable.

--------------------------------------------------------------------------------

#### GIT_TAG

* **Description:** Contains current tag for inspected repository.
* **Required:** Not applicable (variable is set by the build system).
* **Default value:** Current tag for inspected repository. If directory is not versioned by git, variable will be undefined.
* **Origins:** Not applicable (variable is set by the build system).
* **Restrictions:** This is a read-only reserved variable.

--------------------------------------------------------------------------------

#### GIT_VERSION

* **Description:** Contains a candidate version for the project using current repository commit/tag.
* **Required:** Not applicable (variable is set by the build system).
* **Default value:** Candidate version for the project using current repository commit/tag. If directory is not versioned by git, variable value undefined.
* **Origins:** Not applicable (variable is set by the build system).
* **Restrictions:** This is a read-only reserved variable.

--------------------------------------------------------------------------------

## Functions

_This makefile does not expose any function explicitly._
