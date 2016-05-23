# jfmt
Java code formatter. This is an interface to the [Google Java Format](https://github.com/google/google-java-format). For convinience it is stored in this repo in the `fmt` folder.

### Usage
There is two ways. First one is preffered.

**First** is to make an alias to jfmt:

```
# Java Code Format
alias jfmt="~/path/to/jfmt.py"
```

Dont forget to change permissions `chmod +x jfmt.py`. Now you are able to run it like `cd` or whatever.

**Second** run script directly.


### Arguments

`$ jfmt` - (no arguments) script which runned without arguments will recursively walk, starting from current working directory` through earch folder and lint .java files. Be careful. 

`$ jfmt /path/to/directory` - script will walk through files and directories starting from provided path.

`$ jfmt /path/to/file.java` - script will format only .java file which path is passed into it.
