@ECHO OFF
set SPHINXBUILD=sphinx-build
set SOURCEDIR=.
set BUILDDIR=_build

if "%1" == "html" (
    %SPHINXBUILD% -b html %SOURCEDIR% %BUILDDIR%/html
    goto end
)
if "%1" == "api" (
    sphinx-apidoc -o api ..\src
    goto end
)
if "%1" == "clean" (
    rmdir /S /Q %BUILDDIR%
    del /Q api\*.rst
    goto end
)
:end
