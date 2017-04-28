# wal-color-converter
A small utility to convert a wal color scheme into a Konsole profile and to set that profile as the active profile

Now working, and requires [Majjoha's color-converter](https://github.com/majjoha/color-converter) as a dependency.
Might eventually expand this to work with other terminal emulators, but I'm starting small for now.

To run, you need to already have wal installed, as well as the dependency above. At any point after running wal, this program can be run. It needs sudo access because of how Konsole work unfortunately, but you can always just add it to your sudoers file. In addition, you can run it whenever you start a shell by adding (/path/to/script &) into your .zshrc, .bashrc, etc. 

