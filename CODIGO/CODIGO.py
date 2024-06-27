import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(600, 400))

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # Label e TextCtrl para nome
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        label_name = wx.StaticText(panel, label='Nome:')
        hbox1.Add(label_name, flag=wx.RIGHT, border=8)
        self.text_name = wx.TextCtrl(panel)
        hbox1.Add(self.text_name, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # Label e ComboBox para seleção de idioma
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        label_lang = wx.StaticText(panel, label='Idioma:')
        hbox2.Add(label_lang, flag=wx.RIGHT, border=8)
        self.combo_lang = wx.ComboBox(panel, choices=['Python', 'Java', 'C++', 'JavaScript'], style=wx.CB_DROPDOWN)
        hbox2.Add(self.combo_lang, proportion=1)
        vbox.Add(hbox2, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # Checkboxes para seleção de interesses
        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        label_interests = wx.StaticText(panel, label='Interesses:')
        hbox3.Add(label_interests, flag=wx.RIGHT, border=8)
        self.check_python = wx.CheckBox(panel, label='Python')
        self.check_java = wx.CheckBox(panel, label='Java')
        self.check_cpp = wx.CheckBox(panel, label='C++')
        hbox3.Add(self.check_python, flag=wx.LEFT)
        hbox3.Add(self.check_java, flag=wx.LEFT, border=10)
        hbox3.Add(self.check_cpp, flag=wx.LEFT, border=10)
        vbox.Add(hbox3, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # Radiobuttons para escolha de nível de experiência
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        label_experience = wx.StaticText(panel, label='Experiência:')
        hbox4.Add(label_experience, flag=wx.RIGHT, border=8)
        self.radio_beginner = wx.RadioButton(panel, label='Iniciante', style=wx.RB_GROUP)
        self.radio_intermediate = wx.RadioButton(panel, label='Intermediário')
        self.radio_advanced = wx.RadioButton(panel, label='Avançado')
        hbox4.Add(self.radio_beginner, flag=wx.LEFT)
        hbox4.Add(self.radio_intermediate, flag=wx.LEFT, border=10)
        hbox4.Add(self.radio_advanced, flag=wx.LEFT, border=10)
        vbox.Add(hbox4, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # Slider para escolha de idade
        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        label_age = wx.StaticText(panel, label='Idade:')
        hbox5.Add(label_age, flag=wx.RIGHT, border=8)
        self.slider_age = wx.Slider(panel, value=25, minValue=18, maxValue=60, style=wx.SL_HORIZONTAL | wx.SL_LABELS)
        hbox5.Add(self.slider_age, proportion=1)
        vbox.Add(hbox5, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # Botões para abrir dialogs de arquivo e diretório
        hbox6 = wx.BoxSizer(wx.HORIZONTAL)
        self.button_file = wx.Button(panel, label='Abrir Arquivo')
        self.button_dir = wx.Button(panel, label='Escolher Diretório')
        hbox6.Add(self.button_file, proportion=1, flag=wx.EXPAND | wx.RIGHT, border=10)
        hbox6.Add(self.button_dir, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox6, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # TextCtrl para exibir seleção de arquivo/diretório
        hbox7 = wx.BoxSizer(wx.HORIZONTAL)
        self.text_filepath = wx.TextCtrl(panel, style=wx.TE_READONLY)
        hbox7.Add(self.text_filepath, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox7, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        # Botão para mostrar seleção
        hbox8 = wx.BoxSizer(wx.HORIZONTAL)
        self.button_show_selection = wx.Button(panel, label='Mostrar Seleção')
        hbox8.Add(self.button_show_selection, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox8, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)

        panel.SetSizer(vbox)
        self.Centre()
        self.Show()

        # Bind dos eventos aos métodos correspondentes
        self.button_file.Bind(wx.EVT_BUTTON, self.OnOpenFile)
        self.button_dir.Bind(wx.EVT_BUTTON, self.OnOpenDir)
        self.button_show_selection.Bind(wx.EVT_BUTTON, self.OnShowSelection)

    def OnOpenFile(self, event):
        wildcard = "Text files (*.txt)|*.txt|Python files (*.py)|*.py|All files (*.*)|*.*"
        dialog = wx.FileDialog(self, "Escolha um arquivo", wildcard=wildcard,
                               style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
            self.text_filepath.SetValue(f'Arquivo selecionado:\n{path}')

        dialog.Destroy()

    def OnOpenDir(self, event):
        dialog = wx.DirDialog(self, "Escolha um diretório", style=wx.DD_DEFAULT_STYLE)

        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
            self.text_filepath.SetValue(f'Diretório selecionado:\n{path}')

        dialog.Destroy()

    def OnShowSelection(self, event):
        name = self.text_name.GetValue()
        language = self.combo_lang.GetValue()
        interests = ', '.join([label for label, checkbox in [
            ('Python', self.check_python),
            ('Java', self.check_java),
            ('C++', self.check_cpp)
        ] if checkbox.GetValue()])
        experience = ''
        if self.radio_beginner.GetValue():
            experience = 'Iniciante'
        elif self.radio_intermediate.GetValue():
            experience = 'Intermediário'
        elif self.radio_advanced.GetValue():
            experience = 'Avançado'
        age = self.slider_age.GetValue()

        wx.MessageBox(f'Nome: {name}\n'
                      f'Idioma: {language}\n'
                      f'Interesses: {interests}\n'
                      f'Experiência: {experience}\n'
                      f'Idade: {age}', 'Seleção')

if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, title='Projeto Final - wxPython')
    app.MainLoop()
