"""Documenter backend."""
import bottle
import os
import css_extractor as ce
import conf

DEFAULT_HOST = conf.DEFAULT_HOST
DEFAULT_PORT = conf.DEFAULT_PORT


def documenter_backend_console(frontend):
    """Documenter terminal."""
    help_txt = "Commands\n--------\n"
    help_txt += "h    | Help prompt.\n"
    help_txt += "css  | Generate css skeleton for current frontend.\n"
    help_txt += "host | Host current frontend.\n"
    help_txt += "cls  | Clear terminal.\n"
    help_txt += "exit | Exit application.\n"
    try:
        while True:
            com = ""
            try:
                com = input("Documenter> ")
            except EOFError:
                leave()
            if com:
                com = com.strip(" ")
                com = com.lower()
                if com == "host":
                    h = input("Host: ").strip(" ")
                    if not h:
                        print('Using default host.')
                        h = DEFAULT_HOST
                    print("Host set to " + h)
                    p = input('Port: ').strip(' ')
                    if p:
                        try:
                            p = int(p)
                        except ValueError:
                            print("Value error, using default port.")
                            p = DEFAULT_PORT
                    else:
                        print("Default port used.")
                        p = DEFAULT_PORT
                    print("Port set to " + str(p))
                    bottle.run(host=h, port=p)
                elif com == "css":
                    ce.extract_css(frontend)
                elif com == "exit":
                    leave()
                elif com == "h":
                    print(help_txt)
                elif com == "cls":
                    os.system("cls")
                else:
                    print(com + " is not a command!")
    except KeyboardInterrupt:
        leave()


def leave():
    """Close Documenter terminal."""
    print("\nDocumenter shutting down...\n")
    exit()
