!!! hint "Review status: OK"

# native.mk

This makefile tries to detect native host and exposes information through output variables.

Currently supported hosts are `linux-x86`, `linux-x64`, `linux-arm`, `linux-arm64`, `windows-x86`, `windows-x64`, `windows-arm`, `windows-arm64`.

--------------------------------------------------------------------------------

## Basic usage

When this makefile is included, it tries to detect native host and expose information through output variables.

```Makefile
include $(CPB_DIR)/native.mk
```

!!! Note
    This makefile is automatically included by `builder.mk`.

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

### Input variables

_This makefile does not expect any input variables._

--------------------------------------------------------------------------------

### Output variables

The following variables are generated automatically by this makefile in order to expose native host:

#### NATIVE_OS

* **Description:** Contains detected native operting system.
* **Required:**  Not applicable (variable is set by the build system).
* **Default value:** Detected native operting system. If it would not be possible to detect it, variable will be empty/undefined.
* **Origins:**  Not applicable (variable is set by the build system).
* **Restrictions:** This is a read-only reserved variable.

#### NATIVE_ARCH

* **Description:** Contains detected native CPU architecture.
* **Required:** Not applicable (variable is set by the build system).
* **Default value:** Detected native CPU architecture. If it would not be possible to detect it, variable will be empty/undefined.
* **Origins:** Not applicable (variable is set by the build system).
* **Restrictions:** This is a read-only reserved variable.

#### NATIVE_HOST

* **Description:** Contains detected native HOST.
* **Required:** Not applicable (variable is set by the build system).
* **Default value:** Detected native HOST (a combination of [`NATIVE_OS`](#native_os) and [`NATIVE_ARCH`](#native_arch)). If it would not be possible to detect it, variable will be empty/undefined.
* **Origins:** Not applicable (variable is set by the build system).
* **Restrictions:** This is a read-only reserved variable.

--------------------------------------------------------------------------------

## Functions

_This makefile does not expose any function._
