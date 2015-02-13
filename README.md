Sublime-CoolFormat
==========================================

Description
-----------

A Sublime Text plugin for Source Code Formatter. CoolFormat Source Code Formatter is a code formatter for C\C++\C#\CSS \HTML\Java\JavaScript\JSON\Objective-C\PHP\SQL\XML files.

Installation
------------

### With the Package Control plugin

The easiest way to install Sublime-CoolFormat is through [Package Control].

[Package Control]: http://wbond.net/sublime_packages/package_control

Once you have Package Control installed, restart Sublime Text.

1. Bring up the Command Palette (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>
on Windows and Linux. <kbd>⌘</kbd>+<kbd>⇧</kbd>+<kbd>P</kbd> on OS X).
2. Type "Install" and select "Package Control: Install Package".
3. Select "CoolFormat" from list.

The advantage of using Package Control is that it will keep Sublime-CoolFormat up to date.

### Manual Install

**Without Git:**

[Download](https://github.com/akof1314/Sublime-CoolFormat) the latest source code,
and extract it to the Packages directory.

**With Git:**

Type the following command in your Sublime Text 2 or Sublime Text 3 Packages directory:

`git clone https://github.com/akof1314/Sublime-CoolFormat.git`

The "Packages" directory is located at:

**Sublime Text 2**

* **Windows**: `%APPDATA%\Sublime Text 2\Packages`
* **Linux**: `~/.config/sublime-text-2/Packages/`
* **OS X**: `~/Library/Application Support/Sublime Text 2/Packages/`

**Sublime Text 3**

* **Windows**: `%APPDATA%\Sublime Text 3\Packages`
* **Linux**: `~/.config/sublime-text-3/Packages/`
* **OS X**: `~/Library/Application Support/Sublime Text 3/Packages/`

Usage
-----

### Key Bindings

The default key bindings for this plugin:

**Windows, Linux, OSX:**

* <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Alt</kbd>+<kbd>Q</kbd>: Quick Format.
* <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>Alt</kbd>+<kbd>S</kbd>: Selected Format.

### Command Palette

Open the command palette, it appears as `CoolFormat: Quick Format` and `CoolFormat: Selected Format` and `CoolFormat: Formatter Settings`.

Settings
--------

Before starting, you may want to have a look at CoolFormatConfig.cfconfig.

Please visit [http://akof1314.github.io/CoolFormat/doc/index.html](http://akof1314.github.io/CoolFormat/doc/index.html) for more information.
