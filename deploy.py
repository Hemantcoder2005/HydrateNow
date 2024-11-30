from cx_Freeze import setup, Executable

setup(
    name="HydrateNow!",
    version="1.0",
    description="Reminds you to drink water every 10 minutes",
    executables=[Executable("HydrateNow.py", base="Win32GUI")],
)
