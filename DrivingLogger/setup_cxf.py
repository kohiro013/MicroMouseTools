# coding: utf-8

############### cx_Freeze 用セットアップファイル ##########
# コマンドライン上で python setup.py buildとすると、exe化　#
# Mac用のAppを作成するには、buildをbdist_macとする        #
######################################################
 
import sys, os
from cx_Freeze import setup, Executable

#個人的な設定（コマンドライン上でファイルをぶっこみたい）
file_path = input("アプリ化したいpy：")
sys.path.append(os.path.dirname(file_path))

#TCL, TKライブラリのエラーが発生する場合に備え、以下を設定
#参考サイト：http://oregengo.hatenablog.com/entry/2016/12/23/205550
if sys.platform == "win32":
    #base = None # "Win32GUI" ←GUI有効
    base = "Win32GUI"
    #Windowsの場合の記載　それぞれの環境によってフォルダの数値等は異なる
    os.environ['TCL_LIBRARY'] = "C:\\Anaconda3\\tcl\\tcl8.6"
    os.environ['TK_LIBRARY'] = "C:\\Anaconda3\\tcl\\tk8.6"
else:
    base = None # "Win32GUI"

#importして使っているライブラリを記載
packages = [
    
]

#importして使っているライブラリを記載（こちらの方が軽くなるという噂）
includes = [
    "sys",
    "os",
    "serial",
    "csv",
    "datetime",
    "matplotlib",
    "PySide2",
]

#excludesでは、パッケージ化しないライブラリやモジュールを指定する。
"""
numpy,pandas,lxmlは非常に重いので使わないなら、除く。（合計で80MBほど）
他にも、PIL(5MB)など。
"""
excludes = [
    "tkinter",
    "PyQt4", 
    "PyQt5",
    "pandas",
    "lxml",
    "babel",
    "bcrypt",
    "cryptography",
    "cython", "Cython",
    "IPython",
    "jedi",
    "llvmlite",
    "markupsafe",
    "nacl",
    "notebook",
    "numba",
    "PIL",
    "psutil",
    "scipy",
    "sphinx",
    "tornado",
    "typed_ast",
    "win32com",
    "zmq",
]

include_files = [
     (os.path.join('C:\\Anaconda3\\DLLs', 'tcl86t.dll'), os.path.join('lib', 'tcl86t.dll')),
     (os.path.join('C:\\Anaconda3\\DLLs', 'tk86t.dll'),  os.path.join('lib', 'tk86t.dll')),
     (os.path.join('C:\\Anaconda3\\Library\\bin', 'mkl_core.dll'), 'mkl_core.dll'),
     (os.path.join('C:\\Anaconda3\\Library\\bin', 'mkl_def.dll'), 'mkl_def.dll'),
     (os.path.join('C:\\Anaconda3\\Library\\bin', 'mkl_intel_thread.dll'), 'mkl_intel_thread.dll'),
     (os.path.join('C:\\Anaconda3\\Library\\bin', 'libiomp5md.dll'), 'libiomp5md.dll'),
     'C:\\Anaconda3\\Library\\plugins\\platforms',
     # add here further files which need to be included as described in 1.
]

##### 細かい設定はここまで #####

#アプリ化したい pythonファイルの指定触る必要はない
exe = Executable(
    script = file_path,
    base = base,
    targetName = 'MicroMouseLogger.exe',
)
 
# セットアップ
setup(name = 'main',
      options = {
          "build_exe": {
              "packages": packages, 
              "includes": includes, 
              "excludes": excludes,
              "include_files": include_files,
          }
      },
      version = '1.0',
      description = 'converter',
      executables = [exe]
)
