class Generator:
    def __init__(self, class_name:str)->None:
        self.class_name = class_name

    def __start(self)->str:
        return f"class {self.class_name}"

    def __main_method(self)->str:
        return "public static void main(String[] args){"
    
    def codes(self, *args)->str:
        codes = ""
        for x in args:
            codes += x
        return codes
    
    def _generate_format(self, codes)->str:
        format = self.__start() + "{\n" + self.__main_method() + "\n" + self.codes(codes) + "\n}\n}"
        return format
    
    def codes_generate(self, file_name:str, codes:str)->bool:
        try:
            with open(file_name, "w") as javaFile:
                javaFile.write(self._generate_format(codes))
        except FileNotFoundError as err:
            print("File not found")

# if __name__ == '__main__':
#         helloWorld = Generator("HelloWorld")
#         helloWorld.codes_generate("HelloWorld.java", "System.out.println('Hello World');")