# cpp-project-builder-demos

 This directory contains example projects using [cpp-project-builder](http://ljbo82.github.io/cpp-project-builder) build system:

* **`c-app/`**

   Contains an example of a pure-C application executable project.

* **`cpp-app/`**

   Contains an example of a pure C++ application executable project.

* **`deps/`**

   Contains an example of an application project which uses (and builds) dependencies (and their respective transient dependencies).

* **`lib/`**

   Contains an example of a library project.

* **`mixed-app/`**

   Contains an example of an application project containing both C and C++ source files.

* **`multiplatform/`**

   Contains an example of a multiplatorm project containing customizations according to target HOST.

# Building the examples

In order to build the examples, source the script `init-env`. This script will export the variable `CPB_DIR` automatically for the current shell:

> ```bash
> source init-env
> ```

# License

All demos are free and unencumbered software released into the public domain. Please see the [LICENSE](LICENSE) file for details on copying and distribution.
