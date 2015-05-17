##XYplorer
**XYplorer support package for Sublime Text**

*(forked from https://github.com/Binocular222/XYplorer )*

- ####INSTALL:
	+ **With [Package Control](https://packagecontrol.io/)**
		- open Command Palette (<kbd>CTRL</kbd>+<kbd>SHIFT</kbd>+<kbd>P</kbd>) and pick `Package Control: Add Repository`
		- Enter `https://github.com/SammaySarkar/XYplorer` as the Repository URL
		- Now do `Package Control: Install Package`, search for and install `XYplorer`
	+ **Without Package Control**
		- Download this repo as [zip](https://github.com/SammaySarkar/XYplorer/archive/master.zip).
		  There will be a folder inside the zip. Extract and rename the folder to `XYplorer` and move to ` \Data\Packages\ ` .
		- ALTERNATIVELY, and *only if running Sublime Text 3*, zip up *the contents* inside of that `XYplorer` folder, rename
		  the zip file to `XYplorer.sublime-package` and paste it to ` \Data\Installed Packages\ ` .

- ####SETUP & USAGE:
	+ open `Preferences > Package Settings > XYplorer > Settings - User`
	+ and save the opened settings file with following content, using correct path to your XYplorer installation folder.
	```js
	{
	"xypath": "P:\\ath\\to\\XYplorer"
	}
	```
	+ Do the same with `Preferences > Package Settings > XYplorer > Build Settings - User` and this content.
	```js
	{
	"cmd": ["P:\\ath\\to\\XYplorer\\XYplorer.exe", "", "/script=$file", "/flg=2"],
	"selector": "source.xys"
	}
	```
	+ the highlighter automatically activates in `*.xys, *.xyi, *.inc` files.
	+ Build-system integration is available. Doing `Tools > Build` will run the current script file in XYplorer.
	+ **Contextual help**
		- CTRL+ENTER triggers contextual help. Try it on everything: native keywords, commandIDs, user-defined functions...
			+ Command IDs: associated menu caption is displayed in statusbar
			+ UDFs: Go to Definition. (see UDF note below)
			+ other language structures: opens associated location in XYplorer help file
			+ labels in **sub** and **load**: goto the label. (Work-In-Progress)
		- UDF note: add include files to project to use Go to Definition with functions defined in those files.
	+ **Tips**
		- SubScripts, User-Defined Functions and Namespace declarations are listed in Symbols.
		- To assign XYplorer icon to .xys files in sidebar:
			- Create an XYplorer icon in png format and save to `\Data\Packages\Theme - Default\icons\file_type_xys.png`
			- an example png icon is supplied with this package.
	+ (Some features like Goto Definition, SymbolList etc are not available in ST2)

*Happy XYScripting!*
