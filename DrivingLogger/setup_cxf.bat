@rem エコーを出力しない
@echo off

rem batファイルと同じディレクトリのsetup.pyファイルを使用。
cd /d %~dp0

rem Anaconda promptを起動(call以下は各自任意のパスを指定してください)
call C:\Anaconda3\Scripts\activate.bat

rem exe化用の仮想環境へ移動（任意の仮想環境名をactibateさせてください）
rem activate test
python setup_cxf.py build
pause