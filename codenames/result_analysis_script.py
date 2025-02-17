import subprocess


# for everything else but glove vs glove
def run():
    # w2v_thresholds vs w2vglove300
    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(["python", "run_game.py", "players.codemaster_w2v_03.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove", "players/glove/glove.6B.200d.txt",
                        "--game_name","w2v_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(["python", "run_game.py", "players.codemaster_w2v_05.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove", "players/glove/glove.6B.200d.txt",
                        "--game_name","w2v_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(["python", "run_game.py", "players.codemaster_w2v_07.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove", "players/glove/glove.6B.200d.txt",
                        "--game_name","w2v_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    # glove300_thresholds vs w2vglove300 (GLOVE V GLOVE)
    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(["python", "run_game.py", "players.codemaster_glove_03.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.300d.txt",
                        "--glove_guesser", "players/glove/glove.6B.200d.txt",
                        "--game_name","glove300_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(["python", "run_game.py", "players.codemaster_glove_05.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.300d.txt",
                        "--glove_guesser", "players/glove/glove.6B.200d.txt",
                        "--game_name","glove300_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(["python", "run_game.py", "players.codemaster_glove_07.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.300d.txt",
                        "--glove_guesser", "players/glove/glove.6B.200d.txt",
                        "--game_name","glove300_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    # glove200_thresholds vs glove300 (GLOVE V GLOVE)
    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(["python", "run_game.py", "players.codemaster_glove_03.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.200d.txt",
                        "--glove_guesser", "players/glove/glove.6B.200d.txt",
                        "--game_name","glove200_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(["python", "run_game.py", "players.codemaster_glove_05.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.200d.txt",
                        "--glove_guesser", "players/glove/glove.6B.200d.txt",
                        "--game_name","glove200_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(["python", "run_game.py", "players.codemaster_glove_07.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.300d.txt",
                        "--glove_guesser", "players/glove/glove.6B.200d.txt",
                        "--game_name","glove300_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    # glove100_thresholds vs glove300 (GLOVE V GLOVE)
    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(["python", "run_game.py", "players.codemaster_glove_03.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.100d.txt",
                        "--glove_guesser", "players/glove/glove.6B.200d.txt",
                        "--game_name","glove100_thresholds vs w2vglove200""--seed", str_counter])
        counter += 50

    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(["python", "run_game.py", "players.codemaster_glove_05.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.100d.txt",
                        "--glove_guesser", "players/glove/glove.6B.200d.txt",
                        "--game_name","glove100_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(["python", "run_game.py", "players.codemaster_glove_07.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.100d.txt",
                        "--glove_guesser", "players/glove/glove.6B.200d.txt",
                        "--game_name","glove300_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    # glove50_thresholds vs glove300 (GLOVE V GLOVE)
    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(["python", "run_game.py", "players.codemaster_glove_03.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.50d.txt",
                        "--glove_guesser", "players/glove/glove.6B.200d.txt",
                        "--game_name","glove50_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(["python", "run_game.py", "players.codemaster_glove_05.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.50d.txt",
                        "--glove_guesser", "players/glove/glove.6B.200d.txt",
                        "--game_name","glove50_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(["python", "run_game.py", "players.codemaster_glove_07.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
                        "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.50d.txt",
                        "--glove_guesser", "players/glove/glove.6B.200d.txt",
                        "--game_name","glove50_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    # w2vglove300_thresholds vs glove300 (GLOVE V GLOVE)
    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(
            ["python", "run_game.py", "players.codemaster_w2vglove_03.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.300d.txt",
             "--glove_guesser", "players/glove/glove.6B.200d.txt",
             "--game_name","w2vglove300_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(
            ["python", "run_game.py", "players.codemaster_w2vglove_05.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.300d.txt",
             "--glove_guesser", "players/glove/glove.6B.200d.txt",
             "--game_name","w2vglove300_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(
            ["python", "run_game.py", "players.codemaster_w2vglove_07.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.300d.txt",
             "--glove_guesser", "players/glove/glove.6B.200d.txt",
             "--game_name","w2vglove300_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    # w2vglove200_thresholds vs glove300 (GLOVE V GLOVE)
    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(
            ["python", "run_game.py", "players.codemaster_w2vglove_03.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.200d.txt",
             "--glove_guesser", "players/glove/glove.6B.200d.txt",
             "--game_name","w2vglove200_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(
            ["python", "run_game.py", "players.codemaster_w2vglove_05.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.200d.txt",
             "--glove_guesser", "players/glove/glove.6B.200d.txt",
             "--game_name","w2vglove200_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(
            ["python", "run_game.py", "players.codemaster_w2vglove_07.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.200d.txt",
             "--glove_guesser", "players/glove/glove.6B.200d.txt",
             "--game_name","w2vglove200_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    # w2vglove100_thresholds vs glove300 (GLOVE V GLOVE)
    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(
            ["python", "run_game.py", "players.codemaster_w2vglove_03.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.100d.txt",
             "--glove_guesser", "players/glove/glove.6B.200d.txt",
             "--game_name","w2vglove100_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(
            ["python", "run_game.py", "players.codemaster_w2vglove_05.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.100d.txt",
             "--glove_guesser", "players/glove/glove.6B.200d.txt",
             "--game_name","w2vglove100_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(
            ["python", "run_game.py", "players.codemaster_w2vglove_07.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.100d.txt",
             "--glove_guesser", "players/glove/glove.6B.200d.txt",
             "--game_name","w2vglove100_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    # w2vglove50_thresholds vs glove300 (GLOVE V GLOVE)
    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(
            ["python", "run_game.py", "players.codemaster_w2vglove_03.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.50d.txt",
             "--glove_guesser", "players/glove/glove.6B.200d.txt",
             "--game_name","w2vglove50_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(
            ["python", "run_game.py", "players.codemaster_w2vglove_05.AICodemaster", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.50d.txt",
             "--glove_guesser", "players/glove/glove.6B.200d.txt",
             "--game_name","w2vglove50_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50

    counter = 100
    for i in range(30):
        str_counter = str(int(counter))
        subprocess.run(
            ["python", "run_game.py", "players.codemaster_w2vglove_0.AICodemaster7", "players.guesser_w2vglove.AIGuesser", "--w2v",
             "players/GoogleNews-vectors-negative300.bin", "--glove_cm", "players/glove/glove.6B.50d.txt",
             "--glove_guesser", "players/glove/glove.6B.200d.txt",
             "--game_name","w2vglove50_thresholds vs w2vglove200","--seed", str_counter])
        counter += 50


run()
