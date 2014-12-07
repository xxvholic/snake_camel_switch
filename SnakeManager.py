import sublime, sublime_plugin

class SnakeCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        sels = self.view.sel()

        for sel in sels:
            string = self.view.substr(sel)

            if string.find('_') != -1:
                string = self.__toCamel(string)
            else:
                string = self.__toSnake(string)
            
            self.view.replace(edit, sel, string)

    def __toSnake(self, string):
        
        return "".join('_'+s.lower() if s.isupper() else s for s in string)

    def __toCamel(self, string):
        strings = string.split('_')
        return strings[0] + "".join(s.title() for s in strings[1:])
