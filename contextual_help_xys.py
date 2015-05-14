import sublime, sublime_plugin, subprocess

class contextual_help_xys(sublime_plugin.TextCommand):
	def run(self, edit):
		xypath = self.view.settings().get('xypath')
		CursorLocation = self.view.sel()[0]
		ScopeName = self.view.scope_name(CursorLocation.a).strip()
		ScopeText = self.view.substr(self.view.extract_scope(CursorLocation.a))
		if ScopeName == "source.xys entity.name.function.UDF.xys":
			# need to handle namespaces
			self.view.window().run_command('goto_definition', {"symbol" : ScopeText.lower() + '  [udf]'})
		elif ScopeName == "source.xys entity.name.section.NS.xys":
			self.view.window().run_command('goto_definition', {"symbol" : ScopeText.lower() + '  [ns]'})
		elif ScopeName == "source.xys entity.name.function.xys":
			subprocess.Popen(["hh.exe", xypath + "\\XYplorer.chm::/idh_scripting_comref.htm#idh_sc_" + ScopeText])
		elif "variable.parameter.xys" in ScopeName:
			subprocess.Popen(["hh.exe", xypath + "\\XYplorer.chm::/idh_scripting.htm#idh_scripting_variables"])
		elif "variable.parameter.native.xys" in ScopeName:
			subprocess.Popen(["hh.exe", xypath + "\\XYplorer.chm::/idh_variables.htm"])
		elif "string.other.scriptcaption.xys" in ScopeName:
			subprocess.Popen(["hh.exe", xypath + "\\XYplorer.chm::/idh_scripting.htm#idh_scripting_xysadv"])
		elif ScopeName == "source.xys keyword.operator.xys":
			subprocess.Popen(["hh.exe", xypath + "\\XYplorer.chm::/idh_scripting.htm#idh_scripting_operatorprecedence"])
		elif ScopeName == "source.xys string.unquoted.heredoc.xys" or ScopeName == "source.xys string.unquoted.nowdoc.xys":
			subprocess.Popen(["hh.exe", xypath + "\\XYplorer.chm::/idh_scripting.htm#idh_scripting_heredoc"])
		elif ScopeName == "source.xys keyword.control.xys":
			ScopeTextLower = ScopeText.lower().strip('({')
			if ScopeTextLower == "if" or ScopeTextLower == "elseif" or ScopeTextLower == "else":
				subprocess.Popen(["hh.exe", xypath + "\\XYplorer.chm::/idh_scripting.htm#idh_scripting_ifthen"])
			elif ScopeTextLower == "while":
				subprocess.Popen(["hh.exe", xypath + "\\XYplorer.chm::/idh_scripting.htm#idh_scripting_whileloops"])
			elif ScopeTextLower == "foreach":
				subprocess.Popen(["hh.exe", xypath + "\\XYplorer.chm::/idh_scripting.htm#idh_scripting_foreachloops"])
			elif ScopeTextLower == "step" or ScopeTextLower == "unstep" \
					or ScopeTextLower == "break" or ScopeTextLower == "continue":
				subprocess.Popen(["hh.exe", xypath + "\\XYplorer.chm::/idh_scripting_comref.htm#idh_sc_" + ScopeText])
			else:
				subprocess.Popen(["hh.exe", xypath + "\\XYplorer.chm::/idh_scripting.htm"])
		elif ScopeName == "source.xys entity.name.function.CommandID.xys":
			if sublime.version()[0] == '2':
				cmdIDList = open(sublime.packages_path() + '\\XYplorer\\cmdIDs.txt', 'r')
				CmdDict = eval( '{' + cmdIDList.read() + '}' ); cmdIDList.close()
			else:
				CmdDict = eval( '{' + sublime.load_resource("Packages/XYplorer/cmdIDs.txt") + '}' )
			if ScopeText in CmdDict:
				sublime.status_message(CmdDict[ScopeText])
			else:
				sublime.status_message(ScopeText + ": Command ID not recognized")
		else:
			# Contextual_help is assigned to ctrl+enter, which coincides with
			# ST's kb shortcut for new line macro. This is to compensate.
			self.view.window().run_command("move_to", {"to": "hardeol"})        # Add new line
			self.view.window().run_command("insert", {"characters": "\n"})      # Add new line

# ::/idh_scripting_comref.htm#idh_sc_folderreport
# mk:@MSITStore:C:\XYplorer\XYplorer.chm::/idh_scripting_comref.htm#idh_sc_getpathcomponent
