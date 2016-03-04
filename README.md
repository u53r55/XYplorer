##XYplorer
**XYplorer support package for Sublime Text**

*(forked from https://github.com/Binocular222/XYplorer )*

- ####INSTALL:
  + **With [Package Control](https://packagecontrol.io/)**
    - Open Command Palette (<kbd>CTRL</kbd>+<kbd>SHIFT</kbd>+<kbd>P</kbd>), pick `Package Control: Add Repository`
    - Enter `https://github.com/smsrkr/XYplorer` as the Repository URL
    - Now do `Package Control: Install Package`, search for and install `XYplorer`
  + **Without Package Control**
    - Download this repo as [zip](https://github.com/smsrkr/XYplorer/archive/master.zip).
      Extract and rename the *folder inside the zip file* to `XYplorer` and move to `Data\Packages\ `.<br>
      Or go to `Data\Packages` and do `git clone https://github.com/smsrkr/XYplorer ./XYplorer`.
    - ALTERNATIVELY, and *only if running Sublime Text 3*, zip up *the contents inside* that `XYplorer` folder,
      rename the zip file to `XYplorer.sublime-package` and place it in `Data\Installed Packages\ `.

- ####SETUP & USAGE:
  + Open XYplorer package user settings: `Preferences > Package Settings > XYplorer > Settings - User`
  + Save the settings file with following content, using correct paths to your `<xypath>` and `<xyscripts>` folder.
  ```json
  {
  "xypath": "P:\\ath\\to\\XYplorer"
  "xyscripts": "P:\\ath\\to\\XYScripts"
  }
  ```
  + Do the same with `Preferences > Package Settings > XYplorer > Build Settings - User` and this content.
  ```json
  {
  "cmd": ["P:\\ath\\to\\XYplorer\\XYplorer.exe", "", "/script=$file", "/flg=2"],
  "selector": "source.xys"
  }
  ```
  + The highlighter automatically activates in `*.xys, *.xyi` files.
  + Build-system integration is available. Doing `Tools > Build` will run the current script file in XYplorer.
  + **Contextual help**
    - F1 triggers contextual help. Try it on everything: keywords, commandIDs, user-defined functions ...
      + Command ID: associated menu caption is displayed in statusbar
      + UDF, Namespace: Go to Definition/Declaration. (see UDF note below)
      + INCLUDE statement: goto included file (*remember to set corect 'xyscripts' path in package settings*)
      + Other language structures: opens associated location in XYplorer help file
    - UDF note: add include files to project before you can jump to functions defined in those files.
  + **Tips**
    - SubScripts, User-Defined Functions and Namespace declarations are listed in Symbols.
    - To assign XYplorer icon to .xys files in sidebar:
      - Create an XYplorer icon in png format and save to `\Data\Packages\Theme - Default\icons\file_type_xys.png`
      - an example png icon is supplied with this package.
  + Some features like Goto Definition, SymbolList etc are not available in ST2

*Happy XYScripting!*
