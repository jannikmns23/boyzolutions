import os
from datetime import datetime

# Settings
repo_path = r"B:\boyzolutions"  # Path to your local Git repository
filename = f"script_{datetime.now().strftime('%Y%m%d_%H%M%S')}.py"
file_path = os.path.join(repo_path, filename)

# 1. Create a dummy Python file with lyrics
with open(file_path, "w", encoding="utf-8") as f:
    f.write(f"# Security Fix {datetime.now()}\n")
    f.write("print(\"\"\"\n")
    f.write("Huh, roll another one Said\n"
            "I'm never lackin', always pistol packin'\n"
            "(This is a Melo beat)\n"
            "With them automatics, we gon' send him to heaven (Huh)\n"
            "Wait, wait, wait, wait, ayy, ayy, woo (Aw, shit), huh\n"
            "Oh, you feelin' sturdy, huh? (You feelin' sturdy, baby)\n"
            "Shake some', huh\n"
            "Shake it, huh, shake it, huh, shake it, huh\n"
            "She like the way that I dance\n"
            "She like the way that I move\n"
            "She like the way that I rock\n"
            "She like the way that I woo\n"
            "And she let it clap for a nigga\n"
            "(She let it clap for a nigga)\n"
            "And she throw it back for a nigga\n"
            "(Yeah, she throw it back for a nigga)\n"
            "Mike Amiri, Mike Amiri\n"
            "Billie Jean, Billie Jean (Uh)\n"
            "Christian Dior, Dior\n"
            "I'm up in all the stores\n"
            "When it rains, it pours\n"
            "She like the way I rrr\n"
            "Mike Amiri, Mike Amiri\n"
            "Billie Jean, Billie Jean (Uh)\n"
            "Christian Dior, Dior\n"
            "I'm up in all the stores\n"
            "When it rains, it pours\n"
            "She like the way I rrr\n"
            "When I walk in the spot, thirty on me\n"
            "Buy out the club, niggas know that I'm paid\n"
            "Bitch, I'm a thot, get me lit\n"
            "I can't fuck with these niggas 'cause niggas is gay\n"
            "All on my page suckin' dick\n"
            "All in my comments and screamin' my name\n"
            "While I'm in the club, throwin' them hundreds and fifties and ones and ones\n"
            "Pop Smoke, they know I'm wildin'\n"
            "If I'm on the island, I'm snatchin' the cell\n"
            "Brody got locked, denied his bail (Woo)\n"
            "Until he free, I'm raisin' hell\n"
            "Tell my shooters call me FaceTime\n"
            "For all the times we had to face time\n"
            "Free D-Nice, he doin' state time\n"
            "If you need the glizzy, you could take mine\n"
            "Please don't come out your mouth, you know I'm like that\n"
            "I'll make a movie like TNT (Baow)\n"
            "Glock-30 on me, ask who really want it\n"
            "I bet I air it like BNB\n"
            "Nappy Blue wildin' in my section\n"
            "And I keep that .38 for the weapon\n"
            "Remember when I came home from corrections (Uh-huh)\n"
            "All the bad bitches in my direction (Uh)\n"
            "She like the way that I dance\n"
            "She like the way that I move\n"
            "She like the way that I rock\n"
            "She like the way that I woo\n"
            "And she let it clap for a nigga\n"
            "(She let it clap for a nigga)\n"
            "And she throw it back for a nigga\n"
            "(Yeah, she throw it back for a nigga)\n"
            "Mike Amiri, Mike Amiri\n"
            "Billie Jean, Billie Jean (Uh)\n"
            "Christian Dior, Dior\n"
            "I'm up in all the stores\n"
            "When it rains, it pours\n"
            "She like the way I rrr\n"
            "Mike Amiri, Mike Amiri\n"
            "Billie Jean, Billie Jean (Uh)\n"
            "Christian Dior, Dior\n"
            "I'm up in all the stores\n"
            "When it rains, it pours\n"
            "She like the way I rrr\n")
    f.write("\"\"\")\n")

# 2. Git automation
os.chdir(repo_path)
os.system(f"git add {filename}")
os.system(f'git commit -m "Auto push: {filename}"')
os.system("git push origin main")  # Change 'main' to your branch name if needed
