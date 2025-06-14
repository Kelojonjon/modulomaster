

import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
def modulo_chart(mod, start, end):
    lines = []
    row = []

    start_mod = start % mod
    if start_mod != 1 and start_mod != 0:
        left_pad = (mod - start_mod + 1) % mod
        for _ in range(left_pad):
            row.append("xxxxx".ljust(8))

    for i in range(start, end + 1):
        current_mod = i % mod
        label = f"{i}≡{current_mod}".ljust(8)
        row.append(label)

        if len(row) == mod:
            lines.append(" | ".join(row))
            row = []

    if row:
        while len(row) < mod:
            row.append("xxxxx".ljust(8))
        lines.append(" | ".join(row))

    return lines


stored_charts = []

while True:
    clear_screen()
    print("\n\n📐 MODULO CHART STACK\n")

    if stored_charts:
        for index, chart in enumerate(stored_charts):
            print(f"\n--- Chart {index + 1} ---\n")
            for line in chart:
                print(line)

    user_input = input("\nPress [Enter] to add another chart, or type anything to reset: ").strip()

    if user_input:
        stored_charts = []

    mod = int(input("mod: "))
    start = int(input("start: "))
    end = int(input("end: "))

    chart = modulo_chart(mod, start, end)
    stored_charts.append(chart)
