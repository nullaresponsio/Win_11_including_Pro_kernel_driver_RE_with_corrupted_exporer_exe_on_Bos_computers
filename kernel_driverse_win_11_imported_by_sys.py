from pathlib import Path
kernel_drivers = sorted(f.name for f in Path(r'C:\Windows\System32\drivers').glob('*.sys'))
print(kernel_drivers)
