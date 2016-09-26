"""Webface backend."""
import bottle
import os
import css_extractor as ce
import conf


def webface_console(frontend):
    """Webface terminal."""
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
                        h = conf.DEFAULT_HOST
                    print("Host set to " + h)
                    p = input('Port: ').strip(' ')
                    if p:
                        try:
                            p = int(p)
                        except ValueError:
                            print("Value error, using default port.")
                            p = conf.DEFAULT_PORT
                    else:
                        print("Default port used.")
                        p = conf.DEFAULT_PORT
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
    """Close Webface terminal."""
    print("\nWebface shutting down...\n")
    exit()
