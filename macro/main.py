import csv
import pprint
import pyautogui


path = "C:/u/vscode/repo/sxclij_mc/cb/tick/item/cb.csv"
# path = "C:/u/vscode/repo/sxclij_mc/cb/event/dev/register.csv"

with open(path) as f:
    reader = csv.reader(f, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)

    for row in reader:
        
        pyautogui.press("t")
        x = ""
        match row[0]:
            case "repeat":
                x = "/setblock ~ ~ ~1 repeating_command_block"
            case "chain":
                x = "/setblock ~ ~ ~1 chain_command_block"
            case "air":
                x = "/setblock ~ ~ ~1 air"
        match row[1]:
            case "conditional":
                x += "[conditional=true,facing=up]"
            case "unconditional":
                x += "[conditional=false,facing=up]"
        pyautogui.write(x)
        pyautogui.press("enter")

        if(row[2] == "always"):
            pyautogui.press("t")
            pyautogui.write("/data modify block ~ ~ ~1 auto set value 1b")
            pyautogui.press("enter")
    
        pyautogui.press("t")
        pyautogui.write("/data modify block ~ ~ ~1 Command set value \"" + row[3] + "\"")
        pyautogui.press("enter")
        
        pyautogui.press("t")
        pyautogui.write("/tp @s ~ ~1 ~")
        pyautogui.press("enter")