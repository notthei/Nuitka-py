import os
print('exe化するpyファイルのフルパスを入力 or D&D')
pyPath = input('>>')
print('追加のオプションを選択')
print('[1] 黒い画面を出さない')
print('[2] Python環境がないところでも動くようにする')
print('[3] ひとつのexeファイルにまとめる')
print('[4] Tkinterをつかうおまじない')
print('[5] *.icoファイルをアイコンとして使用')
print('[6] なし')
stType = int(input('>>'))
stOption = ['--windows-disable-console',
            '--standalone',
            '--onefile',
            '--enable-plugin=tk-inter',
            '--windows-icon-from-ico="*.ico"',
            '    ']
os.system('nuitka ' + pyPath + ' '+stOption[stType-1])
