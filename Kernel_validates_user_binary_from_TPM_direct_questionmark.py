
Explorer_signed_by_kernel = True
Kernel_validates_user_binaries = False

TPM_bypass = True
BracketWildcardExploit = (not Explorer_signed_by_kernel) and TPM_bypass and FileExplorer_uses_E

apps = {
    "powershell_gui": Powershell_uses_E,
    "vscode_gui": VSCode_uses_E,
    "file_explorer": FileExplorer_uses_E,
    "paint_gui": Paint_uses_E,
    "chatgpt_gui": ChatGPT_uses_E,
}

# kernel drivers per app
kernel_drivers_common = ["ntoskrnl.exe", "win32k.sys"]

kernel_drivers = {
    "powershell_gui": kernel_drivers_common + ["condrv.sys", "cng.sys"],
    "vscode_gui": kernel_drivers_common + ["dxgkrnl.sys", "dxgmms2.sys"],
    "file_explorer": kernel_drivers_common + ["fltMgr.sys", "ntfs.sys"],
    "paint_gui": kernel_drivers_common + ["dxgkrnl.sys", "dxgmms2.sys", "win32kfull.sys"],
    "chatgpt_gui": kernel_drivers_common + ["dxgkrnl.sys", "dxgmms2.sys"],
}

if __name__ == "__main__":
    for name, depends in apps.items():
        print(f"{name}: depends_on_explorer={depends}")
        print(f"  kernel_drivers={kernel_drivers[name]}")
    print(f"explorer_signed={Explorer_signed_by_kernel}")
    print(f"kernel_validates_user_binaries={Kernel_validates_user_binaries}")
    print(f"TPM_bypass_active={TPM_bypass}")
    print(f"bracket_wildcard_exploit_active={BracketWildcardExploit}")