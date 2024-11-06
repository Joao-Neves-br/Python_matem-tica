lang=input("Qual a linguagem de programação você quer aprender?\n")
match lang:
    case("JavaScript"):
        print("Você pode se tornar um desenvolvedor WEB.")
    case("Python"):
        print("Você pode se tornar um cientista de dados.")
    case("PHP"):
        print("Você pode se tornar um desenvolvedor backend.")
    case("Solidity"):
        print("Você pode se tornar um desenvolvedor Blockchain.")
    case("Java"):
        print("Você pode se tornar um desenvolvedor de aplicativos móveis.")
    case(default):
        print("A linguagem não importa, o que importa é resolver problemas")