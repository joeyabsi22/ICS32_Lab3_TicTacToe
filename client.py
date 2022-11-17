import socket


class Client:

    def __init__(self, ip=None, port: int = 9999):
        self.ip = ip
        self.port = port

    def connect(self):
        if self.ip is None:
            self.ip = input("\nPlease enter the IP address:\n\n")
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                client_socket.connect((self.ip, self.port))
                print("\nSuccessfully connected to the server!\n")

                difficulty = None
                while difficulty is None:
                    difficulty = input("Please enter Difficulty:\n1 - Easy\n2 - Medium\n3 - Hard\n\n")
                    try:
                        difficulty = int(difficulty)
                    except Exception:
                        print("\nError: Difficulty must be an integer in range 1-3\n")
                        difficulty = None
                        continue
                    if not 1 <= difficulty <= 3:
                        print("\nError: Difficulty must be in range 1-3\n")
                        difficulty = None
                        continue
                    difficulty_message = ""
                    if difficulty == 1:
                        difficulty_message = "E"
                        print("\nEasy difficulty selected.\n")
                    if difficulty == 2:
                        difficulty_message = "M"
                        print("\nMedium difficulty selected.\n")
                    if difficulty == 3:
                        difficulty_message = "H"
                        print("\nHard difficulty selected.\n")
                    client_socket.send(difficulty_message.encode())

                    while True:

                        server_response = client_socket.recv(1024).decode()
                        if len(server_response) != 1:
                            print(server_response)
                            continue
                        else:
                            if server_response == "M" or server_response == "B":
                                if server_response == "B":
                                    print("Error: That position is already taken.")
                                while True:
                                    move = input("\nPlease enter a move: (cells 1-9, left to right then top to bottom)\n\n")
                                    bad_input = False
                                    try:
                                        move = int(move)
                                        if not 1 <= move <= 9:
                                            bad_input = True
                                    except:
                                        bad_input = True
                                    finally:
                                        if bad_input:
                                            print("\nError: Invalid move entered. Move must be an integer in range 1-9.")
                                            continue
                                        else:
                                            break
                                client_socket.send(str(move).encode())
                                print()
                                continue
                            if server_response == "A":
                                print("\nThe opponent is thinking...\n")
                                continue
                            elif server_response == "P":
                                print("\nYou won!\n\n")
                            elif server_response == "T":
                                print("\nThe game ended in a tie!\n\n")
                            elif server_response == "C":
                                print("\nYou Lost!\n\n")

                            x = input("Please enter 'Y' if you would like to play again:\n\n")
                            if x == "Y" or x == "y":
                                self.connect()
                            else:
                                client_socket.close()
                                quit(0)
        except Exception:
            x = input("\nInvalid IP address entered. Please enter 'Y' if you would like to retry:\n\n")
            if x == "Y" or x == "y":
                self.ip = None
                self.connect()


if __name__ == '__main__':
   Client().connect()
