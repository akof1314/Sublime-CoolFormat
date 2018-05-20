import sublime, sublime_plugin
from ctypes import *
import os

__file__ = os.path.normpath(os.path.abspath(__file__))
__path__ = os.path.dirname(__file__)

class CoolformatCommand(sublime_plugin.TextCommand):
	def run(self, edit, action = 'quickFormat'):
		if action == 'quickFormat':
			self.doFormatSafe(edit, False)
		elif action == 'selectedFormat':
			self.doFormatSafe(edit, True)
		else:
			self.showSettings()

	def doFormatSafe(self, edit, selected):
		try:
			self.doFormat(edit, selected)
		except Exception as e:
			print(str(e))
			sublime.message_dialog('Cannot format this file!')

	def doFormat(self, edit, selected):
		self.loadCFDll()
		if self.DoFormatter == None:
			return

		view = self.view
		line_eol = self.getCFEol()
		lang = self.getCFLang()
		if selected:
			regions = []
			for sel in view.sel():
				initIndent = self.getInitIndent(min(sel.a, sel.b))
				region = sublime.Region(
					view.line(min(sel.a, sel.b)).a,  # line start of first line
					view.line(max(sel.a, sel.b)).b   # line end of last line
				)
				code = view.substr(region)
				formatted_code = self.getFormattedCode(code, lang, line_eol, initIndent)
				view.replace(edit, region, formatted_code)
				if sel.a <= sel.b:
					regions.append(sublime.Region(region.a, region.a + len(formatted_code)))
				else:
					regions.append(sublime.Region(region.a + len(formatted_code), region.a))
			view.sel().clear()
			[view.sel().add(region) for region in regions]
		else:
			region = sublime.Region(0, view.size())
			code = view.substr(region)
			formatted_code = self.getFormattedCode(code, lang, line_eol, None)
			view.replace(edit, region, formatted_code)

	def showSettings(self):
		self.view.window().open_file(__path__ + '/CoolFormatLib/CoolFormatConfig.cfconfig')
		"""
		self.loadCFDll()
		if self.ShowSettings:
			self.ShowSettings()
		"""

	def getInitIndent(self, point):
		line_region = self.view.line(point)
		code = self.view.substr(line_region)
		initIndent = ''
		for _, ch in enumerate(code):
			if ch != ' ' and ch != '\t':
				break
			initIndent = initIndent + ch
		return initIndent

	def getCFLang(self):
		lang = self.view.settings().get('syntax') # eg Packages/C++/C++.tmLanguage
		lang = lang[9:lang.find('/', 9)]
		return Synlanguage.lang_dict.get(lang, -1)

	def getCFEol(self):
		line_eol = self.view.line_endings()
		return '\n'
		"""
		if line_eol == 'Windows':
			return '\r\n'
		elif line_eol == 'Unix':
			return '\n'
		else:
			return '\r'
		"""

	def getFormattedCode(self, code, lang, line_eol, initIndent):
		if self.DoFormatter:
			sizeTextOut = c_int()
			sizeMsgOut = c_int()
			strTextIn = c_char_p(code.encode('utf-8'))
			strLineEol = c_char_p(line_eol.encode('utf-8'))
			strInitIndent = c_char_p(initIndent.encode('utf-8')) if initIndent else None
			if self.DoFormatter(lang, strTextIn, None, byref(sizeTextOut), None, byref(sizeMsgOut), 0, strLineEol, strInitIndent):
				strTextOut = create_string_buffer(sizeTextOut.value + 1)
				strMsgOut = create_string_buffer(sizeMsgOut.value + 1)
				if self.DoFormatter(lang, strTextIn, strTextOut, byref(sizeTextOut), strMsgOut, byref(sizeMsgOut), 0, strLineEol, strInitIndent):
					self.showOutput(strMsgOut.value.decode('utf-8'))
					return strTextOut.value.decode('utf-8')
		return code

	def showOutput(self, msg):
		if len(msg) != 0:
			self.view.window().run_command("show_panel", {"panel": "console"})
			print('=========== CoolFormat Output Begin ===========')
			print(msg)
			print('=========== CoolFormat Output End ===========')

	def loadCFDll(self):
		if self.hInstCF == None:
			platform_name = sublime.platform()
			if platform_name == 'windows':
				dll_name = '/CoolFormatLib.dll'
			elif platform_name == 'osx':
				dll_name = '/libCoolFormatLib.dylib'
			else:
				dll_name = '/libCoolFormatLib.so'
			self.hInstCF = cdll.LoadLibrary(__path__ + '/CoolFormatLib/cf_' + platform_name + '_' + sublime.arch() + dll_name)
			if self.hInstCF:
				self.DoFormatter = self.hInstCF.DoFormatter
				self.ShowSettings = self.hInstCF.ShowSettings
			else:
				sublime.message_dialog('Cannot load CoolFormatLib library!')

	hInstCF = None
	DoFormatter = None
	ShowSettings = None

class Synlanguage:
	(
	SYN_ACTIONSCRIPT,
	SYN_ADA,
	SYN_ASM,
	SYN_ASP,
	SYN_AUTOHOTKEY,
	SYN_AUTOIT,
	SYN_BATCH,
	SYN_COBOL,
	SYN_CPP,
	SYN_CS,
	SYN_CSS,
	SYN_D,
	SYN_FORTRAN,
	SYN_HASKELL,
	SYN_HTML,
	SYN_INI,
	SYN_JAVA,
	SYN_JAVASCRIPT,
	SYN_JSON,
	SYN_JSP,
	SYN_LISP,
	SYN_LUA,
	SYN_NORMALTEXT,
	SYN_OBJECTIVEC,
	SYN_PASCAL,
	SYN_PERL,
	SYN_PHP,
	SYN_PYTHON,
	SYN_RUBY,
	SYN_SQL,
	SYN_VB,
	SYN_VERILOG,
	SYN_VHDL,
	SYN_XML
	) = range(0, 34)
	lang_dict = {
	'C': SYN_CPP,
	'C++':SYN_CPP,
	'C#':SYN_CS,
	'CSS':SYN_CSS,
	'HTML':SYN_HTML,
	'Java':SYN_JAVA,
	'JavaScript':SYN_JAVASCRIPT,
	'JSON':SYN_JSON,
	'Objective-C':SYN_OBJECTIVEC,
	'Objective-C++':SYN_OBJECTIVEC,
	'PHP':SYN_PHP,
	'SQL':SYN_SQL,
	'Verilog':SYN_VERILOG,
	'XML':SYN_XML }
