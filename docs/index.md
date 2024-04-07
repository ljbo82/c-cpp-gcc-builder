# cpp-project-builder

cpp-project-builder provides a makefile-based build system containing standard recipes to build C/C++/Assembly multiplatform projects using a GCC-based compiler.

## License

cpp-project-builder is distributed under MIT License. Please see the  [LICENSE](https://github.com/ljbo82/cpp-project-builder/blob/master/LICENSE) file for details on copying and distribution.


## Basic usage

cpp-project-builder provides a makefile-based build system intended to be used by C/C++/Assembly projects in order to build source files using a GCC-based compiler.

!!! note  "Assumptions"
    * Although the build system simplifies a makefile writing process, the developer must have a basic knowledge about how [GNU Make](https://www.gnu.org/software/make/) works, and how to write makefiles. For details, check [GNU Make official documentation](https://www.gnu.org/software/make/manual/make.html).
    * Although your project's build logic could be splitted into multiple makefiles, in order make easier the explanation of the concepts, it will be assumed a project containing a single makefile responsible by the compilation/distribution process.
    * From this point onwards, the project root directory will be referred to as `<PROJ_ROOT>` and it is the directory where project's `Makefile` is located.

The build system can be either shared by multiple projects (i.e. multiple projects unsing a single copy of the build system), or it can be emebedded directly into your project.

The basic usage is comprised by the following steps:

1. Copy or clone the build system into a directory of your preference (from this point onwards, the directory containing the build system will be referred to as `<CPB_DIR>`).

    !!! note "Build system repository vs Build system aggregator repository"
        There are two respositories in which you can get the build system:

        * **Actual build system repository:**

            [https://github.com/ljbo82/cpp-project-builder-core](https://github.com/ljbo82/cpp-project-builder-core)

        * **Aggregator repository:**

            [https://github.com/ljbo82/cpp-project-builder](https://github.com/ljbo82/cpp-project-builder)

            The aggregator repository contains the actual build system (as a git submodule located in `core` subdirectory) along with documentation sources, testing application, etc.

            Be aware that if you get the aggregator repository, `<CPB_DIR>` should point to its `core` subdirectory.

    !!! note "Recommended way to share the build system with multiple projects"
        It is recommended to declare an environment variable named `CPB_DIR` with value pointing to the directory where the shared build system is located. This environment variable can have any valid name, but be sure to refer to it by using the same name in your project's `Makefile`.

        Both the build system repo, as well the aggregator one provide a convenience script named `init-env`, which expose the variable `CPB_DIR` correctly when sourced.

2. Place project's C/C++/Assembly source and header files into specific directories:

    * Source files should be placed into `<PROJ_ROOT>/src`.
    * If you are developing a library, the public headers should be placed into  `<PROJ_ROOT>/include`.

    !!! note
        Source and public header files can be placed anywhere inside `<PROJ_ROOT>`, but if you use [custom directories](user-guide/#input-directories-and-files), you have to declare them explicitly in your makefile.

3. Create a `Makefile` inside `<PROJ_ROOT>` containing [variables](variables) defining how your project shall be built (a minimal Makefile has to provide, at least, the variables [`PROJ_NAME`](variables/#proj_name) and [`PROJ_TYPE`](variables/#proj_type)).

4. At the end of your `<PROJ_ROOT>/Makefile`, include the file `builder.mk` provided by the build system:

    <pre><code class="language-makefile hljs">include $(CPB_DIR)/builder.mk</code></pre>

Following above guidelines, a minimal `Makefile` would look like this:

```Makefile
PROJ_NAME = MyProject
PROJ_TYPE = app

include $(CPB_DIR)/builder.mk
```

Now your project is ready to be built.

Just call `make` (from `<PROJ_ROOT>` directory, or use `make -C <PROJ_ROOT>` from any other directory) in order to build your project.

For further details about the build system (e.g. how to customize build process, use custom source directories, support multiple platforms, etc.), check the [user guide](user-guide).

For more examples, check the [demos](https://github.com/ljbo82/cpp-project-builder/tree/dev/demos).

## Makefiles

The build system is composed by multiple makefiles which, when included by your project's `Makefile`, they could:

* Expect certain [variables](#../variables) to be defined in order to customize its actions.
* Expose some useful information that can be used during build through [variables](#../variables).
* Provide make targets for certain actions.
* Provide utility functions.

Here is a summary of the makefiles provided by the build system which can be included by your project (note that some of them are included manually uppon including others):

### builder.mk

This is the main makefile provided by the build system. It contains standard recipes to build C/C++/Assembly multiplatform-ready projects using a GCC-based compiler.

Include this file at the end of your `<PROJ_ROOT>/Makefile`.

### doxygen.mk

This makefile provides a target to generate source documentation using [doxygen](https://www.doxygen.nl/index.html).

See makefile [documentation](doxygen.mk.md) for details.

### functions.mk

This makefile exposes utility makefile functions used by the build system, which can also be used by your project.

!!! note
    This makefile is automatically included by [builder.mk](#buildermk), [git.mk](#gitmk), and [doxygen.mk](#doxygenmk).

    If you want to use its functions before the inclusion of `builder.mk`, include it manually.

See makefile [documentation](functions.mk.md) for details.

### git.mk

This file inspects `<PROJ_ROOT>` directory and exposes git repository information (current commit, tag, status, etc) through certain variables.

See makefile [documentation](git.mk.md) for details.

### native.mk

This makefile tries to detect native host and exposes information through output variables.

!!! note
    This makefile is automatically included by `builder.mk`.

    If you want to use its exposed variables before the inclusion of `builder.mk`, include it manually.

See makefile [documentation](native.mk.md) for details.
