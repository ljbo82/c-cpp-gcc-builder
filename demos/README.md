# cpp-project-builder-demos

 [This repository](https://github.com/ljbo82/cpp-project-builder-demos) contains example projects using [cpp-project-builder](tbd) build system:

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

In order to build demos the environment variable `CPB_DIR` must be defined and must point to the directory containing the Build system.

* If you cloned/copied the [whole build system project](https://github.com/ljbo82/cpp-project-builder) (containing documentation, demos, and the build system itself), the `CPB_DIR` environment variable must point to the its `core` subdirectory.

* If you just cloned/copied only the [build system](https://github.com/ljbo82/cpp-project-builder-core), the `CPB_DIR` environment variable must point to the directory containing the copy / cloned repository.

> **Convenience script**
>
> If you cloned/copied the whole build system project, source the script `init-env`. This script will export the variable `CPB_DIR` automatically for the current shell:
>
> ```bash
> source init-env
> ```

# License

All demos are free and unencumbered software released into the public domain. Please see the [LICENSE](LICENSE) file for details on copying and distribution.
