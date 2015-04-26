##XYplorer
*XYplorer support for Sublime Text*

- ####INSTALL
	- ##### With [Package Control](https://packagecontrol.io/)
		+ open Command Palette (<kbd>CTRL</kbd>+<kbd>SHIFT</kbd>+<kbd>P</kbd>) and pick `Package Control: Add Repository`
		+ Enter `https://github.com/SammaySarkar/XYplorer` as the Repository URL
		+ Now do `Package Control: Install Package`, search for and install `XYplorer`
	- ##### Without Package Control
		+ download this repo as [zip](https://github.com/SammaySarkar/XYplorer/archive/master.zip).
		  There will be a folder inside the zip. Extract and rename the folder to `XYplorer` and move to **\Data\Packages\** .
		+ ALTERNATIVELY, and *only if running Sublime Text 3*, zip up that `XYplorer` folder,
		  rename the zip file to XYplorer.sublime-package and paste it to **\Data\Installed Packages\** .

- ####USAGE:
	+ First of all open Preferences > Package Settings > XYplorer > Settings - User
	+ and save the opened settings file with following content, taking care to use correct path to XYplorer installation folder
	```js
	{
	"xypath": "P:\\ath\\to\\XYplorer"
	}
	```
	+ To assign XYplorer icon to .xys files in sidebar:
		+ Create an XYplorer icon in png format and save to \Data\Packages\Theme - Default\icons\file_type_xys.png
		+ The filename must be file_type_xys.png because it's defined in "Icon (xys).tmPreferences"
- Contextual help:
	+ Place cursor on any function such as "replacelist()" > Ctrl+enter will open the corresponding reference in XYplorer help file
	+ Place cursor on any CommandID such as "#101" > Ctrl+enter will display corresponding command text in statusbar
- Snippet: see tabTrigger in the *.sublime-snippet files. Typing these triggers and press Tab will insert a pre-defined script
- Build:
	+ edit file path in XYplorer.sublime-build
	+ Tool > Build (Ctrl+B) will execute current xys file in XYplorer
