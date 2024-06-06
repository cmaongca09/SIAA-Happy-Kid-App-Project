# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['C:\\Users\\arshe\\Documents\\GitHub\\SIAA-Happy-Kid-App-Project\\HappyKid\\kivy_venv\\HAPPY KID DEISGN LOGIN'],
    binaries=[],
    datas=[
        (r'C:\Users\arshe\Documents\GitHub\SIAA-Happy-Kid-App-Project\HappyKid\kivy_venv\HAPPY KID DEISGN LOGIN\main.kv', '.'),
        (r'C:\Users\arshe\Documents\GitHub\SIAA-Happy-Kid-App-Project\HappyKid\kivy_venv\HAPPY KID DEISGN LOGIN\createAccount.kv', '.'),
        (r'C:\Users\arshe\Documents\GitHub\SIAA-Happy-Kid-App-Project\HappyKid\kivy_venv\HAPPY KID DEISGN LOGIN\createAccount2.kv', '.'),
        (r'C:\Users\arshe\Documents\GitHub\SIAA-Happy-Kid-App-Project\HappyKid\kivy_venv\HAPPY KID DEISGN LOGIN\Dashboard.kv', '.'),
        (r'C:\Users\arshe\Documents\GitHub\SIAA-Happy-Kid-App-Project\HappyKid\kivy_venv\HAPPY KID DEISGN LOGIN\termsandcondition.kv', '.'),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main'
)