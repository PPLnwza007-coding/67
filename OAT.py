import os
import time
import random
import sys

COLORS = [
    '\033[91m',
    '\033[93m',
    '\033[92m',
    '\033[96m',
    '\033[94m',
    '\033[95m',
]
RESET = '\033[0m'
BOLD = '\033[1m'

def rainbow_text(text):
    rainbow_str = ""
    for i, char in enumerate(text):
        if char == " ":
            rainbow_str += char
            continue
        color = COLORS[i % len(COLORS)]
        rainbow_str += f"{color}{char}"
    return rainbow_str + RESET

def fake_loading():
    steps = [
        "[*] CONNECTING TO DISCORD API...",
        "[*] BYPASSING CLOUDFLARE SECURITY...",
        "[*] INJECTING PAYLOAD TO MAINFRAME...",
        "[*] EXTRACTING TARGET DATA..."
    ]
    print("\n")
    for step in steps:
        sys.stdout.write(f"\r{COLORS[2]}{step}{RESET}")
        sys.stdout.flush()
        time.sleep(random.uniform(0.5, 1.2))
        sys.stdout.write(" [OK]\n")
    time.sleep(0.5)

def math_minigame():
    """ตรวจสอบว่ามึงโง่มั้ย"""
    print("\n" + COLORS[4] + "="*55 + RESET)
    print(BOLD + COLORS[1] + " [ SYSTEM CHECK: ยืนยันตัวตนคนโหด ]" + RESET)
    print(COLORS[4] + "="*55 + RESET)
    
    question_pool = []
    for _ in range(10):
        type_choice = random.randint(1, 3)
        if type_choice == 1:
            n1, n2 = random.randint(11, 35), random.randint(11, 25)
            question_pool.append({"q": f"{n1} * {n2}", "a": n1 * n2})
        elif type_choice == 2:
            n1, n2, n3 = random.randint(15, 30), random.randint(5, 12), random.randint(100, 200)
            question_pool.append({"q": f"({n1} * {n2}) + {n3}", "a": (n1 * n2) + n3})
        else:
            n1, n2, n3 = random.randint(100, 250), random.randint(10, 80), random.randint(5, 9)
            question_pool.append({"q": f"({n1} - {n2}) * {n3}", "a": (n1 - n2) * n3})

    selected_questions = random.sample(question_pool, 3)
    
    for i, item in enumerate(selected_questions, 1):
        print(COLORS[6] if len(COLORS) > 6 else COLORS[3] + f"\n[!] ข้อที่ {i}/3 | โจทย์: {item['q']} = ?" + RESET)
        try:
            user_input = int(input(COLORS[5] + ">>> ตอบมาไอสัส: " + RESET))
            if user_input == item['a']:
                print(COLORS[2] + "ถูกไอสัส ข้อต่อไป" + RESET)
            else:
                print(COLORS[0] + f"กระจอกสัส คำตอบคือ {item['a']}" + RESET)
                return False
        except ValueError:
            print(COLORS[0] + "ใส่ตัวเลขดิไอควาย" + RESET)
            return False

    print(BOLD + COLORS[2] + "\n[✔] ACCESS GRANTED! สมองมึงคู่ควรกับระบบนี้" + RESET)
    time.sleep(1.5)
    return True

def run_loop_system():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    ascii_art = r"""
        ███████████████████████████████████████████████████████████████████████████████
        █▌                                                                           ▐█
        █▌                                                                           ▐█
        █▌      .d88b.   .d8b.  d888888b       db    db d888888b d8b   db  d888b     ▐█
        █▌     .8P  Y8. d8' `8b `~~88~~'       `8b  d8'   `88'   888o  88 88' Y8b    ▐█
        █▌     88    88 88ooo88    88           `8bd8'     88    88V8o 88 88         ▐█
        █▌     88    88 88~~~88    88             88       88    88 V8o88 88  ooo    ▐█
        █▌     `8b  d8' 88   88    YP             88      .88.   88  V888 88. ~8~    ▐█
        █▌      `Y88P'  YP   YP    YP             YP    Y888888P VP   V8P  Y888P     ▐█
        █▌                                                                           ▐█
        █▌                                                                           ▐█
        █▌     d8888b. d888888b .d8888.  .o88b.  .d88b.  d8888b. d8888b.             ▐█
        █▌     88  `8D   `88'   88'   YP d8P  Y8 .8P  Y8. 88  `8D 88  `8D            ▐█
        █▌     88   88    88    `8bo.    8P      88    88 88oobY' 88   88            ▐█
        █▌     88   88    88      `Y8b. 8b      88    88 88`8b   88   88             ▐█
        █▌     88  .8D   .88.   db   8D Y8b  d8 `8b  d8' 88 `88. 88  .8D             ▐█
        █▌     Y8888D' Y888888P `8888Y'  `Y88P'  `Y88P'  88   YD Y8888D'             ▐█
        █▌                                                                           ▐█
        █▌                                                                           ▐█
        ███████████████████████████████████████████████████████████████████████████████
                            [ ระบบระเบิดดิสที่โหดที่สุดในห้องน้ำ ]                                        
    """
    print(rainbow_text(ascii_art))
    print(BOLD + rainbow_text("     [ Made By RealOAT ]     ") + RESET)
    print(COLORS[4] + "===========================" + RESET)

    target_id = input(BOLD + "\n[?] ENTER DISCORD NAME : " + RESET)
    
    try:
        num_input = input(BOLD + "[?] ENTER PACKET AMOUNT : " + RESET)
        count = int(num_input)

        if not math_minigame():
            print(COLORS[0] + "\n[!] ตอบผิด ไปทำมาใหม่ไอสัส SYSTEM LOCKED!" + RESET)
            input("\nกด Enter เพื่อกลับ...")
            return

        fake_loading()

        messages = [
            "ยิงแม่มึง",
            "ยิงพ่อมึง",
            "แตกแล้วๆ",
            "เสี่ยหนูอ๊ะห์ๆ",
        ]

        os.system('cls' if os.name == 'nt' else 'clear')
        print(rainbow_text("================== ATTACK INITIATED =================="))
        print(COLORS[1] + f"[!] TARGET ENGAGED: {target_id}" + RESET)
        print(COLORS[1] + f"[!] TOTAL PAYLOADS: {count} ROUNDS" + RESET)
        print(COLORS[4] + "------------------------------------------------------" + RESET)
        time.sleep(1.0)

        for i in range(1, count + 1):
            random_msg = random.choice(messages)
            color = random.choice(COLORS)
            hex_fake = ''.join(random.choices('0123456789ABCDEF', k=6))
            
            print(f"{color}[{i:04d}/{count:04d}] [0x{hex_fake}] SENDING TO {target_id} >>> {random_msg}{RESET}")
            time.sleep(0.02) 

        print(COLORS[4] + "------------------------------------------------------" + RESET)
        print(BOLD + COLORS[2] + f"[✓] TARGET {target_id} HAS BEEN COMPLETELY DESTROYED By OAT DEK WARD" + RESET)

    except ValueError:
        print(COLORS[0] + "\n[!] ใส่ตัวเลขดิไอสัส ERROR 0x00000000" + RESET)

    print(COLORS[4] + "\n=======================================================" + RESET)
    input(BOLD + "ไปเริ่มใหม่ กากจัด" + RESET)

if __name__ == "__main__":
    run_loop_system()
